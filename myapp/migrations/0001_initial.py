

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick_name', models.CharField(max_length=20, verbose_name='nick name')),
                ('avatar', models.FileField(blank=True, null=True, upload_to='avatar', verbose_name='avatar')),
                ('gender', models.PositiveSmallIntegerField(choices=[(1, 'Male'), (2, 'Female')], default=2, verbose_name='Gender')),
                ('signature', models.CharField(blank=True, max_length=100, null=True, verbose_name='signature')),
                ('email', models.EmailField(blank=True, max_length=50, null=True, verbose_name='email')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='birthday')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'UserInfo',
                'verbose_name_plural': 'UserInfo',
                'db_table': 'va_userinfo',
            },
        ),
    ]
