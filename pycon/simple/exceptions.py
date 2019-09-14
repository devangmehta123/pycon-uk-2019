from rest_framework import exceptions


class APIGeneralException(exceptions.APIException):
    pass


class APIValidationException(exceptions.APIException):
    serializer = None
    valid = False


class APIException(exceptions.APIException):
    """
    General exception for our API
    """
    error_code = None
    http_status_code = None
    severity = None

    def __init__(self, *args, http_status_code=500, **kwargs):
        try:
            if isinstance(args[0], tuple) and (isinstance(args[0][1], int) or args[0][1] is None):  # Find our structure for error_code handling
                self.error_code = args[0][1]

                # Removing error_code from message
                message = args[0][0]
                self.severity = args[0][2]
                msg_params = kwargs.pop('msg_params', {})
                if msg_params:
                    message = message % msg_params
                extended_args = [message]
                extended_args.extend(args[1:])
                args = tuple(extended_args)
                self.http_status_code = http_status_code
        except IndexError:
            pass

        super().__init__(*args, **kwargs)


class APIInputException(APIException):
    """
    Exception for input problems
    """
    pass


class APIBackendException(exceptions.APIException):
    """
    General exception for our backend API
    """
    pass

class APIBackendValidationException(exceptions.APIException):
    """
    General exception for our backend API
    """
    pass

class APIAuthException(APIException):
    """
    General exception for our API
    """
    pass


class InternalException(exceptions.APIException):
    pass
