from django.db import models

# City model
class Cities(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=100, blank=True, null=True)


# Seat model
class Seat(models.Model):
    id = models.AutoField(primary_key=True)
    seat_number = models.CharField(max_length=100, null=True, blank=True)
    seat_type = models.CharField(max_length=100, null=True, blank=True)
    fare = models.FloatField(default=0.0, null=True, blank=True)


# Route model
class Routes(models.Model):
    id = models.AutoField(primary_key=True)
    source_city = models.ForeignKey(Cities, on_delete=models.CASCADE, related_name='source_city', null=True, blank=True)
    destination_city = models.ForeignKey(Cities, on_delete=models.CASCADE, related_name='destination_city', null=True, blank=True)
    fare = models.FloatField(null=True, default=0.0, blank=True)

#Booking model
class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    route = models.ForeignKey(Routes, on_delete=models.CASCADE)
    total_fare = models.FloatField(null=True, blank=True, default=0.0)
    is_booked = models.BooleanField(default=False)
