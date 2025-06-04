from accounts import models
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password"]


DAY_NAMES = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}


class UserShiftSerializer(serializers.ModelSerializer):
    schedule = serializers.SerializerMethodField()

    class Meta:
        model = models.UserShift
        fields = "__all__"

    def get_schedule(self, obj):
        user = obj.user
        schedule = {}

        for shift in user.user_shifts.all():
            if shift.day_group == "weekdays":
                days = range(0, 5)
            elif shift.day_group == "weekends":
                days = range(5, 7)
            else:
                days = []

            for day in days:
                schedule[DAY_NAMES[day]] = {
                    "start_time": shift.start_time.strftime("%H:%M"),
                    "end_time": shift.end_time.strftime("%H:%M"),
                    "active": shift.is_active,
                }

        return schedule
