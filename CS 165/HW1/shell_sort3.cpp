#include "project1.h"
#include <iostream>
#include <math.h>

using namespace std;

vector<int> pratt_Sequence(int max) {
	int i, last2ind = 0, last3ind = 0;
	vector<int> res;

	res.push_back(1);
	for (i = 0; res[i] < max; ++i) {
		if (res[last2ind] * 2 < res[last3ind] * 3) {
			res.push_back(res[last2ind] * 2);
			last2ind++;
		}
		else if (res[last2ind] * 2 > res[last3ind] * 3) {
			res.push_back(res[last3ind] * 3);
			last3ind++;
		}
		else {
			res.push_back(res[last2ind] * 2);
			last2ind++;
			last3ind++;
		}
	}

	return res;

}

void shell_sort3(vector<int>& nums) {
	vector<int> p_sequence = pratt_Sequence(nums.size());

	vector<int>::reverse_iterator rit = p_sequence.rbegin();

	for (; rit != p_sequence.rend(); ++rit) {
		int gap = *rit;
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
