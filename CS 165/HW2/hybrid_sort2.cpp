#include "project1.h"
#include <iostream>
#include <math.h>

using namespace std;

void hybrid_sort2(vector<int>& nums) {
	int n = nums.size();
	vector<int> res;
	int H = pow(n, 1/3);
	if (n > H) {
		vector<int> S1(nums.begin(), nums.begin() + nums.size() / 2);
		vector<int> S2(nums.begin() + nums.size() / 2, nums.end());
		hybrid_sort2(S1);
		hybrid_sort2(S2);
		nums = merge(S1, S2);
	}
	else {
		insertion_sort(nums);
	}
}
