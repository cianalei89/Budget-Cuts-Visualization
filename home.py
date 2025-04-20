import streamlit as st
import folium
from streamlit_folium import st_folium
from gsheets_connection import GSheetsConnection
import pandas as pd
from folium import IFrame
import time

st.set_page_config(layout="wide", initial_sidebar_state = "collapsed")
st.title("Welcome to the Stories of Science Project")
st.write(" ")
# st.write("We will add context and information and other here!")

col1, col2, col3, col4 = st.columns(4)

with col1:
    button1 = st.button('Explore the Map')
with col2:
    button2 = st.button('Search the Database')
with col3:
    button3 = st.button('Learn About the Project')
with col4:
    button4 = st.button('Find Resources')

if button1:
    st.switch_page("pages/map.py")
if button2:
    st.switch_page("pages/search.py")
if button3:
    st.switch_page("pages/about.py")
if button4:
    st.switch_page("pages/resources.py")
# st.write("#")

from animation import date_animation
import datetime
import time
START_DATE = datetime.date(2025, 1, 20)
date_animation(START_DATE)

from photostack import photostack
image_url1 = "https://i.postimg.cc/0jxwm8km/screenshot.png"
image_url2 = "https://i.postimg.cc/xCLmck2n/Screenshot-2025-04-16-122811.png"
image_url3 = "https://i.postimg.cc/D0gbPt0N/Screenshot-2025-04-16-123142.png"
photostack(image_url1,image_url2,image_url3)
#map storytelling
from streamlit_gsheets import GSheetsConnection
import folium
from streamlit_folium import st_folium
import pandas as pd
from folium import IFrame

# Load data from CSV
conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read()

# Function to create an interactive popup that simulates navigation
def create_popup_html(name, info, image_url):
    popup_html = f"""
    <div id="popup-main" style="width: 250px;">
        <h4>{name}</h4>
        <p>{info}</p>
        <img src="{image_url}" width="100%">
        <br><a href="#" onclick="document.getElementById('popup-main').style.display='none';document.getElementById('popup-more').style.display='block';">More Info</a>
    </div>

    <div id="popup-more" style="width: 250px; display: none;">
        <h4>Details for {name}</h4>
        <p>Here is additional information about this location.</p>
        <a href="#" onclick="document.getElementById('popup-more').style.display='none';document.getElementById('popup-main').style.display='block';">Back</a>
    </div>
    """
    return popup_html

side1, side2 = st.columns(2)

with side1:
    m = folium.Map(location=[38.79, -99.53], zoom_start=5, tiles=None)

    folium.TileLayer(
        tiles='https://tiles.stadiamaps.com/tiles/alidade_satellite/{z}/{x}/{y}{r}.jpg',
        attr='&copy; CNES, Distribution Airbus DS, © Airbus DS, © PlanetObserver (Contains Copernicus Data) | &copy; <a href="https://www.stadiamaps.com/" target="_blank">Stadia Maps</a> &copy; <a href="https://openmaptiles.org/" target="_blank">OpenMapTiles</a> &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        name='Stadia Alidade Satellite',
        min_zoom=0,
        max_zoom=20
    ).add_to(m)

    st_folium(m, width=1000, height=500)

with side2:
    st.header("This is a story")

    