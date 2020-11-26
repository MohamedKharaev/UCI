#include "project2.h"
#include "WAVLTree.h"
#include <tuple>


void first_fit(const std::vector<double>& items, std::vector<int>& assignment, std::vector<double>& free_space) {
	WAVLTree<int, std::vector<double>> tree;
	unsigned long i;
	unsigned long treeSize = 0;
	//std::cout << "Made it to function, items size: " << items.size() << std::endl;
	for (i = 0; i < items.size(); i++) {
		double curr_item = items[i];
		//std::cout << "Starting Item: " << i << " | curr_item size: " << curr_item << std::endl;
		std::tuple<int, double> firstFitVals = tree.firstFit(curr_item);
		double curr_cap = std::get<1>(firstFitVals);
		int bin_num = std::get<0>(firstFitVals);

		//std::cout << "bin_num: " << bin_num << std::endl;
		//std::cout << "curr_cap: " << curr_cap << std::endl;

		if (bin_num == 0) {
			//std::cout << "bin num 0" << std::endl;
			std::vector<double> temp = {1.0-curr_item, 1};
			tree.insert(++treeSize, temp);
			assignment[i] = treeSize;
			tree.updateRC(treeSize);
		} else {
			//std::cout << "bin num not 0" << std::endl;
			std::vector<double> temp = {(curr_cap - curr_item), 1};
			//std::cout << "Updating bin: " << bin_num << "to have rc: " << temp[0] << " and maxrc: " << temp[1] << std::endl;
			tree.update(bin_num, temp);
			//std::cout << "Made it past update" << std::endl;
			assignment[i] = bin_num;
			tree.updateRC(bin_num);
		}
		//std::cout << "Made it to updateRC" << std::endl;
	}
	//std::cout << "Made it past first loop" << std::endl;
	for (i = 1; i <= treeSize; i++) {
		//std::cout << "i: " << i << std::endl;
		//std::cout << "free_space: " << tree.find(i) << std::endl;
		free_space.push_back(tree.find(i)[0]);
	}
	//std::cout << "Made it past push back" << std::endl;

	for (i = 0; i < assignment.size(); i++) {
		//std::cout << assignment[i] << " ";
	}
	//std::cout << std::endl;
}

void first_fit_decreasing(const std::vector<double>& items, std::vector<int>& assignment, std::vector<double>& free_space) {
	std::vector<double> itemsDecreasing(items);

	std::sort(itemsDecreasing.begin(), itemsDecreasing.end());
	std::reverse(itemsDecreasing.begin(), itemsDecreasing.end());

	first_fit(itemsDecreasing, assignment, free_space);
}
