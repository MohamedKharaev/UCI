#include "project1.h"
#include <iostream>
#include <math.h>

using namespace std;

vector<int> A036562_Sequence(int max) {
	int i = 0;
	vector<int> res;
	res.push_back(1);

	while (true) {
		int next_num = pow(4, i + 1) + 3 * pow(2, i) + 1;
		i++;

		if (next_num > max)
			break;

		res.push_back(next_num);
	}

	return res;
}

void shell_sort4(vector<int>& nums) {
	vector<int> p_sequence = A036562_Sequence(nums.size());

	vector<int>::reverse_iterator rit = p_sequence.rbegin();

	for (; rit != p_sequence.rend(); ++rit) {
		int gap = *rit;
		cout << gap << "yes";
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