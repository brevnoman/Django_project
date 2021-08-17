import django.utils.encoding
from django.db import models
import datetime
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Meeting(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, verbose_name="Пользователь")
    description = models.TextField(max_length=255, verbose_name="Описание")
    phone_number = PhoneNumberField(null=False, blank=False, unique=True, verbose_name="Номер телефона")
    is_accepted = models.BooleanField(blank=True, default=False, verbose_name="Принято")
    time_start = models.TimeField(blank=True, default=datetime.time(12,0,0,0), verbose_name="Время начала")
    time_end = models.TimeField(blank=True, default=datetime.time(13,0,0,0), verbose_name="Время конца")
    date = models.DateField(default=django.utils.timezone.now, verbose_name="Дата")
    is_done = models.BooleanField(blank=True, default=False, verbose_name="Окончено")

    class Meta:
        verbose_name = "Встреча"
        verbose_name_plural = 'Встречи'

    def save(self, *args, **kwargs):
        if self.is_accepted and not self.is_done:
            pass
        return super().save(*args, **kwargs)

    def __str__(self):
        if self.is_accepted:
            return f"{self.user.first_name}, {self.user.last_name}, {self.date}, {self.time_start}-{self.time_end}"
        return f"{self.user.first_name}, {self.user.last_name}, {self.date} NEW"


class Conclusion(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, blank=True)
    conclusion_desc = models.TextField(max_length=510, blank=True, verbose_name="Заключение")
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, verbose_name="Встреча")
    create_time = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Время создания")

    class Meta:
        verbose_name = "Заключение"
        verbose_name_plural = 'Заключения'

    def __str__(self):
        return str(self.meeting) + " создано " + str(self.create_time)[:16]





