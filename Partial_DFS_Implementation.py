'''
    * Interrupted variant of depth-first-search, to see some of the output.
    * Contributed to by: Ricky Dodd (220010849)
'''
import networkx as nx
from Shared_Core import *

path = []

'''
    perform_tour(), copied and pasted from DFS_Implementation.py and modified to not give the goal state, but give
    some outputs to see what's actually happening.
'''
def perform_tour(n, u, limit, h):
    G.nodes[u]['path'] = "yes"
    path.append(u)

    print(path)

    if n < limit:
        connected_list = [item for item in G.neighbors(u)]
        i = 0
        goal_state = False
        while i < len(connected_list) and not goal_state:
            if G.nodes[connected_list[i]]['path'] == "no":
                goal_state = perform_tour(n+1, connected_list[i], limit, h)
                h = h + 1
                if h == 10:
                    goal_state = True
            i = i + 1
        if not goal_state:
            G.nodes[path.pop()]['path'] = "no"
    else:
        goal_state = True
    return goal_state

def perform_dfs():
    generate_graph(6)
    perform_tour(0, (0,0), len(G), 0)
    print(path)
    return

perform_dfs()