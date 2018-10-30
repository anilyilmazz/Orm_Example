import hashlib

def md5_converter(password):
    m = hashlib.md5()
    m.update(password.encode('utf-8'))
    return(m.hexdigest())

