from django.db import models


class AirportsData(models.Model):
    id = models.AutoField(db_column="ID", primary_key=True)  # Field name made lowercase.
    aid = models.IntegerField(db_column="AID", blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column="Name", max_length=200, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column="City", max_length=45, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column="Country", max_length=45, blank=True, null=True)  # Field name made lowercase.
    iata_code = models.CharField(
        db_column="IATA_Code", max_length=45, blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    icao_code = models.CharField(
        db_column="ICAO_Code", max_length=45, blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lat = models.DecimalField(db_column="Lat", max_digits=15, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    lng = models.DecimalField(db_column="Lng", max_digits=15, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    max_runway_ft_field = models.CharField(
        db_column="Max_Runway(ft)", max_length=45, blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    continent = models.CharField(db_column="Continent", max_length=45, blank=True, null=True)  # Field name made lowercase.
    hub = models.IntegerField(db_column="Hub", blank=True, null=True)  # Field name made lowercase.
    base = models.IntegerField(db_column="Base", blank=True, null=True)  # Field name made lowercase.
    destination = models.IntegerField(db_column="Destination", blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "airports_data"

    def __str__(self):
        return self.name


class PlaneData(models.Model):
    id = models.AutoField(db_column="ID", primary_key=True)  # Field name made lowercase.
    model = models.CharField(max_length=45, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    range_km_field = models.IntegerField(
        db_column="range(km)", blank=True, null=True
    )  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    speed_kph_field = models.IntegerField(
        db_column="speed(kph)", blank=True, null=True
    )  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    passengers = models.IntegerField(blank=True, null=True)
    co2_cost_lb_per_km_field = models.IntegerField(
        db_column="co2_cost(lb_per_km)", blank=True, null=True
    )  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    runway_required_ft_field = models.IntegerField(
        db_column="runway_required(ft)", blank=True, null=True
    )  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    a_check_price = models.IntegerField(db_column="a-check_price", blank=True, null=True)  # Field renamed to remove unsuitable characters.
    main_check_hours_field = models.IntegerField(
        db_column="main_check(hours)", blank=True, null=True
    )  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    co2_emission_kg_pax_km_field = models.DecimalField(
        db_column="co2_emission(kg/pax/km)", max_digits=5, decimal_places=3, blank=True, null=True
    )  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    delivery_time = models.TimeField(blank=True, null=True)
    service_ciling_ft_field = models.IntegerField(
        db_column="service_ciling(ft)", blank=True, null=True
    )  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = "plane_data"


class PriceHistory(models.Model):
    time = models.CharField(max_length=45, blank=True, null=True)
    fuel = models.IntegerField(blank=True, null=True)
    co2 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "price_history"


class Routes(models.Model):
    route = models.CharField(max_length=255, blank=True, null=True)
    route_type = models.CharField(max_length=15, blank=True, null=True)
    distance = models.IntegerField(blank=True, null=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = "routes"
