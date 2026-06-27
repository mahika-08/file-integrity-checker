import hashlib
def generate_hash(file_path): #created function
    sha256 = hashlib.sha256() #created sha256 object which will receive file data

    with open(file_path, "rb") as f: #opened file in read-binary mode
        while chunk := f.read(4096):  #@reads in chunks
            sha256.update(chunk)

    return sha256.hexdigest() #return final digest as headecimal by conversion
