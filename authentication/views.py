from django.shortcuts import render
from rest_auth.registration.views import SocialLoginView
from rest_auth.registration.serializers import SocialLoginSerializer
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from google.oauth2.credentials import Credentials
from rest_framework import status
from rest_framework.response import Response
import requests
# Create your views here.

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = Credentials
    serializer_class = SocialLoginSerializer

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)
    def post(self, request, *args, **kwargs):
        # Check if the access token is present in the request data
        access_token = request.data.get('access_token')
        if not access_token:
            return Response({'error': 'Access token is missing.'}, status=status.HTTP_400_BAD_REQUEST)

        # Verify the access token using the Google OAuth2 client library
        try:
            credentials = Credentials.from_authorized_user_info(info=None, access_token=access_token)
            # You can add more custom validation logic here if needed
        except Exception as e:
            return Response({'error': 'Invalid access token.'}, status=status.HTTP_400_BAD_REQUEST)

        # Call the parent `post()` method to complete the authentication flow
        return super().post(request, *args, **kwargs)
    # def post(self, request, *args, **kwargs):
    #     access_token = request.data.get('access_token')
    #     if access_token:
    #         # verify access token and get user data
    #         response = requests.get('https://www.googleapis.com/oauth2/v3/userinfo',
    #                                 params={'access_token': access_token})
    #         if response.status_code == 200:
    #             data = response.json()
    #             # create or update user in your database and login
    #             return self.login(request, *args, **kwargs)
    #         return requests.Response({'error': 'invalid access_token'}, status=status.HTTP_400_BAD_REQUEST)
    #     #return requests.Response({'error': 'access_token not provided'}, status=status.HTTP_400_BAD_REQUEST)
    
    