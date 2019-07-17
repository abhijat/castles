# Generated by Django 2.2.2 on 2019-06-18 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, unique=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, unique=True)),
                ('weight_per_ton', models.FloatField()),
                ('flammable', models.BooleanField(default=False)),
                ('mined_at', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='materials', to='castlebuilder.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Castle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, unique=True)),
                ('budget', models.FloatField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='castles', to='castlebuilder.Location')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='castles', to='castlebuilder.Material')),
            ],
        ),
    ]
