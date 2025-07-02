import streamlit as st
import pandas as pd
from recommender import create_similarity_matrix, recommend_movies
import ast

# === Page Setup ===
st.set_page_config(page_title="🎬 Movie Recommender", layout="centered")

# === Helper to extract unique genres from the dataset ===
def extract_unique_genres(df):
    genres_set = set()
    for g in df['genres'].dropna():
        try:
            genres = ast.literal_eval(g)
            for genre in genres:
                genres_set.add(genre['name'])
        except:
            continue
    return sorted(list(genres_set))

# === Load dataset ===
st.markdown("<h1 style='text-align: center; color: #F63366;'>🎬 Movie Recommender System</h1>", unsafe_allow_html=True)
st.markdown("##### 🔍 Get top movie recommendations based on your taste")

try:
    df = pd.read_csv("data/movies.csv")
    df = df[['title', 'overview', 'genres']]
except FileNotFoundError:
    st.error("❌ File not found. Make sure 'data/movies.csv' exists.")
    st.stop()

# === Genre filter ===
st.markdown("---")
st.markdown("### 🎭 Filter by Genre")
genres_list = extract_unique_genres(df)
selected_genre = st.selectbox("Choose a genre (optional):", ["All"] + genres_list)

if selected_genre != "All":
    def has_genre(genre_list_str, selected):
        try:
            genres = ast.literal_eval(genre_list_str)
            return any(genre['name'] == selected for genre in genres)
        except:
            return False

    filtered_df = df[df['genres'].apply(lambda x: has_genre(x, selected_genre))].reset_index(drop=True)
else:
    filtered_df = df.copy().reset_index(drop=True)

if filtered_df.empty:
    st.warning("⚠️ No movies found for the selected genre.")
    st.stop()

# === Similarity matrix ===
similarity = create_similarity_matrix(filtered_df)

# === Dropdown-based Recommendation ===
st.markdown("---")
st.markdown("### 🎥 Pick a Movie from List")
selected_movie = st.selectbox("Choose a movie you like:", filtered_df['title'].values)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🎯 Recommend from List"):
        recommendations = recommend_movies(selected_movie, filtered_df, similarity)
        st.success(f"Top 5 movies similar to: **{selected_movie}**")
        for i, movie in enumerate(recommendations, 1):
            st.write(f"{i}. {movie}")

# === Search bar at the bottom ===
st.markdown("---")
st.markdown("### 🔎 Or Search by Movie Name")

movie_query = st.text_input("Type the movie title (case-insensitive, exact match):")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🔍 Search"):
        matches = filtered_df[filtered_df['title'].str.lower() == movie_query.strip().lower()]
        if matches.empty:
            st.error("❌ Movie not found in selected genre.")
        else:
            selected_movie = matches.iloc[0]['title']
            recommendations = recommend_movies(selected_movie, filtered_df, similarity)
            st.success(f"Top 5 movies similar to: **{selected_movie}**")
            for i, movie in enumerate(recommendations, 1):
                st.write(f"{i}. {movie}")
