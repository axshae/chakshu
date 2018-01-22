# Could be important: https://stackoverflow.com/questions/5022129/ply-lex-parsing-problem

############################################
#	PLEASE TEST THE HELL OUTTA THIS CODE   #
############################################

# They're might be a difference between tokens and reserved words.

from ply import lex
from ply.lex import TOKEN
import parser as py_parser

code = ""

sym_table={}
tokens = [ # if ERROR: No token list is defined then make sure its written as "tokens". It was "TOKENS" before and it made it not not find it.
	"PRINT", # I'm unsure if we should really keep print that fundamental or just make a console support later as a library support.
	# "IF",
	# "ELSE",
	# "OPERATORS",
	 "ASSIGNMENT",
	# "COMPARISON",
	 "ID",
	"NUMBER",
	"STRING",
	"end"
	# "BOOLEAN"
	]

#########################################################################################
#	MIGHT HAVE TO INCLUDE ^ AT THE BEGINNING OF EVERY REGEX BUT WE'LL LOOK INTO THAT.	#
#########################################################################################

# I like commenting like this lol.

op_literal = ['+', '-', '/', '*']

def t_PRINT(t):
	r'print\s+' # no []
	return t

# def t_OPERATORS(t):
# 	r'[+ - * /]$'
# 	return t

def t_ASSIGNMENT(t):
	r'\s* = \s*'
	return t

def t_ID(t):
	r'[a-z A-Z _][a-z A-Z 0-9 _]*'
	# t.value=(t.value,t.type)
	return t


DIGIT= r'\d'

INT=DIGIT+'+'
SIGNED_INT= r'[\+|-]'+INT
DECIMAL = INT +r'\.'+ INT +r'|\.'+ INT
SIGNED_DECIMAL = r'([\+|-]'+INT +r'\.'+ INT +r')|'+ r'[\+|-]'+'\.'+ INT
# float = /-?\d+(\.\d+)?([eE][+-]?\d+)?/
#_EXP: ("e"|"E") SIGNED_INT
#FLOAT: INT _EXP | DECIMAL _EXP?
#SIGNED_FLOAT: ["+"|"-"] INT

NUMBER= DECIMAL +'|'+ INT + '|'+ SIGNED_INT + '|' + SIGNED_DECIMAL
SIGNED_NUMBER= r'[+|-]'+ NUMBER

@TOKEN(NUMBER)
def t_NUMBER(t): # commented cause error: it matches empty string[SOLVED] now new error: Rule 't_NUMBER' returned an unknown token type 't_NUMBER' [SOLVED]. Solution: add t_ignore.
	# r'[0-9]+[.[0-9]+]* ' # no []. $ is used to specify that the string should end after number. Or else, "1233faw" will be recognised as a NUMBER token.
	# r'\d+[\.\d+]*' still works
	#r'\d+'
	# t.value = int(t.value)
	return t

# Please add escapse seq for special characters in t_String(). (Cause mujhe nahi mila xD)
def t_STRING(t):
	r'\" [\w \s]* \"' # \w = alphanumeric. Dont put \" in ""
	return t

def t_end(t):
	r'\#'
	return t
# def t_BOOLEAN(t):
# 	r'["true" "false"]$'
# 	return t

def t_error(t): # why? cuz i'm a good boi. Comment out this def to use python error reporting which is (duh) better.
	print("Error agya re baba!: ", t.value, " me")
	t.lexer.skip(1) # skip 1 token.

t_ignore = ' \t' # See comment at line 37

lexer = lex.lex()

lex.input("print abc bbc")  #input test str

while True:
	tok = lexer.token()
	if not tok:
		break
	print(tok)


#################################
#	LETS BUILD SOME PARSERS!!	#
#################################

from ply import yacc

# precedence = (
#     ('left', '+', '-'),
#     ('left', '*', '/'),
# )

# symbol_table = {} # We might change to the "in-build symbol table you talked about."



def p_start(p):				# remeber to add new production symbol to the start production
	'''start : print_prod
			| assign
			| end_program'''
	# global code
	# code = py_parser.expr(code)
	# code = code.compile("file.py", )
	# eval(code)

def p_print_prod(p):
	'''print_prod : PRINT printable
		'''
	global code
	prin = str(p[1]) + "(" + str(p[2]) + ")"
	code += prin + "\n"
	# if p[2][1]=='ID': # fetching type @index 1
	# 	print(sym_table.get(p[2][0],'undefined variable '+p[2][0]))	#value @index 0
	# else:
	# 	print(p[2]) # works good but prints var name if not present in symbol table
									# also ID regex accepts var name swith space

def p_assign(p):
	'assign : ID ASSIGNMENT printable'

	ass = str(p[1]) + str(p[2]) + str(p[3])
	# print(ass)
	global code
	code += ass + "\n"
	# sym_table[p[1][0]]=p[3]

# def p_rvalue(p):
# 	'rvalue : printable '
# 	p[0] = p[10]

def p_printable(p):
	'''printable : NUMBER
				| STRING
				| ID
				'''
	p[0] = p[1]

def p_end_program(p):
	'end_program : end'
	global code
	tcode = py_parser.suite(code)
	mcode = tcode.compile("file.py")
	op=exec(mcode)
	print(op)
# def p_rvalue(p):
# 	'RVALUE : NUMBER'
	# p[0] = p[1]
# def p_print_statement(p):
# 	'print_start : PRINT PRINTABLE'
# 	print(p[2].value) # Later we'll have to convert it to a language and not just print in native language.

# def p_PRINTABLE(p):
	# '''PRINTABLE : STRING
# 	 			| NUMBER
# 	 			| ID
# 	 			''' # I had to make another function cause my python reads """ """ or ''' ''' as comments.

# def p_operators_statement(p):
# 	'''expr : expr "+" expr
# 			| expr "-" expr
# 			| expr "/" expr
# 			| expr "*" expr
# 			| ID
# 			| NUMBER
# 			'''

# 	if p[2] == '+':
# 		p[0] = p[1] + p[3]
# 	elif p[2] == '-':
		# p[0] = p[1] - p[3]
# 	elif p[2] == '*':
# 		p[0] = p[1] * p[3]
# 	elif p[3] == '/':
# 		p[0] = p[1] * p[3]

# def p_assignment_statement(p):
# 	r'lvalue : ID ASSIGNMENT expr'
# 	p[1] = p[2]


parser = yacc.yacc()

intro = '\nCHAKSHU V0.1 MIT LICENSE APPLICABLE.\nFounded by Akshay Chauhan and Paramdeep Singh.\n'
print(intro)

while True:
    try:
        inp = input('>>> ')
    except EOFError: # so we can exit.
        break
    if not inp:
        continue
    yacc.parse(inp)
