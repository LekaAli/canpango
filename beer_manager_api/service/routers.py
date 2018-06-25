from django.conf.urls import url, include
from rest_framework import routers
from viewsets import UserViewSet, BeerViewSet, ReviewViewSet, UserBeerRatingViewSet


router = routers.DefaultRouter()
router.register('user', UserViewSet, base_name='user')
router.register('beer', BeerViewSet, base_name='beer')
router.register('review', ReviewViewSet, base_name='review')
router.register('userating', UserBeerRatingViewSet, base_name='user-rating')

# urlpatterns = [
# 	url(r'endpoints', include(router.urls)),
# 	]

urlpatterns = router.urls