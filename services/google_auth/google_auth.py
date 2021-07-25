import json
import os

import requests
from flask import request
from models.user import User
from oauthlib.oauth2 import WebApplicationClient

GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET")
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)


class GoogleAuth:

    def __init__(self) -> None:
        self._client = WebApplicationClient(GOOGLE_CLIENT_ID)

    @staticmethod
    def get_provider_cfg():
        return requests.get(GOOGLE_DISCOVERY_URL).json()

    def get_request_uri(self):
        provider_cfg = self.get_provider_cfg()
        authorization_endpoint = provider_cfg["authorization_endpoint"]

        return self._client.prepare_request_uri(
            authorization_endpoint,
            redirect_uri=request.base_url + "/callback",
            scope=["openid", "email", "profile"],
        )

    def get_token(self, token_endpoint):
        code = request.args.get("code")

        token_url, headers, body = self._client.prepare_token_request(
            token_endpoint,
            authorization_response=request.url,
            redirect_url=request.base_url,
            code=code
        )

        token_response = requests.post(
            token_url,
            headers=headers,
            data=body,
            auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
        )
        return token_response.json()

    def get_user_info(self, userinfo_endpoint):
        uri, headers, body = self._client.add_token(userinfo_endpoint)
        userinfo_response = requests.get(uri, headers=headers, data=body)
        return userinfo_response.json()

    def get_user(self):
        provider_cfg = self.get_provider_cfg()
        token_endpoint = provider_cfg["token_endpoint"]
        userinfo_endpoint = provider_cfg["userinfo_endpoint"]

        token = self.get_token(token_endpoint)
        self._client.parse_request_body_response(json.dumps(token))
        userinfo = self.get_user_info(userinfo_endpoint)

        if userinfo.get("email_verified"):
            unique_id = userinfo["sub"]
            users_email = userinfo["email"]
            picture = userinfo["picture"]
            users_name = userinfo["given_name"]
        else:
            return "User email not available or not verified by Google.", 400

        user = User.get(unique_id)

        if user is None:
            User.create(**{
                'id': unique_id,
                'name': users_name,
                'email': users_email,
                'username': users_email,
                'password': None,
                'photo': picture
            })
            user = User.get(unique_id)

        return user
