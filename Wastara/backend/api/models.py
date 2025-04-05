from django.db import models

class User(models.Model):
    ROLE_CHOICES = [
        ('lister', 'Lister'),
        ('collector', 'Collector'),
    ]
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username

class Item(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='items/')
    tags = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ItemRequest(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.requested_by.username} requested {self.item.name}"
