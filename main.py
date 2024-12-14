# filepath: main.py
from fastapi import FastAPI                    # Import FastAPI class from the fastapi module
import requests                                # Import requests library to make HTTP requests

app = FastAPI()                                # Create an instance of the FastAPI class

# Define the URLs for the third-party APIs
CAT_FACTS_API_URL = "https://catfact.ninja/fact"                            # Third-party API: Cat Facts API
DOG_FACTS_API_URL = "https://dog.ceo/api/breeds/image/random"               # Third-party API: Dog Facts API

@app.get("/cat-fact")                                   # Exposed GET API: /cat-fact
async def get_cat_fact():
    response = requests.get(CAT_FACTS_API_URL)          # Consumed third-party API: Cat Facts API
    data = response.json()                              # Parse the JSON response from the API
    return {"cat_fact": data["fact"]}                   # Return a JSON response containing the cat fact

@app.get("/combined-fact")                                                          # Exposed GET API: /combined-fact
async def get_combined_fact():
    cat_response = requests.get(CAT_FACTS_API_URL)                                  # Consumed third-party API: Cat Facts API
    dog_response = requests.get(DOG_FACTS_API_URL)                                  # Consumed third-party API: Dog Facts API
    cat_data = cat_response.json()                                                  # Parse the JSON response from the Cat Facts API
    dog_data = dog_response.json()                                                  # Parse the JSON response from the Dog Facts API
    return {"cat_fact": cat_data["fact"], "dog_image": dog_data["message"]}         # Return a JSON response containing both the cat fact and the dog image URL

if __name__ == "__main__":                              # Check if the script is being run directly (not imported as a module)
    import uvicorn                                      # Import uvicorn server
    uvicorn.run(app, host="0.0.0.0", port=8000)         # Run the FastAPI application using uvicorn on host 0.0.0.0 and port 8000

"""

Personal Notes (to understand the terms used in the code): 
1. "Create an instance of the FastAPI class"
    This means making a new FastAPI app that you can use to create web endpoints.

2. "Exposed GET API: /cat-fact" and "Exposed GET API: /combined-fact"
    These are web addresses (URLs) that you can visit to get information. /cat-fact gives you a cat fact, and /combined-fact gives you both a cat fact and a dog image URL.

3. "Consumed third-party API: Cat Facts API" and "Consumed third-party API: Dog Facts API"
    This means the app is getting information from other websites. One gives cat facts, and the other gives dog facts.

4. "Parse the JSON response from the Cat Facts API" and "Parse the JSON response from the Dog Facts API"
    This means taking the information received from the cat facts and dog facts websites and converting it into a format the app can use.


5. "Return a JSON response containing the cat fact" and "Return a JSON response containing both the cat fact and the dog image URL"
    This means sending back information in a specific format (JSON). One sends back just a cat fact, and the other sends back both a cat fact and a dog image URL.

"""
