"""
Main module for running the Advanced Calculator application.
"""
import os
import logging
from dotenv import load_dotenv
from calculator import App

# Load environment variables from .env
load_dotenv()

# Configure logging: logging both to console and a file
logging.basicConfig(
    level=logging.INFO,  # Change to DEBUG for more verbosity
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # Console output
        logging.FileHandler('app.log')  # File output
    ]
)

def main():
    """Entry point for the Advanced Calculator application."""
    environment = os.getenv("ENVIRONMENT", "production")
    logging.info("Running in %s environment", environment)
    logging.info("Starting Advanced Calculator application")
    app = App()
    app.start()

if __name__ == "__main__":
    main()
