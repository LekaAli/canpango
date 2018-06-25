from __future__ import unicode_literals

from django.db import models


class User(models.Model):

	username = models.CharField(max_length=30, null=False, blank=False)
	password = models.CharField(max_length=30, null=False, blank=False)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)


	def __str__(self):
		return '%s' % self.username


class Beer(models.Model):

	creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='beer', null=False, blank=False)
	# name = models.CharField(max_length=80)
	ibu = models.CharField(max_length=30)
	calories = models.CharField(max_length=30)
	alcohol_by_volume = models.CharField(max_length=30)
	style = models.CharField(max_length=30)
	brewery_location = models.CharField(max_length=50, null=False, blank=False)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '%s' % self.created

	def save(self, *args, **kwargs):
		import datetime
		now = datetime.datetime.now()
		beer_list = Beer.objects.filter(
				creator=self.creator, 
				created__year=now.year, 
				created__month=now.month, 
				created__day=now.day
			)
		if beer_list.count() == 0:
			super(Beer, self).save(*args, **kwargs)


class Review(models.Model):

	AROMA_RATING_OPTIONS = (
		(1, 1), 
		(2, 2), 
		(3, 3), 
		(4, 4), 
		(5, 5)
		)
	APPEARANCE_RATING_OPTIONS = (
		(1, 1), 
		(2, 2), 
		(3, 3), 
		(4, 4), 
		(5, 5)
		)
	TASTE_RATING_OPTIONS = (
		(1, 1), 
		(2, 2), 
		(3, 3), 
		(4, 4), 
		(5, 5), 
		(6, 6), 
		(7, 7), 
		(8, 8), 
		(9, 9), 
		(10, 10)
		)
	reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review', null=False, blank=False)
	beer = models.ForeignKey(Beer, on_delete=models.CASCADE, related_name='review', null=False, blank=False)
	aroma = models.PositiveIntegerField(choices=AROMA_RATING_OPTIONS, default=1)
	apperance = models.PositiveIntegerField(choices=APPEARANCE_RATING_OPTIONS, default=1)
	taste = models.PositiveIntegerField(choices=TASTE_RATING_OPTIONS, default=1)
	overall = models.PositiveIntegerField()
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '%s : %s : %s' % (self.reviewer, self.beer, self.created)

	# def save(self, *args, **kwargs):
	# 	pass

