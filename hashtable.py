""" A dictionary with string keys. This implementation that avoids conveniences like `index` and `enumerate`. """

class EmptyClass:
    def __repr__(self):
        return "Empty"

Empty = EmptyClass()

def array_index(array, key, i):
    while True:
        if array[i] == key:
            return i
        elif array[i] == Empty:
            raise ValueError(f"Value {key} is not in the dictionary")
        i = (i + 1) % len(array)

def djb2_hash(key):
    h = 5381
    for c in key:
        h = ((h << 5 + h) + ord(c)) & 0xffffffff
    return h

start = djb2_hash

class Hashtable:
    def __init__(self, size):
        self.keys = [Empty] * size
        self.values = [Empty] * size

    def __getitem__(self, key):
        return self.values[array_index(self.keys, key, start(key) % len(self.keys))]

    def __setitem__(self, key, value):
        try:
            i = array_index(self.keys, key, start(key) % len(self.keys))
        except ValueError:
            i = array_index(self.keys, Empty, start(key) % len(self.keys))
        self.keys[i] = key
        self.values[i] = value

if __name__ == '__main__':
    d = Hashtable(100)
    d["hello"] = 10
    d["world"] = "foo"
    print(d["hello"])
