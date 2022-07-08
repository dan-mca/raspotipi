from flask import render_template, redirect, request, session
from app import app
from app.spotifyAuth import SpotifyAuth
from app.spotify import Spotify

app.secret_key = "0:Nc8089dfncn"
app.config['SESSION_COOKIE_NAME'] = 'Dans Cookie'
TOKEN_INFO = 'token_info'

@app.route('/')
def home():
    auth = SpotifyAuth()
    auth_url = auth.get_auth_url()
    return redirect(auth_url)

@app.route('/login')
def login():
    if len(session) == 0:
        return """
        <h1>Login</h1>
        <a href="/">Login</a>
        """
    else:
        return redirect('/index')

@app.route('/redirect')
def redirectPage():
    # session.clear()
    if len(session) == 0:
        print(len(session))
        code = request.args.get('code')
        
        # get access token from code
        auth = SpotifyAuth()
        token_info = auth.get_access_token(code)
        print('Getting token...')
        print(token_info['access_token'])

        # store the access token in session token info
        session[TOKEN_INFO] = token_info
        print('session token info...')
        print(session['token_info']['access_token'])

        # return redirect to currently playing
        return redirect('/index')
    else:
        print(len(session))
        return redirect('/index')

@app.route('/index')
def index():
    token = session['token_info']['access_token']

    try:
        currently_playing = Spotify(token).currently_playing()
        user_profile = Spotify(token).current_user()
        if currently_playing:
            return render_template('index.html', title='Home', playing=currently_playing, profile=user_profile)
    except:
        return 'No song playing'

@app.route('/signout')
def sign_out():
    session.pop('token_info', None)
    print(session)
    return redirect('/login')
