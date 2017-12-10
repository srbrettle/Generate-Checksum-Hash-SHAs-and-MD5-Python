import hashlib

def generate_sha256(filename):
    with open(filename, 'rb') as f:
        contents = f.read()
        sha256 = hashlib.sha256(contents).hexdigest()
        return sha256