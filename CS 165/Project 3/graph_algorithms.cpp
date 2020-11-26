#include "graph.h"
#include <iostream>

int get_diameter(Graph graph)
{
	// TODO
	std::map<int, Node> m = graph.get_id_to_node_map();
	Node temp = std::get<0>(graph.furthest_node(m[1]));
	return std::get<1>(graph.furthest_node(temp));
}

float get_clustering_coefficient(Graph graph) 
{
	// TODO
	float C;
	float triangles;
	float twoEdgePaths;

	std::map<int, Node> m = graph.get_id_to_node_map();

	std::map<int, Node>::iterator it = m.begin();
	for (std::pair<int, Node> element : m) {
		float degv = float(graph.get_neighbors(element.second).size());
		twoEdgePaths += (degv * (degv - 1.0) / 2);
	}
	


	return -1; // remove this line if you implement the function
}

std::vector<Node> get_d_degeneracy(Graph graph)
{
	std::vector<Node> ret;
	return ret;
}

std::map<int, int> get_degree_distribution(Graph graph) 
{
	// TODO
	std::map<int, int> ans;
	std::map<int, Node> m = graph.get_id_to_node_map();
	
	std::map<int, Node>::iterator it = m.begin();
	for (std::pair<int, Node> element : m) {
		int degree = graph.get_neighbors(element.second).size();
		if (ans.count(degree)) {
			ans[degree]++;
		} else {
			ans.insert(std::pair<int, int>(degree, 1));
		}
	}
		
		
	return ans; // remove this line if you implement the function
}
