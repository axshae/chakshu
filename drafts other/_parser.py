from ply import *
import _tokens
tokens=_tokens.tokens

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'POWER'),
    ('right', 'UMINUS')
)

def p_program(p):
    r'''program : statement'''
    p[0]=p[1]
def p_program_error(p):
    r'program : error'
    p[0]=p[1]

def p_statement_id(p):
    r'''statement : variable eq expr
                   '''
    p[0]=('ID',p[1],p[3])

def p_statement_id_bad(p):
    r'''statement : variable eq
                    | variable error expr'''
    p[0]='INVALID SYNATX FOR DEFINFING A VARIABLE'

# Arithmetic expressions

def p_expr_binary(p):
    '''expr : expr PLUS expr
            | expr MINUS expr
            | expr TIMES expr
            | expr DIVIDE expr
            | expr POWER expr'''

    p[0] = ('BINOP', p[2], p[1], p[3])


def p_expr_number(p):
    '''expr : INTEGER
            | FLOAT'''
    p[0] = ('NUM', p[1])


def p_expr_variable(p):
    '''expr : variable'''
    p[0] = ('VAR', p[1])


def p_expr_group(p):
    '''expr : LPAREN expr RPAREN'''
    p[0] = ('GROUP', p[2])


def p_expr_unary(p):
    '''expr : MINUS expr %prec UMINUS'''
    p[0] = ('UNARY', '-', p[2])

# Relational expressions


def p_relexpr(p):
    '''relexpr : expr lt expr
               | expr le expr
               | expr gt expr
               | expr ge expr
               | expr eq expr
               | expr ne expr'''
    #   expr EQUALS expr  : use == by defining a seperate token
    p[0] = ('RELOP', p[2], p[1], p[3])

# Variables
def p_variable(p):
    '''variable : ID'''
    p[0]=p[1]


def p_error(p):
    if not p:
        print("SYNTAX ERROR ")


def run_parser():
    intro = '\nCHAKSHU V0.1 MIT LICENSE APPLICABLE.\nFounded by Akshay Chauhan and Paramdeep Singh.\n'
    print(intro)

    while True:
        try:
            inp = input('>>> ')
        except EOFError: # so we can exit.
            break
        if not inp:
            continue
        out=parser.parse(inp)
        print(out)

parser = yacc.yacc(debug=0)
