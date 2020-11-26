CXXFLAGS=-std=c++11 -Wpedantic -Wall -Wextra -Werror -Weffc++ -Wzero-as-null-pointer-constant
CFLAGS=-std=c99 -pedantic -Wall -Wextra -Werror -ansi -Wwrite-strings

main: MyString.cpp
	echo     ------------compiling MyString.ccp to create executable program MyString----------------
	g++  -ggdb   -std=c++11   MyString.cpp   -o   MyString

clean:
	echo ----------------removing executable program MyString--------------------
	/bin/rm MyString
