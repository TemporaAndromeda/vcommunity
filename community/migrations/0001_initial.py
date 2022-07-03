# Generated by Django 4.0.5 on 2022-07-03 15:05

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=4000)),
                ('post_image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='')),
                ('source_link', models.CharField(blank=True, max_length=2000, null=True)),
                ('number_of_comments', models.IntegerField(default=0, editable=False)),
                ('report_value', models.IntegerField(choices=[(1, 'Reported'), (0, 'Report')], default=0)),
                ('report_total', models.IntegerField(blank=True, default=0, null=True)),
                ('vote_total', models.IntegerField(blank=True, default=0, null=True)),
                ('vote_Ratio', models.IntegerField(blank=True, default=0, null=True)),
                ('vote_value', models.IntegerField(choices=[(1, 'UP VOTE'), (-1, 'DOWN VOTE')], default=0)),
                ('creator_name', models.CharField(editable=False, max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('tags', models.ManyToManyField(blank=True, to='community.tag')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('sdescription', models.TextField(blank=True, max_length=4000)),
                ('com_image', models.ImageField(blank=True, upload_to='')),
                ('report_value', models.IntegerField(choices=[(1, 'Reported'), (0, 'Report')], default=0)),
                ('vote_value', models.IntegerField(choices=[(1, 'UP VOTE'), (-1, 'DOWN VOTE')], default=0)),
                ('vote_total', models.IntegerField(blank=True, default=0, null=True)),
                ('vote_ratio', models.IntegerField(blank=True, default=0, null=True)),
                ('creator_name', models.CharField(editable=False, max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.post')),
            ],
        ),
    ]
