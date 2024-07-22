class Element:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None
        self.index = 0

    def __str__(self):
        return (f"Value: {self.value}, "
                f"Next: {self.next.value}, " if self.next else "None, "
                f"Previous: {self.previous.value}, " if self.previous else "None, "
                f"Index: {self.index}")
