# Could be important: https://stackoverflow.com/questions/5022129/ply-lex-parsing-problem

############################################
#	PLEASE TEST THE HELL OUTTA THIS CODE   #
############################################

# They're might be a difference between tokens and reserved words.

from ply import lex

tokens = [ # if ERROR: No token list is defined then make sure its written as "tokens". It was "TOKENS" before and it made it not not find it.
	"PRINT", # I'm unsure if we should really keep print that fundamental or just make a console support later as a library support.
	# "IF",
	# "ELSE",
	"OPERATORS",
	"ASSIGNMENT",
	# "COMPARISON",
	"ID",
	"NUMBER",
	"STRING",
	"BOOLEAN"
	]

#########################################################################################
#	MIGHT HAVE TO INCLUDE ^ AT THE BEGINNING OF EVERY REGEX BUT WE'LL LOOK INTO THAT.	#
#########################################################################################

# I like commenting like this lol.

def t_PRINT(t):
	r'print\s+$' # no []
	return t

def t_OPERATORS(t):
	r'[+ - * /]$'
	return t

def t_ASSIGNMENT(t):
	r'"="$'
	return t

def t_ID(t):
	r'[a-z A-Z _][a-z A-Z 0-9 _]*$'
	# t.type = "VARIABLE"
	return t

def t_NUMBER(t): # commented cause error: it matches empty string[SOLVED] now new error: Rule 't_NUMBER' returned an unknown token type 't_NUMBER' [SOLVED]. Solution: add t_ignore.
	r'[0-9]+[.[0-9]+]* $' # no []. $ is used to specify that the string should end after number. Or else, "1233faw" will be recognised as a NUMBER token.
	return t

# Please add escapse seq for special characters in t_String(). (Cause mujhe nahi mila xD)
def t_STRING(t):
	r'^\" [\w \s]* \"$' # \w = alphanumeric. Dont put \" in "" 
	return t

def t_BOOLEAN(t):
	r'["true" "false"]$'
	return t

def t_error(t): # why? cuz i'm a good boi. Comment out this def to use python error reporting which is (duh) better.
	print("Error agya re baba!: ", t.value, " me")
	t.lexer.skip(1) # skip 1 token.

t_ignore = ' \t' # See comment at line 37

lexer = lex.lex()

# Try your inputs. These inputs work:
# lex.input("2")
lex.input("\"Hello World\"")
# lex.input("3.14")
# lex.input("akad bakad bambe bo 69")
# lex.input("true")
# lex.input("+")

while True:
	tok = lexer.token()
	if not tok:
		break
	print(tok)


#################################
#	LETS BUILD SOME PARSERS!!	#
#################################

from ply import yacc

symbol_table = {} # We might change to the "in-build symbol table you talked about."


def p_print_statement(p):
	"print_start: t_PRINT PRINTABLE"
	print(p[2].value) # Later we'll have to convert it to a language and not just print in native language.

def p_PRINTABLE(p):
	"PRINTABLE: t_STRING | t_NUMBER | t_ID" # I had to make another function cause my python reads """ """ or ''' ''' as comments.

def p_operators_statement(p):
	"expr: expr t_OPERATORS expr | t_ID | t_NUMBER"

	if p[2] == '+':
		p[0] = p[1] + p[3]
	elif p[2] == '-':
		p[0] = p[1] - p[3]
	elif p[2] == '*':
		p[0] = p[1] * p[3]
	elif p[3] == '/':
		p[0] = p[1] * p[3]

def p_assignment_statement(p):
	'lvalue : t_ID t_ASSIGNMENT expr'
	p[1] = p[2]


parser = yacc.yacc()

while True:
    try:
        inp = raw_input('>>> ')
    except EOFError: # so we can exit.
        break
    if not s:
        continue
    yacc.parse(s)