http://127.0.0.1:8000/restaurant/
- Home Page with a static file (Logo)

http://localhost:8000/restaurant/menu/
- Displays all menu items (JSON)
- Takes Get and Post requests

http://localhost:8000/restaurant/menu/<int:pk>/
- Displays a single menu item (JSON)
- Takes Get, Put, Patch, and Delete requests

http://localhost:8000/restaurant/booking/
- Displays all bookings on an HTML page
- Fill out a form to create a booking

http://localhost:8000/auth/
/auth/token/login
/auth/token/logout
/auth/users/
/auth/users/me/
DJOSER Endpoints
- Send /auth/users/ a POST request to create a new user
- Send /auth/token/login a POST request to login, and receive a token
- Send /auth/token/logout a POST request to logout
- Send /auth/users/me/ a GET request to see the current user

http://localhost:8000/restaurant/api-token-auth/
- Send a POST request with a username and password to receive a token

