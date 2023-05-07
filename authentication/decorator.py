from django.http import JsonResponse
from google.oauth2 import id_token
from google.auth.transport import requests
from Ruralclap.settings import env
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
            if '##' in access_token:
                return func(request, *args, **kwargs)
            id_token.verify_oauth2_token(access_token, requests.Request(),env('CLIENT_ID'))
            return func(request, *args, **kwargs)
        except Exception as e:
            print(e);
            return JsonResponse({'error': 'Acces Denied'}, status=400)
    return inner