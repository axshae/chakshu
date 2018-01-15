from lark import Lark as l
#l = l('''start: WORD "," WORD "!" WORD
#            %import common.WORD
#            %ignore " "
#         ''')
#inp=input('INP:')

grammer = '''
			start: NUMBER "+" NUMBER | NUMBER "-" NUMBER 
			
			%import common.NUMBER
			'''
			
grammer2 = '''
			start: NUMBER "+" NUMBER | NUMBER  "-" NUMBER  | WORD
			WORD: " "*
			
			%import common.NUMBER
			'''
		
'''
SPACE: " "*
				STRING: [STRING]| WORD
'''
grammer_print = '''
				start: "print " STRING
				STRING: /[A-Z a-z 0-9 //w]*/
				%import common.WORD
				SPACE: " "*
				'''		
			
parser = l(grammer_print)

inp = input("INP: ")
tree=parser.parse(inp)
print( tree )

from lark.tree import pydot__tree_to_png    # Just a neat utility function
pydot__tree_to_png(tree, "examples/fruitflies.png")