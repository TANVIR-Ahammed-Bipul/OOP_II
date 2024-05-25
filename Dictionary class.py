class MyDictionary:
    def __init__(self):
        self.data = {}

    def add_entry(self, key, value):
        self.data[key] = value

    def get_entry(self, key):
        return self.data.get(key)

    def remove_entry(self, key):
        if key in self.data:
            del self.data[key]
            print("Entry removed.")
        else:
            print("Entry not found.")

# Example usage:
dictionary = MyDictionary()

dictionary.add_entry("apple", "a fruit")
dictionary.add_entry("banana", "another fruit")

print(dictionary.get_entry("apple"))
print(dictionary.get_entry("banana"))
print(dictionary.get_entry("grape"))

dictionary.remove_entry("apple")
print(dictionary.get_entry("apple"))
