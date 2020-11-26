#include "project1.h"
#include <iostream>

using namespace std;

vector<int> merge(vector<int>& S1, vector<int>& S2) {
	vector<int> res;
	int i = 0;
	int j = 0;
	int n1 = S1.size();
	int n2 = S2.size();

	while (i < n1 && j < n2) {
		if (S1[i] <= S2[j]) {
			res.push_back(S1[i]);
			i++;
		}
		else {
			res.push_back(S2[j]);
			j++;
		}
	}

	while (i < n1) {
		res.push_back(S1[i]);
		i++;
	}
	while (j < n2) {
		res.push_back(S2[j]);
		j++;
	}

	return res;
}

void merge_sort(vector<int>& nums) {
	int n = nums.size();
	vector<int> res;
	if (n > 1) {
		vector<int> S1(nums.begin(), nums.begin() + nums.size() / 2);
		vector<int> S2(nums.begin() + nums.size() / 2, nums.end());
		merge_sort(S1);
		merge_sort(S2);
		nums = merge(S1, S2);
	}
}

