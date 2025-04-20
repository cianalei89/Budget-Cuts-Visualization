# Map Page

import streamlit as st
from streamlit_gsheets import GSheetsConnection
import folium
from streamlit_folium import st_folium
import pandas as pd
from folium import IFrame

# Load data from google sheet
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


st.title("Explore the Map")

# Field Filtering function
unique_fields = data['field'].unique().tolist()

# Initialize session state if not present
if "selected_fields" not in st.session_state:
    st.session_state.selected_fields = unique_fields.copy()

# Multiselect box to choose fields
selected_fields = st.multiselect(
    'Select fields to display on the map:',
    unique_fields,
    default=st.session_state.selected_fields
)

# update session state if changed manually via multiselect
if selected_fields != st.session_state.selected_fields:
    st.session_state.selected_fields = selected_fields

# add select/deselect all buttons
btn_col1, btn_col2, _ = st.columns([1, 1, 8])
with btn_col1:
    if st.button("Select All"):
        st.session_state.selected_fields = unique_fields.copy()
        st.rerun()
with btn_col2:
    if st.button("Deselect All"):
        st.session_state.selected_fields = []
        st.rerun()

# filter the data based on selections
filtered_data = data[data['field'].isin(st.session_state.selected_fields)]

# Add markers
for _, row in filtered_data.iterrows():
    iframe = IFrame(create_popup_html(row["name"], row["text"], row["img"]), width=300, height=200)
    folium.Marker(
        location=[row["lat"], row["lon"]],
        popup=folium.Popup(iframe, max_width=300),
        tooltip=row["name"]
    ).add_to(m)


st.write("Click on a marker to view story details.")

# Show Map
st_folium(m, width=1560, height=650)

st.header("Share Your Story")
st.write("Use our submission form below to have your story featured on the map.")

name = st.text_input("What is your name? (Anonymous is okay)")
institution = st.text_input("What is your affiliated institution?")

state = st.selectbox(
    "What state are you located in?",
    ("Alabama",
    "Alaska",
    "Arizona",
    "Arkansas",
    "California",
    "Colorado",
    "Connecticut",
    "Delaware",
    "District of Columbia",
    "Florida",
    "Georgia",
    "Hawaii",
    "Idaho",
    "Illinois",
    "Indiana",
    "Iowa",
    "Kansas",
    "Kentucky",
    "Louisiana",
    "Maine",
    "Maryland",
    "Massachusetts",
    "Michigan",
    "Minnesota",
    "Mississippi",
    "Missouri",
    "Montana",
    "Nebraska",
    "Nevada",
    "New Hampshire",
    "New Jersey",
    "New Mexico",
    "New York",
    "North Carolina",
    "North Dakota",
    "Ohio",
    "Oklahoma",
    "Oregon",
    "Pennsylvania",
    "Rhode Island",
    "South Carolina",
    "South Dakota",
    "Tennessee",
    "Texas",
    "Utah",
    "Vermont",
    "Virginia",
    "Washington",
    "West Virginia",
    "Wisconsin",
    "Wyoming",
    ),
)
city = st.text_input("What city are you located in?")
zipcode = st.text_input("What is your zipcode?")
field = st.text_input("What is your field of research?")
info = st.text_input("Please share any information you would like us to share!")
email = st.text_input("Please share an email we can use to contact you")

import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

from io import StringIO
import json

creds_dict = dict(st.secrets["apikey"])

# Now it's safe to dump to JSON
creds_json = json.dumps(creds_dict)
creds_stream = StringIO(creds_json)

# Load credentials from the dict
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)
 
sh = client.open('submissions')

if st.button("Submit Your Story"):
    row = [name,info, institution, state, city, field, email]
    worksheet = sh.sheet1
    worksheet.append_row(row)
    st.success("Your story has been successfully submited, we will review it shortly!")
