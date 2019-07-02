from django.db import models

# Create your models here.
class Counter(models.Model): # updatOrderNo , 하나씩 뽑는게 아니라

    groupno = models.IntegerField(default=0)
    depth = models.IntegerField(default=0)
    orderno = models.IntegerField(default=0)

    def __str__(self):
        return f'Counter({self.groupno}, {self.depth}, {self.orderno})'