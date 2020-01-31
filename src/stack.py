class Stack:
    """Stack
    A simple implementation of a stack data structure in Python.

    """
    def __init__(self):
        self._data = []

    def push(self,item):
        """Push

        Push an item on to the stack.

        Args:
            arg: Item to be pushed to the top of the stack
        """
        self._data.append(item)

    def pop(self):
        """Pop

        Pop the top item off from the stack and return it.

        Returns:
            element: Item at the top of the stack.
        """
        item = self._data[-1]
        self._data = self._data[:-1]
        return item

    def pop_n(self,n):
        """Pop n elements

        Pops the top n elements from the stack.

        Parameters
        ----------
        arg1 : int
            Number of elements to be popped from the top of the stack

        Returns
        -------
        list
            A list of the top n elements popped from the stack
        """
        items = []
        for i in range(0,n):
            items.append(self.pop())
        return items

    def pop_all(self):
        """Multi-pop

        Pops all the elements from the stack

        Returns
        -------
        list
            A list of every element in the stack
        """
        items = []
        while self.size() > 0:
            items.append(self.pop())
        return items

    def size(self):
        """Get Size

        Determine the size of the stack

        Returns
        -------
        int: A count of elements on the stack
        """
        return len(self._data)
