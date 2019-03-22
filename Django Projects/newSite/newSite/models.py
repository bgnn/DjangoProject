from django.db import models
from django.utils import timezone
 
class Cliente(models.Model):
    
    nome = models.CharField(
                max_length=255,
                null=False,
                blank=False            
            )
    
    endereco = models.CharField(
                max_length=255,
                null=False,
                blank=False            
            )
    
    cep = models.CharField(
            max_length=255,
            null=False,
            blank=False
            )
    
    objetos = models.Manager()
    
    
class Pedido(models.Model):
    
    idCliente = models.IntegerField(
                null=False,
                blank=False            
            )
    
    produto = models.CharField(
            max_length=255,
            null=False,
            blank=False
            )
    
    teste = models.CharField(
            max_length=255,
            null=False,
            blank=False,
            default='teste'
            )

    flag_atendido = models.BooleanField(
            default=False,
            )


    objetos = models.Manager()
	
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title