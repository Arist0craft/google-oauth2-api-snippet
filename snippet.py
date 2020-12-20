from googleapiclient.discovery import build
from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials
from googleapiclient.http import HttpRequest



code: str # Code getted from Google OAuth2 process
google_client_config: Flow
google_client_config.fetch_token(code=code)
credentials: Credentials = google_client_config.credentials
goauth2 = build("oauth2", "v2", credentials=credentials)

tokeninfo_request: HttpRequest = goauth2.tokeninfo()
tokeninfo_result = tokeninfo_request.execute()
print("Tokeninfo")
print(tokeninfo_result)

# Tokeninfo. Delete comments
#{
#   'issued_to': 'client_id_from_oauth2_credentials',
#   'audience': 'client_id_from_oauth2_credentials', 
#   'user_id': 'user_id',
#   'scope': 'https://www.googleapis.com/auth/userinfo.email openid',
#   'expires_in': int, 
#   'email': 'user_email@gmail.com', 
#   'verified_email': True, 
#   'access_type': 'offline'
#}

userinfo = goauth2.userinfo()
me = userinfo.v2().me()
me_info: HttpRequest = me.get()
me_result = me_info.execute()
print("Meinfo")
print(me_result)

# Me info. Delete comments
# Email and UserId the same.
#{
#   'id': 'user_id',
#   'email': 'user_email@gmail.com',
#   'verified_email': True,
#   'picture': 'https://lh5.googleusercontent.com/photo_url.jpg'
#}

userinfo_request: HttpRequest = userinfo.get()
userinfo_result = userinfo_request.execute()
print("Userinfo")
print(userinfo_result)

# User info. Delete comments
# Email and UserId the same.
#{
#   'id': 'user_id',
#   'email': 'user_email@gmail.com',
#   'verified_email': True,
#   'picture': 'https://lh5.googleusercontent.com/photo_url.jpg'
#}
