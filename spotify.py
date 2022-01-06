import os
import requests

client_id = os.environ['spotify_client_id']
client_secret = os.environ['spotify_client_secret']
redirect_uri = "https://spotify-token.ilybenny.repl.co/callback"
spotify_api = "https://api.spotify.com/v1/"

def get_auth_link():
    params = {
        "client_id": client_id,
        "response_type": "code",
        "redirect_uri": redirect_uri,
        "scope": "user-read-playback-state"
    }

    link = "https://accounts.spotify.com/authorize?" + requests.compat.urlencode(params)
    return link

def get_refresh_token(code):
    body = {
        "grant_type": 'authorization_code',
        "code": code,
        "redirect_uri": redirect_uri,
        "content_type": "application/x-www-form-urlencoded"
    }

    resp = requests.post("https://accounts.spotify.com/api/token", data=body, auth=(client_id, client_secret))

    if resp.status_code != 200:
        return None
    
    return resp.json()["refresh_token"]

def get_access_token(code):
    body = {
        "grant_type": 'authorization_code',
        "code": code,
        "redirect_uri": redirect_uri,
        "content_type": "application/x-www-form-urlencoded"
    }

    resp = requests.post("https://accounts.spotify.com/api/token", data=body, auth=(client_id, client_secret))

    if resp.status_code != 200:
        return None
    
    return resp.json()["access_token"]

def get_refreshed_access_token(refresh_token):
    body = {
        "grant_type": 'refresh_token',
        "refresh_token": refresh_token,
        "content_type": "application/x-www-form-urlencoded"
    }

    resp = requests.post("https://accounts.spotify.com/api/token", data=body, auth=(client_id, client_secret))

    if resp.status_code != 200:
        return None
    
    return resp.json()["access_token"]

def get_playing(access_token):
    resp = requests.get(spotify_api + "me/player", headers={"Authorization": "Bearer " + access_token})

    if resp.status_code != 200:
        return None

    return resp.json()