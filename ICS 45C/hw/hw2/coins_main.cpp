#include <iostream>
using namespace std;
#include "Coins.h"

int main()
{
	Coins pocket(5, 3, 6, 8);
	Coins piggyBank(50, 50, 50, 50);
	
	cout << "I have " << pocket << " in my pocket." << endl;
	pocket = pocket.extract_exact_change( coins_required_for_cents( 68 ) ); 
	cout << "I bought chips for 68 cents and now I have " << pocket << " in my pocket " << endl;
	
	cout << "I have " << piggyBank << " in my piggy bank" << endl;

	Coins temp = coins_required_for_cents( 205 );
	piggyBank.extract_exact_change(temp);
	pocket.deposit_coins(temp);

	cout <<"I transferred $2.05 from my piggy back into my pocket. Now I have " << pocket << " in my pocket and " << piggyBank << " in my piggy bank" << endl;

	Coins couch(10, 10, 10, 10);
	
	piggyBank.deposit_coins(couch);
	
	cout << "I found change in the sofa and added it to my piggy bank. Now my piggy bank has ";
	piggyBank.print_dollar(cout);

	return 0;
}
