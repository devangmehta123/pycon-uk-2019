from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class APIBaseView(APIView):

    serializer_class = None
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )

    '''
    def dispatch(self, request, *args, **kwargs):
        self.settings.EXCEPTION_HANDLER = apiv3_exception_handler
        return super().dispatch(request, *args, **kwargs)

    def permission_denied(self, request, **kwargs):
        """
        Overriding permission_denied() for custom auth exceptions.
        """
        if not request.successful_authenticator:
            raise APIAuthException(error_codes.USER_IS_NOT_AUTHENTICATED)
        raise APIAuthException(error_codes.PERMISSION_DENIED)
    '''

    def data_valid(self, data):
        """
        Method is called when data is valid

        :param data: requests data
        :return: HTTP response
        """
        return Response(data={}, status=200)

    def data_invalid(self, serializer):
        """
        Method is called when data is invalid

        :param serializer:
        :return: API response
        """
        return Response(data={}, status=422)

    def get_serializer_class(self):
        """

        :return: Serializer class
        """
        return self.serializer_class

    def get_serializer(self):
        """

        :return: Serializer instance
        """
        serializer = self.get_serializer_class()(data=self.request.data)
        # We have to call is_valid(), otherwise documentation class SimpleMetadata can't parse the fields
        serializer.is_valid()
        return serializer

    def serializer_request(self, request, *args, **kwargs):
        """
        Implementation of POST method. It validate the data and send it to next step. Also catch the exceptions.

        Use this as post, get, put, delete or other methods. If you want post method allowed, use:

            def post(self, *args, **kwargs):
                return self.serializer_request(*args, **kwargs)

        within derived class. GET method:

            def get(self, *args, **kwargs):
                return self.serializer_request(*args, **kwargs)

        :param request: HTTP request
        :return: API response
        """
        serializer = self.get_serializer()
        return self._do_serializer_request(serializer)

    def _do_serializer_request(self, serializer):
        if serializer.is_valid():
            response = self.data_valid(serializer.validated_data)
            return response
        else:
            return self.data_invalid(serializer)

    def get_affiliate_id(self):
        """
        Return affiliate id from URL address
        :return: affiliate id
        """
        return self.kwargs.get("affiliate_id")
