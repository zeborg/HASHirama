from HASHirama import hashlib

class fhash(object):
    def algo(self, fname, buff_size, algo, chain=1):
        hashalg = hashlib.new(algo)
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(buff_size), b""):
                hashalg.update(chunk)
                
        res = hashalg.hexdigest()
        
        for _ in range(chain-1):
            hashalg = hashlib.new(algo)
            hashalg.update(res.encode('utf-8'))
            res = hashalg.hexdigest()
            
        return res

class thash(object):
    def algo(self, text, algo, chain=1):
        hashalg = hashlib.new(algo)
        hashalg.update(text.encode('utf-8'))
        
        res = hashalg.hexdigest()
        
        for _ in range(chain-1):
            hashalg = hashlib.new(algo)
            hashalg.update(res.encode('utf-8'))
            res = hashalg.hexdigest()
        
        return res
        
