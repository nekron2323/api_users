from email import header
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.conf import settings


class Authentication(JWTAuthentication):
    def authenticate(self, request):
        header = self.get_header(request)
        if header is None:
            raw_token = request.COOKIES.get(
                settings.SIMPLE_JWT['AUTH_COOKIE'] or None)
        else:
            raw_token = self.get_raw_token(header)
        if raw_token is None:
            return None
        validate_token = self.get_validated_token(raw_token)
        return self.get_user(validate_token), validate_token
