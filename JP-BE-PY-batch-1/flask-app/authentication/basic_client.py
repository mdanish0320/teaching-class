import urllib.request
import base64

# Replace 'your_username' and 'your_password' with your actual credentials
username = 'john'
password = 'helloo'

# URL of the API endpoint that requires basic authentication
url = 'http://localhost:3000'

# Encode the credentials in base64
credentials = f"{username}:{password}"
credentials_bytes = credentials.encode('ascii')
base64_credentials = base64.b64encode(credentials_bytes).decode('ascii')

# Create a request object with basic authentication header
request = urllib.request.Request(url)
request.add_header("Authorization", "Basic " + base64_credentials)

# Make the request and get the response
with urllib.request.urlopen(request) as response:
    response_data = response.read()
    print("Request successful!")
    print("Response:", response_data.decode('utf-8'))
