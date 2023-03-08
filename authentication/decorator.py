from django.http import JsonResponse
from google.oauth2 import id_token
from google.auth.transport import requests
def token_required(func):
    def inner(request, *args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return JsonResponse({'error': 'Authentication header is missing'}, status=400)
        auth_header_parts = auth_header.split()
        access_token = auth_header_parts[1]
        if not access_token:
            return JsonResponse({'error': 'Access token is missing.'}, status=400)
        try:
            idinfo = id_token.verify_oauth2_token(access_token, requests.Request(),'422436897824-v7gfeacadmg099objpl7269e3kmflsf0.apps.googleusercontent.com' )
            return func(request, *args, **kwargs)
        except Exception as e:
            return JsonResponse({'error': 'Invalid access token.'}, status=400)
    return inner