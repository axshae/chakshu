import _parser as chakshu
import sys
def getCodeFromFile(filePath):
    if filePath:
        code=''
        try:
            code=open(filePath,'r',encoding='utf-8').read()
        except Exception as ex:
            print('Error:%s'%ex)
            return None
        #print(code)
        return code
    else:
        print('Error:Program file not specified')
        return None
def getFileFromArgs():
    args=sys.argv[1:]
    return args[0]

code=getCodeFromFile(getFileFromArgs())
if code:
    print(code)
chakshu.run_parser(code,exec_by_line=True)
