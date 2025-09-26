from linked_list import linked_list_node

class Dictionary:
    def __init__(self, size:int):
        self.size = size
        self.map = [None] * size
    
    def get_hash(self, key:str) -> int:
        return hash(key)
    
    def find_index(self, key:str) -> int:
        return self.get_hash(key) % self.size
    
    # Create
    def add(self, key:str, value:str) -> str:
        index = self.find_index(key)
        if self.map[index] is None:
            self.map[index] = linked_list_node(key, value)
            return "Entry added successfully"
        else:
            if self.map[index].read(key) is not None:
                return "Entry already exists"
            else:
                self.map[index].append(key, value)
                return "Entry added successfully"

    # Read
    def lookup(self, key:str) -> str | None:
        index = self.find_index(key)
        if self.map[index] is None:
            return "Entry not found"
        else:
            result = self.map[index].read(key)
            return result if result is not None else "Entry not found"

    # Update
    def update(self, key:str, value:str) -> str:
        index = self.find_index(key)
        if self.map[index] is None:
            return "Entry not found"
        else:
            updated = self.map[index].update(key, value)
            if updated:
                return "Entry updated successfully"
            else:
                return "Entry not found"

    # Delete
    def delete(self, key:str) -> str:
        index = self.find_index(key)
        if self.map[index] is None:
            return "Entry not found"
        else:
            new_head, successful = self.map[index].delete(key)
            if successful:
                self.map[index] = new_head
                return "Entry deleted successfully"
            else:
                return "Entry not found"

