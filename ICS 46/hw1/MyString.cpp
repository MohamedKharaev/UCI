#include <iostream>
#include <fstream>
using namespace std;

int NumAllocations = 0;

class MyString
{
	char * buf;
	// 2
	void error(const char * s)
	{
		cerr << "Error: " << s << endl;
		throw 0;
	}

private:

	// 2
	static char * new_char_array(const int len)
	{
		NumAllocations += 1;
		return new char[len];
	}

	// 2
	static void delete_char_array(char * s)
	{
		delete[] s;
		NumAllocations -= 1;
	}

	// N + 2
	static int strlen(const char * s)
	{
		int len;
		for (len = 0; s[len] != '\0'; ++len)
			;
		return len;
	}

	// 6N + 3
	static char * strcpy(char * d, const char * s)
	{
		int i;
		for (i = 0; s[i] != '\0'; ++i)
		{
			d[i] = s[i];
		}
		d[i] = '\0';
		return d;
	}

	// 7N + 9
	static char * strdup(const char * s)
	{
		char * arr_dup = new_char_array(strlen(s) + 1);
		strcpy(arr_dup, s);
		return arr_dup;
	}

	// 6N + 4
	static int strcmp(const char * s1, const char * s2)
	{
		int i;
		for (i = 0; s1[i] == s2[i]; ++i)
		{
			if(s1[i] == '\0')
			{
				return 0;
			}
		}
		return s1[i] - s2[i];
	}

	// 7N + 8
	static char * strrev(char * d, char * s)
	{
		int i;
		int slen = strlen(s) - 1;
		for (i = 0; s[i] != '\0'; ++i)
		{
			d[slen - i] = s[i];
		}
		d[i] = '\0';
		return d;
	}

	// 8N + 1
	static char * strcat(char * destination, const char * source)
	{
		while (*destination)
			*destination++;

		while (*source)
			*destination++ = *source++;

		*destination++ = '\0';

		return destination;
	}

	// 16N + 13
	static char * str2dup(const char * s1, const char * s2)
	{
		char * arr2_dup = new_char_array(strlen(s1) + strlen(s2) + 1);
		strcpy(arr2_dup, s1);
		strcat(arr2_dup, s2);
		return arr2_dup;
	}

	// 4N + 1
	static char * strchr(char * s, int c)
	{
		while (*s)
		{
			if (*s == c)
				return s;
			++s;
		}
		return nullptr;
	}

	// 9N^2 + 8N + 4
	static char * strstr(char * s1, const char * s2)
	{
		char * p = s1;
		while (p = strchr(p, s2[0]))
		{
			char * tempp = p;
			const char * s2p = s2;
			while (*tempp && *s2p && (*tempp == *s2p))
			{
				++tempp;
				++s2p;
			}
			if (*s2p == '\0') {
				return p;
			}
		}
		return nullptr;
	}

public:

	// 7N + 10
	explicit MyString(const char * s = "")
	{
		buf = strdup(s);
	}
	
	// 7N + 10
	MyString(const MyString & s)
	{
		buf = strdup(s.buf);
	}

	// 7N + 13
	MyString & operator = (const MyString & s)
	{
		delete_char_array(buf);
		buf = strdup(s.buf);
		return *this;
	}

	// 2
	char & operator [] (const int index)
	{
		return buf[index];
	}

	// N + 3
	int length() const
	{
		return strlen(buf);
	}

	// 4N + 4
	int indexOf(char c) const
	{
		char * p = strchr(buf, c);
		if (p == nullptr)
			return -1;
		return p - buf;
	}

	// 6N + 7
	int indexOf(const MyString & pat) const
	{
		char * p = strstr(buf, pat.buf);
		if (p == nullptr)
			return -1;
		return p - buf;
	}

	// 6N + 7
	bool operator == (const MyString & s) const
	{
		if (strcmp(buf, s.buf) == 0)
		{
			return true;
		}
		return false;
	}

	// 23N + 26
	MyString operator + (const MyString & s) const
	{
		char * result = str2dup(buf, s.buf);
		MyString return_MS(result);
		delete_char_array(result);
		return return_MS;
	}

	// 16N + 18
	MyString & operator += (const MyString & s)
	{
		char * result = str2dup(buf, s.buf);
		delete_char_array(buf);
		buf = result;
		return *this;
	}

	// 15N + 27
	MyString reverse() const
	{
		char * result = new_char_array(strlen(buf) + 1);
		strrev(result, buf);
		MyString return_MS(result);
		delete_char_array(result);
		return return_MS;
	}

	// 1
	void print(ostream & out) const
	{
		out << buf;
	}

	// 7N + 14
	void read(istream & in)
	{
		char input[256];
		in.getline(input, 256);
		delete_char_array(buf);
		buf = strdup(input);
	}

	// 2
	~MyString()
	{
		delete_char_array(buf);
	}
};

// 2
inline ostream & operator << (ostream & out, const MyString & str)
{
	str.print(out);
	return out;
}

// 7N + 15
inline istream & operator >> (istream & in, MyString & str)
{
	str.read(in);
	return in;
}

// 1
MyString copyConstructorTest(MyString l)
{
	return l;
}

// 16N^2 + 33N + 1
void testReverse()
{
	ifstream in("input.txt");
	MyString l;

	while (in >> l)
	{
		cout << copyConstructorTest(l) << " " << l.length() << " " << l.reverse() << endl;
	}
}

//7N^2 + 13N + 1
void testEquals()
{
	ifstream in("input.txt");
	MyString l;
	MyString s;

	while (in >> l)
	{
		cout << "s = l: " << (s = l) << endl;
	}
}
// 7N + 1
void testIndex()
{
	ifstream in("input.txt");
	MyString l;

	while (in >> l)
	{
		cout << "3rd Index of " << l << ": " << l[3] << endl;
	}
}
// N^2 + 8N + 1
void testLength()
{
	ifstream in("input.txt");
	MyString l;

	while (in >> l)
	{
		cout << "Length of " << l << ": " << l.length() << endl;
	}
}
// 10N^2 + 28N + 1
void testIndexOf()
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
// 16N^2 + 30N + 1
void testEquality()
{
	ifstream in("input.txt");
	MyString l;
	MyString flask("Flask");

	while (in >> l)
	{
		cout << "Flask == " << l << ": " << (l == flask) << endl;
	}
}
// 23N^2 + 38N + 11
void testPlus()
{
	ifstream in("input.txt");
	MyString l;
	MyString one("one");

	while (in >> l)
	{
		cout << "one + " << l << ": " << (one + l) << endl;
	}
}
// 16N^2 + 22N + 1
void testPlusEquals()
{
	ifstream in("input.txt");
	MyString l;
	MyString s;

	while (in >> l)
	{
		cout << s << " += " << l << ": " << (s += l) << endl;
	}
}


int main()
{
	try
	{
		testEquals();
		testReverse();
		testIndex();
		testLength();
		testIndexOf();
		testEquality();
		testPlus();
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

