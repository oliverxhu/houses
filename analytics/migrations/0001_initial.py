# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 12:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tm_rental_listings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ListingId', models.IntegerField(null=True)),
                ('Address', models.CharField(max_length=255, null=True)),
                ('AdjacentSuburbIds_0', models.IntegerField(null=True)),
                ('AdjacentSuburbIds_1', models.IntegerField(null=True)),
                ('AdjacentSuburbIds_10', models.IntegerField(null=True)),
                ('AdjacentSuburbIds_11', models.IntegerField(null=True)),
                ('AdjacentSuburbIds_12', models.IntegerField(null=True)),
                ('AdjacentSuburbIds_13', models.IntegerField(null=True)),
                ('AdjacentSuburbIds_14', models.IntegerField(null=True)),
                ('AdjacentSuburbIds_2', models.IntegerField(null=True)),
                ('AdjacentSuburbIds_3', models.IntegerField(null=True)),
                ('AdjacentSuburbIds_4', models.IntegerField(null=True)),
                ('AdjacentSuburbIds_5', models.IntegerField(null=True)),
                ('AdjacentSuburbIds_6', models.IntegerField(null=True)),
                ('AdjacentSuburbIds_7', models.IntegerField(null=True)),
                ('AdjacentSuburbIds_8', models.IntegerField(null=True)),
                ('AdjacentSuburbIds_9', models.IntegerField(null=True)),
                ('AdjacentSuburbNames_0', models.CharField(max_length=50, null=True)),
                ('AdjacentSuburbNames_1', models.CharField(max_length=50, null=True)),
                ('AdjacentSuburbNames_10', models.CharField(max_length=50, null=True)),
                ('AdjacentSuburbNames_11', models.CharField(max_length=50, null=True)),
                ('AdjacentSuburbNames_12', models.CharField(max_length=50, null=True)),
                ('AdjacentSuburbNames_13', models.CharField(max_length=50, null=True)),
                ('AdjacentSuburbNames_14', models.CharField(max_length=50, null=True)),
                ('AdjacentSuburbNames_2', models.CharField(max_length=50, null=True)),
                ('AdjacentSuburbNames_3', models.CharField(max_length=50, null=True)),
                ('AdjacentSuburbNames_4', models.CharField(max_length=50, null=True)),
                ('AdjacentSuburbNames_5', models.CharField(max_length=50, null=True)),
                ('AdjacentSuburbNames_6', models.CharField(max_length=50, null=True)),
                ('AdjacentSuburbNames_7', models.CharField(max_length=50, null=True)),
                ('AdjacentSuburbNames_8', models.CharField(max_length=50, null=True)),
                ('AdjacentSuburbNames_9', models.CharField(max_length=50, null=True)),
                ('Agency', models.CharField(max_length=50, null=True)),
                ('AgencyReference', models.CharField(max_length=50, null=True)),
                ('Agency_Agents_0_FullName', models.CharField(max_length=100, null=True)),
                ('Agency_Agents_0_MobilePhoneNumber', models.CharField(max_length=20, null=True)),
                ('Agency_Agents_0_OfficePhoneNumber', models.CharField(max_length=20, null=True)),
                ('Agency_Agents_0_Photo', models.CharField(max_length=255, null=True)),
                ('Agency_Agents_0_UrlSlug', models.CharField(max_length=50, null=True)),
                ('Agency_Agents_1_FullName', models.CharField(max_length=100, null=True)),
                ('Agency_Agents_1_MobilePhoneNumber', models.CharField(max_length=20, null=True)),
                ('Agency_Agents_1_OfficePhoneNumber', models.CharField(max_length=20, null=True)),
                ('Agency_Agents_1_Photo', models.CharField(max_length=255, null=True)),
                ('Agency_Agents_1_UrlSlug', models.CharField(max_length=50, null=True)),
                ('Agency_Branding_BackgroundColor', models.CharField(max_length=7, null=True)),
                ('Agency_Branding_DisableBanner', models.NullBooleanField()),
                ('Agency_Branding_LargeBannerURL', models.CharField(max_length=255, null=True)),
                ('Agency_Branding_OfficeLocation', models.CharField(max_length=100, null=True)),
                ('Agency_Branding_StrokeColor', models.CharField(max_length=7, null=True)),
                ('Agency_Branding_TextColor', models.CharField(max_length=7, null=True)),
                ('Agency_FaxNumber', models.CharField(max_length=20, null=True)),
                ('Agency_Id', models.IntegerField(null=True)),
                ('Agency_IsLicensedPropertyAgency', models.NullBooleanField()),
                ('Agency_IsRealEstateAgency', models.NullBooleanField()),
                ('Agency_Logo', models.CharField(max_length=255, null=True)),
                ('Agency_Logo2', models.CharField(max_length=255, null=True)),
                ('Agency_Name', models.CharField(max_length=255, null=True)),
                ('Agency_PhoneNumber', models.CharField(max_length=20, null=True)),
                ('Agency_Website', models.CharField(max_length=255, null=True)),
                ('Amenities', models.CharField(max_length=255, null=True)),
                ('AsAt', models.CharField(max_length=21, null=True)),
                ('AvailableFrom', models.CharField(max_length=50, null=True)),
                ('Bathrooms', models.SmallIntegerField(null=True)),
                ('Bedrooms', models.SmallIntegerField(null=True)),
                ('BestContactTime', models.CharField(max_length=50, null=True)),
                ('Category', models.CharField(max_length=15, null=True)),
                ('CategoryPath', models.CharField(max_length=255, null=True)),
                ('District', models.CharField(max_length=50, null=True)),
                ('DistrictId', models.SmallIntegerField(null=True)),
                ('EndDate', models.CharField(max_length=21, null=True)),
                ('GeographicLocation_Accuracy', models.SmallIntegerField(null=True)),
                ('GeographicLocation_Easting', models.DecimalField(decimal_places=10, max_digits=15, null=True)),
                ('GeographicLocation_Latitude', models.DecimalField(decimal_places=10, max_digits=15, null=True)),
                ('GeographicLocation_Longitude', models.DecimalField(decimal_places=10, max_digits=15, null=True)),
                ('GeographicLocation_Northing', models.DecimalField(decimal_places=10, max_digits=15, null=True)),
                ('HasEmbeddedVideo', models.NullBooleanField()),
                ('HasGallery', models.NullBooleanField()),
                ('IdealTenant', models.CharField(max_length=255, null=True)),
                ('IsBold', models.NullBooleanField()),
                ('IsClassified', models.NullBooleanField()),
                ('IsFeatured', models.NullBooleanField()),
                ('IsHighlighted', models.NullBooleanField()),
                ('IsSuperFeatured', models.NullBooleanField()),
                ('ListingGroup', models.CharField(max_length=25, null=True)),
                ('ListingLength', models.NullBooleanField()),
                ('MaxTenants', models.DecimalField(decimal_places=10, max_digits=15, null=True)),
                ('NoteDate', models.CharField(max_length=25, null=True)),
                ('Parking', models.CharField(max_length=255, null=True)),
                ('PetsOkay', models.DecimalField(decimal_places=10, max_digits=15, null=True)),
                ('PhotoUrls_0', models.CharField(max_length=255, null=True)),
                ('PhotoUrls_1', models.CharField(max_length=255, null=True)),
                ('PhotoUrls_10', models.CharField(max_length=255, null=True)),
                ('PhotoUrls_11', models.CharField(max_length=255, null=True)),
                ('PhotoUrls_12', models.CharField(max_length=255, null=True)),
                ('PhotoUrls_13', models.CharField(max_length=255, null=True)),
                ('PhotoUrls_14', models.CharField(max_length=255, null=True)),
                ('PhotoUrls_15', models.CharField(max_length=255, null=True)),
                ('PhotoUrls_16', models.CharField(max_length=255, null=True)),
                ('PhotoUrls_17', models.CharField(max_length=255, null=True)),
                ('PhotoUrls_18', models.CharField(max_length=255, null=True)),
                ('PhotoUrls_2', models.CharField(max_length=255, null=True)),
                ('PhotoUrls_3', models.CharField(max_length=255, null=True)),
                ('PhotoUrls_4', models.CharField(max_length=255, null=True)),
                ('PhotoUrls_5', models.CharField(max_length=255, null=True)),
                ('PhotoUrls_6', models.CharField(max_length=255, null=True)),
                ('PhotoUrls_7', models.CharField(max_length=255, null=True)),
                ('PhotoUrls_8', models.CharField(max_length=255, null=True)),
                ('PhotoUrls_9', models.CharField(max_length=255, null=True)),
                ('PictureHref', models.CharField(max_length=255, null=True)),
                ('PriceDisplay', models.CharField(max_length=50, null=True)),
                ('PropertyId', models.CharField(max_length=20, null=True)),
                ('PropertyType', models.CharField(max_length=20, null=True)),
                ('Region', models.CharField(max_length=50, null=True)),
                ('RegionId', models.SmallIntegerField(null=True)),
                ('RentPerWeek', models.IntegerField(null=True)),
                ('ReserveState', models.SmallIntegerField(null=True)),
                ('SmokersOkay', models.DecimalField(decimal_places=10, max_digits=15, null=True)),
                ('StartDate', models.CharField(max_length=21, null=True)),
                ('StartPrice', models.IntegerField(null=True)),
                ('Suburb', models.CharField(max_length=50, null=True)),
                ('SuburbId', models.IntegerField(null=True)),
                ('Title', models.CharField(max_length=100, null=True)),
                ('Whiteware', models.CharField(max_length=255, null=True)),
                ('job_run_datetime', models.DateTimeField(null=True)),
            ],
        ),
    ]