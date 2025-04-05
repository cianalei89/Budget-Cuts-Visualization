# Search Page

import streamlit as st
from streamlit_gsheets import GSheetsConnection
import folium
from streamlit_folium import st_folium
import pandas as pd
from folium import IFrame

st.title("Search our Database:")

# Load data from CSV
conn = st.connection("gsheets", type=GSheetsConnection)
data = conn.read()

# Create search
text_search = st.text_input("Search stories by institution, field, or state:", value="")

m1 = data["name"].str.contains(text_search)
m2 = data["field"].str.contains(text_search)
m3 = data["state"].str.contains(text_search)
data_search = data[m1 | m2 | m3]

N_cards_per_row = 1
if text_search:
    if data_search.empty:
        st.write("Sorry, no stories currently exist in our database for your search criteria. Please consider submitting your own story to be added to our database.")
    else:
        for n_row, row in data_search.reset_index().iterrows():
            i = n_row%N_cards_per_row
            if i==0:
                st.write("---")
                cols = st.columns(N_cards_per_row, gap="large")
            # draw the card
            with cols[n_row%N_cards_per_row]:
                st.markdown(f"**{row['name']}** - {row['city']}, {row['state']}")
                st.markdown(f"{row['field']}")
                st.markdown(f"*{row['text']}*")
