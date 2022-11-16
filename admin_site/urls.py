from django.contrib import admin
from django.urls import path,include
from admin_site import views

admin.site.site_header="Login to Super_Adimn panel"
admin.site.site_title="Super_admin"
admin.site.index_title="Welcome super admin"

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('category', views.category, name='category'),
    path('services', views.services, name='services'),
    path('vendors', views.vendors, name='vendors'),
    path('addcategory', views.add_category, name='addcategory'),
    path('editcategory/<str:c_id>', views.edit_category, name='editcategory'),
    path('deletecategory/<str:c_id>', views.delete_category, name='deletecategory')
]