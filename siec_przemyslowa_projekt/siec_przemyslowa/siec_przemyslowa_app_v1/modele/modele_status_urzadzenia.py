from django.db import models

class StatusPolaczenia(models.IntegerChoices):
    ONLINE=0,"Online"
    OFFLINE=1,"Offline"