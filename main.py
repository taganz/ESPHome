import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

def main():
    app_name = os.getenv("APP_NAME")
    debug_mode = os.getenv("DEBUG")
    api_key = os.getenv("API_KEY")

    print(f"App Name: {app_name}")
    print(f"Debug Mode: {debug_mode}")
    print(f"API Key: {api_key}")

if __name__ == "__main__":
    main()
