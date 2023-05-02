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
		afficher(self.op,indent+1)
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
	def __init__(self,expressions: list, instructions: list):
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
		for i in range(1,len(self.expressions)):
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
