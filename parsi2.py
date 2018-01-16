from parsimonious.grammar import Grammar
from parsimonious import *
parser = Grammar(r"""
    
    """)		
#	E=E "++" E/"("E")"/id

grammar_expr='''
	E=p 
	p= "++" p / r
	r=id
	id=~"[0-9]*"
	'''		
grammar_recu='''
	Value   = v1 / v2
	v1		= ~"[0-9.]+"
	v2		= "(" Expr ")"
	Product = Expr (("*" / "/") Expr)*
	Sum     = Expr (("+" / "-") Expr)*
	Expr    = Product / Sum / Value
'''	
parser2=Grammar(grammar_recu)
				
code = input("INP: ")


print(parser2.parse(code))