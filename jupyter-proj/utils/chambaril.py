


class Chambaril(object):

	ingredientes = ['paio', 'pirao', 'arroz', 'legumes', 'cenoura', 'maxixe']
	temperatura = 26
	apimentado = False

	def __init__(self, *args, **kwargs):
		super(Chambaril, self).__init__()

	@property
	def preco(self):
		return 10.00

	@property
	def is_cold(self):
		return self.temperatura < 20

	@property
	def is_hot(self):
		return self.temperatura > 30

	@property
	def faltou_ingredientes(self):
		return len(self.ingredientes) < 6

	def marcelo_colocou_pimenta(self):
		self.apimentado = True