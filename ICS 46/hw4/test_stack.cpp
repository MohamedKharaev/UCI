#include <iostream>
#include <fstream>
using namespace std;

#include "exceptions.h"

class Stack
{
public:
	virtual void push(string s) = 0;
	virtual string pop() = 0;
	virtual string top() = 0;
	virtual bool isEmpty() = 0;
	virtual bool isFull() = 0;
	virtual ~Stack() {}
};

class ArrayStack : public Stack
{
private:
	string * buf;
	int capacity, tp;

public:
	ArrayStack(int maxSize) : capacity(maxSize), tp(0), buf(new string[maxSize]) {} // O(1)

	void push(string s) // O(1)
	{
		if (isFull())
		{
			throw ContainerOverflow("Push on Full Stack");
		}
		buf[tp++] = s;
	}

	string pop() // O(1)
	{
		if (isEmpty())
		{
			throw ContainerUnderflow("Pop on Empty Stack");
		}
		return buf[--tp];
	}

	string top() // O(1)
	{
		if (isEmpty())
		{
			throw ContainerUnderflow("Top on Empty Stack");
		}
		return buf[tp - 1];
	}

	bool isEmpty() // O(1)
	{
		return (tp <= 0);
	}

	bool isFull() // O(1)
	{
		return (tp >= capacity);
	}

	~ArrayStack() // O(N)
	{
		delete[] buf;
	}
};

class LinkedStack : public Stack
{
	struct ListNode
	{
		string info;
		ListNode * next;

		ListNode(string newInfo, ListNode * newNext) : info(newInfo), next(newNext) {} // O(1)

	};

private:
	ListNode * head;

	static void deleteList(ListNode * L) // O(N)
	{
		if (L != nullptr)
		{
			deleteList(L -> next);
			delete L;
		}
	}

public:
	LinkedStack() : head(nullptr) {} // O(1)

	void push(string s) // O(1)
	{
		if (isFull())
		{
			throw ContainerOverflow("Push on Full Stack");
		}
		head = new ListNode(s, head);
	}

	string pop() // O(1)
	{
		if (isEmpty())
		{
			throw ContainerUnderflow("Pop on Empty Stack");
		}
		ListNode * L = head;
		head = head -> next;
		string s = L -> info;
		delete L;
		return s;
	}

	string top() // O(1)
	{
		if (isEmpty())
		{
			throw ContainerUnderflow("Top on Empty Stack");
		}
		return (head -> info);		
	}

	bool isEmpty() // O(1)
	{
		return (head == nullptr);
	}

	bool isFull() // O(1)
	{
		return false;
	}

	~LinkedStack() // O(N)
	{
		deleteList(head);
	}
};

void fillAll(Stack & s, char const * filename) // O(N)
{
	ifstream in(filename);
	string word;

	while (in >> word)
	{
		s.push(word);
	}
}

void emptyAll(Stack & s, char const * filename) // O(N)
{
	ofstream out(filename);

	while (!s.isEmpty())
	{
		out << s.pop() << endl;
	}
}

bool isBalanced(string brackets) // O(N)
{
	LinkedStack LS;
	try 
	{
		for (int i = 0; i < brackets.length(); ++i)
		{
			string c(1, brackets[i]);
			if (c == "(" || c == "{" || c == "[")
			{
				LS.push(c);
			}
			else
			{
				string open_char = LS.pop();
				if (!( (c == ")" && open_char == "(") || (c == "}" && open_char == "{") || (c == "]" && open_char == "[") ))
				{
					return false;
				}
			}
		}
	}
	catch(const ContainerUnderflow & err)
	{
		return false;
	}
	return true;
}

int main(int argc, char * argv [])
{
	if (argc == 4)
	{
	ArrayStack A1(45500);
	LinkedStack L1;

	fillAll(A1, argv[1]);
	emptyAll(A1, argv[2]);

	fillAll(L1, argv[1]);
	emptyAll(L1, argv[3]);
	}

	else{
		cout << "isBalanced(\"(({([])}))\"): " << isBalanced("(({([])}))") << endl;
		cout << "isBalanced(\"{{{)}}}\"): " << isBalanced("{{{)}}}") << endl;
		cout << "isBalanced(\"\"): " << isBalanced("") << endl;
		cout << "isBalanced(\")\"): " << isBalanced(")") << endl;
	}
	return 0;
}
