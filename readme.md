## Chakshu

### What is Chakshu?

Chakshu, a small transpiler with high-level syntax made using Ply, is a testament to the power of combining simplicity with efficiency in language processing. Ply, short for Python Lex-Yacc, serves as the backbone for Chakshu, providing a robust parsing framework for the transpiler. The high-level syntax of Chakshu not only makes it accessible for developers but also facilitates the creation of concise and readable code. Leveraging the flexibility of Ply, Chakshu seamlessly translates the source code written in its user-friendly syntax into the desired target language. This project showcases the possibilities that arise when building specialized language processors, offering a valuable tool for developers seeking a straightforward yet powerful transpiler solution.

### Why did i made this?

I started Chakshu as my major for my degree. The project reflects my deep dive into language design and code generation, emphasizing simplicity without sacrificing functionality. Choosing a high-level syntax aims to make it accessible for developers. Completing Chakshu not only fulfilled academic requirements but also showcased my proficiency in language tools and compiler design, marking a milestone in my journey as a software developer.

### Instructions

```
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
**RULES TO REMEMBER**
1. production function must begin with p_
2. token function must begin with t_
3. in production there must be space before and after colon (:)
4. multi line productions using (|) must be written inside three quotes(''' ''')
5. check your regex carefully before compiling like avoid using ^ or $
```
