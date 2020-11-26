#include <iostream>
#include <fstream>
#include "Timer.h"

using namespace std;

class SortedArrayList
{
	string * buf;
	int capacity;
	int size;

public:

	SortedArrayList(int c) : buf(new string[c]), capacity(c), size(0) {} // O(1)

	SortedArrayList(const SortedArrayList & SAL) // O(N)
	{
		buf = new string[SAL.capacity];
		for (int i = 0; i < SAL.capacity; ++i)
		{
			buf[i] = SAL.buf[i];
		}
		capacity = SAL.capacity;
		size = SAL.size;
	}

	SortedArrayList & operator = (const SortedArrayList & SAL) // O(N)
	{
		delete[] buf;
		buf = new string[SAL.capacity];
		for (int i = 0; i < SAL.capacity; ++i)
		{
			buf[i] = SAL.buf[i];
		}
		capacity = SAL.capacity;
		size = SAL.size;
		return *this;
	}

	void insert(string word) // O(N)
	{
		if (size == 0)
		{
			buf[size++] = word;
		}
		else
		{
			int hole = binary_search(buf, word, 0, size - 1);
			if (buf[hole] != word)
			{
				if (isFull())
				{
					throw "Cant insert. Array is full";
				}
				copyDown(hole);
				buf[hole] = word;
			}
		}
	}

	bool find(string word) // O(log(N))
	{
		return (buf[binary_search(buf, word, 0, size)] == word);
	}

	void remove(string word) // O(N)
	{
		if (isEmpty())
		{
			throw "Cant remove. Array is empty";
		}
		int position = binary_search(buf, word, 0, size-1);
		if (buf[position] == word)
		{
			copyUp(position);
		}
	}

	void print()
	{
		for (int i = 0; i < size; i++) // O(N)
		{
			cout << buf[i] << endl;
		}
	}

	~SortedArrayList() // O(1)
	{
		delete[] buf;
	}

private:

	bool isEmpty() // O(1)
	{
		return (size == 0);
	}

	bool isFull() // O(1)
	{
		return (size == capacity);
	}
	
	void copyDown(int i) // O(N)
	{
		for (int x = size; x > i; --x)
			buf[x] = buf[x-1];
		++size;
	}

	void copyUp(int index) // O(N)
	{
		for ( ; index < size; ++index)
			buf[index] = buf[index+1];
		--size;
	}

	int binary_search(string buf[], string key, int min, int max) // O(log(N))
	{
		int mid;
		while (max >= min)
		{
			mid = min + (max - min) / 2;
			if (key < buf[mid])
			{
				max = mid - 1;
			}
			else if (key > buf[mid])
			{

				min = mid + 1;
			}
			else
			{
				return mid;
			}
		}
		if (key < buf[mid])
		{
			return mid;
		}
		else
		{
			return mid + 1;
		}
	}
};

class SortedLinkedList
{
	struct ListNode
	{
		string info;
		ListNode * next;
		
		ListNode(string s, ListNode * n) : info(s), next(n) {} // O(1)
	};

	ListNode * head;

public:
	
	SortedLinkedList() : head(nullptr){} // O(1)

	SortedLinkedList(const SortedLinkedList & SLL) // O(N)
	{
		head = dupList(head);
	}

	SortedLinkedList operator = (const SortedLinkedList & SLL) // O(N)
	{
		deleteList(head);
		head = dupList(head);
		return *this;
	}

	void insert(string word) // O(N)
	{
		head = sorted_insert(word, head);
	}

	bool find(string word) // O(N)
	{
		return sequential_search(word, head);
	}

	void remove(string word) // O(N)
	{
		head = remove_string(word, head);
	}

	bool isEmpty() // O(1)
	{
		return (head == nullptr);
	}

	bool isFull() // O(1)
	{
		return false;
	}

	~SortedLinkedList() // O(N)
	{
		deleteList(head);
	}

	void print() // O(N)
	{
		for (ListNode * p = head; p != nullptr; p = p->next)
		{
			cout << p->info << endl;
		}
	}

private:

	static bool sequential_search(string s, ListNode * L) // O(N)
	{
		for (; L != nullptr; L = L->next)
		{
			if (s == L -> info)
			{
				return true;
			}
		}
		return false;
	}

	static ListNode * remove_string(string s, ListNode * L) // O(N)
	{
		if (!L)
		{
			return nullptr;
		}
		
		ListNode * current;
		ListNode * prev;

		for (current = L, prev = nullptr; current != nullptr; current = current -> next)
		{
			if (s != current -> info)
			{
				prev = current;
			}
			else
			{
				if (prev == nullptr)
				{
					prev = current -> next;
					delete current;
					return prev;
				}
				prev -> next = current -> next;
				delete current;
				break;
			}
		}
		return L;
	}

	static ListNode * sorted_insert(string s, ListNode * L) // O(N)
	{
		if (!L)
		{
			return new ListNode(s, nullptr);
		}
		
		ListNode * current;
		ListNode * prev;
		
		for (current = L, prev = nullptr; current != nullptr; current = current -> next)
		{
			if (s > current -> info)
			{
				prev = current;
			}
			else if (s == current -> info)
			{
				return L;
			}
			else
			{
				if (prev == nullptr)
				{
					return new ListNode(s, current);
				}
				else
				{
					break;
				}
			}
		}
		
		prev -> next = new ListNode(s, current);
		return L;
	}

	static void deleteList(ListNode * L) // O(N)
	{
		if (L != nullptr)
		{
			deleteList(L -> next);
			delete L;
		}
	}

	static ListNode * dupList(ListNode * L) // O(N)
	{
		return (!L) ? nullptr : new ListNode(L -> info, dupList(L -> next));
	}
};

void insertAllWords(SortedArrayList & tSAL) // O(Nlog(N))
{
	ifstream in("random.txt");
	string word;
	
	while (in >> word)
	{
		tSAL.insert(word);
	}
}

void removeAllWords(SortedArrayList & tSAL) // O(N^2)
{
	ifstream in("random.txt");
	string word;

	while (in >> word)
	{
		tSAL.remove(word);
	}
}

void findAllWords(SortedArrayList & tSAL) // O(N^2)
{
	ifstream in("random.txt");
	string word;

	while (in >> word)
	{
		tSAL.find(word);
	}
}

void insertAllWords(SortedLinkedList & tSLL) // O(N^2)
{
	ifstream in("random.txt");
	string word;

	while (in >> word)
	{
		tSLL.insert(word);
	}
}

void removeAllWords(SortedLinkedList & tSLL) // O(N^2)
{
	ifstream in("random.txt");
	string word;

	while (in >> word)
	{
		tSLL.remove(word);
	}
}

void findAllWords(SortedLinkedList & tSLL) // O(N^2)
{
	ifstream in("random.txt");
	string word;

	while (in >> word)
	{
		tSLL.find(word);
	}
}

int main()
{
	SortedArrayList tSAL(45500);
	SortedLinkedList tSLL;
	Timer t;
	double i1;
	double f1;
	double r1;
	double i2;
	double f2;
	double r2;

	t.start();
	insertAllWords(tSAL);
	t.elapsedUserTime(i1);
	cout << "Sorted Array List Insert Time: " << i1 << endl;

	findAllWords(tSAL);
	t.elapsedUserTime(f1);
	cout << "Sorted Array List Find Time: " << (f1 - i1) << endl;
	
	removeAllWords(tSAL);
	t.elapsedUserTime(r1);
	cout << "Sorted Array List Remove Time: " << (r1 - f1) << endl;

	
	insertAllWords(tSLL);
	t.elapsedUserTime(i2);
	cout << "Linked List Insert Time: " << (i2 - r1) << endl;
	
	findAllWords(tSLL);
	t.elapsedUserTime(f2);
	cout << "Linked List Find Time: " << (f2 - i2) << endl;

	removeAllWords(tSLL);
	t.elapsedUserTime(r2);
	cout << "Linked List Remove Time: " << (r2 - f2) << endl;

	return 0;
}
