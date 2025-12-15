from django.db import models


class ShipWreck(models.Model):
    shipwreckno = models.CharField(db_column='ShipWreckNo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    latitude = models.DecimalField(db_column='Latitude', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    longitude = models.DecimalField(db_column='Longitude', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    length = models.CharField(db_column='Length', max_length=45, blank=True, null=True)  # Field name made lowercase.
    weight = models.IntegerField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.
    sinkyear = models.IntegerField(db_column='SinkYear', blank=True, null=True)  # Field name made lowercase.
    buildyear = models.IntegerField(db_column='BuildYear', blank=True, null=True)  # Field name made lowercase.
    nationality = models.CharField(db_column='Nationality', max_length=45, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=45, blank=True, null=True)  # Field name made lowercase.
    propulsion = models.CharField(db_column='Propulsion', max_length=45, blank=True, null=True)  # Field name made lowercase.
    causelost = models.CharField(db_column='CauseLost', max_length=45, blank=True, null=True)  # Field name made lowercase.
    death = models.IntegerField(db_column='Death', blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=45, blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ship_wreck'
