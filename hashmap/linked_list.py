class linked_list_node:
    def __init__(self, key:str, value:str):
        self.key = key
        self.value = value
        self.next = None
    
    # CRUD operations

    # Create
    def append(self, key:str, value:str):
        if self.next is None:
            self.next = linked_list_node(key, value)
        else:
            self.next.append(key, value)

    # dont add duplicates

    # Read
    def read(self, key:str):
        if self.key == key:
            return self.value
        elif self.next is None:
            return None
        else:
            return self.next.read(key)
    
    # Update
    def update(self, key:str, value:str):
        if self.key == key:
            self.value = value
            return True
        elif self.next is None:
            return False
        else:
            return self.next.update(key, value)

    # Delete
    def delete(self, key:str):
        if self.key == key:
            self = self.next
            return self, True
        elif self.next is None:
            return self, False
        elif self.next.key == key:
            self.next = self.next.next
            return self, True
        else:
            _, successful = self.next.delete(key)
            return self, successful
    



