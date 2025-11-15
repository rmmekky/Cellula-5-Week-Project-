# langgraph.py

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, name, func=None):
        self.nodes[name] = func

    def run(self, start_node, state):
        current = start_node
        while current:
            node_func = self.nodes.get(current)
            if node_func is None:
                print(f"Node {current} not found!")
                break
            result = node_func(state)
            if result.get("done"):
                break
            current = result.get("next")
        return state
