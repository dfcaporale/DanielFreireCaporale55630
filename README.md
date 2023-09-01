## WorldTickets Project

### Package download and setup:

`$ git clone https://github.com/dfcaporale/DanielFreireCaporale55630.git`

`$ cd DanielFreireCaporale55630/WorldTickets/`

`$ python manage.py runserver`

To access the homepage, simply open a web browser and navigate to `localhost:8000`.

This website is dedicated to providing guidance on event tickets. In the future, we plan to implement ticket selling functionality. Currently, the app is named `AppTickets`, and the project is known as `WorldTickets`.

The database consists of the following models: `Event`, `Artist`, `Client`, and `Venue`.
- `Event`: Contains a list of events published by the service.
- `Artist`: Includes a list of artists along with their relevant information.
- `Client`: Represents users who are part of the service's community and may be contacted by other users.
- `Venue`: Provides a list of venues from around the world.

The administrator can access the system using the following credentials: `admin`:`12345`.
For all other users, the default password is `*daniel*`.
