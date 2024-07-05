import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('avatar', models.ImageField(blank=True, default='default.png', null=True, upload_to='media')),
                ('room', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chatback.room')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatback.room')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatback.user')),
            ],
        ),
    ]
