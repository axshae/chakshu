import _parser as chakshu
import util
import trans_util
import __trans_py__ as PYTHON_TRANSLATOR
filePath=util.get_file_from_args()
code=''
if filePath:
    code=util.get_code_from_file(filePath)

object_code=chakshu.run_parser(code,enable_input_mode=False)
py_code=PYTHON_TRANSLATOR.make_code(object_code)
trans_util.make_code_file(filePath,'py',py_code)
for i in object_code:
    print(i)
print(py_code)
#chakshu.run_parser_from_file(util.get_file(filePath))
