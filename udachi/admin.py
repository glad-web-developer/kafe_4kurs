from django.contrib import admin

# Register your models here.
from udachi.models import TipBluda, Bluda, Ingridienti, IngridientiVBlude, Akzia, Zakaz


class TipBludaAdmin(admin.ModelAdmin):
    pass


admin.site.register(TipBluda, TipBludaAdmin)

class IngridientiAdmin(admin.ModelAdmin):
    pass


admin.site.register(Ingridienti, IngridientiAdmin)


class IngridientiVBludeInline(admin.TabularInline):
    model = IngridientiVBlude


class BludaAdmin(admin.ModelAdmin):
    inlines = [
        IngridientiVBludeInline,
    ]
    list_display = [
        'id',
        'nazvanie',
        'opisanie',
        'cena',
        'gramovka',
        'tip_bluda',
    ]
    list_filter = ('tip_bluda',)
    list_display_links = ['nazvanie',]
    search_fields = ['nazvanie', 'cena','tip_bluda__nazvanie']
    list_editable = [ 'opisanie', 'cena', 'gramovka', 'tip_bluda']
    ordering = ['-nazvanie',]

admin.site.register(Bluda, BludaAdmin)



class AkziaAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'nazvanie',
    ]
    # list_filter = ('nazvanie',)
    list_display_links = ['id', ]
    search_fields = ['nazvanie',]
    list_editable = [ 'nazvanie', ]
    ordering = ['-nazvanie',]

admin.site.register(Akzia, AkziaAdmin)


class ZakazAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'sposob_otdachi',
        'telephone',
        'fio',
        'akzia',
        'data_i_vremia_zakaza',
        'adres',
        'stolik',
        'zakaz_proveden'
    ]

    list_filter = ('sposob_otdachi', 'akzia', 'stolik', 'zakaz_proveden')
    list_display_links = ['id', ]
    search_fields = ['telephone', 'data_i_vremia_zakaza', 'fio', 'adres', 'stolik']
    # list_editable = [ 'nazvanie', ]

    ordering = ['data_i_vremia_zakaza',]

admin.site.register(Zakaz, ZakazAdmin)