import sys
import __trans_py__ as PYTHON_TRANSLATOR
def make_code_file(file_name,extension,content):
    code_file=open(file_name+'.'+extension,'w+')
    code_file.write(content)
def get_translated_code(code_object,language='py'):
    if language=='py':
        return PYTHON_TRANSLATOR.make_code(code_object)
