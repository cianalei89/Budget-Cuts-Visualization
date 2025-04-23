import streamlit as st
import folium
from streamlit_folium import st_folium
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from folium import IFrame
import time
from map_temp import map_with_popups, get_sheet


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

image_url1 = "https://i.postimg.cc/Gmt2DWrf/Screenshot-2025-04-16-122811.png"
image_url2 = "https://i.postimg.cc/NfpF5shT/screenshot.png"
image_url3 = "https://i.postimg.cc/Gmqc7tMm/Screenshot-2025-04-16-123142.png"
photostack(image_url1,image_url2,image_url3)
#map storytelling
from streamlit_gsheets import GSheetsConnection
from streamlit_folium import st_folium
import pandas as pd
from folium import IFrame

# Function to create an interactive popup that simulates navigation

sheet_name = "Data for Visualization"  
tab = "Universities"  # tab name

# Fetch data from Google Sheets if not already in session
if 'data' not in st.session_state:
    st.session_state.data = get_sheet(sheet_name, tab)

df = st.session_state.data  # Use cached data

# Initialize story index
if 'i' not in st.session_state:
    st.session_state.i = 0

# Generate map with popups
m = map_with_popups(sheet_name, tab, df)

side1, side2 = st.columns(2)

with side2:
    st.header("Across the nation, professors and students are speaking out.")
    
    a, b, spacer = st.columns([2, 2, 6])  # Adjust as needed for spacing

    with a:
        if st.button("⬅ Previous"):
            st.session_state.i = (st.session_state.i - 1) % len(df)

    with b:
        if st.button("Next ➡"):
            st.session_state.i = (st.session_state.i + 1) % len(df)


    name = df.loc[st.session_state.i, "name"]
    story = df.loc[st.session_state.i, "story"]
    st.write(f"At {name}, {story}")

    st.write("Click on a marker to view photos")

    current = st.session_state.i
    total = len(df)
        
    # Dot tracker with ◌ and ◙
    dot_line = "".join(
        "◙ " if i == current else "◌ " for i in range(total)
    )
    st.markdown(
        f"<div style='text-align: center; font-size: 24px;'>{dot_line}</div>",
        unsafe_allow_html=True
    )

with side1:
    # Update map location to current story
    m.location = [df.loc[st.session_state.i, "lat"], df.loc[st.session_state.i, "lon"]]
    st_folium(m, width=700, height=600)
