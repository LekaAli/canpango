from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.views import APIView
from  serializers import UserSerializer, BeerSerializer, ReviewSerializer
from models import User, Beer, Review

# class BaseViewSet(APIView):

# 		authentication_classes = 	(SessionAuthentication, BasicAuthentication)
# 		permission_classes = (IsAuthenticated,)

# 		def get(self, request, action, **kwargs):
# 			print kwargs

# 		def post(self, request, *args, **kwargs):
# 			self.get(request, **kwargs)

class UserViewSet(ModelViewSet):

		queryset = User.objects.all()
		serializer_class = UserSerializer
		authentication_classes = 	(SessionAuthentication, BasicAuthentication)
		permission_classes = (IsAuthenticated,)


class BeerViewSet(ModelViewSet):

		queryset = Beer.objects.all()
		serializer_class = BeerSerializer
		authentication_classes = 	(SessionAuthentication, BasicAuthentication)
		permission_classes = (IsAuthenticated,)


class ReviewViewSet(ModelViewSet):

		serializer_class = ReviewSerializer
		authentication_classes = 	(SessionAuthentication, BasicAuthentication)
		permission_classes = (IsAuthenticated,)

		def get_queryset(self):	
			data = self.request.GET
			if data and self.request.method == 'GET':
				beer_name = data.get('beer')
				return Review.objects.filter(beer__name=beer_name)
			return Review.objects.all()