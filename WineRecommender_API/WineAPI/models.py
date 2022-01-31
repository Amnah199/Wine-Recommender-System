# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import json


class Wine(models.Model):
    wine_id = models.IntegerField(primary_key=True)
    wine_name = models.TextField(blank=True, null=True)
    wine_winery = models.TextField(blank=True, null=True)
    wine_alcohol = models.TextField(blank=True, null=True)
    wine_type = models.TextField(blank=True, null=True)
    wine_year = models.IntegerField(blank=True, null=True)
    wine_country = models.TextField(blank=True, null=True)
    wine_region = models.TextField(blank=True, null=True)
    wine_thumb = models.TextField(blank=True, null=True)
    wine_price = models.FloatField(blank=True, null=True)
    wine_rating = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wine'


class FlavorGroup(models.Model):
    group_id = models.BigIntegerField(primary_key=True)
    group_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flavor_group'


class FlavorWineGroup(models.Model):
    flavor_wine_group_id = models.BigIntegerField(primary_key=True)
    flavor_wine_group_score = models.FloatField(blank=True, null=True)
    wine = models.ForeignKey(Wine, models.DO_NOTHING, blank=True, null=True)
    group = models.ForeignKey(FlavorGroup, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flavor_wine_group'


class LocalWine(models.Model):
    lw_id = models.IntegerField(primary_key=True)
    lw_name = models.TextField(blank=True, null=True)
    lw_country = models.TextField(blank=True, null=True)
    lw_region = models.TextField(blank=True, null=True)
    lw_year = models.TextField(blank=True, null=True)
    lw_type = models.TextField(blank=True, null=True)
    lw_price = models.FloatField(blank=True, null=True)
    lw_url = models.TextField(blank=True, null=True)
    lw_description = models.TextField(blank=True, null=True)
    lw_seller = models.IntegerField(blank=True, null=True)
    wine = models.ForeignKey(Wine, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'local_wine'


class WineStructure(models.Model):
    wine_structure_id = models.IntegerField(primary_key=True)
    wine_acidity = models.FloatField(blank=True, null=True)
    wine_fizziness = models.FloatField(blank=True, null=True)
    wine_intensity = models.FloatField(blank=True, null=True)
    wine_sweetness = models.FloatField(blank=True, null=True)
    wine = models.ForeignKey(Wine, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wine_structure'

class WineDto:
    def __init__(self, id, name, url=""):
        self.id = id
        self.name = name
        self.url = url

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class WineDetailsDto:
    def __init__(self, id, name, picture_url='', description='', facts=[], taste_data=[]):
        self.id = id,
        self.name = name,
        self.picture_url = picture_url,
        self.description = description,
        self.facts = facts,
        self.taste_data = taste_data

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=False, indent=4)


class WineDetailsFacts:
    def __init__(self, label, content):
        self.label = label
        self.content = content

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=False, indent=4)


class WineDetailsTasteData:
    def __init__(self, label, percentage):
        self.label = label
        self.content = percentage

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=False, indent=4)
