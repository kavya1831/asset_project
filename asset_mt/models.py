from __future__ import unicode_literals

from django.db import models

# Create your models here.
class AssetTable(models.Model):
    id           = models.AutoField(primary_key=True)
    asset_name   = models.CharField(max_length=100,default="N/A")
    asset_room   = models.CharField(max_length=80)
    asset_pv     = models.IntegerField(max_length= 50, default="N/A")


    def save(self,*args,**kwargs):
        return super(AssetTable,self).save(*args,**kwargs)

    def __unicode__(self):
        return str(self.id)

    class Meta:
        db_table  ='asset_table_1'
        app_label = 'asset_mt'