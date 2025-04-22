def photostack(image_url1,image_url2,image_url3):
    import streamlit as st

    st.components.v1.html(f"""
    <style>
    body {{
        margin: 0;
        padding-top: 5px;
    }}
    .photopile {{
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        justify-content: center;
        margin: 10px 0 10px 0;
    }}

    .photopile figure {{
        display: inline-block;
        background: #e3cfbc;
        box-shadow: 0 0 0.4rem rgba(0, 0, 0, 0.75);
        margin: -10px -25px 0 -15px;
        transition: transform 0.2s;
        transform: scale(0.7) rotate(2deg);
        transform-origin: top center;
    }}


    .photopile figure img {{
        max-width: 400px;
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
        max-width: 300px;
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
        transform: scale(.8);
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
        max-width: 90vw;
        max-height: 90vh;
        overflow: auto;
    }}

    .popover.active {{
        display: block;
    }}

    .popover img {{
        width: 50vmin;
        height: 50vmin;
        object-fit: contain;
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
        border-radius: 2px;
        cursor: pointer;
    }}
    </style>

    <div class="photopile">
    <button onclick="openPopover('photo1')">
        <figure>
        <img src={image_url1} alt="">
        <figcaption>Funding Frozen/Paused/Cancelled</figcaption>
        </figure>
    </button>
    <button onclick="openPopover('photo2')">
        <figure>
        <img src={image_url2} alt="">
        <figcaption>Federal Workers Put on Leave/In Limbo</figcaption>
        </figure>
    </button>
    <button onclick="openPopover('photo3')">
        <figure>
        <img src={image_url3} alt=" "style="max-height: 500px;>
        <figcaption>Funding Frozen/Paused/Cancelled</figcaption>
        </figure>
    </button>
    </div>

    <!-- Popover modals -->
    <div class="overlay" id="overlay1" onclick="closePopover('photo1')"></div>
    <div class="popover" id="photo1">
    <figure>
        <img src={image_url1} alt="">
        <figcaption>Testimony from theimpactproject.org</figcaption>
        <button class="close-btn" onclick="closePopover('photo1')">Close</button>
    </figure>
    </div>
    <div class="overlay" id="overlay2" onclick="closePopover('photo2')"></div>
    <div class="popover" id="photo2">
    <figure>
        <img src={image_url2} alt="">
        <figcaption>Testimony from theimpactproject.org</figcaption>
        <button class="close-btn" onclick="closePopover('photo2')">Close</button>
    </figure>
    </div>
    <div class="overlay" id="overlay3" onclick="closePopover('photo3')"></div>
    <div class="popover" id="photo3">
    <figure>
        <img src={image_url3} alt="";>
        <figcaption>Testimony from theimpactproject.org</figcaption>
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
    """, height=400)    