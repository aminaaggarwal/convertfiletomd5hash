#Python hashlib hashing function takes variable length of bytes and converts it into a fixed length sequence.
import hashlib
#Variable defined with a max blocksize or the file size
BLOCKSIZE = 65536
#use md5 function from the haslib and save the value in the hasher variable 
hashit = hashlib.md5()
with open('filedirectorypath', 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hashit.update(buf)
        buf = afile.read(BLOCKSIZE)
print(hashit.hexdigest())
