#include "project3.h"
#include "graph.h"
#include "graph.cpp"
#include "graph_algorithms.cpp"
#include "node.h"
#include "node.cpp"
#include <assert.h>
#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <stdlib.h>

using namespace std;

vector<vector<int>> create_barbasi_albert(int nodes, int degree) {
	vector<vector<int>> ret;
	int M[2 * nodes * degree];
	int v, i;
	for (v = 0; v < (2 * nodes * degree); v++) {
		M[v] = -1;
	}
	for (v = 0; v < nodes; v++) {
		for (i = 0; i < degree; i++) {
			int index = 2 * (v * degree + i);
			int r;
			if (index == 0) {
				r = 0;
			} else {
				r = rand() % (2 * (v * degree + i));
			}
			M[2 * (v * degree + i)] = v;
			M[2 * (v * degree + i) + 1] = M[r];
		}
	}
	for (v = 0; v < 2 * nodes * degree; v++) {
		M[v]++;
	}
	vector<int> E1;
	vector<int> E2;
	for (i = 0; i < (nodes * degree); i++) {
		E1.push_back(M[2 * i]);
		E2.push_back(M[2 * i + 1]);
	}
	ret.push_back(E1);
	ret.push_back(E2);
	return ret;
}


int main() {
	Graph graph;

	const vector<int> test_sizes = {5, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000};
	int i, j;
	float diameters[test_sizes.size()];
	for (i = 0; i < test_sizes.size(); i++) {
		float diameter = 0;
		for (j = 0; j < 10; j++) {
			vector<vector<int>>barbasi = create_barbasi_albert(test_sizes[i], 5);
			
			graph = make_graph(test_sizes[i], barbasi[0], barbasi[1]);

			int g = get_diameter(graph);
			cout << g << endl;
			diameter += g;
			//cout << "DIAMETER: " << get_diameter(graph) << endl;
			//cout << "DEGREE DISTRIBUTION" << endl;
			//std::map<int, int> degree_distribution = get_degree_distribution(graph);
			//for (std::pair<int, int> element : degree_distribution)
			//	cout << element.first << ", ";
			//cout << endl << endl;
			//for (std::pair<int, int> element : degree_distribution)
			//	cout << element.second << ", ";
		}
		diameters[i] = diameter / 10;
	}
	for (i = 0; i < test_sizes.size(); i++) {
		cout << "GRAPH SIZE: " << test_sizes[i] << endl;
		cout << "Diameter: " << diameters[i] << endl;
	}
	return 0;
}

/*
create_graph(nodes, degree):
	Create M, int array of size 2 * nodes * degree
	for v in range(nodes):
		for i in range(degree):
			M[2 * (v * d + i)] = v
			r = rand() % (2 * (v * d + i))
			M[2 * (v * d + i) + 1] = M[r]
	E1 = set()
	E2 = set()
	For i in range(n * d):
		E1.add(M[2 * i])
		E2.add(M[2 * i + 1])


M = empty array */