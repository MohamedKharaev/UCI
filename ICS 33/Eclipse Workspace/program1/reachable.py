import goody
import prompt
from collections import defaultdict


def read_graph(f1 : open) -> {str:{str}}:
    return_dict = defaultdict(set)
    for line in f1:
        initial_node, end_node = line.split(';')
        return_dict[initial_node].add(end_node.rstrip())
    return return_dict
    
def graph_as_str(graph : {str:{str}}) -> str:
    return ''.join([('  ' + str(node[0]) + ' -> ' + str(sorted(node[1])) + '\n') for node in sorted(graph.items())])

        
def reachable(graph : {str:{str}}, start : str) -> {str}:
    reached_nodes, exploring_list = set(), [start]
    while exploring_list:
        node = exploring_list.pop()
        reached_nodes.add(node)
        if node in graph.keys():
            for link in graph[node]: 
                if link not in reached_nodes:
                    exploring_list.append(link)
    return reached_nodes


if __name__ == '__main__':
    # Write script here
    f = goody.safe_open('Enter a file representing a graph: ', 'r', 'file did not exist or there was an error')
    graph = read_graph(f)
    print('Graph: source node -> [all destination nodes]', graph_as_str(graph), sep = '\n')
    while True:
        command = prompt.for_string('\nEnter a name representing the start node (else quit): ',
                                     None,
                                     (lambda x: (x in graph.keys() or x == 'quit')),
                                     'Illegal: not a source node')
        if command == 'quit':
            break
        else:
            print('From', command, 'the reachable nodes are ', reachable(graph, command))
    
    # For running batch self-tests
    import driver
    driver.default_file_name = "bsc1.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
