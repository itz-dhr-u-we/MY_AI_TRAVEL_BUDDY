import os
from dotenv import load_dotenv # Load environment variables from .env file

load_dotenv()# Load environment variables from .env file

GROQ_API_KEY = os.getenv("GROQ_API_KEY") # Get the GROQ API key from environment variables
