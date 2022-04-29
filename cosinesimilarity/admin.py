from django.contrib import admin
from .models import cosinesimilarity

class CosineSimilarityAdmin(admin.ModelAdmin):
    list_display=('link','title','score', 'angle')

# Register your models here.
admin.site.register(cosinesimilarity, CosineSimilarityAdmin)


# Register your models here.
