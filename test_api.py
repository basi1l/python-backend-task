import requests

# Step 1: Login and get the JWT token
login_url = "http://127.0.0.1:5000/login"
login_data = {
    "email": "test@example.com",  # Replace with your registered email
    "password": "password123"     # Replace with your registered password
}

response = requests.post(login_url, json=login_data)

if response.status_code == 200:
    token = response.json().get('token')
    print(f"Login successful! Token: {token}")
else:
    print(f"Login failed: {response.text}")

# Step 2: Get protected profiles using the JWT token
if 'token' in locals():  # Only proceed if login was successful
    profiles_url = "http://127.0.0.1:5000/profiles"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    profiles_response = requests.get(profiles_url, headers=headers)

    if profiles_response.status_code == 200:
        print(f"Profiles: {profiles_response.json()}")
    else:
        print(f"Error fetching profiles: {profiles_response.text}")
