# Generated by Django 4.2 on 2023-04-26 01:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("community", "0003_remove_book_borrow_date_remove_book_borrower_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="borrow",
            name="book",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.RESTRICT, to="community.book"
            ),
        ),
        migrations.AlterField(
            model_name="borrow",
            name="borrow_date",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
