from rest_framework import viewsets
from rest_framework import permissions
from  serializers import UserSerializer, BeerSerializer, ReviewSerializer
from models import User, Beer, Review


class UserViewSet(viewsets.ModelViewSet):

		queryset = User.objects.all()
		serializer_class = UserSerializer
		permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class BeerViewSet(viewsets.ModelViewSet):

		queryset = Beer.objects.all()
		serializer_class = BeerSerializer
		permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ReviewViewSet(viewsets.ModelViewSet):

		queryset = Review.objects.all()
		serializer_class = ReviewSerializer
		permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserBeerRatingViewSet(viewsets.ModelViewSet):

		queryset = Review.objects.all()
		serializer_class = ReviewSerializer
		permission_classes = (permissions.IsAuthenticatedOrReadOnly,)