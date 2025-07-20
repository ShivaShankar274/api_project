from django.db import models

class apimodel(models.Model):
    uname=models.CharField(max_length=50)
    unum=models.BigIntegerField()
    uemail=models.EmailField(max_length=50)

    def __str__(self):
     return self.uname
