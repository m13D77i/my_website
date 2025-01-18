from django.db import models


class Contact(models.Model):
    fullname = models.CharField(blank=True,max_length=40, verbose_name="Fullname")
    email = models.EmailField(max_length=254, verbose_name="Email")
    description = models.TextField(blank=True,verbose_name="Description")
    datatime_send = models.DateTimeField(auto_now_add=True, verbose_name="Datatime")

    def __str__(self):
        return self.fullname

