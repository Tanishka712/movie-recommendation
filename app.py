import streamlit as st
import pickle
import requests

# Load data
similarity = pickle.load(open(r"C:\Users\taish\OneDrive\Documents\mypythonprojects\movie recommendation\similarity.pkl", 'rb'))
movies = pickle.load(open(r"C:\Users\taish\OneDrive\Documents\mypythonprojects\movie recommendation\movies_list.pkl", 'rb'))
movies_list = movies['title'].values

st.header("Movie Recommendation System")

# Select box
selectvalue = st.selectbox('Select movie from dropdown', movies_list)

API_KEY = "bb66fdfb0e372887785390ef65a87cd0"

# Function to fetch poster
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    response = requests.get(url)
    data = response.json()
    
    poster_path = data.get('poster_path')
    if poster_path:
        full_path = "https://image.tmdb.org/t/p/w500" + poster_path
        return full_path
    else:
        return "https://via.placeholder.com/500x750?text=No+Poster"

# Recommendation function
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    
    recommended_movies = []
    recommended_posters = []
    for i in distances[1:6]:  # Skip the first (the selected movie itself)
        movie_id = movies.iloc[i[0]].id  # Ensure 'id' column exists in movies
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    
    return recommended_movies, recommended_posters

# Button action
if st.button("Show Recommendations"):
    movie_names, movie_posters = recommend(selectvalue)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(movie_names[0])
        st.image(movie_posters[0])
    with col2:
        st.text(movie_names[1])
        st.image(movie_posters[1])
    with col3:
        st.text(movie_names[2])
        st.image(movie_posters[2])
    with col4:
        st.text(movie_names[3])
        st.image(movie_posters[3])
    with col5:
        st.text(movie_names[4])
        st.image(movie_posters[4])
