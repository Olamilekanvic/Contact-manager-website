from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=225)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title


class Contact(models.Model):
    category = models.ForeignKey(Category, related_name='contacts', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    email = models.EmailField()
    phone = models.CharField(max_length=225)
    address = models.CharField(max_length=225)
    zipcode = models.CharField(max_length=225)
    city = models.CharField(max_length=225)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)

    class Meta:
        ordering =('first_name',)

    def __str__(self):
        return self.first_name