from HASHirama import hashlib

class fhash(object):
    def algo(self, fname, buff_size, algo):
        hashalg = hashlib.new(algo)
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(buff_size), b""):
                hashalg.update(chunk)
        return hashalg.hexdigest()

class thash(object):
    def algo(self, text, algo):
        hashalg = hashlib.new(algo)
        hashalg.update(text.encode('utf-8'))
        return hashalg.hexdigest()