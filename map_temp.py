# Map Page

import streamlit as st
from gsheets_connection import GSheetsConnection
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

col1, col2 = st.columns(2)

with col1:
    m = folium.Map(location=[38.79, -99.53], zoom_start=5)
