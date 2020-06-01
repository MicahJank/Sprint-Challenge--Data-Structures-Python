class RingBuffer:
    def __init__(self, capacity):
        # the number of items the ring buffer can hold
        self.capacity = capacity
        # will hold the items that get added to the ring buffer
        self.storage = []

        # keep track of the oldest index
        self.oldest_index = 0

    def append(self, item):
        # check the length of the storage, if its reached max capacity then we should overwrite the oldest item in the list
        if (len(self.storage) == self.capacity):
            # remove the oldest item
            self.storage.pop(self.oldest_index)

            # next insert the new element at the position where we removed the item
            # of the list (where the element that we removed was at)
            self.storage.insert(self.oldest_index, item)

            # when we reach the end of the list - the oldest index should go back to the beginning of the list to position 0
            if self.oldest_index == len(self.storage) - 1:
                self.oldest_index = 0
            else:
                self.oldest_index += 1

        # otherwise just append the item to the end of the list if there is still space
        else:
            self.storage.append(item)


    def get(self):
        return [item for item in self.storage if item is not None]