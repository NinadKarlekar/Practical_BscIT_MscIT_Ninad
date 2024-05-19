# 11 B. Normalized Web Distance and Word Similarity

# Convert
# Reliance supermarket
# Reliance hypermarket
# Reliance
# Reliance
# Reliance downtown
# Relianc market
# Mumbai
# Mumbai Hyper
# Mumbai dxb
# mumbai airport
# k.m trading
# KM Trading
# KM trade
# K.M. Trading
# KM.Trading
# into
# Reliance
# Reliance
# Reliance
# Reliance
# Reliance
# Reliance
# Mumbai
# Mumbai
# Mumbai
# Mumbai
# KM Trading
# KM Trading
# KM Trading
# KM Trading
# KM Trading

import numpy as np
import re
import textdistance  # pip install textdistance
# we will need scikit-learn>=0.21
import sklearn  # pip install sklearn
from sklearn.cluster import AgglomerativeClustering

texts = [
    'Reliance supermarket', 'Reliance hypermarket', 'Reliance', 'Reliance', 'Reliance downtown', 'Relianc market',
    'Mumbai', 'Mumbai Hyper', 'Mumbai dxb', 'mumbai airport',
    'k.m trading', 'KM Trading', 'KM trade', 'K.M. Trading', 'KM.Trading'
]

def normalize(text):
    """ Keep only lower-cased text and numbers"""
    return re.sub('[^a-z0-9]+', ' ', text.lower())

def group_texts(texts, threshold=0.4):
    """ Replace each text with the representative of its cluster"""
    normalized_texts = np.array([normalize(text) for text in texts])
    distances = 1 - np.array([
        [textdistance.jaro_winkler(one, another) for one in normalized_texts]
        for another in normalized_texts
    ])
    clustering = AgglomerativeClustering(
        distance_threshold=threshold,  # this parameter needs to be tuned carefully
        affinity="precomputed", linkage="complete", n_clusters=None
    ).fit(distances)
    centers = dict()
    for cluster_id in set(clustering.labels_):
        index = clustering.labels_ == cluster_id
        centrality = distances[:, index][index].sum(axis=1)
        centers[cluster_id] = normalized_texts[index][centrality.argmin()]
    return [centers[i] for i in clustering.labels_]

print(group_texts(texts))
