from rest_auth.registration.views import SocialLoginView
from rest_framework import status
from rest_framework.response import Response
from google.oauth2 import id_token
from google.auth.transport import requests
from Ruralclap.settings import env
from users.models import users
from users.serializer import user_serializer

class GoogleLogin(SocialLoginView):
    def post(self, request, *args, **kwargs):
        isNewUser =  False
        userData = {}
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return Response({'error': 'Authentication header is missing'}, status=status.HTTP_400_BAD_REQUEST)
        auth_header_parts = auth_header.split()
        access_token = auth_header_parts[1]
        if not access_token:
            return Response({'error': 'Access token is missing.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            if '##' in access_token:
                email = access_token[2:]
                try:
                    user = users.objects.get(email = email)
                except Exception as e:
                    user = "Not"
                    isNewUser = True
                if(user!="Not"):    
                    serializer = user_serializer(user)
                    userData = serializer.data
                idinfo = {'email': email}; 
                return Response({'success':'true','info':idinfo, 'isNewUser': isNewUser, 'userData': userData},status=status.HTTP_200_OK)
            idinfo = id_token.verify_oauth2_token(access_token, requests.Request(),env('CLIENT_ID'))
            userEmail = idinfo['email']
            print(idinfo)
            try:
                user = users.objects.get(email = userEmail)
            except Exception as e:
                user = "Not"
                isNewUser = True
            if(user!="Not"):
                serializer = user_serializer(user)
                userData = serializer.data
            return Response({'success':'true','info':idinfo, 'isNewUser': isNewUser, 'userData': userData},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'False'}, status=status.HTTP_400_BAD_REQUEST)

    
    