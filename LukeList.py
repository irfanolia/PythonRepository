class LukesList:
    def __init__(self):
        """Initialize an empty list."""
        self._items = []

    def add(self, item):
        """Add an item to the end of the list."""
        self._items.append(item)

    def __getitem__(self, index):
        """Retrieve an item by index."""
        return self._items[index]

    def __setitem__(self, index, value):
        """Set an item at a specific index."""
        self._items[index] = value

    def __repr__(self):
        """Return a string representation of the list."""
        return str(self._items)

    def __len__(self):
        """Return the length of the list."""
        return len(self._items)


my_list = LukesList()

my_list.add("Data Nerd")

my_list.add("Finance Nerd")

print(my_list)

print(len(my_list))