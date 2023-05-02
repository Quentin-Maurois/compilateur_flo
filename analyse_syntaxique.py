import sys
from sly import Parser
from analyse_lexicale import FloLexer
import arbre_abstrait

class FloParser(Parser):
	debugfile = 'parser.out'
	# On récupère la liste des lexèmes de l'analyse lexicale
	tokens = FloLexer.tokens
	# Règles gramaticales et actions associées

	precedence = (
		('left', 'ET', 'OU'),
		('right', 'NON'),
		('left', 'INFERIEUR_OU_EGAL', 'SUPERIEUR_OU_EGAL', 'EGAL', 'DIFFERENT', 'INFERIEUR', 'SUPERIEUR'),
		('left', '+', '-'),
		('left', '*', '/', '%'),
		('left', '(', ')'),
	)

	@_('listeInstructions')
	def prog(self, p):
		return arbre_abstrait.Programme(p[0])

	@_('instruction')
	def listeInstructions(self, p):
		l = arbre_abstrait.ListeInstructions()
		l.instructions.append(p[0])
		return l
					
	@_('instruction listeInstructions')
	def listeInstructions(self, p):
		p[1].instructions.append(p[0])
		return p[1]
		
	@_('ecrire')
	def instruction(self, p):
		return p[0]

	@_('IDENTIFIANT "=" LIRE "(" ")" ";"')
	def instruction(self, p):
		return arbre_abstrait.Lire(p[0])
	
	@_('ECRIRE "(" expr ")" ";"')
	def ecrire(self, p):
		return arbre_abstrait.Ecrire(p.expr)
		
	@_('expr "+" expr')
	def expr(self, p):
		return arbre_abstrait.Operation('+',p[0],p[2])

	@_('expr "-" expr')
	def expr(self, p):
		return arbre_abstrait.Operation('-',p[0],p[2])

	@_('expr "*" expr')
	def expr(self, p):
		return arbre_abstrait.Operation('*',p[0],p[2])

	@_('expr "/" expr')
	def expr(self, p):
		return arbre_abstrait.Operation('/',p[0],p[2])

	@_('expr "%" expr')
	def expr(self, p):
		return arbre_abstrait.Operation('%',p[0],p[2])

	@_('"(" expr ")"')
	def expr(self, p):
		return p.expr #ou p[1]
		
	@_('ENTIER')
	def expr(self, p):
		return arbre_abstrait.Entier(p.ENTIER) #p.ENTIER = p[0]
	
	@_('expr INFERIEUR expr')
	def expr(self, p):
		return arbre_abstrait.Operation('<',p[0],p[2])
	
	@_('expr SUPERIEUR expr')
	def expr(self, p):
		return arbre_abstrait.Operation('>',p[0],p[2])
	
	@_('expr INFERIEUR_OU_EGAL expr')
	def expr(self, p):
		return arbre_abstrait.Operation('<=',p[0],p[2])
	
	@_('expr SUPERIEUR_OU_EGAL expr')
	def expr(self, p):
		return arbre_abstrait.Operation('>=',p[0],p[2])
	
	@_('expr EGAL expr')
	def expr(self, p):
		return arbre_abstrait.Operation('==',p[0],p[2])
	
	@_('expr DIFFERENT expr')
	def expr(self, p):
		return arbre_abstrait.Operation('!=',p[0],p[2])
	
	@_('expr ET expr')
	def expr(self, p):
		return arbre_abstrait.Operation('&&',p[0],p[2])
	
	@_('expr OU expr')
	def expr(self, p):
		return arbre_abstrait.Operation('||',p[0],p[2])
	
	@_('NON expr')
	def expr(self, p):
		return arbre_abstrait.Operation('!',p[1])
	
	@_('VRAI')
	def expr(self, p):
		return arbre_abstrait.Vrai()
	
	@_('FAUX')
	def expr(self, p):
		return arbre_abstrait.Faux()
	
	@_('SI "(" expr ")" "{" listeInstructions "}"',
       'SI "(" expr ")" "{" listeInstructions "}" listeSinonSi',
       'SI "(" expr ")" "{" listeInstructions "}" SINON "{" listeInstructions "}"',
       'SI "(" expr ")" "{" listeInstructions "}" listeSinonSi SINON "{" listeInstructions "}"'
       )
	def conditionnelle(self, p):
		print("conditionnelle", p)
		conditions = [p[2]]
		instructions = [p[5]]
		for i in range(6,len(p),2):
			conditions.append(p[i])
			instructions.append(p[i+3])
		if len(p) == 11 or len(p) == 12:
			instructions.append(p[len(p)-2])
		return arbre_abstrait.Conditionnelle(conditions,instructions)
	
	@_('SINON_SI "(" expr ")" "{" listeInstructions "}"',
	   'SINON_SI "(" expr ")" "{" listeInstructions "}" listeSinonSi'
	   )
	def listeSinonSi(self, p):
		if len(p) == 8:
			return self.conditionnelle(p[2],p[5])
		elif len(p) == 9:
			return self.conditionnelle(p[2],[p[5], p[7]])
		
	"""@_('TANTQUE "(" expr ")" { listeInstructions }')
	def instruction(self, p):
		return arbre_abstrait.TantQue(p.expr,p.listeInstructions)"""


if __name__ == '__main__':
	lexer = FloLexer()
	parser = FloParser()
	if len(sys.argv) < 2:
		print("usage: python3 analyse_syntaxique.py NOM_FICHIER_SOURCE.flo")
	else:
		with open(sys.argv[1],"r") as f:
			data = f.read()
			try:
				arbre = parser.parse(lexer.tokenize(data))
				arbre.afficher()
			except EOFError:
				exit()
