# -*- coding: utf-8 -*-


class CoderMixIn(object):

    tree_list   = []
    LEFT_SLUG   = 'L'
    SLUG_RIGHT  = 'R'

    def serialize(self):
        if self.tree_list:
            return str(self.tree_list)
        self.preorder()
        return str(self.tree_list)

    def add_left(self,new_node):
        if self.left is None:
            self.left = Node(new_node)
        else:
            t = Node(new_node)
            t.left = self.left
            self.left = t

    def add_right(self,new_node):
        if self.right is None:
            self.right = Node(new_node)
        else:
            t = Node(new_node)
            t.right = self.right
            self.right = t

    def preorder(self, part=None, parent=None):
        self.tree_list.append([self.value, part, parent])
        if self.left:
            self.left.preorder(part=self.LEFT_SLUG, parent=self.value)
        if self.right:
            self.right.preorder(part=self.SLUG_RIGHT, parent=self.value)

    def search_setter(self, name, part, new):
        if self.value == name:
            if part == self.LEFT_SLUG:
                self.add_left(new)
            else:
                self.add_right(new)
            return
        if self.left:
            self.left.search_setter(name=name, part=part, new=new)
        if self.right:
            self.right.search_setter(name=name, part=part, new=new)
            
    @classmethod
    def decode(self, tree_str):
        object = None
        for i, elem in enumerate(eval(tree_str)):
            if i == 0:
                object = Node(elem[0])
                continue
            object.search_setter(elem[2], elem[1], elem[0])
        return object


class Node(CoderMixIn):
    def __init__(self, key_value):
        self.value  = key_value
        self.left   = None
        self.right  = None


class TreeHelper(object):
    def create(self):
        t = Node('a')

        t.add_left('b')
        t.add_right('c')

        t.left.add_left('d')
        t.left.add_right('e')

        t.right.add_right('f')
        return t

    def print_values(self, t, slug):
        printer_list = [slug.upper()]
        printer_list.append(t.value) 
        printer_list.append(t.left.value)
        printer_list.append(t.left.left.value)
        printer_list.append(t.left.right.value)

        printer_list.append(t.right.value)
        printer_list.append(t.right.right.value)
        return ' '.join(printer_list)
