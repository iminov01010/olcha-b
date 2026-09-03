from django.db import models


class Top(models.Model):
    id = models.BigAutoField(primary_key=True) 
    img = models.ImageField( upload_to='media/', blank=True, null=True )
    nomi = models.CharField( max_length=150, blank=True, null=True )
    puli = models.DecimalField(  max_digits=10, decimal_places=2, blank=True, null=True )
    oyiga_qancha = models.DecimalField( max_digits=12, decimal_places=2,  blank=True, null=True )
    necha_oyga = models.PositiveIntegerField( blank=True, null=True )

    def __str__(self):
        return self.nomi 


class Tovar(models.Model):
    id = models.BigAutoField(primary_key=True)
    img = models.ImageField( upload_to='media/', blank=True, null=True )
    nomi = models.CharField( max_length=150, blank=True, null=True)
    puli = models.DecimalField( max_digits=10, decimal_places=2, blank=True, null=True )
    oyiga_qancha = models.DecimalField( max_digits=12, decimal_places=2, blank=True, null=True)
    necha_oyga = models.PositiveIntegerField( blank=True, null=True )

    def __str__(self):
        return self.nomi 