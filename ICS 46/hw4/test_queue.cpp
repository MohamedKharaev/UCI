#include <iostream>
#include <fstream>
using namespace std;

#include "exceptions.h"

class Queue
{
public:
	Queue() {}
	virtual void enque(string s) = 0;
	virtual string deque() = 0;
	virtual string front() = 0;
	virtual bool isEmpty() = 0;
	virtual bool isFull() = 0;
	virtual ~Queue() {}
};

class ArrayQueue : public Queue
{
private:
	string * buf;
	int capacity, start, rear;

public:
	ArrayQueue(int maxSize) : capacity(maxSize + 1), start(0), rear(0), buf(new string[maxSize + 1]) {} // O(1)

	void enque(string s) // O(1)
	{
		if (isFull())
		{
			throw ContainerOverflow("Enque on Full Queue");
		}
		buf[rear] = s;
		rear = (rear + 1) % capacity;
	}

	string deque() // O(1)
	{
		if (isEmpty())
		{
			throw ContainerUnderflow("Deque on Empty Queue");
		}
		string ret = buf[start];
		start = (start + 1) % capacity;
		return ret;
	}

	string front() // O(1)
	{
		if (isEmpty())
		{
			throw ContainerUnderflow("Front on Empty Queue");
		}
		return buf[start];
	}

	bool isEmpty() // O(1)
	{
		return (start == rear);
	}

	bool isFull() // O(1)
	{
		return ((rear + 1) % capacity == start);
	}

	~ArrayQueue() // O(N)
	{
		delete[] buf;
	}
};

class LinkedQueue : public Queue
{

	struct ListNode
	{
		string info;
		ListNode * next;

		ListNode(string newInfo, ListNode * newNext) : info(newInfo), next(newNext) {} // O(1)}
	};

private:

	ListNode * tail;
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

	LinkedQueue() : tail(nullptr), head(tail) {} // O(1)

	void enque(string s) // O(1)
	{
		if (isFull())
		{
			throw ContainerOverflow("Enque on Full Queue");
		}
		ListNode * newNode = new ListNode(s, nullptr);
		if (isEmpty())
		{
			head = newNode;
		}
		else
		{
			tail -> next = newNode;
		}
		tail = newNode;
	}

	string deque() // O(1)
	{
		if (isEmpty())
		{
			throw ContainerUnderflow("Deque on Empty Queue");
		}
		ListNode * L = head;
		head = head -> next;
		string s = L -> info;
		delete L;
		return s;
	}

	string front() // O(1)
	{
		if (isEmpty())
		{
			throw ContainerUnderflow("Front on Empty Queue");
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

	~LinkedQueue() // O(N)
	{
		deleteList(head);
	}
};

void fillAll(Queue & q, const char * filename) // O(N)
{
	string word;
	ifstream in(filename);

	while (in >> word)
	{
		q.enque(word);
	}
}

void emptyAll(Queue & q, const char * filename) // O(N)
{
	ofstream out(filename);

	while (!q.isEmpty())
	{
		out << q.deque() << endl;
	}
}

int main(int argc, char * argv[])
{
	if (argc == 4)
	{
		ArrayQueue A1(45500);
		LinkedQueue L1;

		fillAll(A1, argv[1]);
		emptyAll(A1, argv[2]);

		fillAll(L1, argv[1]);
		emptyAll(L1, argv[3]);
	}
	return 0;
}
