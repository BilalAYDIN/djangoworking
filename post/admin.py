from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):

    list_display=['title','titleiki','titleuc','publishing_date','slug','satış_date','kazanc','confirm','esnaf','alımad','alımtc'] # ,'satış_date' eklicen
    list_display_links=['publishing_date']
    list_filter=['publishing_date']
    search_fields=['title'] # 'publishing_date' burdan çıkarttık çünkü aramayı sadece seri ile yapıcak yani title ile
    list_editable=['title']


    class Meta:
        model=Post


admin.site.register(Post,PostAdmin)
