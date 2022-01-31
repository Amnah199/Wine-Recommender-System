# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import json

# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group'
#
#
# class AuthGroupPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)
#
#
# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)
#
#
# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.BooleanField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.BooleanField()
#     is_active = models.BooleanField()
#     date_joined = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user'
#
#
# class AuthUserGroups(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)
#
#
# class AuthUserUserPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)
#
#
# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.SmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'
#
#
# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)
#
#
# class DjangoMigrations(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_migrations'
#
#
# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_session'
#
#
# class DjangoSite(models.Model):
#     domain = models.CharField(unique=True, max_length=100)
#     name = models.CharField(max_length=50)
#
#     class Meta:
#         managed = False
#         db_table = 'django_site'


class Wine(models.Model):
    wine_id = models.IntegerField(primary_key=True)
    wine_name = models.TextField(blank=True, null=True)
    wine_type = models.TextField(blank=True, null=True)
    wine_year = models.IntegerField(blank=True, null=True)
    wine_alcohol = models.FloatField(blank=True, null=True)
    wine_country = models.TextField(blank=True, null=True)
    wine_price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wine'


class LocalWine(models.Model):
    lw_id = models.IntegerField(primary_key=True)
    lw_name = models.TextField(blank=True, null=True)
    lw_country = models.TextField(blank=True, null=True)
    lw_region = models.TextField(blank=True, null=True)
    lw_year = models.TextField(blank=True, null=True)
    lw_type = models.TextField(blank=True, null=True)
    lw_price = models.TextField(blank=True, null=True)
    lw_alcohol = models.TextField(blank=True, null=True)
    lw_seller = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'local_wine'


class Flavor(models.Model):
    flavor_id = models.IntegerField(primary_key=True)
    flavor_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flavor'


class FlavorGroup(models.Model):
    group_id = models.BigIntegerField(primary_key=True)
    group_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flavor_group'


class FlavorWine(models.Model):
    flavor_wine_id = models.IntegerField(primary_key=True)
    flavor_group = models.TextField(blank=True, null=True)
    flavor_count = models.IntegerField(blank=True, null=True)
    wine = models.ForeignKey(Wine, on_delete=models.DO_NOTHING)
    flavor = models.ForeignKey(Flavor, on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'flavor_wine'


class FlavorWineGroup(models.Model):
    flavor_wine_group_id = models.IntegerField(primary_key=True)
    flavor_wine_group_score = models.FloatField(blank=True, null=True)
    wine = models.ForeignKey(Wine, on_delete=models.DO_NOTHING)
    group = models.ForeignKey(FlavorGroup, on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'flavor_wine_group'


class WineStructure(models.Model):
    wine_structure_id = models.IntegerField(primary_key=True)
    wine_acidity = models.FloatField(blank=True, null=True)
    wine_fizziness = models.FloatField(blank=True, null=True)
    wine_intensity = models.FloatField(blank=True, null=True)
    wine_sweetness = models.FloatField(blank=True, null=True)
    wine = models.ForeignKey(Wine, on_delete=models.DO_NOTHING)

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