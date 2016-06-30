from pprint import pprint


class Node(object):
    def __init__(self, value):
        self.connections = {}
        self.plain_values = []
        self.value = value

    def __repr__(self):
        return "<Node> " + str(self.value)

    def get(self, fieldname):
        return self.connections.get(fieldname)

    def add(self, fieldname, node, final_node=None):
        conn = self.connections.get(fieldname)
        if not conn:
            if final_node:
                node.connections[final_node.value] = final_node
            self.connections[fieldname] = [node]
            self.plain_values.append(node.value)

        elif node.value not in self.plain_values:
            conn.append(node)
            self.plain_values.append(node.value)
        elif node.value in self.plain_values and final_node:
            import ipdb; ipdb.set_trace()


    def print_connections(self):
        pprint(self.connections)
