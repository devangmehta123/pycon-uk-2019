from rest_framework.response import Response
from .base import APIBaseView
from .postcode_serializer import SimplePostcodeRequestSerializer


class DistIdsView(APIBaseView):
    """
    """
    serializer_class = SimplePostcodeRequestSerializer

    def data_valid(self, data):
        """
        If data are valid, this will be called.

        :param data: data from API client
        :return: HTTP response
        """

        return Response(data={'postcode': data['postcode'], 'dist_id': '14'}, status=200)

    def post(self, request, *args, **kwargs):
        """
        ---
        request_serializer: SimplePostcodeRequestSerializer
        response_serializer: DistIdsResponseSerializer
        """
        return self.serializer_request(request, *args, **kwargs)


