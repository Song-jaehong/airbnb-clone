from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    fieldsets = (
        (
            "Basic Info",
            {
                "fields": ("name", "description", "country", "price", "address"),
            },
        ),
        (
            "Times",
            {
                "fields": ("check_in", "check_out", "instant_book"),
            },
        ),
        (
            "More About The Space",
            {
                "classes": ("collapse",),
                "fields": (
                    "amenities",
                    "facility",
                    "house_rules",
                ),
            },
        ),
        (
            "Spaces",
            {
                "fields": ("guest", "beds", "bedrooms", "baths"),
            },
        ),
        (
            "Last Detail",
            {
                "fields": ("host",),
            },
        ),
    )

    list_display = (
        "name",
        "description",
        "country",
        "city",
        "price",
        "address",
        "guest",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
    )

    list_filter = (
        "instant_book",
        "room_type",
        "amenities",
        "facility",
        "house_rules",
        "city",
        "country",
    )

    search_fields = ["city"]

    filter_horizontal = (
        "amenities",
        "facility",
        "house_rules",
    )

    def count_amenities(self, obj):

        return "potato"

    count_amenities.short_description = "hello"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    pass