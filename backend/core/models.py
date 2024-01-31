import uuid
from django.db import models


class Metrics(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    start_date = models.DateField()
    # audit data
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "metrics"


class Departments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    functions = models.CharField(null=True, max_length=200)
    new = models.CharField(null=True, max_length=200)
    retained = models.CharField(null=True, max_length=200)
    churned = models.CharField(null=True, max_length=200)
    metric = models.ForeignKey(Metrics, on_delete=models.CASCADE, related_name='departments')
    # audit data
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "departments"