from django.db import models

class Birdnest(models.Model):
    LIBRARY = 'Library'
    FRAMEWORK = 'Framework'
    VIDEO = 'Video'
    DOCUMENT = 'Document'

    CATEGORY_CHOICES = [
        (LIBRARY, 'Library'),
        (FRAMEWORK, 'Framework'),
        (VIDEO, 'Video'),
        (DOCUMENT, 'Document'),
    ]
    
    name = models.CharField(max_length=200)  
    category = models.CharField(max_length=200, choices=CATEGORY_CHOICES)
    description = models.CharField(max_length=200)