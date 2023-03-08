from rest_auth.registration.views import SocialLoginView
from rest_auth.registration.serializers import SocialLoginSerializer
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from google.oauth2.credentials import Credentials
from rest_framework import status
from rest_framework.response import Response
from google.oauth2 import id_token
from google.auth.transport import requests


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = Credentials
    serializer_class = SocialLoginSerializer

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)
    def post(self, request, *args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return Response({'error': 'Authentication header is missing'}, status=status.HTTP_400_BAD_REQUEST)
        auth_header_parts = auth_header.split()
        access_token = auth_header_parts[1]
        if not access_token:
            return Response({'error': 'Access token is missing.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            idinfo = id_token.verify_oauth2_token(access_token, requests.Request(),'422436897824-v7gfeacadmg099objpl7269e3kmflsf0.apps.googleusercontent.com' )
            return Response({'success':'true','info':idinfo},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Invalid access token.'}, status=status.HTTP_400_BAD_REQUEST)

    
    