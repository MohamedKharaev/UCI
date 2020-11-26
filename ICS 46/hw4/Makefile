GS=-std=c++11 -Wpedantic -Wall -Wextra -Werror -Weffc++ -Wzero-as-null-pointer-constant
CFLAGS=-std=c99 -pedantic -Wall -Wextra -Werror -ansi -Wwrite-strings

main: test_stack.cpp
	echo     ------------compiling test_stack.ccp and test_queue.cpp to create executable program test_stack and test_queue----------------
	g++  -ggdb   -std=c++11   test_stack.cpp   -o   test_stack
	g++  -ggdb   -std=c++11   test_queue.cpp   -o   test_queue

clean:
	echo ----------------removing executable program test_stack and test_queue--------------------
	/bin/rm test_stack
	/bin/rm test_queue


