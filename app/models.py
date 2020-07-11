from django.db import models

# Create your models here.
class exam(models.Model):
    hallticket = models.AutoField(primary_key=True,auto_created=True,serialize=False)
    Name = models.CharField(max_length=30)
    t = models.PositiveIntegerField()
    h = models.PositiveIntegerField()
    e = models.PositiveIntegerField()
    m = models.PositiveIntegerField()
    s = models.PositiveIntegerField()
    so = models.PositiveIntegerField()

