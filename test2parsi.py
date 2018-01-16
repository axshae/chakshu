from parsimonious.grammar import Grammar
from parsimonious import *
parser = Grammar(r"""
    styled_text = bold_text / italic_text
    bold_text   = "((" text "))"
    italic_text = "''" text "''"
    text        = ~"[A-Z 0-9]*"i
    """)		
#	E=E "++" E/"("E")"/id

grammar_expr='''
	E=p 
	p= "++" p / r
	r=id
	id=~"[0-9]*"
	'''			
parser2=Grammar(grammar_expr)
				
code = input("INP: ")


print(parser2.parse(code))