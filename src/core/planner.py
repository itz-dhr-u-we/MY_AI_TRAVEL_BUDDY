from langchain_core.messages import HumanMessage, AIMessage #used to create messages for the language model
from src.chains.itinerary_chain import generate_itinerary #used to generate an itinerary based on user preferences and requirements
from src.utils.logger import get_logger #used to get a logger for logging information and errors
from src.utils.custom_exception import CustomException #used to define a custom exception for handling errors in the planner

class TravelPlanner:
    def __init__(self):
        self.messages = [] # Initialize an empty list to store messages for the language model
        self.destination = ""# Initialize an empty string to store the destination for the trip
        self.duration = 0 # Initialize a variable to store the duration of the trip
        self.user_preferences = "" # Initialize a variable to store the user's preferences
        self.user_requirements = "" # Initialize a variable to store the user's requirements
        self.logger = get_logger(__name__)

        self.logger.info("TravelPlanner initialized successfully.")

    def set_destination(self, destination: str):
        try:
            self.destination = destination
            self.messages.append(HumanMessage(content=f"Destination set to {destination}"))
            self.logger.info(f"Destination set to {destination}")
        except Exception as e:
            self.logger.error(f"Error setting destination: {e}")
            raise CustomException("Failed to set destination", e)

    def set_duration(self, duration: int):
        try:
            self.duration = duration
            self.messages.append(HumanMessage(content=f"Duration set to {duration} days"))
            self.logger.info(f"Duration set to {duration} days")
        except Exception as e:
            self.logger.error(f"Error setting duration: {e}")
            raise CustomException("Failed to set duration", e)

    def set_user_preferences(self, preferences: str):
        try:
            self.user_preferences = preferences
            self.messages.append(HumanMessage(content=f"User preferences set to {preferences}"))
            self.logger.info(f"User preferences set to {preferences}")
        except Exception as e:
            self.logger.error(f"Error setting user preferences: {e}")
            raise CustomException("Failed to set user preferences", e)

    def set_user_requirements(self, requirements: str):
        try:
            self.user_requirements = requirements
            self.messages.append(HumanMessage(content=f"User requirements set to {requirements}"))
            self.logger.info(f"User requirements set to {requirements}")
        except Exception as e:
            self.logger.error(f"Error setting user requirements: {e}")
            raise CustomException("Failed to set user requirements", e)
    
    def create_itinerary(self):
        try:
            self.logger.info("Generating itinerary...")
            generated_itinerary = generate_itinerary(
                destination=self.destination,
                duration=self.duration,
                user_preferences=self.user_preferences,
                user_requirements=self.user_requirements
            )
            self.itinerary = generated_itinerary
            self.messages.append(AIMessage(content=f"Generated itinerary: {generated_itinerary}"))
            self.logger.info("Itinerary generated successfully.")
            return generated_itinerary
        except Exception as e:
            self.logger.error(f"Error generating itinerary: {e}")
            raise CustomException("Failed to generate itinerary", e)
            