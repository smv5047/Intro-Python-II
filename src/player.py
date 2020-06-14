# Write a class to hold player information, e.g. what room they are in
# currently.

from item import Item


class Player:

    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def get_item(self, item):
        item = Item(item, self)
        self.items.append(item)

    def drop_item(self, item):
        item = Item(item, self)
        self.items.remove(item)
