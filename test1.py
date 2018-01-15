from lark import Lark as l
#l = l('''start: WORD "," WORD "!" WORD
#            %import common.WORD
#            %ignore " "
#         ''')
#inp=input('INP:')

grammar = '''
			start: NUMBER "+" NUMBER | NUMBER "-" NUMBER 
			
			%import common.NUMBER
			'''
			
grammar2 = '''
			start: NUMBER "+" NUMBER | NUMBER  "-" NUMBER  | WORD
			WORD: " "*
			
			%import common.NUMBER
			'''
		
'''
SPACE: " "*
				STRING: [STRING]| WORD
'''
grammar_print = '''
			start: "print" SPACE STRING
			STRING: QUOTES /[A-Z a-z 0-9 //w]*/ QUOTES
			QUOTES: "\'"
			%import common.WORD
			SPACE: " "+
'''	
			
parser = l(grammar_print)

inp = input("INP: ")
tree=parser.parse(inp)
print( tree )

from lark.tree import pydot__tree_to_png    # Just a neat utility function
pydot__tree_to_png(tree, "examples/fruitflies.png")
