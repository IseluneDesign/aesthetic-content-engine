import streamlit as st
from openai import OpenAI

# 1. Reliable Page Configuration Setup
st.set_page_config(
    page_title="Aesthetic Content Engine | Iselune Design",
    page_icon="✦",
    layout="centered"
)

# 2. Complete Boho-Celestial Component Overhaul
st.markdown(
    """
    <style>
    /* 1. Global Page Background & Base Text */
    .stApp, [data-testid="stAppViewContainer"] {
        background-color: #faf7f2 !important; /* Soft warm linen background */
        color: #51463e !important;
    }
    
    /* Hide native Streamlit headers, toolbars, and menus */
    header, footer, [data-testid="stHeader"], .stAppDeployButton, #MainMenu, [data-testid="stViewerBadge"], [data-testid="stDecoration"], [data-testid="stToolbar"] {
        visibility: hidden !important; 
        display: none !important;
    }
    
    /* Layout alignment and sizing */
    .block-container {
        max-width: 520px !important;
        padding-top: 2.5rem !important;
        padding-bottom: 3rem !important;
    }

    /* Typography headers styling */
    h1 {
        font-family: 'Georgia', serif !important;
        font-weight: 400 !important;
        color: #40352e !important;
        font-size: 28px !important;
        letter-spacing: 0.5px !important;
        margin-bottom: 8px !important;
        text-align: center;
    }
    
    .subtitle-text {
        font-size: 14px !important;
        color: #8c7b70 !important;
        line-height: 1.6 !important;
        margin-bottom: 30px !important;
        text-align: center;
    }

    /* 2. Form Labels (Fixes the invisible text above boxes) */
    div[data-testid="stWidgetLabel"] p {
        font-size: 11px !important;
        font-weight: 600 !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        color: #7a6c61 !important; /* Richer taupe color so you can actually read it */
        margin-bottom: 4px !important;
    }

    /* 3. Dropdown Bars, Inputs, & Textareas (Restyled out of dark mode) */
    div[data-baseweb="select"] > div, textarea, [data-testid="stTextArea"] textarea {
        background-color: #ffffff !important;
        border: 1px solid #e6ded6 !important;
        border-radius: 10px !important;
        color: #51463e !important;
    }
    
    /* Input interactive focus state indicators */
    textarea:focus, div[data-baseweb="select"] > div:focus-within {
        border-color: #bfa895 !important;
        box-shadow: 0 0 0 3px rgba(191, 168, 149, 0.15) !important;
    }

    /* 4. EXHAUSTIVE DROPDOWN PANEL OVERRIDE (Fixes the opened dropdown lists) */
    div[data-baseweb="popover"], div[role="listbox"], ul[role="listbox"] {
        background-color: #ffffff !important;
        border: 1px solid #e6ded6 !important;
        border-radius: 10px !important;
    }
    
    li[role="option"] {
        background-color: #ffffff !important;
        color: #51463e !important;
        font-size: 14px !important;
        padding: 10px 14px !important;
        transition: background-color 0.2s ease;
    }
    
    /* Highlight color when hovering options inside dropdown menu */
    li[role="option"]:hover, li[data-highlighted="true"] {
        background-color: #faf7f2 !important;
        color: #40352e !important;
    }

    /* Fixing default select text alignment color properties */
    div[data-baseweb="select"] [aria-selected="true"] {
        color: #51463e !important;
    }

    /* 5. Earthy Premium Action Button styling */
    div.stButton > button {
        width: 100% !important;
        background-color: #51463e !important; /* Elegant deep espresso brown */
        color: #faf7f2 !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 14px !important;
        font-size: 13px !important;
        font-weight: 600 !important;
        letter-spacing: 1px !important;
        text-transform: uppercase !important;
        transition: all 0.2s ease !important;
        margin-top: 15px !important;
        box-shadow: 0 4px 15px rgba(81, 70, 62, 0.15) !important;
    }

    div.stButton > button:hover {
        background-color: #40352e !important;
        box-shadow: 0 6px 20px rgba(81, 70, 62, 0.25) !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. Dynamic Logo Path Mapping (Updated to look for logo.png asset)
github_logo_url = "https://githubusercontent.com"

# 4. Main Presentation Layout Section
st.markdown(
    f"""
    <div style="text-align: center;">
        <img src="{github_logo_url}" style="max-width: 150px; height: auto; margin-bottom: 12px;" alt="Iselune Design">
        <h1>Aesthetic Content Engine</h1>
        <p class="subtitle-text">Generate high-converting, luxury social media captions for your templates in seconds.</p>
    </div>
    """, 
    unsafe_allow_html=True
)

# 5. Core Operational Form Inputs
niche = st.selectbox(
    "What template are you using today?",
    ["Med Spa & Esthetician", "Hair Stylist & Nail Tech", "Wedding Invitations & Events", "Seasonal & Holidays"]
)

topic = st.text_area(
    "What is the specific topic, announcement, or offer for this post?",
    placeholder="e.g., A 10% off flash sale on lip fillers, or Saturday lash openings..."
)

tone = st.selectbox(
    "What tone of voice should the caption use?",
    ["Luxurious & Elegant", "Friendly & Welcoming", "Educational & Expert", "Witty & Trendy"]
)

# 6. AI Generation Processing Pipeline
if st.button("Generate Caption"):
    if not topic.strip():
        st.warning("Please type a topic or announcement first!")
    else:
        if "OPENAI_API_KEY" in st.secrets:
            api_key = st.secrets["OPENAI_API_KEY"]
        else:
            st.error("API Key missing. Please configure OPENAI_API_KEY in Streamlit Secrets.")
            st.stop()
            
        client = OpenAI(api_key=api_key)
        
        with st.spinner("Crafting your copy..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    max_tokens=450,  
                    temperature=0.7,
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are an expert social media copywriter specializing in high-end aesthetic branding, "
                                "beauty businesses, and luxury weddings. Your task is to write a high-converting Instagram caption. "
                                "Structure the final output beautifully using clear spacing and formatting so the user can easily copy and paste it into their templates:\n\n"
                                "1. ✨ **HOOK:** 2-3 variations of punchy, attention-grabbing opening lines tailored for a visual graphic.\n"
                                "2. 📝 **BODY COPY:** An engaging, value-packed caption that flows smoothly into a clear Call to Action (CTA).\n"
                                "3. 🏷️ **HASHTAGS:** 5-10 highly relevant, aesthetic hashtags matching their specific niche."
                            )
                        },
                        {
                            "role": "user",
                            "content": f"Category: {niche}\nTopic/Offer: {topic}\nTone: {tone}"
                        }
                    ]
                )
                
                # Render results below the form
                st.markdown("---")
                st.success("Your Content is Ready!")
                st.write(response.choices[0].message.content)
                
            except Exception as e:
                st.error("An error occurred while generating copy. Please try again.")
