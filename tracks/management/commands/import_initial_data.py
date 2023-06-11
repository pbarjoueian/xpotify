from typing import Dict

import pandas as pd
from django.core.management import BaseCommand

from tracks.models import Track


class Command(BaseCommand):
    help = "Initial tracks data"

    def add_arguments(self, parser):
        parser.add_argument("--path", type=str)

    def handle(self, *args, **kwargs):
        path = kwargs["path"]
        tracks_df = pd.read_csv(path)
        for _, row in tracks_df.iterrows():
            data: Dict = {
                "acousticness": row["acousticness"],
                "album_id": row["album_id"],
                "analysis_url": row["analysis_url"],
                "artists_id": row["artists_id"],
                "available_markets": row["available_markets"],
                "country": row["country"],
                "danceability": row["danceability"],
                "disc_number": row["disc_number"],
                "duration_ms": row["duration_ms"],
                "energy": row["energy"],
                "href": row["href"],
                "instrumentalness": row["instrumentalness"],
                "key": row["key"],
                "liveness": row["liveness"],
                "loudness": row["loudness"],
                "lyrics": row["lyrics"],
                "mode": row["mode"],
                "name": row["name"],
                "playlist": row["playlist"],
                "popularity": row["popularity"],
                "preview_url": row["preview_url"],
                "speechiness": row["speechiness"],
                "tempo": row["tempo"],
                "time_signature": row["time_signature"],
                "track_href": row["track_href"],
                "track_name_prev": row["track_name_prev"],
                "track_number": row["track_number"],
                "uri": row["uri"],
                "valence": row["valence"],
            }
            Track.objects.update_or_create(uuid=row["id"], defaults=data)

        self.stdout.write(self.style.SUCCESS("Successfully initialized."))
