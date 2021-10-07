from django.db import models

# Create your models here.


class Rate(models.Model):

    from_currency_code = models.CharField(max_length=10)
    to_currency_code = models.CharField(max_length=10)
    exchange_rate = models.FloatField()
    bid_price = models.FloatField()
    ask_price = models.FloatField()
    rate_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s / %s Rate is %f" % (self.from_currency_code, self.to_currency_code, self.exchange_rate)
