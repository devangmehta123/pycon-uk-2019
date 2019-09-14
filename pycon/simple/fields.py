import re
from rest_framework import serializers
class PostcodeField(serializers.CharField):

    def __init__(self, *args, **kwargs):
        kwargs['help_text'] = "UK Postcode (excluding Northern Ireland) with or without space and can have both upper and lower case characters"
        kwargs['max_length'] = 8
        super().__init__(*args, **kwargs)

    def to_internal_value(self, data):
        if data is None:
            return None
        value = super().to_internal_value(data)
        value = value.strip().upper()  # strip all surrounding whitespace and make upper case
        # only do cleanup and matching if value has an actual postcode. blanks and nulls are allowed.
        if value:
            if value.find(' ') > -1:  # there is at least one space
                incode = value[-3:]
                outcode = value[:-3].strip()
                value = outcode + incode
                if value.find(' ') > -1:  # there is a space within the incode or outcode
                    raise serializers.ValidationError(
                        "postcode has a space either within the incode or the outcode, '{0}', '{1}'".format(incode,
                                                                                                            outcode))
            # source of regex
            # http://stackoverflow.com/a/17507615/2775749
            if value.startswith('BT'):
                raise serializers.ValidationError('postcode is a Northern Ireland postcode which is not supported')
            valid_postcode = re.compile(r'^(GIR ?0AA|[A-PR-UWYZ]([0-9]{1,2}|([A-HK-Y][0-9]([0-9ABEHMNPRV-Y])?)|[0-9][A-HJKPS-UW]) ?[0-9][ABD-HJLNP-UW-Z]{2})$')
            if not valid_postcode.match(value):
                raise serializers.ValidationError('input postcode did not match validation regex')
        return value



