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


class Comparaison:
	def __init__(self,op,exp1,exp2):
		self.exp1 = exp1
		self.op = op
		self.exp2 = exp2

	def afficher(self,indent=0):
		afficher("<Comparaison>",indent)
		afficher("[Comparateur:" + self.op + "]",indent+1)
		self.exp1.afficher(indent+1)
		self.exp2.afficher(indent+1)
		afficher("</Comparaison>",indent)


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
	def __init__(self, expression, instructions):
		self.expression = expression
		self.instructions = instructions
		print("patate1================================================================================================================")
	def afficher(self, indent = 0):
		print("patate=================================================================================================================")
		afficher("<tantQue>", indent)
		afficher("<expression>", indent + 1)
		self.expression.afficher(indent + 2)
		# afficher(self.expression, indent + 2)
		afficher("</expression>", indent + 1)
		afficher("<instructions>", indent + 1)
		self.instructions.afficher(indent + 2)
		# afficher(self.instructions, indent + 2)
		afficher("<instructions>", indent + 1)
		afficher("</tantQue>", indent)


class Declaration:
	def __init__(self, type, nom):
		self.type = type
		self.nom = nom
	def afficher(self, indent = 0):
		afficher("<declaration>", indent)
		afficher("[type = " + self.type + "]", indent + 1)
		afficher("[nom = " + self.nom + "]", indent + 1)
		afficher("</declaration>", indent)


class Affectation:
	def __init__(self, nom, expression):
		self.nom = nom
		self.expression = expression
	def afficher(self, indent = 0):
		afficher("<affectation>",indent)
		afficher("[nom = \"" + self.nom + "\"]", indent + 1)
		self.expression.afficher(indent + 1)
		afficher("</affectation>",indent)


class DeclarationAffectation:
	def __init__(self, type, nom, expression):
		self.type = type
		self.nom = nom
		self.expression = expression
	def afficher(self, indent = 0):
		afficher ("<declaration>", indent)
		afficher("[type = " + self.type + "]", indent + 1)
		afficher("[nom = " + self.nom + "]", indent + 1)
		afficher("<affectation>",indent + 1)
		afficher("[nom = \"" + self.nom + "\"]", indent + 2)
		self.expression.afficher(indent + 2)
		afficher("</affectation>",indent + 1)
		afficher ("<declaration>", indent)