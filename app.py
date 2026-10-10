import streamlit as st
from openai import OpenAI

# 1. Page Configuration & Styling
st.set_page_config(page_title="Aesthetic Content Engine", page_icon="✨", layout="centered")

st.markdown("""
    <style>
    /* Change background and font colors */
    .main {background-color: #FAF9F6;}
    h1 {color: #2C2C2C; font-family: 'Helvetica Neue', sans-serif;}
    
    /* Style the custom action button */
    div.stButton > button:first-child {
        background-color: #2C2C2C;
        color: white;
        border-radius: 8px;
        padding: 10px 24px;
        border: none;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Target and completely remove the upper right toolbar (Share, Star, running status) */
    [data-testid="stHeader"] {
        display: none !important;
    }
    .stAppDeployButton {
        display: none !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("✨ Aesthetic Content Engine")
st.write("Generate high-converting, luxury social media captions for your templates in seconds.")

# 2. Frontend Form Questions
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

# 3. AI Generation Trigger
if st.button("Generate Caption"):
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
        
        with st.spinner("Crafting your copy..."):
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
                
                # Output the finished result onto the user's screen
                st.markdown("---")
                st.success("Your Content is Ready!")
                st.write(response.choices[0].message.content)
                
            except Exception as e:
                st.error("An error occurred while generating copy. Please try again.")
