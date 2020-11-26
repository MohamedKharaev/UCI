const int CENTS_PER_QUARTER = 25, CENTER_PER_DIME = 10, CENTS_PER_NICKEL = 5;
class Coins
{
public:
	Coins( int q, int d, int n, int p )
	{
		quarters = q;
		dimes = d;
		nickels = n;
		pennies = p;
	}

	void deposit_coins( Coins & c )
	{
		quarters += c.quarters;
		dimes += c.dimes;
		nickels += c.nickels;
		pennies += c.pennies;
		c.quarters = 0;
		c.dimes = 0;
		c.nickels = 0;
		c.pennies = 0;
	}

	bool has_exact_change_for_coins( Coins c )
	{
		return (quarters >= c.quarters && dimes >= c.dimes && nickels >= c.nickels && pennies >= c.pennies);
	}

	Coins extract_exact_change( Coins c )
	{
		quarters -= c.quarters;
		dimes -= c.dimes;
		nickels -= c.nickels;
		pennies -= c.pennies;
		return c;
	}

	int total_value_in_cents()
	{
		return ((quarters * 25) + (dimes * 10) + (nickels * 5) + (pennies * 1));
	}

	void print( ostream & out )
	{
		cout << quarters << " quarters, " << dimes << " dimes, " << nickels << " nickels, " << pennies << " pennies" << endl;	
	}
	
	void print_dollar( ostream & out )
	{
		cout << "$" << (total_value_in_cents() / 100.0) << endl;
	}

private:
	int quarters, dimes, nickels, pennies;
};

ostream & operator << ( ostream & out, Coins c )
{
	c.print(cout);
}

Coins coins_required_for_cents(int amount_in_cents)
{
	int q_needed = 0;
	int d_needed = 0;
	int n_needed = 0;
	int p_needed = 0;
	while (amount_in_cents - 25 >= 0)
	{
		++q_needed;
		amount_in_cents -= 25;
	}
	while (amount_in_cents - 10 >= 0)
	{
		++d_needed;
		amount_in_cents -= 10;
	}
	while (amount_in_cents - 5 >= 0)
	{
		++n_needed;
		amount_in_cents -= 5;
	}
	while (amount_in_cents - 1 >= 0)
	{
		++p_needed;
		amount_in_cents -= 1;
	}
	return Coins(q_needed, d_needed, n_needed, p_needed);
}


