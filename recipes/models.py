from xml.etree.ElementInclude import default_loader

from django.db import models

# EDITED
# title description slug
# preparation_time preparation_time_unit
# servings servings_unit
# preparation_step
# preparation_step_is_html
# created_at updated_at
# is_published
# conver
# category (relação)
# author (relação)


class Recipe(models.Model):
    titile = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=100)
    serving = models.IntegerField()
    servings_unit = models.CharField(max_length=165)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
