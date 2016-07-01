from pprint import pprint


class Node(object):
    def __init__(self, value):
        self.connections = {}
        self.value = value

    def __repr__(self):
        return "<Node> " + str(self.value)

    def get(self, fieldname):
        return self.connections.get(fieldname)

    def add(self, fieldname, node, final_node=None):
        if node.value not in self.connections:
            self.connections[node.value] = node
        if final_node:
            self.connections[node.value].add(final_node.value, final_node)

    def print_connections(self):
        pprint(self.connections)
