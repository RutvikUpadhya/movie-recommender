import streamlit as st
import pickle
import numpy
import pandas as pd
import requests

API_Key = "fd4e9bbc"

def fetch_image_and_rating(movie):
    url = f"http://www.omdbapi.com/?apikey={API_Key}&t={movie}"
    data = requests.get(url).json()
    
    poster = data.get('Poster', 'N/A')
    if poster == 'N/A':
        poster = "Assets/noImage.jpg" 

    ratings = data.get('Ratings', [])

    if ratings == []:
        rating = 'N/A'
    else:
        rating = ratings[0].get("Value", 'N/A')

    return poster, rating

def display_movie(movie, image_url):
    st.markdown(f"""
    <div style="width:100%;">
    <div style="
        font-weight:bold;
        margin-bottom:8px;
        line-height:1.3em;
        height: 2.6em;              
        overflow-y:auto;           
        padding-right:4px;
    ">
        {movie}
    </div>
    </div>
    """, unsafe_allow_html=True)
    st.image(image_url)


def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    sim_list = similarity[movie_index]
    y = []
    sorted_sim_list = sorted(list(enumerate(sim_list)), reverse=True, key=lambda x: x[1])[1: 6]
    for i in sorted_sim_list:
        y.append(movies_df.iloc[i[0]].title)
    return y

movies_dict = pickle.load(open('model/movies_dict.pkl', 'rb'))
movies_df = pd.DataFrame(movies_dict)

similarity = pickle.load(open('model/similarity.pkl', 'rb'))

st.markdown(
    "<h1 style='text-align:center; font-size:4.25vw;'>MOVIE RECOMMENDER SYSTEM</h1>",
    unsafe_allow_html=True
)
def get_img(coln, n):
    with coln:
        
        image, rating = fetch_image_and_rating(list[n-1])
        # st.image(image)
        display_movie(list[n-1], image)
        st.write("")
        st.markdown(f'**IMDB** :  {rating}' )


choice = st.selectbox("Films_selection",movies_df['title'].values, index = None, placeholder = "Search a film", label_visibility="collapsed")
if choice is not None:
    
    st.markdown(f'### {choice.upper()}')
    image, rating = fetch_image_and_rating(choice)
    st.image(image)
    st.markdown(f'**IMDB** :  {rating}' )
    st.write("")
    st.write("")
    st.write("")
    st.subheader("Also Watch")
    st.write("")
    list = recommend(choice)
    col1, col2, col3,col4,col5 = st.columns(5)
    get_img(col1, 1)
    get_img(col2, 2)
    get_img(col3, 3)
    get_img(col4, 4)
    get_img(col5, 5)

