#include "WAVLTree.h"
#include "project2.h"
#include "first_fit.cpp"
#include "best_fit.cpp"
#include "next_fit.cpp"
#include <iostream>
#include <utility>
#include <string>
#include <cmath> 
#include <stdlib.h>
#include <iostream>
#include <random>
#include <cstdlib>
#include <ctime>

using namespace std;

double test_next_fit(vector<double> dataset) {
	vector<int> assignment(dataset.size(), 0);
	vector<double> free_space;

	next_fit(dataset, assignment, free_space);

	double free_space_sum = 0;
	int i;
	for (i = 0; i < free_space.size(); i++) {
		free_space_sum += free_space[i];
	}

	return free_space_sum;
}

double test_first_fit(vector<double> dataset) {
	vector<int> assignment(dataset.size(), 0);
	vector<double> free_space;

	first_fit(dataset, assignment, free_space);

	double free_space_sum = 0;
	int i;
	for (i = 0; i < free_space.size(); i++) {
		free_space_sum += free_space[i];
	}

	return free_space_sum;
}

double test_first_fit_decreasing(vector<double> dataset) {
	vector<int> assignment(dataset.size(), 0);
	vector<double> free_space;

	first_fit_decreasing(dataset, assignment, free_space);

	double free_space_sum = 0;
	int i;
	for (i = 0; i < free_space.size(); i++) {
		free_space_sum += free_space[i];
	}

	return free_space_sum;
}

void test_dataset(vector<double> dataset) {
	cout << "TESTING N: " << dataset.size() << endl;

	int i;
	vector<int> assignment(dataset.size(), 0);
	vector<double> free_space;

	double dataset_sum = 0;
	for (i = 0; i < dataset.size(); i++) {
		dataset_sum += dataset[i];
	}

	cout << "next_fit:             | waste(N): " << (dataset_sum - test_next_fit(dataset)) << endl;
	cout << "first_fit:            | waste(N): " << (dataset_sum - test_first_fit(dataset)) << endl;
	cout << "first_fit_decreasing: | waste(N): " << (dataset_sum - test_first_fit_decreasing(dataset)) << endl;
	cout << endl;
}

void test() {
	const vector<int> test_sizes = {500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000 };

	vector<vector<double>> datasets;

	default_random_engine generator;
  	uniform_int_distribution<int> distribution(0,70);

	int test_size;
	for (test_size = 0; test_size < test_sizes.size(); test_size++) {
		vector<double> items;
		int i;
		for (i = 0; i < test_sizes[test_size]; i++) {
			float r = static_cast <float> (rand()) / (static_cast <float> (RAND_MAX/0.7));
			items.push_back(r);
		}
		datasets.push_back(items);
	}

	int dataset;
	for (dataset = 0; dataset < datasets.size(); dataset++) {
		test_dataset(datasets[dataset]);
	}

}

int main()
{
	test();

}