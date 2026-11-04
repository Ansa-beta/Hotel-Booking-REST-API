from django.db import models

class RoomDb(models.Model):
    room_number=models.IntegerField()
    room_type=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return self.room_number

class BookingDb(models.Model):
    customer_name=models.CharField(max_length=100)
    room_number=models.IntegerField()
    check_in_date=models.DateField()
    check_out_date=models.DateField()
    booking_number=models.IntegerField(editable=False,null=True)
    booking_time=models.TimeField(editable=False,null=True)

    def __str__(self):
        return self.customer_name
