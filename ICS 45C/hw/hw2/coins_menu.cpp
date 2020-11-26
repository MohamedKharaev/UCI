#include <iostream>
using namespace std;
#include "Coins.h"

int main()
{
	string str;
	string dummy;
	int amount;
	Coins balance(0,0,0,0);

	while (true) 
	{

	cout << "Would you like to deposit change(d), extract change(e), print change(p) or stop(s)?" << endl;
	getline(cin, str);

		if (str == "d")
		{
			cout << "How much would you like to deposit (cents): ";
			cin >> amount;
			getline(cin, dummy);
	
			Coins temp = coins_required_for_cents(amount);
			balance.deposit_coins(temp);
			continue;
		}	
		else if (str == "e")
		{
			cout << "How much would you like to extract (cents): ";
			cin >> amount;
			getline(cin, dummy);

			Coins temp = coins_required_for_cents(amount);
			if (balance.has_exact_change_for_coins(temp))
			{
				balance.extract_exact_change(temp);
			}
			else
			{
				cout << "You do not have to required coins for that" << endl;
			}
		}
		else if (str == "p")
		{
			cout << "You have: " << balance << endl;
		}
		else if (str == "s")
		{
			break;
		}
		else
		{
			cout << "Invalid" << endl;
		}
	}
	return 0;
}
