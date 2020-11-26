#include "project2.h"

void best_fit(const std::vector<double>& items, std::vector<int>& assignment, std::vector<double>& free_space) {
	/*WAVLTree<double, int> tree;
	unsigned long treeSize = 0;
	unsigned long i;
	for (i = 0; i < items.size(); i++) {
		std::tuple<double, int> bestFitVals = tree.bestFit(items[i]);
		double curr_cap = std::get<0>(bestFitVals);
		int bin_num = std::get<1>(bestFitVals);

		//std::cout << "Inserting value: " << items[i] << std::endl;

		if (bin_num == 0) {
			tree.insert(1.0 - items[i], ++treeSize);
			//std::cout << "Created new bin #" << treeSize << " - with remaining capacity: " << 1.0-items[i] << std::endl; 
			assignment[i] = treeSize;
		} else {
			tree.deleteNode(curr_cap, bin_num);
			tree.insert(curr_cap - items[i], bin_num);
			//std::cout << "Inserted item into bin #" << bin_num << ". Previously had: " << curr_cap << " | Now has: " << curr_cap - items[i] << std::endl;
			//std::cout << tree.getSize() << " = Size" << std::endl;
			assignment[i] = bin_num;
		}
	}
	
	for (i = 0; i < treeSize; i++) {
		free_space.push_back(0);
	}
	*/
}

void best_fit_decreasing(const std::vector<double>& items, std::vector<int>& assignment, std::vector<double>& free_space) {
	/*std::vector<double> itemsDecreasing(items);

	std::sort(itemsDecreasing.begin(), itemsDecreasing.end());
	std::reverse(itemsDecreasing.begin(), itemsDecreasing.end());

	best_fit(itemsDecreasing, assignment, free_space);
	*/
}
