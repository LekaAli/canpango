# Canpango


# Install dependencies
pip install -r requirements.txt


# Running the application
1. Change directory into canpango, then into beer_manager_api, then run the follow command: python manager runserver
2. Type the following into your prefered web browser: 127.0.0.1:8000/endpoints
3. You will need to login in order to access the endpoints api
# Login Details
Username: canpango
Password: 12345can

# App API endpoints

- User creation/retrieving: 127.0.0.1:8000/endpoints/user
- Beer creation/retrival: 127.0.0.1:8000/endpoints/beer
- Beer reviewing: 127.0.0.1:8000/endpoints/review
- filtering beer rating: 127.0.0.1:8000/endpoints/review/?beer=<name_of_the_beer>

