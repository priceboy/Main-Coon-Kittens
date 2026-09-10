import urllib.parse
from django.db import models
from django.urls import reverse

class Breed(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self): return self.name

class Kitten(models.Model):
    GENDER_CHOICES = [("M", "Male"), ("F", "Female")]
    STATUS_CHOICES = [("available", "Available"), ("reserved", "Reserved"), ("sold", "Placed")]
    name = models.CharField(max_length=100)
    breed = models.ForeignKey(Breed, null=True, blank=True, on_delete=models.SET_NULL)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age_weeks = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="available")
    description = models.TextField(blank=True)
    vaccinated = models.BooleanField(default=False)
    dewormed = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: ordering = ["-created_at"]
    def __str__(self): return self.name
    def get_absolute_url(self): return reverse("kitten_detail", kwargs={"slug": self.slug})
    def whatsapp_link(self, phone_number):
        message = f"Hello! I would like to know more about {self.name}. Is this kitten still available?"
        return f"https://wa.me/{phone_number}?text={urllib.parse.quote(message)}"

class KittenPhoto(models.Model):
    kitten = models.ForeignKey(Kitten, related_name="photos", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="kittens/")
    order = models.PositiveIntegerField(default=0)
    class Meta: ordering = ["order"]
    def __str__(self): return f"{self.kitten.name} photo {self.order}"
