import hashlib
import io
class Loader:
    def __init__(self,file):
        self.file = file
        self.ihash = hashlib.sha256()
        print(self.file)
		
    def compute(self):
        with open(self.file,"rb") as f:
            while True:
                data = f.read(io.DEFAULT_BUFFER_SIZE)
                self.ihash.update(data)
                if not data:
                    break
            return self.ihash.hexdigest()