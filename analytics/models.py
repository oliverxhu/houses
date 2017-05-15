from django.db import models


# Create your models here.

class Current_Listing(models.Model):
    id_current_listing = models.ForeignKey(Listing)

class Listing(models.Model):
    id_listing = models.IntegerField(primary_key=True)
    listing_type = models.CharField(max_length=20)
    id_agency = models.ForeignKey(Agency)
    is_current = models.NullBooleanField()
    data_source = models.CharField(max_length=20)
    job_run_datetime = models.DateTimeField()
    last_updated = models.DateTimeField()

class Detail_Main_Rental(models.Model):
    id_listing = models.ForeignKey(Listing)
    amenities = models.TextField(null=True)
    available_from = models.DateTimeField(null=True)
    bathrooms = models.PositiveSmallIntegerField(null=True)
    bedrooms = models.PositiveSmallIntegerField(null=True)
    best_contact_time = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    ideal_tenant = models.TextField(null=True)
    listing_group = models.CharField(max_length=30, null=True)
    max_tenants = models.SmallIntegerField(null=True)
    parking = models.TextField(null=True)
    pets_okay = models.NullBooleanField()
    price_display = models.CharField(max_length=30, null=True)
    property_id = models.CharField(max_length=20, null=True)
    property_type = models.CharField(max_length=20, null=True)
    smokers_okay = models.NullBooleanField()
    start_date = models.DateTimeField(null=True)
    start_price = models.DecimalField(max_digits=11, decimal_places=2, null=True)
    title = models.CharField(max_digits=100, null=True)
    rent_per_week = models.DecimalField(max_digits=11, decimal_places=2, null=True)
    whiteware = models.CharField(max_length=255, null=True)
    last_updated = models.DateTimeField()

class Detail_Main_Residential(models.Model):
    id_listing = models.ForeignKey(Listing)
    amenities = models.TextField(null=True)
    available_from = models.DateTimeField(null=True)
    bathrooms = models.PositiveSmallIntegerField(null=True)
    bedrooms = models.PositiveSmallIntegerField(null=True)
    best_contact_time = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    ideal_tenant = models.TextField(null=True)
    listing_group = models.CharField(max_length=30, null=True)
    max_tenants = models.SmallIntegerField(null=True)
    parking = models.TextField(null=True)
    pets_okay = models.NullBooleanField()
    price_display = models.CharField(max_length=30, null=True)
    property_id = models.CharField(max_length=20, null=True)
    property_type = models.CharField(max_length=20, null=True)
    smokers_okay = models.NullBooleanField()
    start_date = models.DateTimeField(null=True)
    start_price = models.DecimalField(max_digits=11, decimal_places=2, null=True)
    title = models.CharField(max_digits=100, null=True)
    rent_per_week = models.DecimalField(max_digits=11, decimal_places=2, null=True)
    whiteware = models.CharField(max_length=255, null=True)
    last_updated = models.DateTimeField()

class Agency(models.Model):
    id_agency = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    fax = models.CharField(max_length=30, null=True)
    is_licenced_property = models.NullBooleanField()
    is_real_estate = models.NullBooleanField()
    phone = models.CharField(max_length=30, null=True)
    website = models.URLField(null=True)
    last_updated = models.DateTimeField()

class Agency_Brand(models.Model):
    id_agency = models.ForeignKey(Agency)
    logo1 = models.URLField(null=True)
    logo2 = models.URLField(null=True)
    brand_background_color = models.CharField(max_length=20, null=True)
    brand_stroke_color = models.CharField(max_length=20, null=True)
    brand_text_color = models.CharField(max_length=20, null=True)
    brand_large_banner = models.URLField(null=True)
    brand_disable_banner = models.NullBooleanField()
    brand_office_location = models.CharField(max_length=100)
    last_updated = models.DateTimeField()

class Agent(models.Model):
    id_agent = models.IntegerField(primary_key=True)
    fullname = models.CharField(max_length=50, null=True)
    mobile = models.CharField(max_length=20, null=True)
    office_phone = models.CharField(max_length=20, null=True)
    photo = models.URLField(null=True)
    url_slug = models.CharField(max_length=50, null=True)
    last_updated = models.DateTimeField()

class Agent_Detail(models.Model):
    id_listing = models.ForeignKey(Listing)
    id_agent = models.ForeignKey(Agent)
    last_updated = models.DateTimeField()

class Listing_Location(models.Model):
    id_listing = models.ForeignKey(Listing)
    id_location = models.ForeignKey(Location)
    address = models.CharField(max_length=255, null=True)
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    easting = models.CharField(max_length=20)
    northing = models.CharField(max_length=20)
    last_updated = models.DateTimeField()

class Region(models.Model):
    id_region = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    last_updated = models.DateTimeField()

class District(models.Model):
    id_district = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    last_updated = models.DateTimeField()

class Suburb(models.Model):
    id_suburb = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    last_updated = models.DateTimeField()

class Location(models.Model):
    id_location = models.IntegerField(primary_key=True)
    id_region = models.ForeignKey(Region)
    id_district = models.ForeignKey(District)
    id_suburb = models.ForeignKey(Suburb)
    last_updated = models.DateTimeField()

class Adjacent_Suburb(models.Model):
    id_listing = models.ForeignKey(Listing)
    id_adjacent_suburb = models.ForeignKey(Suburb)
    last_updated = models.DateTimeField()

class Tm_Detail_Sub_Rental(models.Model):
    id_listing = models.ForeignKey(Listing)
    agency_reference = models.CharField(max_length=30)
    category = models.CharField(max_length=30, null=True)
    category_path = models.CharField(max_length=100, null=True)
    has_embedded_video = models.NullBooleanField()
    has_gallery = models.NullBooleanField()
    is_bold = models.NullBooleanField()
    is_featured = models.NullBooleanField()
    is_highlighted = models.NullBooleanField()
    is_super_featured = models.NullBooleanField()
    listing_length = models.CharField(max_length=20, null=True)  # what is this?
    note_date = models.DateTimeField(null=True)
    reserve_state = models.SmallIntegerField(null=True)
    is_boosted = models.NullBooleanField()
    last_updated = models.DateTimeField()

class Tm_Detail_Sub_Residential(models.Model):
    id_listing = models.ForeignKey(Listing)
    agency_reference = models.CharField(max_length=30)
    category = models.CharField(max_length=30, null=True)
    category_path = models.CharField(max_length=100, null=True)
    has_embedded_video = models.NullBooleanField()
    has_gallery = models.NullBooleanField()
    is_bold = models.NullBooleanField()
    is_featured = models.NullBooleanField()
    is_highlighted = models.NullBooleanField()
    is_super_featured = models.NullBooleanField()
    listing_length = models.CharField(max_length=20, null=True)  # what is this?
    note_date = models.DateTimeField(null=True)
    reserve_state = models.SmallIntegerField(null=True)
    is_boosted = models.NullBooleanField()
    last_updated = models.DateTimeField()

class Photo(models.Model):
    id_listing = models.ForeignKey(Listing)
    photo_key = models.CharField(max_length=20)
    last_updated = models.DateTimeField()

class photo_type_helper(models.Model):
    id_photo_type = models.SmallIntegerField(primary_key=True)
    url_name = models.CharField(max_length=30)
    description = models.CharField(max_length=50, null=True)
    last_updated = models.DateTimeField()
