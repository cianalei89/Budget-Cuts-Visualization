# Map Page

import streamlit as st
from streamlit_gsheets import GSheetsConnection
import folium
from streamlit_folium import st_folium
import pandas as pd
from folium import IFrame

# Load data from CSV
conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read()

# Create a Folium map centered at the US
m = folium.Map(location=[38.79, -99.53], zoom_start=5)

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

# Filtering function
unique_fields = data['field'].unique()

selected_fields = st.multiselect(
    'Select fields to display on the map:',
    unique_fields,
    default=unique_fields  # Show all by default
)

if not selected_fields:
    selected_fields = unique_fields

# Filter data based on the selected fields
filtered_data = data[data['field'].isin(selected_fields)]


# Add markers with the improved popups
for _, row in filtered_data.iterrows():
    iframe = IFrame(create_popup_html(row["name"], row["text"], row["img"]), width=300, height=200)
    
    folium.Marker(
        location=[row["lat"], row["lon"]],
        popup=folium.Popup(iframe, max_width=300),
        tooltip=row["name"]
    ).add_to(m)


st.title("Explore the Map")
st.write("Click on a marker to view story details.")
st_folium(m, width=1560, height=650)