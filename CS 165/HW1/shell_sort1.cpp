#include "project1.h"
#include <iostream>
#include <math.h>

using namespace std;

void shell_sort1(vector<int>& nums) {
	int n = nums.size();
	int logn = log2(n);
	for (int k = 1; k <= logn; k++) {
		int gap = int((n / pow(2, k)));
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
