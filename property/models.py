from time import timezone
from django.db import models
from django.contrib.auth.models import User
import datetime
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.


class Property(models.Model):
    owner = models.ForeignKey(User,related_name='property_owner',on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(upload_to="property/")
    price = models.IntegerField(default=0)
    description = models.TextField(max_length=10000)
    place = models.ForeignKey(
        'Place', related_name='property_place', on_delete=models.CASCADE)
    category = models.ForeignKey(
        'Category', related_name='property_category', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Property, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    

    def get_absolute_url(self):
        return reverse('property:property_detail', kwargs={'slug': self.slug})
    
    
    def check_avaliabilty(self):
        all_reservations = self.book_property.all()
        now = datetime.datetime.now().date()
        for reservation in all_reservations:
            if now > reservation.date_to:
                return 'Avaliable'
            elif now > reservation.date_from and now < reservation.date_to:
                reserved = reservation.date_to
                return f'in progress {reserved}'
            else:
                return 'avaliable'
        
    def avg_rating(self):
        all_reviews = self.review_property.all()
        all_rating = 0
        
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_rating += review.rate
            return round(all_rating / len(all_reviews),2)
        else:
            return '-'

class PropertyImage(models.Model):
    property = models.ForeignKey(
        Property, related_name="property_image", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="property_images/")

    def __str__(self):
        return str(self.property)


class Place(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="places/")

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=40)
    icon = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class PropertyReview(models.Model):
    author = models.ForeignKey(
        User, related_name='review_author', on_delete=models.CASCADE)
    property = models.ForeignKey(
        Property, related_name='review_property', on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)
    feedback = models.TextField(max_length=2000)
    created_at = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return str(self.author)


COUNT = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4)
)


class PropertyBook(models.Model):
    user = models.ForeignKey(
        User, related_name='book_owner', on_delete=models.CASCADE)
    property = models.ForeignKey(
        Property, related_name='book_property', on_delete=models.CASCADE)
    date_from = models.DateField(default=datetime.datetime.now)
    date_to = models.DateField(default=datetime.datetime.now)
    guest = models.IntegerField(max_length=2, choices=COUNT)
    childern = models.IntegerField(max_length=2, choices=COUNT)

    def __str__(self):
        return str(self.user)

    def in_progress(self):
        now = datetime.datetime.now().date()
        return now > self.date_from and now < self.date_to
        
    in_progress.boolean = True