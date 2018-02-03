import _parser as chakshu
import util
filePath=util.get_file_from_args()
code=''
if filePath:
    code=util.get_code_from_file(filePath)

chakshu.run_parser(code)
#chakshu.run_parser_from_file(util.get_file(filePath))
