# lib/models.py
# from django.db import models

# Create your models here.
from django.db import models


class Book(models.Model):
    class Meta:
        db_table = 'book'

    name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    pub_house = models.CharField(max_length=200)
    pub_housebig = models.CharField(max_length=200, default='hahaha')
    pub_date = models.DateTimeField('date published')


class Platformtype(models.Model):
    class Meta:
        db_table = 'platformtype'

    platformTypeID = models.IntegerField(primary_key=True)
    platformType = models.CharField(max_length=100)


class Queue(models.Model):
    class Meta:
        db_table = 'queue'

    queueId = models.IntegerField(primary_key=True)
    # priority = models.SmallIntegerField()
    userName = models.CharField(max_length=100, default='', db_index=True)
    # command = models.CharField(max_length=255)
    #description = models.TextField()
    status = models.SmallIntegerField(default='3')
    # prefix = models.CharField(max_length=20)
    build = models.CharField(max_length=255, blank=True,null=True)
    # tftpIP = models.CharField(max_length=200)
    testbed = models.CharField(max_length=35, blank=True,null=True)
    suite = models.CharField(max_length=255)
    # dbResults = models.CharField(max_length=1)
    # runID = models.SmallIntegerField()
    # pidOfRun = models.IntegerField()
    creationDate = models.DateTimeField(default='0000-00-00 00:00:00')
    lastChangeDate = models.DateTimeField(default='0000-00-00 00:00:00')
    finishDate = models.DateTimeField(default='0000-00-00 00:00:00')
    # oem = models.CharField(max_length=30)
    # loadAlcatel = models.CharField(max_length=2)
    # userIP = models.CharField(max_length=255)
    # removerIP = models.CharField(max_length=255)
