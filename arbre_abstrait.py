"""
Affiche une chaine de caractère avec une certaine identation
"""

def afficher(s,indent=0):
	print(" "*indent+s)
	
class Programme:
	def __init__(self,listeInstructions):
		self.listeInstructions = listeInstructions
	def afficher(self,indent=0):
		afficher("<programme>",indent)
		self.listeInstructions.afficher(indent+1)
		afficher("</programme>",indent)

class ListeInstructions:
	def __init__(self):
		self.instructions = []

	def afficher(self,indent=0):
		afficher("<listeInstructions>",indent)
		for instruction in self.instructions:
			instruction.afficher(indent+1)
		afficher("</listeInstructions>",indent)


class sinonsi:
	def __init__(self,expression,instructions):
		self.expression = expression
		self.instructions = instructions

	def afficher(self,indent=0):
		afficher("<sinonsi>",indent)
		self.expression.afficher(indent+1)
		self.instructions.afficher(indent+1)
		afficher("</sinonsi>",indent)


class listeSinonsi:
	def __init__(self):
		self.sinonsi = []

	def afficher(self,indent=0):
		for sinonsi in self.instructions:
			sinonsi.afficher(indent)
			
class Ecrire:
	def __init__(self,exp):
		self.exp = exp
	def afficher(self,indent=0):
		afficher("<ecrire>",indent)
		self.exp.afficher(indent+1)
		afficher("</ecrire>",indent)


class Operation:
	def __init__(self,op,exp1,exp2):
		self.exp1 = exp1
		self.op = op
		self.exp2 = exp2

	def afficher(self,indent=0):
		afficher("<operation>",indent)
		afficher("[Opérateur:" + self.op + "]",indent+1)
		self.exp1.afficher(indent+1)
		self.exp2.afficher(indent+1)
		afficher("</operation>",indent)


class Entier:
	def __init__(self,valeur):
		self.valeur = valeur

	def afficher(self,indent=0):
		afficher("[Entier:"+str(self.valeur)+"]",indent)


class Booleen:
    def __init__(self,valeur):
        self.valeur = valeur
	
    def afficher (self, indent=0):
        afficher("[Booleen : "+str(self.valeur)+"]",indent)


class Vrai:
	def __init__(self):
		self.valeur = True

	def afficher (self, indent=0):
		afficher("[Vrai : "+str(self.valeur)+"]",indent)


class Faux:
	def __init__(self):
		self.valeur = False

	def afficher (self, indent=0):
		afficher("[Faux : "+str(self.valeur)+"]",indent)


class Conditionnelle:
	def __init__(self,expressions , instructions):
		self.expressions = expressions
		self.instructions = instructions

	def afficher(self,indent=0):
		afficher("<Conditionnelle>",indent)
		afficher("<Si>",indent+1)
		self.expressions[0].afficher(indent+2)
		afficher("</Si>",indent)
		afficher("<Alors>",indent)
		self.instructions[0].afficher(indent+2)
		afficher("</Alors>",indent)
		i = 1
		while i < len(self.expressions):
			afficher("<SinonSi>",indent)
			self.expressions[i].afficher(indent+2)
			afficher("</SinonSi>",indent)
			afficher("<Alors>",indent)
			self.instructions[i].afficher(indent+2)
			afficher("</Alors>",indent)
		if len(self.instructions) > i+1:
			afficher("<Sinon>",indent+1)
			self.listeSinon.afficher(indent+2)
			afficher("</Sinon>",indent+1)
		afficher("</Conditionnelle>",indent)


class TantQue:
	def __init__(self,condition,faire):
		self.condition = condition
		self.faire = faire
	def afficher(self,indent=0):
		afficher("<tantQue>",indent)
		self.condition.afficher(indent+1)
		self.faire.afficher(indent+1)
		afficher("</tantQue>",indent)


class Declaration:
	def __init__(self, type, nom):
		self.type = type
		self.nom = nom
	def afficher(self, indent = 0):
		afficher("<declaration>", indent)
		self.type.afficher(indent + 1)
		self.nom.afficher(indent + 1)
		afficher("</declaration>", indent)
