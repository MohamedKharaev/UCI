#include <iostream>
#include <fstream>
using namespace std;

int NumAllocations = 0;

class MyString
{

	struct ListNode
	{
		char info;
		ListNode * next;

		ListNode(char c, ListNode * n) : info(c), next(n) // O(1) 
		{
		++NumAllocations;
		}
	};

private:

	ListNode * head;

	static ListNode * stringToList(const char * s) // O(N)
	{
		return (s[0] == '\0') ? nullptr : new ListNode(s[0], stringToList(s+1));
	}

	static ListNode * dupList(ListNode * l) // O(N)
	{
		return(l == nullptr) ? nullptr : new ListNode(l->info, dupList(l->next));
	}

	static int nodeLength(ListNode * l)  // O(N)
	{
		return (l == nullptr) ? 0 : 1 + nodeLength(l->next);
	}

	static void deleteNode(ListNode * l) // O(N)
	{
		if (l != nullptr)
		{
			deleteNode(l->next);
			delete l;
			--NumAllocations;
		}	
	}

	static ListNode * strchr(char c, ListNode * l) // O(N)
	{
		for (ListNode * p = l; p != nullptr; p = p->next)
		{
			if (p->info == c)
				return p;
		}
		return nullptr;
	}

	static ListNode * strstr(ListNode * pat, ListNode * s2) // O(N^2)
	{
		ListNode * p = strchr(pat->info, s2);
		while (p != nullptr)
		{
			ListNode * tempp = p;
			ListNode * patp = pat;
			while (tempp && patp && (tempp->info == patp->info))
			{
				tempp = tempp->next;
				patp = patp->next;
			}
			if (patp == nullptr) {
				return p;
			}
			p = strchr(pat->info, p->next);
		}
		return nullptr;
	}

	static ListNode * indexList(int index, ListNode * l) // O(N)
	{
		ListNode * result = l;
		for (int i = 1; i <= index; ++i)
		{
			if (result->next == nullptr)
			{
				if (i == index)
					return result;
				else
					throw 1;
			}
			else
			{
			result = result -> next;
			}
		}
		return result;
	}

	static ListNode * str2dup(ListNode * L1, ListNode * L2) // O(N)
	{
		if (L1 == nullptr)
			return dupList(L2);
		ListNode * result = dupList(L1);
		ListNode * temp = result;
		while (temp->next != nullptr)
			temp = temp->next;
		temp->next = dupList(L2);
		return result;
	}

	static int strcmp(ListNode * L1, ListNode * L2) // O(N)
	{
		if (!L1 && !L2) return 0;
		if (!L1 && L2) return -1;
		if (L1 && !L2)return 1;
		else
			if (L1->info == L2->info)
				return strcmp(L1->next, L2->next);
		return L1->info - L2->info;
	}

	static ListNode * strrev(ListNode * l) // O(N)
	{
		ListNode * result = nullptr;

		for (ListNode * p = l; p != nullptr; p = p->next)
		{
			result = new ListNode(p->info, result);
		}

		return result;
	}

public:

	explicit MyString(const char * s = "") // O(N)
	{
		head = stringToList(s);
	}

	MyString(const MyString & s) // O(N)
	{
		head = dupList(s.head);
	}

	MyString & operator = (const MyString & s) // O(N)
	{
		deleteNode(head);
		head = dupList(s.head);
		return *this;
	}

	char & operator [] (const int index)  // O(N)
	{
		return indexList(index, head) -> info;
	}

	int length() const // O(N)
	{
		return nodeLength(head);
	}

	int indexOf(char c) const // O(N)
	{
		ListNode * charpos = strchr(c, head);
		if (charpos == nullptr)
			return -1;
		else
		{
			int posNum = 0;
			for (ListNode * pos = head; pos != nullptr; pos = pos->next, ++posNum)
			{
				if (pos == charpos)
					return posNum;
			}
		}
	}

	int indexOf(const MyString & pat) const // O(N^2)
	{
		ListNode * charpos = strstr(pat.head, head);
		if (charpos == nullptr)
			return -1;
		else
		{
			int posNum = 0;
			for (ListNode * pos = head; pos != nullptr; pos = pos->next, ++posNum)
			{
				if (pos == charpos)
					return posNum;
			}
		}
	}

	bool operator == (const MyString & s) const // O(N)
	{
		return (strcmp(head, s.head) == 0);
	}

	MyString operator + (const MyString & s) const // O(N)
	{
		ListNode * resultHead = str2dup(head, s.head);
		MyString result;
		result.head = resultHead;
		return result;
	}

	MyString & operator += (const MyString & s) // O(N)
	{
		ListNode * result = str2dup(head, s.head);
		deleteNode(head);
		head = result;
		return *this;
	}

	MyString reverse() const // O(N)
	{
		ListNode * rev = strrev(head);
		MyString result;
		result.head = rev;
		return result;
	}

	void print(ostream & out) const // O(N)
	{
		for (ListNode * p = head; p != nullptr; p = p->next)
		{
			out << p->info;
		}
	}

	void read(istream & in) // O(N)
	{
		char input[256];
		in.getline(input, 256);
		deleteNode(head);
		head = stringToList(input);
	}

	~MyString() // O(N)
	{
		deleteNode(head);
	}
};

inline ostream & operator << (ostream & out, const MyString & str) // O(N)
{
	str.print(out);
	return out;
}

inline istream & operator >> (istream & in, MyString & str) // O(N)
{
	str.read(in);
	return in;
}

MyString copyConstructorTest(MyString l) // O(N)
{
	return l;
}


void testReverse() // O(N)
{
	ifstream in("input.txt");
	MyString l;

	while (in >> l)
	{
		cout << copyConstructorTest(l) << " " << l.length() << " " << l.reverse() << endl;
	}
}


void testEquals() // O(N)
{
	ifstream in("input.txt");
	MyString l;
	MyString s;

	while (in >> l)
	{
		cout << "s = l: " << (s = l) << endl;
	}
}

void testIndex() // O(N)
{
	ifstream in("input.txt");
	MyString l;

	while (in >> l)
	{
		cout << "3rd Index of " << l << ": " << l[2] << endl;
	}
}

void testLength() // O(N)
{
	ifstream in("input.txt");
	MyString l;

	while (in >> l)
	{
		cout << "Length of " << l << ": " << l.length() << endl;
	}
}

void testIndexOf() // O(N^2)
{
	ifstream in("input.txt");
	MyString l;
	MyString hi("hi");

	while (in >> l)
	{
		cout << "Index of (a) in " << l << ": " << l.indexOf('a') << endl;
		cout << "Index of (hi) in " << l << ": " << l.indexOf(hi) << endl;
	}
}

void testEquality() // O(N)
{
	ifstream in("input.txt");
	MyString l;
	MyString flask("Flask");

	while (in >> l)
	{
		cout << "Flask == " << l << ": " << (l == flask) << endl;
	}
}

void testPlus() // O(N)
{
	ifstream in("input.txt");
	MyString l;
	MyString one("one");

	while (in >> l)
	{
		cout << "one + " << l << ": " << (one + l) << endl;
	}
}

void testPlusEquals() // O(N)
{
	ifstream in("input.txt");
	MyString l;
	MyString s;

	in >> s;

	while (in >> l)
	{
		cout << s << " += " << l << ": ";
		cout << (s += l) << endl;
	}
}


int main()
{
    try
    {
        testEquals();
    }
    catch (int i)
    {
        cout << "Got an exception: " << i << endl;
    }

    try
    {
        testReverse();
    }
    catch (int i)
    {
        cout << "Got an exception: " << i << endl;
    }

    try
    {
        testIndex();
    }
    catch (int i)
    {
        cout << "Got an exception: " << i << endl;
    }

    try
    {
        testLength();
    }
    catch (int i)
    {
        cout << "Got an exception: " << i << endl;
    }

    try
    {
        testIndexOf();
    }
    catch (int i)
    {
        cout << "Got an exception: " << i << endl;
    }

    try
    {
        testEquality();
    }
    catch (int i)
    {
        cout << "Got an exception: " << i << endl;
    }

    try
    {
        testPlus();
    }
    catch (int i)
    {
        cout << "Got an exception: " << i << endl;
    }

    try
    {
        testPlusEquals();
    }
    catch (int i)
    {
        cout << "Got an exception: " << i << endl;
    }



	cerr << "Net memory allocated at program end: " << NumAllocations << endl;
	cerr << "(should be zero! positive = memory leak, negative = duplicate delete)\n";
	return 0;
}


