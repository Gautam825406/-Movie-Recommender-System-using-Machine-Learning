import streamlit as st
import pickle
import pandas as pd
import requests

st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

try:
    API_KEY = st.secrets["TMDB_API_KEY"]
except Exception:
    API_KEY = None

if not API_KEY:
    st.error("TMDB API key is missing.")
    st.info(
        "Create .streamlit/secrets.toml with: TMDB_API_KEY=\"your_tmdb_api_key_here\""
    )
    st.stop()

movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        return None

    data = response.json()
    poster_path = data.get("poster_path")

    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    return None

def recommend(movie):
    movie_index = movies[movies['title'].str.lower() == movie.lower()].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #020617, #0f172a);
    }
    .main-title {
        text-align: center;
        color: white;
        font-size: 3rem;
        font-weight: 800;
        margin-top: 10px;
        margin-bottom: 0px;
    }
    .sub-title {
        text-align: center;
        color: #cbd5e1;
        font-size: 1.1rem;
        margin-bottom: 30px;
    }
    .movie-name {
        background-color: #111827;
        padding: 10px;
        border-radius: 12px;
        text-align: center;
        color: white;
        font-size: 15px;
        font-weight: 600;
        margin-top: 8px;
        min-height: 60px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #ef4444, #f59e0b);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.75rem 1rem;
        font-size: 1rem;
        font-weight: 700;
    }
    .stSelectbox label {
        color: white !important;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🎬 Movie Recommender System</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Find movies similar to your favorite one</div>', unsafe_allow_html=True)

selected_movie = st.selectbox(
    "Choose a movie",
    movies['title'].values
)

if st.button("Recommend Movies"):
    names, posters = recommend(selected_movie)

    st.markdown("## Recommended for you")

    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            if posters[i]:
                st.image(posters[i], use_container_width=True)
            else:
                st.write("No Image Available")

            st.markdown(
                f'<div class="movie-name">{names[i]}</div>',
                unsafe_allow_html=True
            )