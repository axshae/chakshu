

_py_carbon={

    'ID':'$name=$rvalue',
    'IF':'if $rvalue :',
    'ELSE':'else $rvalue:',
    'ELIF':'elif $rvalue :',
    'PRINT':'print($rvalue)'
}
# 'abc'*'bbcbc'
def get_spaces(scope):
    _=0
    _space=''
    while _ < scope:
        _space+='\t'
        _+=1
    return _space

def generate_code(obj,scope):
    t=obj[0]
    gen_code=''
    _scope_spaces=get_spaces(scope)
    if t=='ID':
        gen_code=_py_carbon[t].replace('$name',obj[1])
        gen_code=gen_code.replace('$rvalue',obj[2])

    elif t in ['IF','ELIF','ELSE','PRINT']:
        gen_code=_py_carbon[t].replace('$rvalue',obj[1])
    return _scope_spaces+gen_code+'\n'

def make_code(oobj):
    _scope=0
    _py_code=''
    for obj in oobj:
        _py_code+=generate_code(obj,_scope)
        if obj[0] in ['IF','ELIF','ELSE']:  #QUESTION: obj[0] is type
            _scope+=1
        elif obj[0]=='END':
            _scope-=1
            if _scope<0:
                _scope=0
    return _py_code
