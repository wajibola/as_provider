from django.db import models

# Create your models here.
class ASInfo(models.Model):
    range_start = models.GenericIPAddressField(protocol='both', unpack_ipv4=False)
    range_end = models.GenericIPAddressField(protocol='both', unpack_ipv4=False)
    as_number = models.IntegerField()
    country_code = models.CharField(max_length=10, null=True)
    as_description = models.TextField()

    class Meta:
        db_table = 'as_info'