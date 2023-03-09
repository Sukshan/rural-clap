from rest_auth.registration.views import SocialLoginView
from rest_framework import status
from rest_framework.response import Response
from google.oauth2 import id_token
from google.auth.transport import requests
from Ruralclap.settings import env


class GoogleLogin(SocialLoginView):
    def post(self, request, *args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return Response({'error': 'Authentication header is missing'}, status=status.HTTP_400_BAD_REQUEST)
        auth_header_parts = auth_header.split()
        access_token = auth_header_parts[1]
        if not access_token:
            return Response({'error': 'Access token is missing.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            idinfo = id_token.verify_oauth2_token(access_token, requests.Request(),env('CLIENT_ID') )
            return Response({'success':'true','info':idinfo},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': e}, status=status.HTTP_400_BAD_REQUEST)

    
    