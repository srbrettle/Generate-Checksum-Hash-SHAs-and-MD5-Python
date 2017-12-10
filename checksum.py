import hashlib

def generateHash(filename):
    with open(filename, 'rb') as f:
        content = f.read()
        # SHA-1
        sha1 = hashlib.sha1(content).hexdigest()
        # SHA-224
        sha224 = hashlib.sha224(content).hexdigest()
        # SHA-256
        sha256 = hashlib.sha256(content).hexdigest()
        # SHA-384
        sha384 = hashlib.sha384(content).hexdigest()
        # SHA-512
        sha512 = hashlib.sha512(content).hexdigest()
        # SHA-3-224
        sha3_224 = hashlib.sha3_224(content).hexdigest()
        # SHA-3-256
        sha3_256 = hashlib.sha3_256(content).hexdigest()
        # SHA-3-348
        sha3_384 = hashlib.sha3_384(content).hexdigest()
        # SHA-3-512
        sha3_512 = hashlib.sha3_512(content).hexdigest()

        # MD5
        md5 = hashlib.md5()
        for i in range(0, len(content), 8192):
            md5.update(content[i:i + 8192])
        md5 = md5.hexdigest()

    return {'sha1':sha1, 'sha224':sha224, 'sha256':sha256, 'sha384':sha384,
            'sha512':sha512, 'sha3_224':sha3_224, 'sha3_256':sha3_256,
            'sha3_384':sha3_384, 'sha3_512':sha3_512, 'md5':md5}