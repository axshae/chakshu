
import trans_util as UTIL
_py_carbon={

    'ID':'$name=$rvalue',
    'IF':'if $rvalue :',
    'ELSE':'else $rvalue:',
    'ELIF':'elif $rvalue :',
    'PRINT':'print($rvalue)',
    'FUNCTION':'def $name($params):',
    'FUNCTION-CALL':'$name($params)',
    'REPEAT': 'while $rvalue :'
}
# 'abc'*'bbcbc'
def get_spaces(scope):
    _=0
    _space=''
    while _ < scope:
        _space+='\t'
        _+=1
    return _space

def join_params_list(ls):
    params_list=' '
    for p in ls:
        params_list=params_list+p+','
    return params_list[:-1]

def generate_code(obj,scope):
    t=obj[0]
    gen_code=''
    _scope_spaces=get_spaces(scope)
    if t=='ID':
        gen_code=_py_carbon[t].replace('$name',obj[1])
        gen_code=gen_code.replace('$rvalue',obj[2])
    elif t in ['FUNCTION','FUNCTION-CALL']:
        gen_code=_py_carbon[t].replace('$name',obj[1])
        params=obj[2]
        if type(params) != type([]):
            params=join_params_list(params)
        gen_code=gen_code.replace('$params',params)

    elif t in ['IF','ELIF','ELSE','PRINT','REPEAT']:
        gen_code=_py_carbon[t].replace('$rvalue',obj[1])
    return _scope_spaces+gen_code+'\n'

def make_code(oobj):
    _scope=0
    _py_code=''
    for obj in oobj:
        _py_code+=generate_code(obj,_scope)
        if obj[0] in ['IF','ELIF','ELSE','REPEAT','FUNCTION']:  #QUESTION: obj[0] is type
            _scope+=1
        elif obj[0]=='END':
            _scope-=1
            if _scope<0:
                _scope=0
    return _py_code
