import flask
import requests
import spotify

app = flask.Flask(__name__, template_folder="templates")

@app.route("/")
def index():
    auth_link = spotify.get_auth_link()
    return flask.render_template("index.html", auth_link=auth_link)

@app.route("/callback")
def callback():
    code = flask.request.args.get("code")
    refresh_token = spotify.get_refresh_token(code)
    
    if refresh_token is None:
        return flask.redirect("/")

    refreshed_access_token = spotify.get_refreshed_access_token(refresh_token)
    if refreshed_access_token is None:
        return flask.redirect("/")

    return f"<h1>Your Spotify token</h1><pre>{refreshed_access_token}</pre>"