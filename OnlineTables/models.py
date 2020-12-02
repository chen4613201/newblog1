from django.db import models
from django.db.models import CASCADE
# Create your models here.


class TablePanels(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return self.name


class OneTable(models.Model):
    name = models.CharField(max_length=100, unique=True)
    panels = models.ForeignKey(TablePanels, on_delete=CASCADE)

    class Meta:
        db_table = 'T_OneTable'

    def __unicode__(self):
        return self.name


