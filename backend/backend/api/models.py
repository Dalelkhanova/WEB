from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password
        }


class Category(models.Model):
    name = models.CharField(max_length=100)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
        }


class newBooksManager(models.Manager):
    def get_new_books(self):
        return super(newBooksManager, self).get_queryset().filter(new=True)


class Books(models.Model):
    name = models.CharField(max_length=500, default='')
    imageLink = models.TextField(default='')
    imageLink2 = models.TextField(default='')
    imageLink3 = models.TextField(default='')
    price = models.CharField(max_length=100, default='')
    description = models.TextField(default="description")
    new = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    objects = newBooksManager()

    def to_json(self):
        return {
            'id': self.id,
            'imageLink': self.imageLink,
            'imageLink2': self.imageLink2,
            'imageLink3': self.imageLink3,
            'price': self.price,
            'description': self.description,
            'category': self.category.id,
        }

