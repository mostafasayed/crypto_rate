from django.contrib import admin
from .models import Rate
# Register your models here.


class RateAdmin(admin.ModelAdmin):

    # View all fields as readonly, as data populated from API
    readonly_fields = ('from_currency_code', 'to_currency_code',
                       'exchange_rate', 'bid_price', 'ask_price', 'rate_time')


admin.site.register(Rate, RateAdmin)
