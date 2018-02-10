import argparse
import _parser as chakshu_parser
import util
import trans_util
import os
'''
# QUESTION arparse help: https://docs.python.org/3/library/argparse.html#nargs
'''
_help_text={
'-intro':'\nCHAKSHU V0.1 MIT LICENSE APPLICABLE . Authored by Akshay Chauhan and Paramdeep Singh.\n',
'-f':'chakshu program path',
'-e':'execute and output result of the input program (always use as last arg)',
'-c':'output translated program (always use as last arg)'
}
_aparser=argparse.ArgumentParser(description=_help_text['-intro']+'\nchakshu.py -f filename.ck [--execute --compile --help]')
_aparser.add_argument('-f','--file',nargs=1,help=_help_text['-f'])
_aparser.add_argument('-e','--execute',nargs='?',help=_help_text['-e'],default='-1')
_aparser.add_argument('-c','--compiled-output',nargs='?',help=_help_text['-c'],default='-1')
all_args=_aparser.parse_args()
print(all_args)

if all_args.file:
    _file_path=all_args.file[0] #file path from args
    _code_from_file=util.get_code_from_file(_file_path) #fetching code from input file $func inside util
    object_code=chakshu_parser.run_parser(_code_from_file,enable_input_mode=False)     #making chakshu object code i.e parsing/validating code and returing object $func inside _parser
    py_code=trans_util.get_translated_code(object_code,language='py') #generating code for from chakshu object code $func in trans_util
    trans_util.make_code_file(_file_path,'py',py_code)  #making file for translated code $func in util
    if all_args.compiled_output is None:        #print translated code
        print(py_code.strip())
    if all_args.execute is None:    #print the output of program
        os.system('python '+_file_path+'.py')

else :
    #_aparser.parse_args(['-h'])
    chakshu_parser.run_parser(enable_input_mode=True)
#print(all_args)
