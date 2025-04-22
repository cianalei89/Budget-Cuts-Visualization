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
image_url1 = "https://i.postimg.cc/0jxwm8km/screenshot.png"
image_url2 = "https://i.postimg.cc/xCLmck2n/Screenshot-2025-04-16-122811.png"
image_url3 = "https://i.postimg.cc/D0gbPt0N/Screenshot-2025-04-16-123142.png"
photostack(image_url1,image_url2,image_url3)
#map storytelling
from streamlit_gsheets import GSheetsConnection
from streamlit_folium import st_folium
import pandas as pd
from folium import IFrame

# Load data from CSV
conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read()

# Function to create an interactive popup that simulates navigation
def create_popup_html(name, info, image_urls):
    image_list = image_urls.split(',') if isinstance(image_urls, str) else image_urls
    popup_html = f"""
    <div id="popup-main" style="width: 250px;">
        <h4>{name}</h4>
        <p>{info}</p>
        <img src="{image_list[0]}" width="100%">
        <img src="{image_list[1]}" width = "100%">
        <br><a href="#" onclick="document.getElementById('popup-main').style.display='none';document.getElementById('popup-more').style.display='block';">Click for more</a>
    </div>

    <div id="popup-more" style="width: 250px; display: none;">
        <h4>More about {name}</h4>
        <p>Here is additional information about this location.</p>
        <img src="{image_list[2]}" width = "100%">
        <a href="#" onclick="document.getElementById('popup-more').style.display='none';document.getElementById('popup-main').style.display='block';">Back</a>
    </div>
    """
    return popup_html



sheet_name = "Data for Visualization"  
tab = "Universities" # tab name
if 'data' not in st.session_state:
# If not cached, fetch data from Google Sheets
    st.session_state.data = get_sheet(sheet_name,tab)

df = st.session_state.data  # Use the cached data

m = map_with_popups(sheet_name,tab,df)
if 'i' not in st.session_state:
    st.session_state.i = 0

side1, side2 = st.columns(2)
    
with side2:
    st.header("Across the nation, professors and students are speaking out about these cuts.")
    a,b=st.columns(2)
    with a:
        if st.button("Next"):
            if st.session_state.i < len(df) - 1:  
                st.session_state.i += 1  
            else:
                st.warning("You have reached the last item.")
    with b:
        if st.button("Back"):
            if st.session_state.i > 0:  
                st.session_state.i -= 1  
            else:
                st.warning("You are already at the first item.")

    name = df.loc[st.session_state.i, "name"]
    story = df.loc[st.session_state.i, "story"]
    st.write(f"At {name}, {story}")


with side1:
    m.location = [df.loc[st.session_state.i, "lat"], df.loc[st.session_state.i, "lon"]]  # Update map location
    st_folium(m, width=700, height=600)
    





    