from django.db import models

class Vote(models.Model):
    
    class_name = models.CharField(max_length=100)
    no_of_votes = models.IntegerField(default=0)

    def __str__(self):
        return self.class_name
