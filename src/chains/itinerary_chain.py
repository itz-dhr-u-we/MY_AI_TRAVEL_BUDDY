from langchain_groq import ChatGroq #used to interact with the Groq API for natural language processing tasks

from langchain_core.prompts import ChatPromptTemplate #used to create chat prompts for the language model   
from src.config.config import GROQ_API_KEY #used to access the GROQ API key from the config file 


#initiailize llm model
llm = ChatGroq(
    groq_api_key=GROQ_API_KEY, # Pass the GROQ API key to the ChatGroq constructo
    model="llama-3.3-70b-versatile", # Specify the language model to use
    temperature=0.3, # Set the temperature for controlling the randomness of the model's responses
    # why temperature? - The temperature parameter is used to control the randomness of the model's responses. A higher temperature (e.g., 1.0) will make the model's output more random and creative, while a lower temperature (e.g., 0.2) will make the output more focused and deterministic.
    # In this case, a temperature of 0.3 is chosen to strike a balance between creativity and coherence in the model's responses.
)
itinerary_prompt = ChatPromptTemplate([
    ("system", "You are a helpful travel assistant that helps users plan their trips. You can provide information about destinations, suggest activities, and help with travel arrangements.Create a detailed itinerary for the user based on their preferences:{user_preferences} and requirements:{user_requirements}. Provide a brief,bulleted list of the itinerary, including the destinations, activities, and travel arrangements. Make sure to include any specific requirements mentioned by the user."),
    ("human","Create an itinerary for my trip to {destination} for {duration} days. I prefer {user_preferences} and have the following requirements: {user_requirements}.")
])

def generate_itinerary(destination: str, duration: int, user_preferences: str, user_requirements: str) -> str:
    llm_response = llm.invoke(
        itinerary_prompt.format_messages(destination=destination, duration=duration, user_preferences=user_preferences, user_requirements=user_requirements)
    )
    return llm_response.content

    #response is a dict with a content key that contains the generated itinerary as a string. The function returns this string, which can then be used to display the itinerary to the user or for further processing.