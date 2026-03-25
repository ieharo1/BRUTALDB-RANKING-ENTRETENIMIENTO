from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('role', models.CharField(blank=True, max_length=120)),
            ],
            options={'ordering': ['name']},
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=180)),
                ('artist', models.CharField(max_length=180)),
                ('year', models.PositiveIntegerField()),
                ('album', models.CharField(blank=True, max_length=180)),
                ('score', models.DecimalField(decimal_places=1, max_digits=3)),
                ('cover_url', models.URLField(blank=True)),
                ('description', models.TextField()),
            ],
            options={'ordering': ['-score', '-year', 'title']},
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180)),
                ('media_type', models.CharField(choices=[('movie', 'Película'), ('series', 'Serie'), ('documentary', 'Documental')], max_length=20)),
                ('year', models.PositiveIntegerField()),
                ('duration', models.CharField(blank=True, max_length=40)),
                ('score', models.DecimalField(decimal_places=1, max_digits=3)),
                ('synopsis', models.TextField()),
                ('poster_url', models.URLField(blank=True)),
                ('trailer_url', models.URLField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('cast', models.ManyToManyField(blank=True, related_name='titles', to='catalog.person')),
            ],
            options={'ordering': ['-score', '-year', 'name']},
        ),
    ]
