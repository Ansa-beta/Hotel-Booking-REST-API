
# Hotel Booking REST API

A Django REST Framework project for managing hotel rooms and customer bookings. The API supports room and booking management, including validation to prevent conflicting bookings for the same room on overlapping dates.

## Features

- Create, read, update, and delete rooms
- Create, read, update, and delete bookings
- Prevent overlapping bookings for the same room
- Automatic booking number generation
- Automatic booking time generation
- Authentication-based API access
- JSON response format

## Tech Stack

- Python
- Django
- Django REST Framework
- MySQL
- Django ORM

## Project Structure

```bash
HotelBookingSystem/
│
├── HotelBookingSystem/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── hotelapp/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── views.py
│   └── migrations/
│
├── manage.py
├── db.sqlite3
├── README.md
└── requirements.txt
```

## Prerequisites

- Python 3.10+
- MySQL Server
- Virtual environment

## Installation

1. Clone the repository

```bash
git clone https://github.com/your-username/hotel-booking-rest-api.git
cd hotel-booking-rest-api
```

2. Create and activate a virtual environment

```bash
python -m venv venv
```

Windows:
```bash
venv\Scripts\activate
```

macOS/Linux:
```bash
source venv/bin/activate
```

3. Install dependencies

```bash
pip install django djangorestframework mysqlclient
```

4. Configure MySQL in `HotelBookingSystem/settings.py`

Update the `DATABASES` section with your local MySQL database credentials.

5. Apply migrations

```bash
python manage.py migrate
```

6. Run the server

```bash
python manage.py runserver
```

The project will run at:

```bash
http://127.0.0.1:8000/
```

## API Endpoints

### Room Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/room/` | Get all rooms |
| POST | `/room/` | Create a room |
| GET | `/room/{id}/` | Get room by ID |
| PUT | `/room/{id}/` | Update room |
| DELETE | `/room/{id}/` | Delete room |

### Booking Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/booking/` | Get all bookings |
| POST | `/booking/` | Create a booking |
| GET | `/booking/{id}/` | Get booking by ID |
| PUT | `/booking/{id}/` | Update booking |
| DELETE | `/booking/{id}/` | Delete booking |

## Example: Create a Room

```http
POST /room/
Content-Type: application/json
```

```json
{
  "room_number": 103,
  "room_type": "Single",
  "price": "1000.00",
  "is_available": true
}
```

## Example: Create a Booking

```http
POST /booking/
Content-Type: application/json
```

```json
{
  "customer_name": "Ansa",
  "room_number": 103,
  "check_in_date": "2026-11-18",
  "check_out_date": "2026-11-19"
}
```

The API validates the booking dates and rejects requests where the new booking overlaps with an existing reservation for the same room.

## Notes

This project demonstrates backend development using Django REST Framework, model-based data handling, and business rule validation for hotel booking operations.

## License

This project is for educational and portfolio purposes.
