from django.db import models
from django.utils.timezone import timezone
import uuid

from jinja2.async_utils import auto_aiter


class Category(models.Model):

    name=models.CharField(max_length=15,null=False,unique=True,default=None)
    description = models.TextField(max_length=100)
    c_id = models.UUIDField(default=uuid.uuid4, null=False, blank=False, unique=True, primary_key=True, editable=False)
    cat_image = models.ImageField(default=None ,upload_to='photos/categories')

    class Meta:
         verbose_name='category'
         verbose_name_plural='categories'


    def __str__(self):
        return self.name

class Vendor(models.Model):
    vendor_id=models.UUIDField(default=uuid.uuid4, null=False, blank=False, unique=True, primary_key=True, editable=False)
    vendor_name=models.CharField(max_length=100,unique=True)
    vendor_dec = models.CharField(max_length=100, unique=True)
    slug=models.CharField(max_length=100,unique=True)
    vend_img=models.ImageField(upload_to='photos/vendor',blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vendor_name

