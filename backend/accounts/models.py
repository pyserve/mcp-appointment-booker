from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

DAY_GROUP_CHOICES = [
    ("weekdays", "Monday to Friday"),
    ("weekends", "Saturday and Sunday"),
]


class UserShift(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_shifts")
    day_group = models.CharField(max_length=10, choices=DAY_GROUP_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_active = models.BooleanField(default=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ("user", "day_group")
        ordering = ["user", "day_group"]
