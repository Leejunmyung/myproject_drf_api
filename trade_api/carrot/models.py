from django.db import models

class Board(models.Model):
    id = models.AutoField(primary_key=True)
    photo = models.ImageField()
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    area = models.TextField()
    created_at = models.TimeField()
    comment_number = models.IntegerField()
    like_number = models.IntegerField()

    def __str__(self):
        return self.title

class Sell(models.Model):
    sell_id = models.ForeignKey(Board, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    photo = models.ImageField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()


class Comment(models.Model):
    comment_id = models.ForeignKey(Sell, on_delete=models.CASCADE)
    content = models.TextField()
    area = models.TextField()
    created_at = models.DateField()






