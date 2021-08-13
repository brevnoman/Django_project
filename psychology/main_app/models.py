import django.utils.encoding
from django.db import models
import datetime
from django.contrib.auth.models import User


class Meeting(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    description = models.TextField(max_length=255)
    phone_number = models.CharField(max_length=13, default="no number")
    is_accepted = models.BooleanField(blank=True, default=False)
    time_start = models.TimeField(blank=True, default=datetime.time(12,0,0,0))
    time_end = models.TimeField(blank=True, default=datetime.time(13,0,0,0))
    date = models.DateField(default=datetime.date.today())
    is_done = models.BooleanField(blank=True, default=False)

    def __str__(self):
        if self.is_accepted:
            return f"{self.user.first_name}, {self.user.last_name}, {self.date}, {self.time_start}-{self.time_end}"
        return f"{self.user.first_name}, {self.user.last_name}, {self.date} NEW"

class Conclusion(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, blank=True)
    conclusion_desc = models.TextField(max_length=510, blank=True)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    create_time = models.DateTimeField(default=django.utils.timezone.now)


    def __str__(self):
        return str(self.meeting) + " создано " + str(self.create_time)[:16]

    # def __repr__(self):
    #     return self.conclusion_desc, self.meeting




