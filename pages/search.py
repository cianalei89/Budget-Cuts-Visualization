# Search Page

import streamlit as st
from streamlit_gsheets import GSheetsConnection
import folium
from streamlit_folium import st_folium
import pandas as pd
from folium import IFrame

st.title("Search our Database of Stories:")

# load data from google sheet
conn = st.connection("gsheets", type=GSheetsConnection)
data = conn.read()

# create search box
text_search = st.text_input("Search stories by institution, field, or state:", value="")

# filter data by the search input
if text_search:
    m1 = data["name"].str.contains(text_search, case=False, na=False)
    m2 = data["field"].str.contains(text_search, case=False, na=False)
    m3 = data["state"].str.contains(text_search, case=False, na=False)
    data_search = data[m1 | m2 | m3]
else:
    # show all the data by default (no search)
    data_search = data

# initialize session state for data pages
ENTRIES_PER_PAGE = 5
if "page_num" not in st.session_state:
    st.session_state.page_num = 0

# calculate total number of pages
total_entries = len(data_search)
total_pages = (total_entries - 1) // ENTRIES_PER_PAGE + 1

# slice data for current page
start_idx = st.session_state.page_num * ENTRIES_PER_PAGE
end_idx = start_idx + ENTRIES_PER_PAGE
current_data = data_search.iloc[start_idx:end_idx]

# display entries
if current_data.empty:
    st.write("Sorry, no stories currently exist in our database for your search criteria. Please consider submitting your own story to be added to our database.")
else:
    for n_row, row in current_data.reset_index().iterrows():
        st.write("---")
        st.markdown(f"**{row['name']}** - {row['city']}, {row['state_abb']}")
        st.markdown(f"{row['field']}")
        st.markdown(f"*{row['text']}*")

    # page navigation buttons for displaying > "ENTRIES_PER_PAGE" number of entries
    st.write("---")
    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        if st.session_state.page_num > 0:
            if st.button("⬅ Previous"):
                st.session_state.page_num -= 1

    with col2:
        st.markdown(f"<div style='text-align:center'>Showing stories {start_idx+1}-{min(end_idx, total_entries)} of {total_entries}</div>", unsafe_allow_html=True)

    with col3:
        if end_idx < total_entries:
            if st.button("Next ➡"):
                st.session_state.page_num += 1

