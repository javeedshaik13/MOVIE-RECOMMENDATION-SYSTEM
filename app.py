import streamlit as st
import pickle
import pandas as pd
import requests
import os
import time
API_KEY = "df5d969bdb3fd702825dc3a59d32676e" ##this is my api key replace with your own

@st.cache_data
def load_data():
    raw = pickle.load(open('movie_dict.pkl', 'rb'))
    df = pd.DataFrame(raw)
    
    if 'poster_path' not in df.columns:
        poster_paths = []
        for movie_id in df['movie_id']:
            path = fetch_poster_path(movie_id)
            poster_paths.append(path)
            time.sleep(0.2) 
        df['poster_path'] = poster_paths
        with open('movie_dict.pkl', 'wb') as f:
            pickle.dump(df.to_dict(), f)
    return df
def fetch_poster_path(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    try:
        res = requests.get(url, timeout=5)
        res.raise_for_status()
        data = res.json()
        return data.get('poster_path')
    except:
        return None
    

def get_poster_url(poster_path):
    return f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else "https://via.placeholder.com/500x750.png?text=No+Image"

similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_df = load_data()

def recommend(movie_title):
    try:
        idx = movies_df[movies_df['title'] == movie_title].index[0]
    except IndexError:
        return [], []
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]
    titles = [movies_df.iloc[i[0]]['title'] for i in scores]
    posters = [get_poster_url(movies_df.iloc[i[0]]['poster_path']) for i in scores]
    return titles, posters


st.title("🎬 Movie Recommendation System")
st.markdown("Pick a movie and get 5 similar recommendations with posters!")

selected_movie = st.selectbox("Choose a movie:", [""] + list(movies_df['title'].values))

if st.button("Get Recommendations"):
    if selected_movie:
        st.subheader(f"Recommendations for: **{selected_movie}**")
        titles, posters = recommend(selected_movie)
        cols = st.columns(5)
        for i in range(len(titles)):
            with cols[i]:
                st.image(posters[i], width='stretch')
                st.caption(titles[i])
    else:
        st.warning("Please select a movie.")
