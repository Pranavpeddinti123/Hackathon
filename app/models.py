from django.db import models
from django.contrib.auth.models import User

# Model to handle Book information
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    published_date = models.DateField()
    image = models.ImageField(upload_to='book_images/', blank=True, null=True)

    def __str__(self):
        return self.title

# User Profile extension (if you plan to add extra fields to user profile)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

# Model for Translator service if needed (optional)
class Translator(models.Model):
    name = models.CharField(max_length=255)
    source_language = models.CharField(max_length=100)
    target_language = models.CharField(max_length=100)
    translated_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Translation by {self.name} from {self.source_language} to {self.target_language}"

# Model for Services page
class Service(models.Model):
    service_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.service_name

# Model to capture Shedule information (assuming scheduling feature)
class Schedule(models.Model):
    event_name = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()

    def __str__(self):
        return f"{self.event_name} on {self.date}"

# Feature model (you mentioned features earlier)
class Feature(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
