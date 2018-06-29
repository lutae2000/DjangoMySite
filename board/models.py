from django.db import models
from user.models import User


class Board(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=20)
    contents = models.CharField(max_length=500)
    count = models.IntegerField(default=0)
    regdate = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Board(%d, %s, %s, %s, %s, %s, %d)"\
               % (
                   self.id,
                   self.title,
                   self.name,
                   self.contents,
                   self.count,
                   self.regdate,
                   self.user.id)
