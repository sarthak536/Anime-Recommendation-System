import streamlit as st
import pickle
import pandas as pd
import requests
import streamlit_lottie
import json


st.set_page_config(page_title="Anime Recommendation System", page_icon=":sports_medal:", layout="wide")

def recommend(animes):
    anime_index = anime[anime['title'] == animes].index[0]
    distance = similarity[anime_index]
    anime_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_anime = []
    recommended_anime_posters=[]
    for i in anime_list:
        recommended_anime.append(anime.iloc[i[0]].title)
        recommended_anime_posters.append(anime.iloc[i[0]].mainpic)
    return recommended_anime,recommended_anime_posters




anime_dict=pickle.load(open('anime_dict.pkl','rb'))
anime = pd.DataFrame(anime_dict)
similarity=pickle.load(open('similarity.pkl','rb'))
streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap');

			html, body, [class*="css"]  {
			font-family: 'Roboto', sans-serif;
			}
			</style>
			"""
st.markdown(streamlit_style, unsafe_allow_html=True)

st.markdown("""
<style>
.big-font {
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)

with st.container():
    left_column, right_column=st.columns([0.2,0.8])
    with left_column:
        url = requests.get("https://lottie.host/ff8d2a1f-c56a-4eec-bc23-d4cb6f56f026/m0yAAxwuH1.json")

        url_json = dict()

        if url.status_code == 200:
            url_json = url.json()
        else:
            print("Error in the URL")

        st.lottie(url_json, height=300, width=300)

    with right_column:

        st.title(':red[What] is anime?')

        st.markdown(
            '<p class="big-font">Anime is an art form originating from Japan. The word anime is derived from the english word "Animation" however it has now evolved into animation with a specific art style originating mainly from Japan but has some enteries from South Korea as well as China. It has also went on to inspire many western shows such as Avatar: The Last Airbender as well as leading to western adaptations made by companies such as Netflix, Amazon, etc. Anime are mainly adapted from 3 different sources: Manga (Comic Books), Light Novels (Books with some illusrations sprinkled in and Anime Originals where the storyline is specifically created for a new anime.</p>',
            unsafe_allow_html=True)
st.divider()

with st.container():
    l_column, r_column=st.columns([0.85,0.15])
    with l_column:

        st.title(':rainbow[Anime Recommendation System]')

        selected_anime_name = st.selectbox('Select your Anime: ', anime['title'].values)

    with r_column:
        url = requests.get("https://lottie.host/d2031295-2382-49d6-8603-4f051f17083d/WvuCqC2I5w.json")

        url_json_justaway = dict()

        if url.status_code == 200:
            url_json_justaway = url.json()
        else:
            print("Error in the URL")

        st.lottie(url_json_justaway, height=200, width=200)

if st.button('Recommend'):
    names,posters=recommend(selected_anime_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

st.divider()

with st.container():
    l1, r1=st.columns([0.3,0.7])
    with l1:
        url = requests.get("https://lottie.host/abad261f-a6d3-4161-92b7-4218da1b4177/PoI3Bjp36x.json")

        url_json_bye = dict()

        if url.status_code == 200:
            url_json_bye = url.json()
        else:
            print("Error in the URL")
        st.lottie(url_json_bye, height=300, width=300)

    with r1:
        st.header('How to use our :red[program]')
        st.markdown('<p class="big-font">Our website is very easy to use, all you need to do is input an anime you like and the system will recommend you 5 anime based on the one you have selected. We handpick each recommendation based on factors like storytelling, character development, animation quality, and overall impact.</p>', unsafe_allow_html=True)