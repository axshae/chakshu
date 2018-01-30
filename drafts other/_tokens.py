from ply import lex
from ply.lex import TOKEN
keywords=(
        'if', 'else', 'break', 'function', 'then', 'in', 'repeat',
        'print', 'input', 'include', 'compile', 'until', 'to',
        'start', 'end', 'lt', 'le', 'gt', 'ge', 'ne','eq','and','or'
)
tokens = keywords + (
     'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'POWER',
      'COMMA', 'SEMI', 'INTEGER', 'FLOAT', 'STRING',
    'ID', 'NEWLINE','LPAREN','RPAREN'
)
t_ignore=' \t \n'
def t_ID(t):
    r'[A-Z a-z _][A-Z0-9a-z_]*'
    if t.value in keywords:
        t.type =t.value
    return t

t_eq = r'=|(?i)EQ'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_POWER = r'\^'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_lt = r'<|(?i)LT'
t_le = r'<=|(?i)LE'
t_gt = r'>|(?i)GT'
t_ge = r'>=|(?i)GE'
t_ne = r'\!\=|(?i)NE'
t_COMMA = r'\,'
t_SEMI = r';'
t_INTEGER = r'\d+'
t_FLOAT = r'((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))'
t_STRING = r'(\".*?\")|(\'.*?\')'


def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += 1
    return t


def t_error(t):
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)

lexer=lex.lex()
'''
inp=''
while True:
    _inp_=input('>>')
    inp=inp+_inp_+'\n'
    lex.input(inp)
    if _inp_=='end':
        break
while True:
	tok = lexer.token()
	if not tok:
		break
	print(tok)
'''
