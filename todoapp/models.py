from django.db import models

class TaskModel(models.Model):
    user=models.CharField(max_length=200)
    title=models.CharField(max_length=100)
    options=(
        ("pending","pending"),
        ("completed","completed"),
        ("in progress","in progress")
    )
    created_date=models.DateTimeField(auto_now_add=True,blank=True)
    status=models.CharField(max_length=300,choices=options,default="pending")

    def __str__(self):
        return self.title