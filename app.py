import streamlit as st

# 1. Page Configuration Setup
st.set_page_config(
    page_title="Aesthetic Content Engine | Iselune Design",
    page_icon="✦",
    layout="centered"
)

# 2. Inject CSS to hide Streamlit padding and change the master background color
st.markdown(
    """
    <style>
        /* Force the entire background screen to match your aesthetic theme */
        .stApp {
            background-color: #faf7f2 !important;
        }
        /* Remove default Streamlit header and footer spacing blocks */
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .block-container {
            padding-top: 2rem !important;
            padding-bottom: 0rem !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. Dynamic Logo Path Definition
github_logo_url = "https://githubusercontent.com"

# 4. Integrated Aesthetic Interface Component Design
boho_interface_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <style>
        body, html {
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
            background-color: #faf7f2; /* Smooth warm linen background match */
            font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
            color: #51463e; /* Gentle, earthy charcoal-taupe text */
            display: flex;
            justify-content: center;
            align-items: flex-start;
            overflow: hidden;
        }

        .engine-card {
            background-color: #ffffff; /* Clean white canvas card dashboard layout */
            width: 100%;
            max-width: 500px;
            margin: 10px auto;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 12px 40px rgba(163, 145, 129, 0.12);
            border: 1px solid rgba(214, 201, 188, 0.5);
            box-sizing: border-box;
            text-align: center;
        }

        .brand-header {
            margin-bottom: 30px;
        }

        .brand-logo {
            display: block;
            max-width: 160px; /* Elegant scale fitting the logo geometry */
            height: auto;
            margin: 0 auto 16px;
        }

        h1 {
            font-family: 'Georgia', serif; /* Luxurious typography matching your logo */
            font-weight: 400;
            font-size: 26px;
            color: #40352e;
            margin: 0 0 8px 0;
            letter-spacing: 0.5px;
        }

        .subtitle {
            font-size: 13px;
            color: #8c7b70;
            margin: 0 0 25px 0;
            line-height: 1.5;
        }

        .form-group {
            text-align: left;
            margin-bottom: 20px;
        }

        label {
            display: block;
            font-size: 11px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: #8c7b70;
            margin-bottom: 8px;
        }

        select, textarea {
            width: 100%;
            box-sizing: border-box;
            background-color: #faf7f2;
            border: 1px solid #e6ded6;
            border-radius: 10px;
            padding: 12px 14px;
            font-size: 14px;
            color: #51463e;
            outline: none;
            transition: all 0.25s ease;
            font-family: inherit;
        }

        select {
            cursor: pointer;
            appearance: none;
            background-image: url("data:image/svg+xml;charset=UTF-8,%3Csvg xmlns='http://w3.org' width='12' height='12' viewBox='0 0 24 24' fill='none' stroke='%238c7b70' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
            background-repeat: no-repeat;
            background-position: right 14px center;
            padding-right: 40px;
        }

        textarea {
            resize: none;
            height: 90px;
            line-height: 1.5;
        }

        textarea::placeholder {
            color: #bcaea1;
            opacity: 0.6;
        }

        select:focus, textarea:focus {
            border-color: #bfa895;
            background-color: #ffffff;
            box-shadow: 0 0 0 3px rgba(191, 168, 149, 0.15);
        }

        .submit-btn {
            width: 100%;
            background-color: #51463e; /* Luxurious dark espresso shade */
            color: #faf7f2;
            border: none;
            border-radius: 10px;
            padding: 14px;
            font-size: 13px;
            font-weight: 600;
            letter-spacing: 1px;
            text-transform: uppercase;
            cursor: pointer;
            transition: all 0.2s ease;
            margin-top: 5px;
            box-shadow: 0 4px 15px rgba(81, 70, 62, 0.2);
        }

        .submit-btn:hover {
            background-color: #40352e;
            transform: translateY(-1px);
        }
    </style>
</head>
<body>

    <div class="engine-card">
        <div class="brand-header">
            <!-- Uses safe token replacement placeholder to load the image smoothly -->
            <img class="brand-logo" src="{LOGO_URL}" alt="Iselune Design Logo">
            <h1>Aesthetic Content Engine</h1>
            <div class="subtitle">Generate high-converting, luxury social media captions for your templates in seconds.</div>
        </div>

        <div class="form-group">
            <label for="template">What template are you using today?</label>
            <select id="template">
                <option>Med Spa & Esthetician</option>
                <option>Yoga Studio & Wellness</option>
                <option>Celestial Jewelry Boutique</option>
                <option>Boho Interior & Decor</option>
            </select>
        </div>

        <div class="form-group">
            <label for="topic">What is the specific topic, announcement, or offer?</label>
            <textarea id="topic" placeholder="e.g., A 10% off flash sale on lip fillers, or Saturday lash openings..."></textarea>
        </div>

        <div class="form-group">
            <label for="tone">What tone of voice should the caption use?</label>
            <select id="tone">
                <option>Luxurious & Elegant</option>
                <option>Mystic & Grounded</option>
                <option>Minimalist & Modern</option>
                <option>Warm & Welcoming</option>
            </select>
        </div>

        <button class="submit-btn">Generate Caption</button>
    </div>

</body>
</html>
"""

# Inject the GitHub logo path safely without formatting errors
final_html_render = boho_interface_code.replace("{LOGO_URL}", github_logo_url)

# Render the application cleanly inside Streamlit
st.components.v1.html(final_html_render, height=660, scrolling=False)
