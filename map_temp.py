import streamlit as st
from streamlit_gsheets import GSheetsConnection
import folium
from streamlit_folium import st_folium
import pandas as pd
from folium import IFrame

def get_sheet(spreadsheet_name,tab):
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']


    from io import StringIO
    import json
    
    creds_dict = dict(st.secrets["apikey"])
    creds_json = json.dumps(creds_dict)
    creds_stream = StringIO(creds_json)


# Load credentials from the dict
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)
 
    sh = client.open(f'{spreadsheet_name}')
    worksheet = sh.worksheet(f'{tab}')  # Access the tab with the given name
    
    # Get all records (rows) from the sheet
    data = worksheet.get_all_records()  # Returns a list of dictionaries (rows)
    df = pd.DataFrame(data)  # Convert to a pandas DataFrame
    return df

def create_popup_html(name, info, image_urls):
    image_list = image_urls.split(',') if isinstance(image_urls, str) else image_urls
    # for i in range(len(image_list)):
    #     popup_html = f"""
    #     <div id="popup-main" style="width: 250px;">
    #         <h4>{name}</h4>
    #         <img src="{image_list[i]}" width="100%">
    #         <img src="{image_list[i+1]}" width = "100%">
    #         <img src="{image_list[i+2]}" width = "100%">
    #         <p>{info}</p>
    #         <br><a href="#" onclick="document.getElementById('popup-main').style.display='none';document.getElementById('popup-more').style.display='block';">Click for more</a>
    #     </div>


    #     <div id="popup-more" style="width: 250px; display: none;">
    #         <h4>More about {name}</h4>
    #         <p>Here is additional information about this location.</p>
    #         <a href="#" onclick="document.getElementById('popup-more').style.display='none';document.getElementById('popup-main').style.display='block';">Back</a>
    #     </div>
    #     """
    popup_html = f"""
    <div id="popup-main" style="width: 250px;">
        <h4>{name}</h4>
    """
    for i in range(len(image_list)):
        popup_html += f'<img src="{image_list[i].strip()}" width="200%"><br>'
    
    # Add additional information
    popup_html += f"""
        <p>{info}</p>
        <br><a href="#" onclick="document.getElementById('popup-main').style.display='none';document.getElementById('popup-more').style.display='block';">Click for more</a>
    </div>

    <div id="popup-more" style="width: 250px; display: none;">
        <h4>More about {name}</h4>
        <p>Here is additional information about this location.</p>
        <a href="#" onclick="document.getElementById('popup-more').style.display='none';document.getElementById('popup-main').style.display='block';">Back</a>
    </div>
    """
    return popup_html

def map_with_popups(sheet_name,tab,df):

    m = folium.Map(location=[df["lat"].mean(), df["lon"].mean()], zoom_start=10)

    for index, row in df.iterrows():  
        name = row['name']
        info = row['text']
        image_url = row["img"]

        iframe = IFrame(create_popup_html(name, info, image_url),width=500,height=400)
        
        folium.Marker(
            location=[row["lat"], row["lon"]],
            popup=folium.Popup(iframe, max_width=500),
            tooltip=row["name"]
        ).add_to(m)
    return m

