#ifndef NODE_H
#define NODE_H

class Node {
	public:
		// DO NOT MODIFY MEMBERS BELOW THIS LINE 
		bool operator==(const Node& other) const {return id == other.id;} 	// used for comparing two nodes, already implemented	
		int id; 															// uniquely identifies a node (no two nodes have the same id). 
				   															// id must be set in the constructor and thereafter not modified
		// DO NOT MODIFY MEMBERS ABOVE THIS LINE 
		Node();
		Node(int i);
		bool operator<(Node other) const {return id < other.id;}
		
	// you should declare a constructor/any other members you need
	// implement any newly declared member functions in node.cpp
	
};

#endif
