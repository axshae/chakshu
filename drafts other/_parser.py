from ply import *
import _tokens
import util
import copy
tokens=_tokens.tokens
_CODE=[]
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'POWER'),
    ('right', 'UMINUS'),
)
parse_tree = []

def p_program(p):
    '''program : statement
            '''
    p[0]=p[1]
    #parse_tree.append(p[0])
    #print("p_program reached.") # unreachable.
def p_program_error(p):
    r'program : error'
    print(p[0])
    p[0]=p[1]

def p_statement_id(p):
    r'''statement : variable eq expr
                 | variable eq relexpr
                   '''
    p[0]=(('ID',p[1]),p[3],('OPR',p[2]))
    p[0]=('ID',p[1],p[3])
    # print("p_statement_id reached.")

def p_statement_id_bad(p):
    r'''statement : variable eq
                    | variable error expr
                    | variable error relexpr
                    '''
    p[0]='INVALID SYNTAX FOR DEFINFING A VARIABLE'


# Arithmetic expressions

def p_expr_binary(p):
    '''expr : expr PLUS expr
            | expr MINUS expr
            | expr TIMES expr
            | expr DIVIDE expr
            | expr POWER expr'''

    p[0] = ('BINOP', p[2], p[1], p[3])
    p[0]=p[1]+p[2]+p[3]

# a + 2
#('ID','name',($data),('OPR','='))
# ('ID',('a',()))
#((ID, a), +, 2)
def p_expr_number(p):
    '''expr : INTEGER
            | FLOAT
            '''
    p[0] = ('NUM', p[1])
    p[0]=p[1]

def p_expr_string(p):
    'expr : STRING'
    p[0]=('STR',p[1])
    if p[1].startswith('\''):
         p[0]=p[1].replace("\'",'\"')
    else :
        p[0]=p[1]

def p_expr_variable(p):
    '''expr : variable'''
    p[0] = ('VAR', p[1])
    p[0]=p[1]

def p_expr_group(p):
    '''expr : LPAREN expr RPAREN'''
    p[0] = ('GROUP', p[2])
    p[0]=p[1]+p[2]+p[3]

def p_expr_unary(p):
    '''expr : MINUS expr %prec UMINUS'''
    p[0] = ('UNARY', '-', p[2])
    p[0]='-'+p[2]
# Relational expressions


def p_relexpr(p):
    '''relexpr : expr lt expr
               | expr le expr
               | expr gt expr
               | expr ge expr
               | expr eq expr
               | expr ne expr'''
    #   expr EQUALS expr  : use == by defining a seperate token
    relexpr={'lt':'<','gt':'>','ge':'>=','eq':'=','ne':'!=','le':'<='}
    if p[2] in relexpr:
        p[2]=relexpr[p[2]]
    p[0] = ('RELOP', p[2], p[1], p[3])
    p[0]=p[1]+p[2]+p[3]

def p_relexpr_group(p):
    '''relexpr : LPAREN relexpr RPAREN'''
    p[0] = ('GROUP', p[2])
    p[0]=p[1]+[2]+p[3]
# Variables
def p_variable(p):
    '''variable : ID'''
    p[0]=p[1]


def p_error(p):
    if not p:
        print("SYNTAX ERROR ")

# Tokens
def p_statement_print(p):
    '''statement : print expr
                     '''
    p[0] = ('PRINT', p[2])

def p_statement_if(p):
    '''statement : if expr then
            | if relexpr then'''
    p[0]=('IF',p[2])

def p_statement_else(p):
    '''statement : else  then
            '''
    p[0]=('ELSE','')

def p_statement_elif(p):
    '''statement : else if expr then
            | else if relexpr then'''
    p[0]=('ELIF',p[3])

def p_statement_repeat(p):
    '''statement : repeat until relexpr then
                | repeat until expr then
            '''
    p[0] = ('REPEAT', p[3])

def p_statement_function(p):
    '''
    statement : function variable LPAREN args RPAREN then
        '''
    print(p)
    p[0] = ('FUNCTION', p[2],(p[4]))

def p_statement_function_call(p):
    '''
    statement : ID LPAREN call_args RPAREN
    '''
    p[0] = ('FUNCTION-CALL', p[1],(p[3]))

def p_call_args(p):
    '''
    call_args : expr COMMA call_args
             |  expr
    '''
    if len(p)>2:    #this fucking was causing error
        p[0] = p[1] #still have error coz expr is a tuple and didnt have append method
        p[0].append(p[3])
    else :
        p[0]=list(p[1])

def p_args(p):
    '''
    args : args COMMA variable
        | variable
    '''
    if len(p)>2:    #this fucking was causing error
        p[0] = p[1]
        p[0].append(p[3])
    else:
        p[0] =[p[1]]

def p_statement_end(p):
    'statement : end'
    p[0]=('END','')
# #####                 #######
#       Parser functions      #
# ####                  #######
# hello...?


def yield_next_line():
    global  _CODE
    _CODE=_CODE.split('\n')
    for code in _CODE:
        yield code


# def run_parser_from_file(_file,exec_by_line=False):
#     intro = '\nCHAKSHU V0.1 MIT LICENSE APPLICABLE.\nFounded by Akshay Chauhan and Paramdeep Singh.\n'
#     print(intro)
#     global _CODE_FILE
#     _CODE_FILE=_file
#     #_CODE_FILE= copy.copy(_file)
#     if not _CODE_FILE:
#         print('Error Parse : Unable to open file')
#         pass
#     while True:
#         code=''
#         try:
#             code=fetch_next_line()
#             print(code)
#             if code.strip()=='':
#                 continue
#             if not code:
#                 break
#             out=parser.parse(code)
#             print(out)
#         except EOFError:
#             break



def run_parser(code='',enable_input_mode=False):

    global _CODE
    _CODE=code
    code_next=yield_next_line()
    output_list=[]
    while True:
        if enable_input_mode:
            try:
                if enable_input_mode:
                    code = input('>>> ')
                    out=parser.parse(code)
                    print(out)
            except : # so we can exit.
                break
        else :
            try:
                code=next(code_next)   #last element will always be '' so ignore it
                if not code :
                    continue

                out=parser.parse(code)
                output_list.append(out)
                #print(out)
            except StopIteration:
                # for i in output_list:
                #     print(i)
                #     print('\n')
                #print('\n\nEOP CALL : Program execution completed')
                return output_list
        #print("Parse tree now: ")
        #print(parse_tree)

parser = yacc.yacc()
