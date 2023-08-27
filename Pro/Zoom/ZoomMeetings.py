import jwt
import requests
import json
from time import time

# Replace with your own API key and secret
API_KEY = 'Your API key'
API_SECRET = 'Your API secret'

# Create a function to generate a token using the PyJWT library
def generate_token():
   
   # Create a payload of the token containing API key and expiration time
   token_payload = {'iss': API_KEY, 'exp': time() + 5000}

   # Secret used to generate token signature
   secret_key = API_SECRET

   # Specify the hashing algorithm
   algorithm = 'HS256'

   # Encode the token
   token = jwt.encode(token_payload, secret_key, algorithm=algorithm)
   return token.decode('utf-8')
   
# Create JSON data for the Zoom meeting details
meeting_details = {
   "topic": "The title of your Zoom meeting",
   "type": 2,
   "start_time": "2019-06-14T10:21:57",
   "duration": "45",
   "timezone": "Europe/Madrid",
   "agenda": "test",
   "recurrence": {
      "type": 1,
      "repeat_interval": 1 
   },
   "settings": {
      "host_video": "true",
      "participant_video": "true",
      "join_before_host": "False",
      "mute_upon_entry": "False",
      "watermark": "true",
      "audio": "voip",
      "auto_recording": "cloud"
   }
}

# Send a request with headers including a token and meeting details
def create_zoom_meeting():
   headers = {
      'authorization': 'Bearer ' + generate_token(),
      'content-type': 'application/json'
   }

   # Make a POST request to the Zoom API endpoint to create the meeting
   response = requests.post(
      f'https://api.zoom.us/v2/users/me/meetings',  headers=headers, data=json.dumps(meeting_details)
   )
   print("\nCreating Zoom meeting...\n")

   # Convert the response to JSON and extract the meeting details
   response_json = json.loads(response.text)
   join_url = response_json["join_url"]
   meeting_password = response_json["password"]

   # Print the meeting details
   print(f'\nHere is your Zoom meeting link {join_url} and your password: "{meeting_password}"\n')
   
# Run the create_zoom_meeting function
create_zoom_meeting() 