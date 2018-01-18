1. try ply_example file to know the how yacc actually works
2. A production is defined by using p char before the name of the function which parses and perform the logic defined by us

  Example:
  def p_expression_binop(p):
      '''expression : expression '+' expression
                    | expression '-' expression
                    | expression '*' expression
                    | expression '/' expression'''
      if p[2] == '+':
          p[0] = p[1] + p[3]
      elif p[2] == '-':
          p[0] = p[1] - p[3]
      elif p[2] == '*':
          p[0] = p[1] * p[3]
      elif p[2] == '/':
          p[0] = p[1] / p[3]

.............................................................................................................

i. here p_expression_binop is a production and p is an array
    expression : expression '+' expression
        ^             ^       ^       ^
      p[0]          p[1]    p[2]    p[3]

ii.   p[0] = p[1] + p[3]              --------------------------------------(%11)
      performing the logic on the values returned by Parsing the input using the grammer otherwise error production
      will be fired by the parser.
...............................................................................................................
** Solution To remove recursion is to provide proper operator precedence set
precedence = (
    ('left', '+', '-'),
    ('left', '*', '/'),
    ('right', 'UMINUS'),
)

** here +,- has lowest precedence of level1 and UNIMINUS having level2

...............................................................................................................

** how should we use this for our language?

1. We will parse our grammar using the same yacc and will perform the translation of the code at the logic part of the production
  as explained in (%11) and storing the translations as per our requirement

2.  https://github.com/dabeaz/ply/tree/master/example
  *read these example so that we could learn how to actually code our language

  ...............................................................................................................
