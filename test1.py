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
			STRING: QUOTES /[\\w \\s \\W \\d]*/ QUOTES	
			QUOTES: "\'"
			%import common.WORD
			SPACE: " "+
			%ignore SPACE
'''	
	#	*\\w for all words    	*\\W non word special symbols  *\\s for space tabs  *\\d for digits		
parser = l(grammar_print)

inp = input("INP: ")
tree=parser.parse(inp)
print( tree )

from lark.tree import pydot__tree_to_png    # Just a neat utility function
#pydot__tree_to_png(tree, "examples/fruitflies.png")
