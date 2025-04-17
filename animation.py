
import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd
from folium import IFrame
import datetime
import time
START_DATE = datetime.date(2025, 1, 20)
def date_animation(date):
    START_DATE = date
    st.components.v1.html(f"""
        <!DOCTYPE html>
        <html>
        <head>
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@600&family=Silkscreen:wght@400;700&display=swap" rel="stylesheet">
            <style>
                /* Apply the custom font */
                body {{
                    font-family: "Roboto Mono", monospace;
                    font-optical-sizing: auto;
                    font-weight: 600;
                    font-style: normal;
                    text-align: center;
                    background-color: #471515;
                    overflow: visible;
                    word-wrap: break-word;
                    overflow-wrap: break-word;
                    color: #e3c4a6;
                }}

                body, html {{
                    height: 100%;
                    width: 100%;
                    overflow: visible;
                }}

                .content {{
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    height: 100%;
                    padding: 20px;
                }}
                .counter {{
                    font-weight: bold;
                    color: #F42C04;
                    font-size: 1.5em;
                }}
            </style>
            <script>
                function updateCounter() {{
                    let startDate = new Date("{START_DATE.isoformat()}Z");  // Ensure correct format
                    let now = new Date();

                    let timeDiff = now - startDate;

                    let days = Math.floor(timeDiff / (1000 * 60 * 60 * 24));
                    let hours = Math.floor((timeDiff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                    let minutes = Math.floor((timeDiff % (1000 * 60 * 60)) / (1000 * 60));
                    let seconds = Math.floor((timeDiff % (1000 * 60)) / 1000);

                    document.getElementById("days").textContent = days;
                    document.getElementById("hours").textContent = String(hours).padStart(2, '0');
                    document.getElementById("minutes").textContent = String(minutes).padStart(2, '0');
                    document.getElementById("seconds").textContent = String(seconds).padStart(2, '0');
                }}

                setInterval(updateCounter, 1000);  // Refresh every second
                window.onload = updateCounter;  // Run immediately when page loads
            </script>
        </head>
        <body>
            <h2 class="silkscreen"> It has been <br>
            <span id="days" class="counter">0</span> days, 
            <span id="hours" class="counter">00</span> hours, 
            <span id="minutes" class="counter">00</span> minutes, 
            <span id="seconds" class="counter">00</span> seconds <br>
            since the first budget cut was made.
            Scroll to see how these cuts have impacted people and research around the country.</h2>
        </body>
        </html>
    """, height=230)




