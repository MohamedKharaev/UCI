#include "project2.h"
#include "WAVLTree.h"

void next_fit(const std::vector<double>& items, std::vector<int>& assignment, std::vector<double>& free_space) {
	WAVLTree<int, double> tree;
	unsigned long j = 1;
	tree.insert(j, 1.0);

	unsigned long i;
	double curr_bin = 1.0;
	for (i = 0; i < items.size(); i++) {
		double curr_item = items[i];
		if (curr_bin - curr_item >= -.001) {
			tree.update(j, curr_bin - curr_item);
			curr_bin = curr_bin - curr_item;
			assignment[i] = j;
		} else {
			j += 1;
			tree.insert(j, 1.0 - curr_item);
			curr_bin = 1.0 - curr_item;
			assignment[i] = j;
		}
	}
	for (i = 1; i <= j; i++) {
		free_space.push_back(tree.find(i));
	}
}
