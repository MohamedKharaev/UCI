#include "project1.h"
#include "hybrid_sort1.cpp"
#include "hybrid_sort2.cpp"
#include "hybrid_sort3.cpp"
#include "merge_sort.cpp"
#include "shell_sort1.cpp"
#include "shell_sort2.cpp"
#include "shell_sort3.cpp"
#include "shell_sort4.cpp"

#include <chrono>
#include <math.h>

using namespace std;

vector<int> sorted_permutation(int size) {
	vector<int> res;
	for (int i = 1; i <= size; i++) {
		res.push_back(i);
	}
	return res;
}

vector<int> reverse_sorted_permutation(int size) {
	vector<int> res;
	for (int i = size; i >= 1; i--) {
		res.push_back(i);
	}
	return res;
}

vector<int> almost_sorted_permutation(int size) {
	vector<int> res = sorted_permutation(size);
	int swaps = 2 * int(log2(size));

	for (int i = 0; i < swaps; i++) {
		int j1 = rand() % size;
		int j2 = rand() % size;

		int temp = res[j1];
		res[j1] = res[j2];
		res[j2] = temp;
	}
	return res;
}

vector<int> uniform_permutation(int size) {
	vector<int> res = sorted_permutation(size);
	for (int i = size - 1; i >= 1; i--) {
		int swap = rand() % i;
		int temp = res[i];
		res[i] = res[swap];
		res[swap] = temp;
	}
	return res;
}

void print_vector(vector<int> vect) {
	for (int i = 0; i < vect.size(); i++) {
		cout << vect[i] << ", ";
	}
	cout << endl;
}

void print_array(long arr[], int arr_size) {
	cout << "[";
	for (int i = 0; i < arr_size; i++) {
		cout << arr[i] << ", ";
	}
	cout << "]" << endl;
}

long avg_array(int arr[], int arr_size) {
	long res = 0;
	for (int i = 0; i < arr_size; i++) {
		res += arr[i];
	}
	return long(res/arr_size);
}

void test_sort(void (*func)(vector<int>&)) {
	int sizes[] = {100, 500, 1000, 2500, 5000, 10000, 25000, 50000};
	int sizes_len = 8;
	int tests = 8;

	vector<vector<vector<int>>> uniformVectors(tests, vector<vector<int>>());
	vector<vector<vector<int>>> almostSortedVectors(tests, vector<vector<int>>());
	vector<vector<vector<int>>> reverseVectors(tests, vector<vector<int>>());

	long uniformOutput[sizes_len];
	long almostSortedOutput[sizes_len];
	long reverseOutput[sizes_len];

	for (int j = 0; j < sizes_len; j++) {

		for (int i = 0; i < tests; i++) {
			uniformVectors[j].push_back(uniform_permutation(sizes[j]));
			almostSortedVectors[j].push_back(almost_sorted_permutation(sizes[j]));
			reverseVectors[j].push_back(reverse_sorted_permutation(sizes[j]));
		}

		int allUniformOutputs[tests];
		for (int i = 0 ; i < tests; i++) {
			auto start = chrono::high_resolution_clock::now();
			func(uniformVectors[j][i]);
			auto stop = chrono::high_resolution_clock::now();
			auto duration = chrono::duration_cast<chrono::microseconds>(stop - start);
			allUniformOutputs[i] = duration.count();
		}
		uniformOutput[j] = avg_array(allUniformOutputs, tests);

		int allAlmostSortedOutputs[tests];
		for (int i = 0 ; i < tests; i++) {
			auto start = chrono::high_resolution_clock::now();
			func(almostSortedVectors[j][i]);
			auto stop = chrono::high_resolution_clock::now();
			auto duration = chrono::duration_cast<chrono::microseconds>(stop - start);
			allAlmostSortedOutputs[i] = duration.count();
		}
		almostSortedOutput[j] = avg_array(allAlmostSortedOutputs, tests);

		int allReverseOutputs[tests];
		for (int i = 0 ; i < tests; i++) {
			auto start = chrono::high_resolution_clock::now();
			func(reverseVectors[j][i]);
			auto stop = chrono::high_resolution_clock::now();
			auto duration = chrono::duration_cast<chrono::microseconds>(stop - start);
			allReverseOutputs[i] = duration.count();
		}
		reverseOutput[j] = avg_array(allReverseOutputs, tests);

	}

	cout << "Uniform_Distribution = ";
	print_array(uniformOutput, sizes_len);
	cout << "Almost_Sorted_Distribution = ";
	print_array(almostSortedOutput, sizes_len);
	cout << "Reverse_Distribution = ";
	print_array(reverseOutput, sizes_len);

}

int main() {
	cout << "hybrid_sort1" << endl;
	test_sort(hybrid_sort1);
	cout << endl << "hybrid_sort2" << endl;
	test_sort(hybrid_sort2);
	cout << endl << "hybrid_sort3" << endl;
	test_sort(hybrid_sort3);
	cout << endl << "insertion_sort" << endl;
	test_sort(insertion_sort);
	cout << endl << "merge_sort" << endl;
	test_sort(merge_sort);
	cout << endl << "shell_sort1" << endl;
	test_sort(shell_sort1);
	cout << endl << "shell_sort2" << endl;
	test_sort(shell_sort2);
	cout << endl << "shell_sort3" << endl;
	test_sort(shell_sort3);
	cout << endl << "shell_sort4" << endl;
	test_sort(shell_sort4);
	return 0;
}