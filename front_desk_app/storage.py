# storage.py

class StorageArea:
    def __init__(self, size, capacity):
        self.size = size
        self.capacity = capacity
        self.available_boxes = capacity

    def accept_box(self):
        if self.available_boxes > 0:
            self.available_boxes -= 1
            return True
        return False
