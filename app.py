import streamlit as st
from openai import OpenAI

# 1. Stable Page Configuration Setup
st.set_page_config(
    page_title="Aesthetic Content Engine | Iselune Design",
    page_icon="✦",
    layout="centered"
)

# 2. Seamless Global Interface Styling (No "box-in-a-box" layouts)
st.markdown(
    """
    <style>
    /* Force the main background and text colors to be perfectly uniform */
    .stApp {
        background-color: #faf7f2 !important; /* Soft warm linen background */
        color: #51463e !important;
    }
    
    /* Clean up default application spacing and headers */
    header {visibility: hidden !important; display: none !important;}
    footer {visibility: hidden !important; display: none !important;}
    [data-testid="stHeader"] {display: none !important;}
    .stAppDeployButton {display: none !important;}
    #MainMenu {visibility: hidden !important; display: none !important;}
    [data-testid="stViewerBadge"] {display: none !important;}
    [data-testid="stDecoration"] {display: none !important;}
    [data-testid="stToolbar"] {display: none !important; visibility: hidden !important;}
    
    /* Center and elegantly constrain the maximum container width */
    .block-container {
        max-width: 550px !important;
        padding-top: 3rem !important;
        padding-bottom: 3rem !important;
    }

    /* Style titles and captions to align with luxury branding */
    h1 {
        font-family: 'Georgia', serif !important;
        font-weight: 400 !important;
        color: #40352e !important;
        font-size: 30px !important;
        letter-spacing: 0.5px !important;
        margin-bottom: 8px !important;
    }
    
    .subtitle-text {
        font-size: 14px !important;
        color: #8c7b70 !important;
        line-height: 1.6 !important;
        margin-bottom: 25px !important;
    }

    /* Format input form field label markers elegantly */
    div[data-testid="stWidgetLabel"] p {
        font-size: 11px !important;
        font-weight: 600 !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        color: #8c7b70 !important;
    }

    /* Beautiful, cohesive styling for inputs and selects */
    div[data-baseweb="select"] > div, textarea {
        background-color: #ffffff !important;
        border: 1px solid #e6ded6 !important;
        border-radius: 10px !important;
        color: #51463e !important;
    }

    textarea:focus, div[data-baseweb="select"] > div:focus-within {
        border-color: #bfa895 !important;
        box-shadow: 0 0 0 3px rgba(191, 168, 149, 0.15) !important;
    }

    /* Earthy Premium Action Button Customization */
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
        margin-top: 10px !important;
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

# 3. Dynamic Logo Path Definition from GitHub
github_logo_url = "https://githubusercontent.com"

# 4. Content Presentation Layout Block
st.markdown(
    f"""
    <div style="text-align: center;">
        <img src="{github_logo_url}" style="max-width: 160px; height: auto; margin-bottom: 16px;" alt="Iselune Design">
        <h1>Aesthetic Content Engine</h1>
        <p class="subtitle-text">Generate high-converting, luxury social media captions for your templates in seconds.</p>
    </div>
    """, 
    unsafe_allow_html=True
)

# 5. Core Operational Form Layout (Ensuring reliable alignment)
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
                
                # Render final results cleanly on page reload
                st.markdown("---")
                st.success("Your Content is Ready!")
                st.write(response.choices[0].message.content)
                
            except Exception as e:
                st.error("An error occurred while generating copy. Please try again.")
