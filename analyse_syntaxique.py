import sys
from sly import Parser
from analyse_lexicale import FloLexer
import arbre_abstrait

class FloParser(Parser):
	# On récupère la liste des lexèmes de l'analyse lexicale
	tokens = FloLexer.tokens

	precedence = (  
		('left', 'ET'),
		('left','OU'),
		('right', 'NON'),
		('right', 'EGAL'),
		('left', '<', '>', 'INFERIEUR_OU_EGAL', 'SUPERIEUR_OU_EGAL', 'DIFFERENT'),
		('left', '+', '-'),
		('left', '*', '/', '%'),
)

	# Règles gramaticales et actions associées

	@_('listeFonctions listeInstructions')
	def prog(self, p):
		return arbre_abstrait.Programme(p[0], p[1])
	
	@_('fonction')
	def listeFonctions(self, p):
		l = arbre_abstrait.ListeFonctions()
		l.fonctions.append(p[0])
		return l

	@_('fonction listeFonctions')
	def listeFonctions(self, p):
		p[1].fonctions.insert(0, p[0])
		return p[1]

	@_('instruction')
	def listeInstructions(self, p):
		l = arbre_abstrait.ListeInstructions()
		l.instructions.append(p[0])
		return l
					
	@_('instruction listeInstructions')
	def listeInstructions(self, p):
		p[1].instructions.insert(0,p[0])
		return p[1]

	@_('ecrire')
	def instruction(self, p):
		return p[0]
	
			
	@_('ECRIRE "(" expr ")" ";"')
	def ecrire(self, p):
		return arbre_abstrait.Ecrire(p.expr) #p.expr = p[2]
		
	##@_('expr "+" expr')
	##def expr(self, p):
	##	return arbre_abstrait.Operation('+',p[0],p[2])

	##@_('expr "*" expr')
	##def expr(self, p):
	##	return arbre_abstrait.Operation('*',p[0],p[2])


	@_('"(" expr ")"')
	def fact(self, p):
		return p[1]
		
	@_('ENTIER')
	def fact(self, p):
		return arbre_abstrait.Entier(p.ENTIER) #p.ENTIER = p[0]
	
	@_('fact')
	def produit(self,p):
		return p.fact
	
	@_('expr "+" produit')
	def expr(self,p):
		return arbre_abstrait.Operation('+',p[0],p[2])
	
	@_('produit')
	def expr(self,p):
		return p[0]
	
	@_('expr "-" produit')
	def expr(self,p):
		return arbre_abstrait.Operation('-',p[0],p[2])

	@_('"-" fact')
	def produit(self,p):
		return arbre_abstrait.Operation('*',arbre_abstrait.Entier(-1),p[1])

	@_('produit "*" fact')
	def produit(self,p):
		return arbre_abstrait.Operation('*',p[0],p[2])

	@_('produit "/" fact')
	def produit(self,p):
		return arbre_abstrait.Operation('/',p[0],p[2])

	@_('produit "%" fact')
	def produit(self,p):
		return arbre_abstrait.Operation('%',p[0],p[2])
	
	@_('expr "<" expr')
	def expr(self,p):
		return arbre_abstrait.Comparaison('<',p[0],p[2])
	
	@_('expr ">" expr')
	def expr(self,p):
		return arbre_abstrait.Comparaison('>',p[0],p[2])
	
	@_('expr EGAL expr')
	def expr(self,p):
		return arbre_abstrait.Comparaison('=',p[0],p[2])
	
	@_('expr INFERIEUR_OU_EGAL expr')
	def expr(self,p):
		return arbre_abstrait.Comparaison('<=',p[0],p[2])
	
	@_('expr SUPERIEUR_OU_EGAL expr')
	def expr(self,p):
		return arbre_abstrait.Comparaison('>=',p[0],p[2])
	
	@_('expr DIFFERENT expr')
	def expr(self,p):
		return arbre_abstrait.Comparaison('!=',p[0],p[2])
	
	
	
	@_('LIRE "(" ")"')
	def expr(self,p):
		return arbre_abstrait.Lire()
	
	@_('IDENTIFIANT')
	def variable(self,p):
		return arbre_abstrait.Variable(p[0])
	
	@_('variable')
	def fact(self, p):
		return p[0]

	@_('expr "," expr',
    'superExpression "," expr')
	def superExpression(self, p):
		return arbre_abstrait.SuperExpression(p[0], p[2])
	
	@_('TYPE_ENTIER expr',
    'TYPE_BOOLEEN expr')
	def parametre(self, p):
		return arbre_abstrait.Parametre(p[0], p[1])
	
	@_('parametre')
	def listeParametres(self, p):
		l = arbre_abstrait.ListeParametres()
		l.parametres.append(p[0])
		return l

	@_('parametre listeParametres')
	def listeParametres(self, p):
		p[1].parametres.insert(0, p[0])
		return p[1]
	
	@_('TYPE_ENTIER IDENTIFIANT "(" listeParametres ")" "{" listeInstructions "}"',
    'TYPE_BOOLEEN IDENTIFIANT "(" listeParametres ")" "{" listeInstructions "}"')
	def fonction(self, p):
		return arbre_abstrait.DeclarationFonction(p[0], p[1], p[3], p[6])

	@_('TYPE_ENTIER IDENTIFIANT "(" ")" "{" listeInstructions "}"',
    'TYPE_BOOLEEN IDENTIFIANT "(" ")" "{" listeInstructions "}"')
	def fonction(self, p):
		return arbre_abstrait.DeclarationFonction(p[0], p[1], arbre_abstrait.ListeParametres(), p[6])

	@_('IDENTIFIANT "(" expr ")"',
    'IDENTIFIANT "(" superExpression ")" ')
	def fact(self,p):
		return arbre_abstrait.Fonction(p[0],p[2])

	@_('VRAI')
	def booleen(self,p):
		return arbre_abstrait.Booleen(True)

	@_('FAUX')
	def booleen(self,p):
		return arbre_abstrait.Booleen(False)
    
	@_("booleen")
	def expr(self,p):
		return p[0]
		
	@_("expr ET expr")
	def expr(self,p):
		return arbre_abstrait.LogOp("et",p[0],p[2])	
	
	@_("expr OU booleen")
	def expr(self,p):
		return arbre_abstrait.LogOp("ou",p[0],p[2])
	
	@_("NON booleen")
	def expr(self,p):
		return arbre_abstrait.NegLogOp(p[1])
	
	
	@_('SI "(" expr ")" "{" listeInstructions "}" condSuite')
	def instruction(self, p):
		conditions = [p[2]]
		instructions = [p[5]]

		a,b = p[7]
		conditions.extend(a)
		instructions.extend(b)
		return arbre_abstrait.Conditionnelle(conditions,instructions)
	
	
	@_('SINON_SI "(" expr ")" "{" listeInstructions "}" condSuite')
	def condSuite(self, p):
		a,b = p[7]
		return ([p[2]] + a, [p[5]] + b)
	

	@_('SINON "{" listeInstructions "}" ')
	def condSuite(self, p):
		return ([None], [p[2]])

	@_('')
	def condSuite(self, p):
		return ([], [])
	

	@_('TANT_QUE "(" expr ")" "{" listeInstructions "}"')
	def instruction(self,p):
		return arbre_abstrait.TantQue(p[2], p[5])
	
	@_('RETOURNER expr ";"')
	def instruction(self, p):
		return arbre_abstrait.Retourner(p[1])
	
	@_('TYPE_ENTIER IDENTIFIANT ";"',
    'TYPE_BOOLEEN IDENTIFIANT ";"')
	def instruction(self, p):
		return arbre_abstrait.Declaration(p[0], p[1])
	
	@_('IDENTIFIANT "=" expr ";"')
	def instruction(self, p):
		return arbre_abstrait.Affectation(p[0], p[2])
	
	@_('TYPE_ENTIER IDENTIFIANT "=" expr ";"',
    'TYPE_BOOLEEN IDENTIFIANT "=" expr ";"')
	def instruction(self, p):
		return arbre_abstrait.DeclarationAffectation(p[0], p[1], p[3])
	
	

	

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