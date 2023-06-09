# Generated by Django 4.2 on 2023-05-16 00:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("community", "0006_alter_borrow_borrow_date_alter_borrow_manager_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="borrow",
            name="manager",
            field=models.ForeignKey(
                blank=True,
                max_length=10,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
