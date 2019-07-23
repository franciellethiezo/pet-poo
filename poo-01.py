from datetime import datetime

class Pessoa:
	def __init__(self, nome_pessoa, data_nasc):
		self.nome_pessoa = nome_pessoa
		self.data_nasc = datetime.strptime(data_nasc, '%d/%m/%Y')

	def imprimir_nome(self):
		print(self.nome_pessoa)
	
	def imprimir_idade(self):
		hoje = datetime.today()
		ano_nasc = self.data_nasc.year
		idade = hoje.year - ano_nasc
		print(idade)

class Pet: 
	def __init__(self, nome_pet, nome_dono, data_nasc):
		self.nome_pet = nome_pet
		self.nome_dono = nome_dono
		self.data_nasc = datetime.strptime(data_nasc, '%d/%m/%Y')

	def imprimir_pet(self):
		print(self.nome_pet)

	def imprimir_dono(self):
		print(self.nome_dono)
	
	def imprimir_nasc(self):
		hoje = datetime.today()
		ano_nasc = self.data_nasc.year
		idade = hoje.year - ano_nasc
		print(idade)

dono = Pessoa("Victor", "14/08/1995")
dono.imprimir_nome()
dono.imprimir_idade()

pet = Pet("nightmare", "Victor", "22/07/2017")
pet.imprimir_pet()
pet.imprimir_nasc()
pet.imprimir_dono()