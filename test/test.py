import hashlib

#https://stackoverflow.com/questions/16874598/how-do-i-calculate-the-md5-checksum-of-a-file-in-python?rq=1
def md5_check(filename):
    with open(filename) as file_to_check:
        # read contents of the file
        data = file_to_check.read()    
        # pipe contents of the file through
        md5_returned = hashlib.md5(data.encode('utf-8')).hexdigest()
    return md5_returned


md5_original = 1
md5_bajo_prueba = 2

# calcular md5 de ambos archivos
md5_original = md5_check('test/patron.txt')
md5_bajo_prueba = md5_check('RMS_0.1ms2.pvc')

#comparar
if md5_original == md5_bajo_prueba:
    print("Success")
else:
    print("Fail")
