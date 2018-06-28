from rest_framework import serializers
from models import User, Beer, Review


class UserSerializer(serializers.ModelSerializer):

		class Meta:
				model = User
				fields = '__all__'


class BeerSerializer(serializers.ModelSerializer):

		class Meta:
				model = Beer
				fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):

		class Meta:
				model = Review
				fields = ('reviewer', 'beer', 'aroma', 'apperance', 'taste', 'overall', 'created')
				read_only_field = ('overall')