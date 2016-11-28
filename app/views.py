from app. models import (
    Actor,
    ActorInfo,
    Address,
    Category,
    City,
    Country,
    Customer,
    CustomerList,
    Film,
    FilmActor,
    FilmCategory,
    FilmList,
    FilmText,
    Inventory,
    Language,
    NicerButSlowerFilmList,
    Payment,
    Rental,
    SalesByFilmCategory,
    SalesByStore,
    Staff,
    StaffList,
    Store
)
from app.serializers import (
    ActorSerializer,
    ActorInfoSerializer,
    AddressSerializer,
    CategorySerializer,
    CitySerializer,
    CountrySerializer,
    CustomerSerializer,
    CustomerListSerializer,
    FilmSerializer,
    FilmActorSerializer,
    FilmCategorySerializer,
    FilmListSerializer,
    FilmTextSerializer,
    InventorySerializer,
    LanguageSerializer,
    NicerButSlowerFilmListSerializer,
    PaymentSerializer,
    RentalSerializer,
    SalesByFilmCategorySerializer,
    SalesByStoreSerializer,
    StaffSerializer,
    StaffListSerializer,
    StoreSerializer
)
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets


class ActorViewSet(viewsets.ViewSet):
    def get_object(self, pk):
        try:
            return Actor.objects.get(pk=pk)
        except Actor.DoesNotExist:
            raise Http404

    def list(self, request):
        """
        Please provide endpoint description
        """
        items = Actor.objects.all()
        serializer = ActorSerializer(items, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = ActorSerializer(item)
        return Response(serializer.data)

    def create(self, request):
        """
        Please provide endpoint description
        """
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = ActorSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActorInfoViewSet(viewsets.ViewSet):
    def get_object(self, pk):
        try:
            return ActorInfo.objects.get(pk=pk)
        except ActorInfo.DoesNotExist:
            raise Http404

    def list(self, request):
        """
        Please provide endpoint description
        """
        items = Actor_info.objects.all()
        serializer = Actor_infoSerializer(items, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = Actor_infoSerializer(item)
        return Response(serializer.data)

    def create(self, request):
        """
        Please provide endpoint description
        """
        serializer = Actor_infoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = Actor_infoSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AddressViewSet(viewsets.ViewSet):
    def get_object(self, pk):
        try:
            return Address.objects.get(pk=pk)
        except Address.DoesNotExist:
            raise Http404

    def list(self, request):
        """
        Please provide endpoint description
        """
        items = Address.objects.all()
        serializer = AddressSerializer(items, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = AddressSerializer(item)
        return Response(serializer.data)

    def create(self, request):
        """
        Please provide endpoint description
        """
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = AddressSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryViewSet(viewsets.ViewSet):
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def list(self, request):
        """
        Please provide endpoint description
        """
        items = Category.objects.all()
        serializer = CategorySerializer(items, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = CategorySerializer(item)
        return Response(serializer.data)

    def create(self, request):
        """
        Please provide endpoint description
        """
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = CategorySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CityViewSet(viewsets.ViewSet):
    def get_object(self, pk):
        try:
            return City.objects.get(pk=pk)
        except City.DoesNotExist:
            raise Http404

    def list(self, request):
        """
        Please provide endpoint description
        """
        items = City.objects.all()
        serializer = CitySerializer(items, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = CitySerializer(item)
        return Response(serializer.data)

    def create(self, request):
        """
        Please provide endpoint description
        """
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = CitySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CountryViewSet(viewsets.ViewSet):
    def get_object(self, pk):
        try:
            return Country.objects.get(pk=pk)
        except Country.DoesNotExist:
            raise Http404

    def list(self, request):
        """
        Please provide endpoint description
        """
        items = Country.objects.all()
        serializer = CountrySerializer(items, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = CountrySerializer(item)
        return Response(serializer.data)

    def create(self, request):
        """
        Please provide endpoint description
        """
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = CountrySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomerViewSet(viewsets.ViewSet):
    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    def list(self, request):
        """
        Please provide endpoint description
        """
        items = Customer.objects.all()
        serializer = CustomerSerializer(items, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = CustomerSerializer(item)
        return Response(serializer.data)

    def create(self, request):
        """
        Please provide endpoint description
        """
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = CustomerSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomerListViewSet(viewsets.ViewSet):
    def get_object(self, pk):
        try:
            return CustomerList.objects.get(pk=pk)
        except CustomerList.DoesNotExist:
            raise Http404

    def list(self, request):
        """
        Please provide endpoint description
        """
        items = Customer_list.objects.all()
        serializer = Customer_listSerializer(items, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = Customer_listSerializer(item)
        return Response(serializer.data)

    def create(self, request):
        """
        Please provide endpoint description
        """
        serializer = Customer_listSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = Customer_listSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FilmViewSet(viewsets.ViewSet):
    def get_object(self, pk):
        try:
            return Film.objects.get(pk=pk)
        except Film.DoesNotExist:
            raise Http404

    def list(self, request):
        """
        Please provide endpoint description
        """
        items = Film.objects.all()
        serializer = FilmSerializer(items, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = FilmSerializer(item)
        return Response(serializer.data)

    def create(self, request):
        """
        Please provide endpoint description
        """
        serializer = FilmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = FilmSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FilmActorViewSet(viewsets.ViewSet):
    def get_object(self, pk):
        try:
            return FilmActor.objects.get(pk=pk)
        except FilmActor.DoesNotExist:
            raise Http404

    def list(self, request):
        """
        Please provide endpoint description
        """
        items = Film_actor.objects.all()
        serializer = Film_actorSerializer(items, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = Film_actorSerializer(item)
        return Response(serializer.data)

    def create(self, request):
        """
        Please provide endpoint description
        """
        serializer = Film_actorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = Film_actorSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FilmCategoryViewSet(viewsets.ViewSet):
    def get_object(self, pk):
        try:
            return FilmCategory.objects.get(pk=pk)
        except FilmCategory.DoesNotExist:
            raise Http404

    def list(self, request):
        """
        Please provide endpoint description
        """
        items = Film_category.objects.all()
        serializer = Film_categorySerializer(items, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = Film_categorySerializer(item)
        return Response(serializer.data)

    def create(self, request):
        """
        Please provide endpoint description
        """
        serializer = Film_categorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = Film_categorySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FilmListViewSet(viewsets.ViewSet):
    def get_object(self, pk):
        try:
            return FilmList.objects.get(pk=pk)
        except FilmList.DoesNotExist:
            raise Http404

    def list(self, request):
        """
        Please provide endpoint description
        """
        items = Film_list.objects.all()
        serializer = Film_listSerializer(items, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = Film_listSerializer(item)
        return Response(serializer.data)

    def create(self, request):
        """
        Please provide endpoint description
        """
        serializer = Film_listSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = Film_listSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FilmTextViewSet(viewsets.ViewSet):
    def get_object(self, pk):
        try:
            return FilmText.objects.get(pk=pk)
        except FilmText.DoesNotExist:
            raise Http404

    def list(self, request):
        """
        Please provide endpoint description
        """
        items = Film_text.objects.all()
        serializer = Film_textSerializer(items, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = Film_textSerializer(item)
        return Response(serializer.data)

    def create(self, request):
        """
        Please provide endpoint description
        """
        serializer = Film_textSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = Film_textSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class InventoryViewSet(viewsets.ViewSet):
    def get_object(self, pk):
        try:
            return Inventory.objects.get(pk=pk)
        except Inventory.DoesNotExist:
            raise Http404

    def list(self, request):
        """
        Please provide endpoint description
        """
        items = Inventory.objects.all()
        serializer = InventorySerializer(items, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = InventorySerializer(item)
        return Response(serializer.data)

    def create(self, request):
        """
        Please provide endpoint description
        """
        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = InventorySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LanguageViewSet(viewsets.ViewSet):
    def get_object(self, pk):
        try:
            return Language.objects.get(pk=pk)
        except Language.DoesNotExist:
            raise Http404

    def list(self, request):
        """
        Please provide endpoint description
        """
        items = Language.objects.all()
        serializer = LanguageSerializer(items, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = LanguageSerializer(item)
        return Response(serializer.data)

    def create(self, request):
        """
        Please provide endpoint description
        """
        serializer = LanguageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = LanguageSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NicerButSlowerFilmListViewSet(viewsets.ViewSet):
    def get_object(self, pk):
        try:
            return NicerButSlowerFilmList.objects.get(pk=pk)
        except NicerButSlowerFilmList.DoesNotExist:
            raise Http404

    def list(self, request):
        """
        Please provide endpoint description
        """
        items = Nicer_but_slower_film_list.objects.all()
        serializer = Nicer_but_slower_film_listSerializer(items, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = Nicer_but_slower_film_listSerializer(item)
        return Response(serializer.data)

    def create(self, request):
        """
        Please provide endpoint description
        """
        serializer = Nicer_but_slower_film_listSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = Nicer_but_slower_film_listSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PaymentViewSet(viewsets.ViewSet):
    def get_object(self, pk):
        try:
            return Payment.objects.get(pk=pk)
        except Payment.DoesNotExist:
            raise Http404

    def list(self, request):
        """
        Please provide endpoint description
        """
        items = Payment.objects.all()
        serializer = PaymentSerializer(items, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = PaymentSerializer(item)
        return Response(serializer.data)

    def create(self, request):
        """
        Please provide endpoint description
        """
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = PaymentSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RentalViewSet(viewsets.ViewSet):
    def get_object(self, pk):
        try:
            return Rental.objects.get(pk=pk)
        except Rental.DoesNotExist:
            raise Http404

    def list(self, request):
        """
        Please provide endpoint description
        """
        items = Rental.objects.all()
        serializer = RentalSerializer(items, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = RentalSerializer(item)
        return Response(serializer.data)

    def create(self, request):
        """
        Please provide endpoint description
        """
        serializer = RentalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = RentalSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SalesByFilmCategoryViewSet(viewsets.ViewSet):
    def get_object(self, pk):
        try:
            return SalesByFilmCategory.objects.get(pk=pk)
        except SalesByFilmCategory.DoesNotExist:
            raise Http404

    def list(self, request):
        """
        Please provide endpoint description
        """
        items = Sales_by_film_category.objects.all()
        serializer = Sales_by_film_categorySerializer(items, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = Sales_by_film_categorySerializer(item)
        return Response(serializer.data)

    def create(self, request):
        """
        Please provide endpoint description
        """
        serializer = Sales_by_film_categorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = Sales_by_film_categorySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SalesByStoreViewSet(viewsets.ViewSet):
    def get_object(self, pk):
        try:
            return SalesByStore.objects.get(pk=pk)
        except SalesByStore.DoesNotExist:
            raise Http404

    def list(self, request):
        """
        Please provide endpoint description
        """
        items = Sales_by_store.objects.all()
        serializer = Sales_by_storeSerializer(items, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = Sales_by_storeSerializer(item)
        return Response(serializer.data)

    def create(self, request):
        """
        Please provide endpoint description
        """
        serializer = Sales_by_storeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = Sales_by_storeSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StaffViewSet(viewsets.ViewSet):
    def get_object(self, pk):
        try:
            return Staff.objects.get(pk=pk)
        except Staff.DoesNotExist:
            raise Http404

    def list(self, request):
        """
        Please provide endpoint description
        """
        items = Staff.objects.all()
        serializer = StaffSerializer(items, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = StaffSerializer(item)
        return Response(serializer.data)

    def create(self, request):
        """
        Please provide endpoint description
        """
        serializer = StaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = StaffSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StaffListViewSet(viewsets.ViewSet):
    def get_object(self, pk):
        try:
            return StaffList.objects.get(pk=pk)
        except StaffList.DoesNotExist:
            raise Http404

    def list(self, request):
        """
        Please provide endpoint description
        """
        items = Staff_list.objects.all()
        serializer = Staff_listSerializer(items, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = Staff_listSerializer(item)
        return Response(serializer.data)

    def create(self, request):
        """
        Please provide endpoint description
        """
        serializer = Staff_listSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = Staff_listSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StoreViewSet(viewsets.ViewSet):
    def get_object(self, pk):
        try:
            return Store.objects.get(pk=pk)
        except Store.DoesNotExist:
            raise Http404

    def list(self, request):
        """
        Please provide endpoint description
        """
        items = Store.objects.all()
        serializer = StoreSerializer(items, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = StoreSerializer(item)
        return Response(serializer.data)

    def create(self, request):
        """
        Please provide endpoint description
        """
        serializer = StoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        serializer = StoreSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Please provide endpoint description
        """
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
