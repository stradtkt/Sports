# Generated by Django 2.1.3 on 2018-12-17 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, max_digits=20)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matchup', models.CharField(max_length=100)),
                ('opp1', models.CharField(max_length=50)),
                ('opp2', models.CharField(max_length=50)),
                ('team_picked', models.CharField(max_length=50)),
                ('difference', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='Plans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('level', models.CharField(choices=[(1, 'Pro'), (2, 'Platinum'), (3, 'Pick of the week')], default=1, max_length=20)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('DOB', models.DateField()),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.PositiveIntegerField()),
                ('dates_from', models.DateTimeField()),
                ('dates_to', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='week',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drego.Week'),
        ),
        migrations.AddField(
            model_name='cart',
            name='plans',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='drego.Plans'),
        ),
    ]