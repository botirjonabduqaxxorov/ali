from django.db import models




class Xodimlar(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=14)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name
    

class Davomat(models.Model):
    xodim = models.ForeignKey(Xodimlar, on_delete=models.CASCADE)
    sana = models.DateTimeField( auto_now_add = True, null=True)

    def __str__(self):
        return f"{self.xodim.full_name} - {self.sana}"

