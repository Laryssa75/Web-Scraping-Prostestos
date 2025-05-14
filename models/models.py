from django.db import models

class ConsultaCNPJ(models.Model):
    Status_decisoes = [
        ('pendente', 'Pendente'),
        ('consultado', 'Consultado'),
    ]

    cnpj = models.CharField(max_length= 18, unique=True)
    resultado = models.TextField(blank=True, null=True)
    consultado_data = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=Status_decisoes, default='pendente')

    def __str__(self):
        return self.cnpj
