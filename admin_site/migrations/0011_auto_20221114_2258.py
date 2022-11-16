# Generated by Django 3.2.16 on 2022-11-14 17:28

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('admin_site', '0010_category_cat_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('vendor_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('vendor_name', models.CharField(max_length=100, unique=True)),
                ('vendor_dec', models.CharField(max_length=100, unique=True)),
                ('slug', models.CharField(max_length=100, unique=True)),
                ('vend_img', models.ImageField(blank=True, upload_to='photos/vendor')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_site.category')),
            ],
        ),
    ]
