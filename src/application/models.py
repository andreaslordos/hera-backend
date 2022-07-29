from django.db import models
import uuid

class Backup(models.Model):
    # generate unique access token upon instantiation of the model
    accessToken = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    data = models.TextField()
