# Generated by Django 2.1.3 on 2018-12-07 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('pub_house', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField()),
                ('pub_housebig', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'book',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Platformtype',
            fields=[
                ('platformtypeid', models.AutoField(db_column='platformTypeID', primary_key=True, serialize=False)),
                ('platformtype', models.CharField(blank=True, db_column='platformType', max_length=32, null=True)),
            ],
            options={
                'db_table': 'platformtype',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('queueid', models.AutoField(db_column='queueId', primary_key=True, serialize=False)),
                ('priority', models.PositiveIntegerField()),
                ('username', models.CharField(db_column='userName', max_length=100)),
                ('command', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('status', models.PositiveIntegerField()),
                ('prefix', models.CharField(blank=True, max_length=20, null=True)),
                ('build', models.CharField(blank=True, max_length=255, null=True)),
                ('tftpip', models.CharField(db_column='tftpIP', max_length=200)),
                ('testbed', models.CharField(blank=True, max_length=35, null=True)),
                ('suite', models.CharField(blank=True, max_length=255, null=True)),
                ('dbresults', models.CharField(db_column='dbResults', max_length=1)),
                ('runid', models.PositiveIntegerField(db_column='runID')),
                ('pidofrun', models.PositiveIntegerField(db_column='pidOfRun')),
                ('creationdate', models.DateTimeField(db_column='creationDate')),
                ('lastchangedate', models.DateTimeField(db_column='lastChangeDate')),
                ('finishdate', models.DateTimeField(db_column='finishDate')),
                ('oem', models.CharField(blank=True, max_length=30, null=True)),
                ('loadalcatel', models.CharField(blank=True, db_column='loadAlcatel', max_length=2, null=True)),
                ('userip', models.CharField(blank=True, db_column='userIP', max_length=255, null=True)),
                ('removerip', models.CharField(blank=True, db_column='removerIP', max_length=255, null=True)),
            ],
            options={
                'db_table': 'queue',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Testbeds',
            fields=[
                ('testbedID', models.IntegerField(primary_key=True, serialize=False)),
                ('testbed', models.CharField(blank=True, max_length=32, null=True)),
            ],
            options={
                'db_table': 'testbeds',
            },
        ),
    ]