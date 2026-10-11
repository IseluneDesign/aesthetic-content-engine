import streamlit as st
from openai import OpenAI

# 1. Page Configuration & Boho Styling
st.set_page_config(page_title="Aesthetic Content Engine", page_icon="🌿", layout="centered")

st.markdown("""
    <style>
    /* Boho Base Palette and Backgrounds */
    .main {background-color: #FAF6F0;}
    
    /* Elegant Serif Header styling mimicking custom boho fonts */
    h1 {
        color: #4A3E3D; 
        font-family: 'Georgia', serif;
        font-weight: 300;
        text-align: center;
    }
    .sub-text {
        color: #7D6B63;
        font-family: 'Helvetica Neue', sans-serif;
        text-align: center;
        margin-bottom: 25px;
    }
    
    /* Warm Earthy Inputs */
    div[data-testid="stSelectbox"] label, div[data-testid="stTextArea"] label {
        color: #4A3E3D !important;
        font-family: 'Georgia', serif;
        font-weight: bold;
    }
    
    div[data-testid="stSelectbox"] div[data-baseweb="select"], div[data-testid="stTextArea"] textarea {
        background-color: #FFFFFF !important;
        border: 1px solid #E6DFD3 !important;
        border-radius: 12px !important;
        color: #4A3E3D !important;
    }
    
    /* Terracotta Boho Action Button */
    div.stButton > button:first-child {
        background-color: #D4A373;
        color: white;
        border-radius: 20px;
        padding: 12px 30px;
        border: none;
        font-family: 'Georgia', serif;
        font-size: 16px;
        width: 100%;
        box-shadow: 0px 4px 10px rgba(212, 163, 115, 0.2);
        transition: all 0.3s ease;
    }
    
    div.stButton > button:first-child:hover {
        background-color: #BC6C25;
        color: white;
        box-shadow: 0px 6px 15px rgba(188, 108, 37, 0.3);
    }
    
    /* Completely hide menus, headers, and toolbars */
    #MainMenu {visibility: hidden !important; display: none !important;}
    header {visibility: hidden !important; display: none !important;}
    [data-testid="stHeader"] {display: none !important;}
    .stAppDeployButton {display: none !important;}
    
    /* Target and destroy the footer, viewer badge, and any floating profile bars at the bottom */
    footer {visibility: hidden !important; display: none !important;}
    .viewerBadge {display: none !important;}
    [data-testid="stViewerBadge"] {display: none !important;}
    [data-testid="stDecoration"] {display: none !important;}
    div[class^="st-emotion-cache"] > footer {display: none !important;}
    
    /* Force-hide the parent toolbar block that hosts the profile name badge */
    [data-testid="stToolbar"] {
        display: none !important;
        visibility: hidden !important;
    }
    
    /* Destroy any container hosting creator attribution names or badges at the root level */
    div[class*="viewer"], div[class*="Viewer"], div[class*="attribution"] {
        display: none !important;
        visibility: hidden !important;
    }
    
    /* Hide the entire bottom-right floating utilities grid block completely */
    div[class*="stStatusWidget"] {
        display: none !important;
        visibility: hidden !important;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Header and Logo Layout
# Using the raw path to pull your logo directly from your repository asset
logo_url = "https://githubusercontent.com"

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(logo_url, use_container_width=True)

st.markdown("<h1>Aesthetic Content Engine</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-text'>Generate high-converting, luxury social media captions for your templates in seconds.</p>", unsafe_allow_html=True)

# 3. Frontend Form Questions
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

# 4. AI Generation Trigger
if st.button("✨ Craft Content"):
    if not topic.strip():
        st.warning("Please type a topic or announcement first!")
    else:
        # Access the securely hidden OpenAI API key from Streamlit settings
        if "OPENAI_API_KEY" in st.secrets:
            api_key = st.secrets["OPENAI_API_KEY"]
        else:
            st.error("API Key missing. Please configure OPENAI_API_KEY in Streamlit Secrets.")
            st.stop()
            
        client = OpenAI(api_key=api_key)
        
        with st.spinner("Weaving your copy together..."):
            try:
                # Hidden system prompt instructions mimicking your FormWise build
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    max_tokens=450,  # Strict cap to prevent buyers from draining credits
                    temperature=0.7,
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are an expert social media copywriter specializing in high-end aesthetic branding, "
                                "bohemian lifestyle trends, beauty businesses, and luxury weddings. Your task is to write a high-converting Instagram caption. "
                                "Structure the final output beautifully using clear spacing, intentional line breaks, and earthy, warm aesthetic emojis (like ✨, 🌿, 🌾, 🤎, ✨) so the user can easily copy and paste it into their templates:\n\n"
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
                
                # Output the finished result onto the user's screen
                st.markdown("---")
                st.success("Your Content is Ready!")
                st.write(response.choices[0].message.content)
                
            except Exception as e:
                st.error("An error occurred while generating copy. Please try again.")
