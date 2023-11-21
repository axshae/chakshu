import sys
def get_code_from_file(filePath):
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


def get_file_from_args():
    args=sys.argv[1:]
    if args:
        return args[0]
    else :
        return None

def get_file(filePath):
    if filePath:
        try:
            _file=open(filePath,'r',encoding='utf-8')
            return _file
        except Exception as ex:
            print('Error:%s'%ex)
            return None
        #print(code)
    else:
        print('Error:Program file not specified')
        return None


# get_file(get_file_from_args())
