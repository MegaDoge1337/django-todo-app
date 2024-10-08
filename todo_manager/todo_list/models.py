from django.db import models

# Create your models here.
class ToDoItem(models.Model):
  title = models.CharField(max_length=250)
  is_done = models.BooleanField(default=False)

  def __str__(self):
    return self.title

  class Meta:
    verbose_name = "To do item"