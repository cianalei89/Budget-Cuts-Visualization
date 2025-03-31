import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd
from folium import IFrame
import time

st.set_page_config(layout="wide")

st.title("Welcome to Project _____")
st.write("We will add context and information and other here!")

col1, col2, col3 = st.columns(3)

with col1:
    button1 = st.button('Explore the Map')
with col2:
    button2 = st.button('Search the Database')
with col3:
    button3 = st.button('Learn About the Project')

if button1:
    st.switch_page("pages/map.py")
if button2:
    st.switch_page("pages/search.py")
if button3:
    st.switch_page("pages/about.py")
    