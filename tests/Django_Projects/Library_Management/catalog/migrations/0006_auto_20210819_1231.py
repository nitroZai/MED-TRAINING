# Generated by Django 3.2.3 on 2021-08-19 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_delete_usersaccount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='ISBN',
            new_name='isbn',
        ),
        migrations.RenameField(
            model_name='borrower',
            old_name='Renewal_date',
            new_name='renewal_date',
        ),
        migrations.RenameField(
            model_name='staffborrower',
            old_name='Renewal_date',
            new_name='renewal_date',
        ),
    ]