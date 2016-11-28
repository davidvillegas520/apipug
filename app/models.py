import datetime
from django.db import models


class Actor(models.Model):
    """
    Model class of Actor
    """
    actor_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'actor'


class ActorInfo(models.Model):
    """
    Model class of ActorInfo
    """
    actor_id = models.IntegerField()
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    film_info = models.CharField(max_length=200)

    class Meta:
        db_table = 'actor_info'


class Address(models.Model):
    """
    Model class of Address
    """
    address_id = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    city_id = models.IntegerField()
    postal_code = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'address'


class Category(models.Model):
    """
    Model class of Category
    """
    category_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'category'


class City(models.Model):
    """
    Model class of City
    """
    city_id = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=200)
    country_id = models.IntegerField()
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'city'


class Country(models.Model):
    """
    Model class of Country
    """
    country_id = models.IntegerField(primary_key=True)
    country = models.CharField(max_length=200)
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'country'


class Customer(models.Model):
    """
    Model class of Customer
    """
    customer_id = models.IntegerField(primary_key=True)
    store_id = models.IntegerField()
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address_id = models.IntegerField()
    active = models.IntegerField()
    create_date = models.CharField(max_length=200)
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'customer'


class CustomerList(models.Model):
    """
    Model class of CustomerList
    """
    ID = models.IntegerField()
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)
    SID = models.IntegerField()

    class Meta:
        db_table = 'customer_list'


class Film(models.Model):
    """
    Model class of Film
    """
    film_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    release_year = models.CharField(max_length=200)
    language_id = models.IntegerField()
    original_language_id = models.IntegerField()
    rental_duration = models.IntegerField()
    rental_rate = models.CharField(max_length=200)
    length = models.IntegerField()
    replacement_cost = models.CharField(max_length=200)
    rating = models.CharField(max_length=200)
    special_features = models.CharField(max_length=200)
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'film'


class FilmActor(models.Model):
    """
    Model class of FilmActor
    """
    actor_id = models.IntegerField(primary_key=True)
    film_id = models.IntegerField(primary_key=True)
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'film_actor'


class FilmCategory(models.Model):
    """
    Model class of FilmCategory
    """
    film_id = models.IntegerField(primary_key=True)
    category_id = models.IntegerField(primary_key=True)
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'film_category'


class FilmList(models.Model):
    """
    Model class of FilmList
    """
    FID = models.IntegerField()
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    length = models.IntegerField()
    rating = models.CharField(max_length=200)
    actors = models.CharField(max_length=200)

    class Meta:
        db_table = 'film_list'


class FilmText(models.Model):
    """
    Model class of FilmText
    """
    film_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    class Meta:
        db_table = 'film_text'


class Inventory(models.Model):
    """
    Model class of Inventory
    """
    inventory_id = models.IntegerField(primary_key=True)
    film_id = models.IntegerField()
    store_id = models.IntegerField()
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'inventory'


class Language(models.Model):
    """
    Model class of Language
    """
    language_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'language'


class NicerButSlowerFilmList(models.Model):
    """
    Model class of NicerButSlowerFilmList
    """
    FID = models.IntegerField()
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    length = models.IntegerField()
    rating = models.CharField(max_length=200)
    actors = models.CharField(max_length=200)

    class Meta:
        db_table = 'nicer_but_slower_film_list'


class Payment(models.Model):
    """
    Model class of Payment
    """
    payment_id = models.IntegerField(primary_key=True)
    customer_id = models.IntegerField()
    staff_id = models.IntegerField()
    rental_id = models.IntegerField()
    amount = models.CharField(max_length=200)
    payment_date = models.CharField(max_length=200)
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'payment'


class Rental(models.Model):
    """
    Model class of Rental
    """
    rental_id = models.IntegerField(primary_key=True)
    rental_date = models.CharField(max_length=200)
    inventory_id = models.IntegerField()
    customer_id = models.IntegerField()
    return_date = models.CharField(max_length=200)
    staff_id = models.IntegerField()
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'rental'


class SalesByFilmCategory(models.Model):
    """
    Model class of SalesByFilmCategory
    """
    category = models.CharField(max_length=200)
    total_sales = models.CharField(max_length=200)

    class Meta:
        db_table = 'sales_by_film_category'


class SalesByStore(models.Model):
    """
    Model class of SalesByStore
    """
    store = models.CharField(max_length=200)
    manager = models.CharField(max_length=200)
    total_sales = models.CharField(max_length=200)

    class Meta:
        db_table = 'sales_by_store'


class Staff(models.Model):
    """
    Model class of Staff
    """
    staff_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address_id = models.IntegerField()
    picture = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    store_id = models.IntegerField()
    active = models.IntegerField()
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'staff'


class StaffList(models.Model):
    """
    Model class of StaffList
    """
    ID = models.IntegerField()
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    SID = models.IntegerField()

    class Meta:
        db_table = 'staff_list'


class Store(models.Model):
    """
    Model class of Store
    """
    store_id = models.IntegerField(primary_key=True)
    manager_staff_id = models.IntegerField()
    address_id = models.IntegerField()
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'store'
