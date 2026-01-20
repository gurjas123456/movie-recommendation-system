import pickle
import streamlit as st
import requests

API_KEY = "59bf8e7b6845ec1a77cd7d87d70636bd"
NO_POSTER_URL = "https://via.placeholder.com/300x450?text=No+Poster+Available"


@st.cache_data(show_spinner=False)
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {
        "api_key": API_KEY,
        "language": "en-US"
    }

    try:
        r = requests.get(url, params=params, timeout=5)

        if r.status_code != 200:
            return None

        data = r.json()
        poster_path = data.get("poster_path")

        if not poster_path:
            return None

        return "https://image.tmdb.org/t/p/w500" + poster_path

    except:
        return None


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:]:
        movie_id = movies.iloc[i[0]].movie_id
        poster = fetch_poster(movie_id)

        # ❌ Skip movies with no posters
        if poster is None:
            continue

        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(poster)

        # ✅ Stop once we have 5 good movies
        if len(recommended_movie_names) == 5:
            break

    # Fallback if still less than 5
    while len(recommended_movie_names) < 5:
        recommended_movie_names.append("Poster Not Available")
        recommended_movie_posters.append(NO_POSTER_URL)

    return recommended_movie_names, recommended_movie_posters


# ================= STREAMLIT UI =================

st.header("Movie Recommender System")

movies = pickle.load(open("model/movie_list.pkl", "rb"))
similarity = pickle.load(open("model/similarity.pkl", "rb"))

movie_list = movies["title"].values

selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button("Show Recommendation"):
    names, posters = recommend(selected_movie)

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])
