from django.db import models
from django.utils import timezone
from select_multiple_field.models import SelectMultipleField

# Create your models here.

class Post(models.Model):
    ASPI = 'a'
    CODE = 'c'
    CATEGORIES = (
        (ASPI, 'Aspigirl'),
        (CODE, 'Programming')
    )

    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    category = SelectMultipleField(max_length=10, choices=CATEGORIES, default=ASPI)
    main_image = models.ForeignKey('Image',blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Faq(models.Model):
    question = models.CharField(max_length=500)
    answer = models.TextField()
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.question

class Image(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=500)
    credits = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class Paragraph(models.Model):
    index = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=500)
    text = models.TextField()
    image = models.ForeignKey('Image',blank=True, null=True)
    post = models.ForeignKey('Post',blank=True, null=True)

    def __str__(self):
        return self.title
