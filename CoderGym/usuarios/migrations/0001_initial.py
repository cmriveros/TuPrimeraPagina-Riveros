# Generated by Django 4.2.7 on 2023-11-30 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.IntegerField(verbose_name=10)),
                ('nombre_actividad', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('edad', models.IntegerField(verbose_name=5)),
                ('fecha_ingreso', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('asistio', models.BooleanField(default=False)),
                ('actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.actividad')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asistencia', to='usuarios.cliente')),
            ],
        ),
        migrations.AddField(
            model_name='actividad',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actividades', to='usuarios.cliente'),
        ),
    ]
