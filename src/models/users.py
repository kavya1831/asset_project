from django.db import models

class Users(models.Model):
    id           = models.AutoField(primary_key=True)
    asset_name   = models.CharField(max_length=100, default="")
    asset_room   = models.CharField(max_length=80,default="")
    asset_pv     = models.CharField(max_length=10, default="")



    def save(self,*args,**kwargs):
        return super(Users,self).save(*args,**kwargs)

    def __unicode__(self):
        return str(self.id)

    class Meta:
        db_table  ='users'
        app_label = 'src'