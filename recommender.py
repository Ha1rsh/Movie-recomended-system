import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import ast

def clean_genres(genres_str):
    try:
        genres = ast.literal_eval(genres_str)
        return " ".join([g['name'] for g in genres])
    except:
        return ""

def create_similarity_matrix(df):
    df['genres'] = df['genres'].fillna("").apply(clean_genres)
    df['overview'] = df['overview'].fillna("")
    df['combined'] = df['overview'] + " " + df['genres']

    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(df['combined'])

    similarity = cosine_similarity(tfidf_matrix)
    return similarity

def recommend_movies(title, df, similarity_matrix):
    if title not in df['title'].values:
        return ["Movie not found."]
    
    idx = df[df['title'] == title].index[0]
    sim_scores = list(enumerate(similarity_matrix[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    
    recommended_titles = [df.iloc[i[0]]['title'] for i in sim_scores]
    return recommended_titles
