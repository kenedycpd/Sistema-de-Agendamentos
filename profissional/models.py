from django.db import models


class Prof(models.Model):
	nome = models.CharField('Profissional', max_length=100,blank=True)
	telefone = models.CharField('Telefone', max_length=9,blank=True)

	class Meta:
		verbose_name = 'Profissional'
		verbose_name_plural = 'Profissional'

	def __str__(self):
		return self.nome

class Service(models.Model):
	nome = models.CharField('Seviço', max_length=100)
	pag = (
    	('D', 'Dinheiro'),
    	('CD', 'Cartão Debito'),
    	('CC', 'Cartão Credito'),
    	)
	pagamento = models.CharField('Pagamento', max_length=2, choices=pag,blank=True)
	class Meta:
		verbose_name = 'Serviço'
		verbose_name_plural = 'Serviços'

	def __str__(self):
		return self.nome