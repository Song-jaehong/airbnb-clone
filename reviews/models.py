from django.db import models
from core import models as core_models
from users import models as user_models
from rooms import models as room_models


class Review(core_models.TimeStampedModel):

    """ Review Model Definition """

    content = models.TextField()
    accuracy = models.IntegerField()
    comminication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_input = models.IntegerField()
    value = models.IntegerField()

    user = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    room = models.ForeignKey(room_models.Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.content} - {self.room.name}"
