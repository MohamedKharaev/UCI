#include "graph.h"
#include <algorithm>
#include <iostream> 
#include <queue>

Graph make_graph(int num_nodes, std::vector<int> u, std::vector<int> v){
	// TODO
	Graph* g = new Graph(num_nodes, u, v);
	return *g;
}

Graph::Graph() {

}

Graph::Graph(int num_nodes, std::vector<int> u, std::vector<int> v){
	this->numnodes = num_nodes;
	this->numedges = u.size();
	int i;
	for (i = 1; i <= this->numnodes; i++) {
		Node* n = new Node(i);
		this->nodes.push_back(*n);
	}
	for (i = 0; i < this->numnodes; i++) {
		std::vector<Node> empty_vect;
		this->neighbors.push_back(empty_vect);
	}
	for (i = 0; i < this->numedges; i++) {
		this->neighbors[u[i]-1].push_back(this->nodes[v[i]-1]);;
		this->neighbors[v[i]-1].push_back(this->nodes[u[i]-1]);
	}
//	for (i = 0; i < this->numedges; i++) {
//		std::sort(this->neighbors[i].begin(), this->neighbors[i].end());
//	}

}

int Graph::get_num_nodes() {
	// TODO
	return this->numnodes; // remove this line if you implement the function
}

int Graph::get_num_edges() {
	// TODO
	return this->numedges; // remove this line if you implement the function
}

std::vector<Node> Graph::get_neighbors(Node u) {
	// TODO
	return this->neighbors[u.id-1]; // remove this line if you implement the function
}

std::map<int, Node> Graph::get_id_to_node_map(){
	// TODO
	std::map<int, Node> ans; // remove this line if you implement the function
	int i;
	for (i = 1; i <= this->numnodes; i++) {
		ans[i] = this->nodes[i-1];
	}
	return ans;
}

std::tuple<Node, int> Graph::furthest_node(Node node) {
	std::vector<bool> visited(this->get_num_nodes(), false);
	std::vector<int> distance(this->get_num_nodes(), 0);
	std::queue<Node> q;

	int max_distance = 0;
	Node max_node = node;

	q.push(node.id);
	visited[node.id-1] = true;

	while (!q.empty()) {
		node = q.front();
		q.pop();

		for (Node n : this->get_neighbors(node)) {
			if (!visited[n.id - 1]) {
				visited[n.id - 1] = true;
				distance[n.id -1] = distance[node.id-1] + 1;
				if (distance[n.id-1] > max_distance) {
					max_node = n;
					max_distance = distance[n.id-1];
				}
				q.push(n);
			}
		}
	}
	return std::tuple<Node, int>(max_node, max_distance);

}

