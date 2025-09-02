from django.db import models


class SinicaArchaeologySites(models.Model):
    id = models.CharField(
        db_column="ID", primary_key=True, max_length=20
    )  # Field name made lowercase.
    name = models.CharField(
        db_column="Name", max_length=20, blank=True, null=True
    )  # Field name made lowercase.
    code = models.CharField(
        db_column="Code", max_length=20, blank=True, null=True
    )  # Field name made lowercase.
    des = models.TextField(
        db_column="Des", blank=True, null=True
    )  # Field name made lowercase.
    era = models.JSONField(
        db_column="Era", blank=True, null=True
    )  # Field name made lowercase.
    culture_type = models.JSONField(
        db_column="Culture_type", blank=True, null=True
    )  # Field name made lowercase.
    rating = models.CharField(
        db_column="Rating", max_length=20, blank=True, null=True
    )  # Field name made lowercase.
    year = models.JSONField(
        db_column="Year", blank=True, null=True
    )  # Field name made lowercase.
    city = models.CharField(
        db_column="City", max_length=20, blank=True, null=True
    )  # Field name made lowercase.
    town = models.CharField(
        db_column="Town", max_length=20, blank=True, null=True
    )  # Field name made lowercase.
    lat = models.DecimalField(
        db_column="Lat", max_digits=13, decimal_places=10, blank=True, null=True
    )  # Field name made lowercase.
    lng = models.DecimalField(
        db_column="Lng", max_digits=13, decimal_places=10, blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "sinica_archaeology_sites"
