import streamlit as st
import requests
from datetime import date, datetime

# --- 1. LITURGICAL DATA & THEME ---
try:
    res = requests.get("http://calapi.inadiutorium.cz/api/v1/calendars/general-en/today").json()
    celebration = res['celebrations'][0]
    saint = celebration['title']
    color_name = celebration['colour']
except:
    saint = "Ordinary Time"; color_name = "green"

color_map = {"green": "#228B22", "purple": "#800080", "red": "#B22222", "white": "#DAA520", "violet": "#800080"}
app_color = color_map.get(color_name.lower(), "#228B22")

st.set_page_config(page_title="Catholic Daily", page_icon="✝️")

st.markdown(f"<style>[data-testid='stSidebar'] {{background-color: {app_color};}} [data-testid='stSidebar'] * {{color: white !important;}}</style>", unsafe_allow_html=True)

# --- 2. NAVIGATION ---
page = st.sidebar.radio("Go to:", ["Daily Home", "Today's Readings", "Daily Reflection", "Holy Rosary", "Confession Guide", "Prayer Library", "Novena Tracker"])

# --- 3. PAGES ---
if page == "Daily Home":
    st.title("🙏 Catholic Daily")
    st.write(f"### {date.today().strftime('%A, %B %d, %Y')}")
    st.info(f"**Today's Saint/Feast:** {saint}")
    st.write("Welcome to your spiritual companion. Let us walk with the Lord today.")

elif page == "Today's Readings":
    st.title("📖 Daily Mass Readings")
    try:
        readings_res = requests.get(f"https://bible-api.com/verse_of_the_day?translation=dra").json()
        st.subheader("The Gospel")
        st.write(f"*{readings_res['verse']['text']}*")
        st.caption(f"— {readings_res['verse']['name']} (Douay-Rheims)")
    except:
        st.write("Check your connection to load the Word.")

elif page == "Daily Reflection":
    st.title("✍️ My Spiritual Journal")
    st.write("Reflect on today's Gospel. What is God saying to you?")
    
    reflection = st.text_area("Write your thoughts here...", placeholder="Today, the Gospel touched my heart because...")
    
    if st.button("Complete Reflection"):
        st.balloons()
        st.success("Reflection recorded in your heart! God bless you.")
    
    st.divider()
    st.subheader("Reflection Guide")
    st.write("**1. Observe:** What happened in the reading?")
    st.write("**2. Reflect:** How does this apply to my life right now?")
    st.write("**3. Pray:** Talk to Jesus about it.")
    st.write("**4. Act:** One small thing I will do today because of this Word.")

elif page == "Holy Rosary":
    st.title("📿 The Holy Rosary")
    day_of_week = datetime.now().strftime('%A')
    mysteries = {"Monday": "Joyful", "Tuesday": "Sorrowful", "Wednesday": "Glorious", "Thursday": "Luminous", "Friday": "Sorrowful", "Saturday": "Joyful", "Sunday": "Glorious"}
    st.success(f"Today is {day_of_week}: Pray the **{mysteries[day_of_week]} Mysteries**.")

elif page == "Confession Guide":
    st.title("🕊️ Confession Guide")
    st.write("**Examination of Conscience:**")
    st.checkbox("Have I loved God above all things?")
    st.checkbox("Have I been kind and forgiven others?")

elif page == "Prayer Library":
    st.title("📚 Prayer Book")
    p = st.selectbox("Choose:", ["Anima Christi", "St. Michael Prayer", "The Angelus"])
    if p == "Anima Christi": st.write("Soul of Christ, sanctify me...")
    elif p == "St. Michael Prayer": st.write("St. Michael the Archangel, defend us in battle...")
    else: st.write("The Angel of the Lord declared unto Mary...")

elif page == "Novena Tracker":
    st.title("⏳ Novena")
    day = st.slider("Day", 1, 9)
    st.progress(day/9)
