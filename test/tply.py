import ply.lex as lex
tokens=(
    "print",
    "number",
    "string"
)


t_print=r'print[\s]+'
t_number=r'\d+'
t_string=r'[A-Z a-z \s]+'


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer=lex.lex()
inp=input('INP: ')
lexer.input(inp)
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok.type, tok.value, tok.lineno, tok.lexpos)
