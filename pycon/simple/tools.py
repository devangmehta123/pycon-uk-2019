

def api_response_v3(status_code, message="", data=None, errors=None, msg_params=None):
    """
    API response generator. It contains static structure because of static languages.
    If the status is false, data should be empty and vice versa.

    :param message: explanation of status_code
    :param status_code: integer with error code for msg
    :param data: returned data
    :param errors: list of error messages returned from serializer (this is only usefull for validation)
    :param msg_params: dict with variable data for messages
    :return:

    >>> sorted(api_response_v3(200, "test", {"test": 1}, errors=[1,2,3]).items())
    [('data', {'test': 1}), ('errors', [1, 2, 3]), ('message', 'test'), ('statusCode', 200)]

    """

    if errors is None:
        errors = []
    if msg_params is None:
        msg_params = {}

    response_data = {
        "statusCode": status_code,
    }

    if message:
        response_data["message"] = message % msg_params
    if errors:
        response_data["errors"] = errors
    if data:
        response_data["data"] = data

    return response_data


def api_response_v3_with_message(message, data=None, errors=None, msg_params=None, upgraded_version=False):
    """
    API response generator. It contains static structure because of static languages.
    If the status is false, data should be empty and vice versa.

    :param message: message from error_codes.py
    :param data: returned data
    :param errors: list of error messages returned from serializer (this is only usefull for validation)
    :param msg_params: dict with variable data for messages
    :param upgraded_version: returns record/records key instate of data depends on number of records
    :return:

    >>> GENERAL_OK = ("OK", 1000)
    >>> sorted(api_response_v3_with_message(GENERAL_OK, {"test": 1}, errors=[1,2,3]).items())
    [('data', {'test': 1}), ('errors', [1, 2, 3]), ('message', 'OK'), ('statusCode', 1000)]
    """

    if errors is None:
        errors = []
    if msg_params is None:
        msg_params = {}

    response_data = {
        "statusCode": message[1],
        "message": message[0] % msg_params,
    }

    if errors:
        response_data["errors"] = errors
    if data and not upgraded_version:
        response_data["data"] = data
    if data and upgraded_version:
        if isinstance(data, list):
            response_data["data"] = {"records": data}
        else:
            response_data["data"] = {"records": [data]}

    return response_data


def api_response_v3_with_message_and_defaults(message, data=None, errors=None, msg_params=None, defaults_data=None):
    response_data = api_response_v3_with_message(message=message, data=data, errors=errors,
                                                 msg_params=msg_params, upgraded_version=True)

    response_data['data']['defaults'] = defaults_data

    return response_data


