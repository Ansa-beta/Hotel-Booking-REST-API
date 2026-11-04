# Hotel Booking System API

A Django REST Framework API for managing hotel rooms and customer bookings. It provides CRUD endpoints for rooms and bookings and rejects bookings that overlap for the same room.

## Features

- Create, list, retrieve, update, and delete rooms.
- Create, list, retrieve, update, and delete bookings.
- Check for overlapping bookings when creating or updating a booking.
- Assign a booking number and booking time when a booking is created.

## Requirements

- Python 3.10+
- MySQL

The project settings use Django 5.0.1, Django REST Framework, and a local MySQL database. The MySQL database must exist before running migrations.

## Setup

1. Clone the repository and enter the project directory.
2. Create and activate a virtual environment:

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. Install the dependencies:

   ```powershell
   python -m pip install Django==5.0.1 djangorestframework mysqlclient
   ```

4. Configure the `DATABASES` setting in `HotelBookingSystem/settings.py` for your local MySQL database. Keep database credentials out of source control.
5. Apply migrations and start the development server:

   ```powershell
   python manage.py migrate
   python manage.py runserver
   ```

The API is available at `http://127.0.0.1:8000/`.

## API endpoints

All endpoints accept and return JSON.

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/room/` | List rooms |
| `POST` | `/room/` | Create a room |
| `GET` | `/room/{id}/` | Retrieve a room |
| `PUT` | `/room/{id}/` | Update a room |
| `DELETE` | `/room/{id}/` | Delete a room |
| `GET` | `/booking/` | List bookings |
| `POST` | `/booking/` | Create a booking |
| `GET` | `/booking/{id}/` | Retrieve a booking |
| `PUT` | `/booking/{id}/` | Update a booking |
| `DELETE` | `/booking/{id}/` | Delete a booking |

### Create a room

```http
POST /room/
Content-Type: application/json
```

```json
{
  "room_number": 103,
  "room_type": "Single",
  "price": "1000.00"
}
```

`is_available` is optional and defaults to `true`.

### Create a booking

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

On success, the API returns a booking success message with the assigned booking number and time. A booking is rejected if its date range overlaps another booking for the same room. Check-in and check-out dates use the `YYYY-MM-DD` format.

## API request examples

The repository includes additional request examples in [`HotelBookingSystem/APIDOC.http`](HotelBookingSystem/APIDOC.http).
