import streamlit as st
from dotenv import load_dotenv
from src.core.planner import TravelPlanner

st.set_page_config(page_title="AI Travel Planner", page_icon=":airplane:", layout="wide")
st.title("AI Travel Planner")
st.write("Plan your perfect trip with the help of AI! Enter your destination, duration, preferences, and requirements to get a personalized itinerary.")

load_dotenv()

with st.form("planner_form"):
    destination = st.text_input("Enter the name of your destination")
    duration = st.number_input("Enter the Duration (in days)", min_value=1, max_value=365)
    user_preferences = st.text_area("Enter your Preferences (e.g., nature, culture, adventure)")
    user_requirements = st.text_area("Enter your Requirements (e.g., budget, accessibility needs)")
    
    submit_button = st.form_submit_button("Generate Itinerary")
    if submit_button:
        if destination and duration and user_preferences and user_requirements:
            planner = TravelPlanner()
            planner.set_destination(destination)
            planner.set_duration(duration)
            planner.set_user_preferences(user_preferences)
            planner.set_user_requirements(user_requirements)
            
            with st.spinner("Generating your itinerary..."):
                itinerary = planner.create_itinerary()
                st.success("Itinerary generated successfully!")
                st.subheader("😎 Your Personalized Itinerary:")
                st.markdown(itinerary)
        else:
            st.warning("Please fill in all the fields.")
            