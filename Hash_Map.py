class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

class Hash_Map:
    def __init__(self):
        self.size = 6
        self.map = [None] * self.size

    def get_hash(self,key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def insert(self,key,value):
        key_hash = self.get_hash(key)
        key_value = [key, value]
        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    def search(self,key):
        key_hash = self.get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self,key):
        key_hash = self.get_hash(key)
        if self.map[key_hash] is None:
            return False
        for i in range(0,len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
        return False
    
    def print(self):
        print('-------DREAM DESTINATION-------')
        for item in self.map:
            if item is not None:
                print(item)

h=Hash_Map()
h.insert('Siddhu','London')
h.insert('Bhairab','Paris')
h.insert('Ashutosh','USA')
h.insert('Ashish','Japan')
h.insert('Anshuman','Russia')
h.insert('Arijit','Switzerland')
h.insert('Rahul','France')
h.insert('Saswat','Australia')
h.print()
h.delete('Rahul')
h.print()
print('Ashish: '+ h.search('Ashish'))
