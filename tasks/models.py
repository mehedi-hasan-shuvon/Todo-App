from django.db import models
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=200)
    complete=models.BooleanField(default=False)
    created     = models.DateTimeField(editable=False)
    

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        
        return super(Task, self).save(*args, **kwargs)
    

    def __str__(self):
        return self.title