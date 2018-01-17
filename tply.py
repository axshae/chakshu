import ply.lex as lex
tokens=(
    "print",
    "number",
    "string"
)
t_print=r'print[\s]+'
t_number=r'\d+'
t_string=r'.+'
lexer=lex.lex()
inp=input('INP: ')
lexer.input(inp)
print(lexer.token())
