def photostack(image_url1,image_url2,image_url3):
    import streamlit as st

    st.components.v1.html(f"""
    <style>
    .photopile {{
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        justify-content: center;
        max-width: 100%;
        margin-top: 30px;
    }}

    .photopile figure {{
        display: inline-block;
        background: #e3cfbc;
        box-shadow: 0 0 0.4rem rgba(0, 0, 0, 0.75);
        margin: 0 -25px;
        transition: transform 0.2s;
        transform: scale(1) rotate(2deg);
    }}

    .photopile figure img {{
        max-width: calc(100%);
        margin: 1rem 1rem 0 1rem;
        border: none;
    }}

    .photopile figcaption {{
        text-align: center;
        margin: 0.5rem 1rem 1rem 1rem;
        font-size: 1rem;
        color: #471515;
    }}

    .photopile button {{
        background: none;
        border: none;
        max-width: 80%;
        cursor: pointer;
    }}

    .overlay {{
        display: none;
        position: fixed;
        top: 0;
        left: 0;
        height: 100vh;
        width: 100vw;
        background: rgba(0, 0, 0, 0.5);
        z-index: 998; /* Behind popover (999) */
        }}
    .overlay.active {{
        display: block;
    }}

    .photopile button:hover figure {{
        transform: scale(1.1);
        z-index: 10;
        }}


    .photopile button:nth-child(2n) {{ transform: rotate(-10deg); }}
    .photopile button:nth-child(3n) {{ transform: rotate(5deg); }}
    .photopile button:nth-child(4n) {{ transform: rotate(4deg); }}
    .photopile button:nth-child(5n) {{ transform: rotate(-2deg); }}
    .photopile button:nth-child(6n) {{ transform: rotate(-7deg); }}

    /* Popover modal styling */
    .popover {{
        display: none;
        position: fixed;
        top: 50vh;
        left: 50vw;
        transform: translate(-50%, -50%);
        background: #e3c4a6;
        z-index: 999;
        border-radius: 5px;
        box-shadow: 0 0 0.4rem rgba(0, 0, 0, 0.75);
        padding: 1rem;
        text-align: center;
    }}

    .popover.active {{
        display: block;
    }}

    .popover img {{
        width: 50vmin;
        border: 1px inset #e3c4a6;
        margin-bottom: 1rem;
    }}

    .popover figcaption {{
        font-size: 1.5rem;
        color: #471515;
        margin-bottom: 1rem;
    }}

    .close-btn {{
        background: #471515;
        color: #e3c4a6;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        cursor: pointer;
    }}
    </style>

    <div class="photopile">
    <button onclick="openPopover('photo1')">
        <figure>
        <img src={image_url1} alt="">
        <figcaption>caption 1</figcaption>
        </figure>
    </button>
    <button onclick="openPopover('photo2')">
        <figure>
        <img src={image_url2} alt="">
        <figcaption>caption 2</figcaption>
        </figure>
    </button>
    <button onclick="openPopover('photo3')">
        <figure>
        <img src={image_url3} alt="">
        <figcaption>caption 3</figcaption>
        </figure>
    </button>
    </div>

    <!-- Popover modals -->
    <div class="overlay" id="overlay1" onclick="closePopover('photo1')"></div>
    <div class="popover" id="photo1">
    <figure>
        <img src={image_url1} alt="">
        <figcaption>big caption 1</figcaption>
        <button class="close-btn" onclick="closePopover('photo1')">Close</button>
    </figure>
    </div>
    <div class="overlay" id="overlay2" onclick="closePopover('photo2')"></div>
    <div class="popover" id="photo2">
    <figure>
        <img src={image_url2} alt="">
        <figcaption>big caption 2</figcaption>
        <button class="close-btn" onclick="closePopover('photo2')">Close</button>
    </figure>
    </div>
    <div class="overlay" id="overlay3" onclick="closePopover('photo3')"></div>
    <div class="popover" id="photo3">
    <figure>
        <img src={image_url3} alt="">
        <figcaption>big caption 3</figcaption>
        <button class="close-btn" onclick="closePopover('photo3')">Close</button>
    </figure>
    </div>

    <script>
    function openPopover(id) {{
        document.getElementById(id).classList.add("active");
        document.getElementById("overlay" + id.replace("photo", "")).classList.add("active");
    }}

    function closePopover(id) {{
        document.getElementById(id).classList.remove("active");
        document.getElementById("overlay" + id.replace("photo", "")).classList.remove("active");
    }}
    </script>
    """, height=500)    