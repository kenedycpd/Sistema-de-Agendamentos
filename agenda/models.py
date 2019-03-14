from django.db import models
from cliente.models import Person
from profissional.models import Prof, Service

class Agenda(models.Model):
	cliente = models.ForeignKey(Person, on_delete=models.CASCADE,null=True,blank=True)
	profissional = models.ForeignKey(Prof, on_delete=models.CASCADE,null=True,blank=True)
	servico = models.ForeignKey(Service, on_delete=models.CASCADE,null=True,blank=True)
	data = models.DateField(auto_now_add=False, null=True)
	hora = models.TimeField(auto_now_add=False, null=True)
	statu = (
		('A', 'Aberto'),
		('E', 'Andamento'),
		('F', 'Fechado'),
		)
	status = models.CharField('Status', max_length=1, choices=statu, null=True,blank=True)
	preco = models.DecimalField('Preço', max_digits=7, decimal_places=2,null=True,blank=True)
	pag = (
    	('D', 'Dinheiro'),
    	('CD', 'Cartão Debito'),
    	('CC', 'Cartão Credito'),
    	)
	pagamento = models.CharField('Pagamento', max_length=2, choices=pag, null=True,blank=True)
	class Meta:
		verbose_name_plural = 'Agenda'
		verbose_name = 'Agenda'

	

	def __str__(self):
		return "%s" % self.cliente