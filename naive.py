""" A dictionary with string keys. This implementation that avoids conveniences like `index` and `enumerate`. """

class EmptyClass:
    def __repr__(self):
        return "Empty"

Empty = EmptyClass()

def array_index(array, key):
    for i in range(len(array)):
        if array[i] == key:
            return i
    raise ValueError(f"Value {key} not found.")

class NaiveDict:
    def __init__(self, size):
        self.keys = [Empty] * size
        self.values = [Empty] * size

    def __getitem__(self, key):
        return self.values[array_index(self.keys, key)]

    def __setitem__(self, key, value):
        try:
            i = array_index(self.keys, key)
        except ValueError:
            i = array_index(self.keys, Empty)
        self.keys[i] = key
        self.values[i] = value

if __name__ == '__main__':
    d = NaiveDict(100)
    d["hello"] = 10
    d["world"] = "foo"
    print(d["hello"])
