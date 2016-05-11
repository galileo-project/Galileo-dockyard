from hashlib import md5, sha1

def encrypt(data):
    if not data:
        return data

    data     = data.encode()
    md5_str  = md5(data).hexdigest().encode()
    sha1_str = sha1(data).hexdigest().encode()
    return md5(md5_str + sha1_str + data).hexdigest()