from django.db import models


class Category(models.Model):
  name=models.CharField(max_length=100)

  class Meta:
    verbose_name_plural = "categories"

  def __str__(self):
    return self.name


class Place(models.Model):
  name = models.CharField(max_length=200)
  lat = models.CharField(max_length=100, null=False,blank=True)
  lng = models.CharField(max_length=100, null=False,blank=True)
  is_world_herritage = models.BooleanField(default=False)
  is_city_area = models.BooleanField(default=False)
  major_district = models.CharField(max_length=100)
  description = models.TextField()
  category = models.ManyToManyField(Category)

  def __str__(self):
    return self.name