from django.db import models

class Product(models.Model):
    author = models.ForeignKey("User", on_delete=models.CASCADE)
    photo = models.ImageField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    area = models.TextField()
    created_at = models.TimeField()
    comment_number = models.IntegerField()
    like_number = models.IntegerField()

    def __str__(self):
        return self.title



class Comment(models.Model):
    user_id = models.ForeignKey("User", on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()






