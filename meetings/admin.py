from django.contrib import admin
from .models import Meeting, Room
# Register your models here.
@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    pass

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass

