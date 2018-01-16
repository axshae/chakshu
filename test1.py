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
			start: "print" /\\s+/ STRING
			STRING: QUOTES /[\\w \\s \\W ]*/ QUOTES
			QUOTES: "\'"
			%import common.WORD
			SPACE: /\\s+/
						EXP: NUMBER "+" NUMBER | NUMBER  "-" NUMBER  |NUMBER "*" NUMBER|NUMBER "/" NUMBER |NUMBER "%" NUMBER| NUMBER

'''	
grammer_var='''
			start: VNAME /[\\s]*/ LIT_EQ /[\\s]*/ STMT /[\\s]*/
			VNAME: /^[A-Z a-z _][\\w _]*/
			LIT_EQ:"="
			STMT: NUM|STR
			NUM:/\\d*/
			STR:QUOTES /[\\w \\s \\W ]*/ QUOTES
			QUOTES: "\'"
			
			
'''

grammer_v1='''
			start: VNAME LIT_EQ STMT
			VNAME: /[A-Z a-z _ ^\\s][\\w _]*/
			LIT_EQ:"="
			STMT: NUMBER|STR
			STR: ESCAPED_STRING
			%import common.ESCAPED_STRING
			%import common.NUMBER
			%import common.WS
			%ignore WS
			
			
'''


	#	*\\w for all words    	*\\W non word special symbols  *\\s for space tabs  *\\d for digits	
# removed space production so it doesnt count as token	
#parser = l(grammar_print)
parser=l(grammer_v1)
inp = input("INP: ")
tree=parser.parse(inp)
print( tree )

from lark.tree import pydot__tree_to_png    # Just a neat utility function
#pydot__tree_to_png(tree, "examples/fruitflies.png")
