import sys
import spotipy
import spotipy.util as util
import json

scope = 'user-top-read'
username = 'cowaar'
token = util.prompt_for_user_token(username,
                                   scope,
                                   client_id='a533855a85d5443eb1964a9947a6ef7b',
                                   client_secret='7393047608c944d596c813c0eaa16bbc',
                                   redirect_uri='http://localhost:5000')

if token:
    sp = spotipy.Spotify(auth=token)
else:
    print("Can't get token for", username)


def getTopTracks():
    return sp.current_user_top_tracks(time_range="long_term", limit=150)


def addTracksAnalysis(tracks):
    for track in tracks['items']:
        uri = track['uri']
        track['analysis'] = sp.audio_features(uri)[0]
    return tracks


def orderBy(tracksWithAnalysis, characteristic):
    tracks = tracksWithAnalysis['items']
    tracksWithAnalysis['items'] = sorted(tracks, key=lambda k: k['analysis'][characteristic])
    return tracksWithAnalysis


def saveAsJson(dict):
    with open('data.json', 'w') as fp:
        json.dump(dict, fp)


def run(characteristic):

    top = getTopTracks()
    topWithAnalysis = addTracksAnalysis(top)
    result = orderBy(topWithAnalysis, characteristic)
    return result

