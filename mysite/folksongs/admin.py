from django.contrib import admin

from .models import Song, SongImage

class SongImageAdmin(admin.StackedInline):
	model=SongImage

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
	inlines = [SongImageAdmin]

	class Meta:
		model=Song

@admin.register(SongImage)
class SongImageAdmin(admin.ModelAdmin):
	pass