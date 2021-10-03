import hashlib
BLOCKSIZE = 65536
hasher = hashlib.md5()
with open('/Users/amina.aggarwal/test.txt', 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)
print(hasher.hexdigest())
