from django.db import models

class TempSites(models.Model):
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=45, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    latitude = models.DecimalField(db_column='Latitude', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    longitude = models.DecimalField(db_column='Longitude', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=45, blank=True, null=True)  # Field name made lowercase.
    county = models.CharField(db_column='County', max_length=45, blank=True, null=True)  # Field name made lowercase.
    town = models.CharField(db_column='Town', max_length=45, blank=True, null=True)  # Field name made lowercase.
    towncode = models.CharField(db_column='Towncode', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'temp_sites'
