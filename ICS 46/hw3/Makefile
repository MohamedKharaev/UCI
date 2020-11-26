XXFLAGS=-std=c++11 -Wpedantic -Wall -Wextra -Werror -Weffc++ -Wzero-as-null-pointer-constant
CFLAGS=-std=c99 -pedantic -Wall -Wextra -Werror -ansi -Wwrite-strings

main: testMystring.cpp
	echo     ------------compiling testMystring.ccp to create executable program testMystring----------------
	g++  -ggdb   -std=c++11   testMystring.cpp   -o   testMystring

clean:
	echo ----------------removing executable program testMystring--------------------
	/bin/rm testMystring

