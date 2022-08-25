from django.db import models

# Create your models here.
class TODO(models.Model):
    title = models.CharField(max_length=50)
    dis = models.CharField(max_length=250)
    is_completed = models.BooleanField()
    date_posted = models.DateField(auto_now_add =True)

    class Meta:
        ordering = ['title']
        db_table = 'TODO'

    def __str__(self):
        return self.title
