import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd
from folium import IFrame
st.set_page_config(layout="wide")

page = st.sidebar.radio("Choose a page:", ("Home", "Page 1", "Page 2"))
    

# Load data from CSV
@st.cache_data
def load_data():
    return pd.read_csv("datav.csv")

data = load_data()

# Create a Folium map centered at the first location
m = folium.Map(location=[data['lat'][1], data['lon'][1]], zoom_start=12)

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

# Add markers with the improved popups
for _, row in data.iterrows():
    iframe = IFrame(create_popup_html(row["name"], row["text"], row["img"]), width=300, height=200)
    
    folium.Marker(
        location=[row["lat"], row["lon"]],
        popup=folium.Popup(iframe, max_width=300),
        tooltip=row["name"]
    ).add_to(m)

if page == "Home":

    # Display the map in Streamlit
    st.title("Example Map")
    st.write("Click on a marker to see details.")
    st_folium(m, width=1050, height=500)

elif page == "Page 1":
    st.title("Page 1")
    st.write("This is Page 1 content.")
    st.write("You can add other widgets or data here.")

elif page == "Page 2":
    st.title("Page 2")
    st.write("This is Page 2 content.")
    st.write("Add whatever you need here as well.")