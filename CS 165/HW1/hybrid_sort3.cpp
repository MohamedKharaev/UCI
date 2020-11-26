#include "project1.h"
#include <iostream>
#include <math.h>

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

void insertion_sort(vector<int>& nums) {
	for (int i = 0; i < nums.size(); i++) {
		int temp = nums[i];

		int j = i;
		while (j > 0 && nums[j-1] > temp) {
			nums[j] = nums[j-1];
			j--;
		}

		nums[j] = temp;
	}
}

void hybrid_sort3(vector<int>& nums) {
	int n = nums.size();
	vector<int> res;
	int H = pow(n, 1/4);
	if (n > H) {
		vector<int> S1(nums.begin(), nums.begin() + nums.size() / 2);
		vector<int> S2(nums.begin() + nums.size() / 2, nums.end());
		hybrid_sort3(S1);
		hybrid_sort3(S2);
		nums = merge(S1, S2);
	}
	else {
		insertion_sort(nums);
	}
}