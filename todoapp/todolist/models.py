from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class List(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    priority = models.CharField(max_length=30,
                                choices=(
                                    ("High Priority", "High Priority"),
                                    ("Medium Priority", "Medium Priority"),
                                    ("Low Priority", "Low Priority"),
                                    ("Optional", "Optional")
                                ),
                                default="Medium Priority"
                                )
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + " | " + str(self.completed)

    class Meta:
        ordering = ["priority", "-created"]

    