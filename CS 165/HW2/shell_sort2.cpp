#include "project1.h"
#include <iostream>
#include <math.h>

using namespace std;

void shell_sort2(vector<int>& nums) {
	int n = nums.size();
	int logn = log2(n);
	for (int k = logn; k > 0; k--) {
		int gap = pow(2, k) - 1;
		for (int i = gap; i < nums.size(); i++) {
			int temp = nums[i];
			int j = i;
			while (j >= gap && temp < nums[j - gap]) {
				nums[j] = nums[j - gap];
				j -= gap;
			}
			nums[j] = temp;
		}
	}
}
