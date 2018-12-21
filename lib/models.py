# Database version: 8.0.12
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    pub_house = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    pub_housebig = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'book'


class Platformtype(models.Model):
    platformtypeid = models.AutoField(db_column='platformTypeID', primary_key=True)  # Field name made lowercase.
    platformtype = models.CharField(db_column='platformType', max_length=32, blank=True,
                                    null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'platformtype'


class Testbeds(models.Model):
    testbedID = models.IntegerField(primary_key=True)
    testbed = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testbeds'


class Queue(models.Model):
    queueid = models.AutoField(db_column='queueId', primary_key=True)  # Field name made lowercase.
    priority = models.PositiveIntegerField()
    username = models.CharField(db_column='userName', max_length=100)  # Field name made lowercase.
    command = models.CharField(max_length=255)
    description = models.TextField()
    status = models.PositiveIntegerField()
    prefix = models.CharField(max_length=20, blank=True, null=True)
    build = models.CharField(max_length=255, blank=True, null=True)
    tftpip = models.CharField(db_column='tftpIP', max_length=200)  # Field name made lowercase.
    testbed = models.CharField(max_length=35, blank=True, null=True)
    suite = models.CharField(max_length=255, blank=True, null=True)
    dbresults = models.CharField(db_column='dbResults', max_length=1)  # Field name made lowercase.
    runid = models.PositiveIntegerField(db_column='runID')  # Field name made lowercase.
    pidofrun = models.PositiveIntegerField(db_column='pidOfRun')  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='creationDate')  # Field name made lowercase.
    lastchangedate = models.DateTimeField(db_column='lastChangeDate')  # Field name made lowercase.
    finishdate = models.DateTimeField(db_column='finishDate')  # Field name made lowercase.
    oem = models.CharField(max_length=30, blank=True, null=True)
    loadalcatel = models.CharField(db_column='loadAlcatel', max_length=2, blank=True,
                                   null=True)  # Field name made lowercase.
    userip = models.CharField(db_column='userIP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    removerip = models.CharField(db_column='removerIP', max_length=255, blank=True,
                                 null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'queue'
