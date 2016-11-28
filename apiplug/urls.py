"""sampleapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from app import views
admin.autodiscover()


router = routers.DefaultRouter()
router.register(r'actor', views.ActorViewSet,'Actor'),
router.register(r'actor_info', views.ActorInfoViewSet,'ActorInfo'),
router.register(r'address', views.AddressViewSet,'Address'),
router.register(r'category', views.CategoryViewSet,'Category'),
router.register(r'city', views.CityViewSet,'City'),
router.register(r'country', views.CountryViewSet,'Country'),
router.register(r'customer', views.CustomerViewSet,'Customer'),
router.register(r'customer_list', views.CustomerListViewSet,'CustomerList'),
router.register(r'film', views.FilmViewSet,'Film'),
router.register(r'film_actor', views.FilmActorViewSet,'FilmActor'),
router.register(r'film_category', views.FilmCategoryViewSet,'FilmCategory'),
router.register(r'film_list', views.FilmListViewSet,'FilmList'),
router.register(r'film_text', views.FilmTextViewSet,'FilmText'),
router.register(r'inventory', views.InventoryViewSet,'Inventory'),
router.register(r'language', views.LanguageViewSet,'Language'),
router.register(r'nicer_but_slower_film_list', views.NicerButSlowerFilmListViewSet,'NicerButSlowerFilmList'),
router.register(r'payment', views.PaymentViewSet,'Payment'),
router.register(r'rental', views.RentalViewSet,'Rental'),
router.register(r'sales_by_film_category', views.SalesByFilmCategoryViewSet,'SalesByFilmCategory'),
router.register(r'sales_by_store', views.SalesByStoreViewSet,'SalesByStore'),
router.register(r'staff', views.StaffViewSet,'Staff'),
router.register(r'staff_list', views.StaffListViewSet,'StaffList'),
router.register(r'store', views.StoreViewSet,'Store')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', include('rest_framework_swagger.urls'))
]
