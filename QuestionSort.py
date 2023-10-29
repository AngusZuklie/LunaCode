"""
NOTE FOR GITHUB:
I am not able to include files or information referencing app user data and, as such, will be including the tag <fake> to all filenames, including user data
"""

import tensorflow_hub as hub
import pandas as pd
from sklearn.cluster import KMeans


# Load the Universal Sentence Encoder model
embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder-large/5")

data = pd.read_csv('<fake>questions.csv', usecols=['question'])

data = data.dropna()

# Extract sentences from the DataFrame
sentences = data['question'].tolist()

# Compute sentence embeddings
sentence_embeddings = embed(sentences)

# Define the number of clusters
num_clusters = 50

# Perform K-Means clustering
kmeans = KMeans(n_clusters=num_clusters)
clustered_sentences = kmeans.fit_predict(sentence_embeddings)

# Add cluster labels to the original DataFrame
data['Cluster'] = clustered_sentences

# Create DataFrames for each cluster 
cluster_dataframes = {}
for cluster_label in range(num_clusters):
    cluster_df = data[data['Cluster'] == cluster_label].drop(columns=['Cluster'])
    cluster_dataframes[cluster_label] = cluster_df

# Write each DataFrame to a CSV file
for cluster_label, cluster_df in cluster_dataframes.items():
    csv_filename = f'<fake>_output/cluster_{cluster_label + 1}.csv'
    cluster_df.to_csv(csv_filename, index=False)
    print(f'Cluster {cluster_label + 1} of len {len(cluster_df)}')
