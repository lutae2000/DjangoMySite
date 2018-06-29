from django.db import models

# Create your models here.
class Guestbook(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    message = models.CharField(max_length=2000)
    # INSERT 될 때 자동으로 시스템 시간을 넣겠다.
    regdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Guestbook(%s, %s, %s, %s)" % (self.name, self.password, self.message, self.regdate)

