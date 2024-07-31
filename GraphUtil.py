import time as t
import networkx as nx
import matplotlib.pyplot as plt
import itertools as it


class GraphUtil:
    class NoRender:

        def __getattr__(self, item):
            return lambda *args, **kwargs: None

    def __init__(self, graph=nx.DiGraph(), render_delay=0.5):
        self.graph = graph
        self.render_delay = render_delay

    def reset_and_render_all(self, linked_list):
        self.graph.clear()
        self.graph.add_node("start", color="green")
        if linked_list.start is not None:
            self.graph.add_edge("start", linked_list.start.index, color="gray", label="start", w="1")
        current_element = linked_list.start
        while current_element is not None:
            self.graph.add_node(current_element.index, color="yellow")
            if current_element.previous is not None:
                self.graph.add_edge(current_element.index, current_element.previous.index, color="green", label=f"prev",
                                    w="1")
            if current_element.next is not None:
                self.graph.add_edge(current_element.index, current_element.next.index, color="green", label=f"next",
                                    w="1")
            current_element = current_element.next

        self.draw()

    def mark_node_for_deletion(self, element):
        self.graph.add_node(element.value, color="red")
        self.draw()

    def draw(self, render_delay=None):
        G = self.graph

        fig, ax = plt.subplots()

        # Works with arc3 and angle3 connectionstyles
        connectionstyle = [f"arc3,rad={r}" for r in it.accumulate([0.15] * 4)]
        # connectionstyle = [f"angle3,angleA={r}" for r in it.accumulate([30] * 4)]

        #Layout - line
        pos = {n: [i, 0] for i, n in enumerate(self.graph)}
        #layout - circle
        # pos = nx.shell_layout(G)

        node_colors = nx.get_node_attributes(G, "color").values()
        edge_colors = nx.get_edge_attributes(G, "color").values()

        nx.draw_networkx_nodes(G, pos, node_color=node_colors, ax=ax)
        nx.draw_networkx_labels(G, pos, font_size=10, ax=ax)
        nx.draw_networkx_edges(
            G, pos, edge_color=edge_colors, connectionstyle=connectionstyle, ax=ax
        )
        attr_name = "label"
        labels = {
            tuple(edge): f"{attrs[attr_name]}"
            for *edge, attrs in G.edges(keys=True, data=True)
        }
        nx.draw_networkx_edge_labels(
            G,
            pos,
            labels,
            connectionstyle=connectionstyle,
            label_pos=0.3,
            font_color="blue",
            bbox={"alpha": 0},
            ax=ax,
        )

        plt.show()
        t.sleep(render_delay if render_delay is not None else self.render_delay)
