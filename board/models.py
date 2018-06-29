from django.db import models

# Create your models here.
class Board(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=20)
    contents = models.CharField(max_length=500)
    count = models.IntegerField(default=0)
    regdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Board(%d, %s, %s, %s, %s, %s)" % (self.id, self.title, self.name, self.contents, self.count, self.regdate)