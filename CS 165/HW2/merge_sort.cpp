#include "project1.h"
#include <iostream>

using namespace std;

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

