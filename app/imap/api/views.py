"""Views for Email IMAP API"""
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import EmailCredentials
from imap.api.serializers import EmailCredentialsSerializer
from imap.imap_handler import IMAPHandler

class EmailCredentialsView(APIView):
    """Email Credentials View"""

    def post(self, request, *args, **kwargs):
        serializer = EmailCredentialsSerializer(data=request.data)

        if serializer.is_valid():
            credentials = serializer.validated_data
            email_address = credentials['email_address']
            password = credentials['password']
            imap_server = credentials['imap_server']

            try:
                emails = IMAPHandler.get_emails(email_address, password, imap_server)
                return Response({'emails': emails}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)