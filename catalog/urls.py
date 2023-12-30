from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, HomeListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    VersionCreateView, VersionUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('create_product/', ProductCreateView.as_view(), name='create_product'),
    path('update_product/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('create_version/', VersionCreateView.as_view(), name='create_version'),
    path('update_version/<int:pk>/', VersionUpdateView.as_view(), name='update_version'),
]
