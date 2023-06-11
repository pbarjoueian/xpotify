from datetime import datetime

import joblib
import pandas as pd
from celery import shared_task
from sklearn.cluster import KMeans

from tracks.models import Track


@shared_task
def run_tracks_clustering():
    tracks_df = pd.DataFrame(list(Track.objects.all().values()))

    model = KMeans(n_clusters=5)

    model.fit(
        tracks_df[["energy", "valence", "danceability", "instrumentalness", "tempo"]]
    )

    now = datetime.now().strftime("%I:%M%p on %B %d, %Y")
    joblib.dump(model, f"ml/trained_models/tracks-kmeans-{now}")

    tracks_df["cluster_number"] = model.labels_

    for _, row in tracks_df.iterrows():
        Track.objects.filter(uuid=row["uuid"]).update(
            cluster_number=row["cluster_number"]
        )
