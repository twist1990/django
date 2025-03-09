from django.db import models

class WeatherData(models.Model):
    location = models.CharField(max_length=100)
    temperature = models.CharField(max_length=10)
    condition = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.location} - {self.temperature} - {self.condition}"
