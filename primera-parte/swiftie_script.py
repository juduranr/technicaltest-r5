import pandas as pd
import json
import os

def load_data(json_file):
    with open(json_file, 'r') as file:
        return json.load(file)

def process_data(data):
    return [
        {
            'disc_number': track['disc_number'],
            'duration_ms': track['duration_ms'],
            'explicit': track['explicit'],
            'track_number': track['track_number'],
            'track_popularity': track['track_popularity'],
            'track_id': track['track_id'],
            'track_name': track['track_name'],
            'audio_features.danceability': track['audio_features']['danceability'],
            'audio_features.energy': track['audio_features']['energy'],
            'audio_features.key': track['audio_features']['key'],
            'audio_features.loudness': track['audio_features']['loudness'],
            'audio_features.mode': track['audio_features']['mode'],
            'audio_features.speechiness': track['audio_features']['speechiness'],
            'audio_features.acousticness': track['audio_features']['acousticness'],
            'audio_features.instrumentalness': track['audio_features']['instrumentalness'],
            'audio_features.liveness': track['audio_features']['liveness'],
            'audio_features.valence': track['audio_features']['valence'],
            'audio_features.tempo': track['audio_features']['tempo'],
            'audio_features.id': track['audio_features']['id'],
            'audio_features.time_signature': track['audio_features']['time_signature'],
            'artist_id': data['artist_id'],
            'artist_name': data['artist_name'],
            'artist_popularity': data['artist_popularity'],
            'album_id': album['album_id'],
            'album_name': album['album_name'],
            'album_release_date': album['album_release_date'],
            'album_total_tracks': album['album_total_tracks']
        }
        for album in data['albums'] for track in album['tracks']
    ]

def save_to_csv(df, csv_file):
    file_exists = os.path.isfile(csv_file)
    with open(csv_file, 'a' if file_exists else 'w', newline='', encoding='utf-8') as f:
        df.to_csv(f, header=not file_exists, index=False)

json_file_name = 'taylor_swift_spotify.json'
csv_file_name = 'dataset.csv'

try:
    data = load_data(json_file_name)
    tracks_data = process_data(data)
    df_tracks = pd.DataFrame(tracks_data)
    save_to_csv(df_tracks, csv_file_name)
except Exception as e:
    print(f"Error: {e}")
