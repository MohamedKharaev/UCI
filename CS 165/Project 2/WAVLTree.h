#ifndef WAVLTREE_H
#define WAVLTREE_H
#include <algorithm>
#include <cmath>
#include <iostream>
#include <limits>
#include <tuple>

// explanations for public member functions are provided in project2.h
// each file that uses a WAVL tree should #include this file 
template <typename KeyType, typename ValType>
class WAVLTree {
	public:
		// DO NOT MODIFY PUBLIC MEMBERS BELOW THIS LINE
		WAVLTree();
		~WAVLTree();
		void insert(KeyType key, ValType val);
		ValType find(const KeyType& key);
		int getSize();
		int getHeight();
		int getRank(const KeyType& key);
		// DO NOT MODIFY PUBLIC MEMBERS ABOVE THIS LINE

		// define new public members
		class Node {
			public:
				KeyType key;
				ValType val;
				int height;
				Node* left;
				Node* right;
				Node(KeyType k, ValType v) {
					height = 1;
					key = k;
					val = v;
					left = nullptr;
					right = nullptr;
				}
		};

		Node* root = nullptr;

        void update(KeyType key, ValType val);
        void deleteNode(KeyType key, ValType val);
        std::tuple<KeyType, ValType> bestFit(KeyType key);
        std::tuple<KeyType, double> firstFit(double v);
        void updateRC(KeyType k);

	private:
		// define new private members
		int height(Node* head) {
			if (head == nullptr) return 0;
			return head->height;
		}

		int rank(Node* head) {
			if (head == nullptr) {
				return 0;
			}
			int rl = rank(head->left);
			int rr = rank(head->right);
			int r = 1 + std::max(rl, rr);

			int rankDifferenceRight = r - rr;
			int rankDifferenceLeft = r - rl;
			if (rankDifferenceLeft > 2 || rankDifferenceRight > 2) {
				r -= 1;
			} else if (rankDifferenceRight == 2 && rankDifferenceLeft == 2 && rl == 0 && rr == 0) {
				r -= 1;
			}
			return r;
		}

		int sizeUtil(Node* head) {
			if (head == nullptr) {
				return 0;
			}
			return 1 + sizeUtil(head->left) + sizeUtil(head->right);
		}

		Node* rightRotation(Node* head) {
			Node* newhead = head->left;
			head->left = newhead->right;
			newhead->right = head;
			head->height = 1 + std::max(height(head->left), height(head->right));
			newhead->height = 1 + std::max(height(newhead->left), height(newhead->right));
			return newhead;
		}

		Node* leftRotation(Node* head){
            Node* newhead = head->right;
            head->right = newhead->left;
            newhead->left = head;
            head->height = 1 + std::max(height(head->left), height(head->right));
            newhead->height = 1 + std::max(height(newhead->left), height(newhead->right));
            return newhead;
        }

        Node* insertUtil(Node* head, KeyType k, ValType v) {
        	if (head == nullptr) {
        		Node* temp = new Node(k, v);
        		return temp;
        	}
        	if (k < head->key) head->left = insertUtil(head->left, k, v);
        	else if (k > head->key) head->right = insertUtil(head->right, k, v);
        	head->height = 1 + std::max(height(head->left), height(head->right));
        	int bal = height(head->left) - height(head->right);

        	if (bal > 1) {
        		if (k < head->left->key) {
        			return rightRotation(head);
        		} else {
        			head->left = leftRotation(head->left);
        			return rightRotation(head);
        		}
        	} else if (bal < -1) {
        		if (k > head->right->key) {
        			return leftRotation(head);
        		} else {
        			head->right = rightRotation(head->right);
        			return leftRotation(head);
        		}
        	}
        	return head;
        }

        Node* removeUtil(Node* head, KeyType k, ValType v) {
        	if (head == nullptr) return nullptr;

        	if (k < head->key) {
        		head->left = removeUtil(head->left, k, v);
        	} else if (k > head->key) {
        		head->right = removeUtil(head->right, k, v);
        	} else {
        		if (head->val != v) {
        			head->left = removeUtil(head->right, k, v);
        		} else {
         			Node* r = head->right;
        			if (head->right == nullptr) {
        				Node* l = head->left;
        				//std::cout << "1deleting node (" << head->key << ", " << head->val << ")" << std::endl;
        				delete(head);
        				head = l;
        			} else if (head->left == nullptr) {
        				//std::cout << "2deleting node (" << head->key << ", " << head->val << ")" << std::endl;
        				delete(head);
        				head = r;
        			} else {
        				while (r->left != nullptr) r = r->left;
        				head->key = r->key;
        				head->right = removeUtil(head->right, r->key, r->val);
        			}
        		}
        	}

        	if (head == nullptr) return head;
        	head->height = 1 + std::max(height(head->left), height(head->right));

        	int bal = height(head->left) - height(head->right);
        	if (bal > 1) {
        		if (k > head->left->key) {
        			return rightRotation(head);
        		} else {
        			head->left = leftRotation(head->left);
        			return rightRotation(head);
        		}
        	} else if (bal < -1) {
        		if (k < head->right->key) {
        			return leftRotation(head);
        		} else {
        			head->right = rightRotation(head->right);
        			return leftRotation(head);
        		}
        	}

        	return head;
        }

        Node* findUtil(Node* head, KeyType k) {
        	if (head == nullptr) return nullptr;
        	else if (head->key == k) return head;
        	else if (head->key > k) return findUtil(head->left, k);
        	else return findUtil(head->right, k);
        }

        Node* bestFitUtil(Node* head, KeyType k) {
        	if (head == nullptr) return nullptr;
        	if (k < head->key || AreSame(k, head->key)) {
        		Node* lbest = bestFitUtil(head->left, k);
        		if (lbest == nullptr) return head;
        		else return lbest;
        	}
        	else return bestFitUtil(head->right, k);
        }

        Node* firstFitUtil(Node* head, double v) {
        	if (head == nullptr) return nullptr;
        	//std::cout << "currently in firstFitUtil, looking at bin #: " << head->key << std::endl;
        	//std::cout << "currently has rc and maxrc: " << head->val[0] << ", " << head->val[1] << std::endl;
        	if (v < head->val[1] || AreSame(v, head->val[1])) {
        		Node* lfirst = firstFitUtil(head->left, v);
        		if (lfirst == nullptr) {
        			if (v < head->val[0] || AreSame(v, head->val[0])) {
        				//std::cout << "here1" << std::endl;
        				//std::cout << "returning head with key: "; 
        				//std::cout << head->key << " and vals: " << head->val[0] << ", " << head->val[1] << std::endl;
        				return head;
        			} else {
        				//std::cout << "here2" << std::endl;
        				return firstFitUtil(head->right, v);
        			}
        		} else {
                    return lfirst;
                }
        	} 
        	//std::cout << "here3" << std::endl;
        	return nullptr;
        }

        double updateRCUtil(Node* head, KeyType k) {
            if (head == nullptr) return 0;
            double maxChildRC;
            if (k < head->key) {
                if (head->right != nullptr) {
                    maxChildRC = std::max(updateRCUtil(head->left, k), head->right->val[1]);
                } else {
                    maxChildRC = updateRCUtil(head->left, k);
                }
            }
            else if (k > head->key) {
                if (head->left != nullptr) {
                    maxChildRC = std::max(updateRCUtil(head->right, k), head->left->val[1]);
                } else {
                    maxChildRC = updateRCUtil(head->right, k);
                }
            }
            else {
                maxChildRC = std::max(updateRCUtil(head->left, k), updateRCUtil(head->right, k));
            }
            head->val[1] = std::max(head->val[0], maxChildRC);
            return head->val[1];
        }

        void updateUtil(Node* head, ValType v) {
            head->val = v;
        }

        bool AreSame(double a, double b) {
    		return std::fabs(a - b) < 0.001;
		}
};

// fill in the definitions for each public member function and for any additional public/private members you define

template <typename KeyType, typename ValType>
WAVLTree<KeyType, ValType>::WAVLTree()
{

}


template <typename KeyType, typename ValType>
WAVLTree<KeyType, ValType>::~WAVLTree()
{

}

template <typename KeyType, typename ValType>
void WAVLTree<KeyType, ValType>::insert(KeyType key, ValType val)
{
	root = insertUtil(root, key, val);
}

template <typename KeyType, typename ValType>
void WAVLTree<KeyType, ValType>::update(KeyType key, ValType val)
{
    updateUtil(findUtil(root, key), val);
}

template <typename KeyType, typename ValType>
void WAVLTree<KeyType, ValType>::deleteNode(KeyType key, ValType val)
{
	root = removeUtil(root, key, val); 
}

template <typename KeyType, typename ValType>
ValType WAVLTree<KeyType, ValType>::find(const KeyType& key)
{
	return findUtil(root, key)->val; 
}

template <typename KeyType, typename ValType>
int WAVLTree<KeyType, ValType>::getSize()
{
	return sizeUtil(root);
}

template <typename KeyType, typename ValType>
int WAVLTree<KeyType, ValType>::getHeight()
{
	return height(root); 
}

template <typename KeyType, typename ValType>
int WAVLTree<KeyType, ValType>::getRank(const KeyType& key)
{
	return rank(findUtil(root, key));
}

template <typename KeyType, typename ValType>
void WAVLTree<KeyType, ValType>::updateRC(KeyType k)
{
    updateRCUtil(root, k);
}

template <typename KeyType, typename ValType>
std::tuple<KeyType, ValType> WAVLTree<KeyType, ValType>::bestFit(KeyType k)
{
	Node* temp = bestFitUtil(root, k);
	if (temp == nullptr) {
		return {0, 0};
	}
	return {temp->key, temp->val};
}

template <typename KeyType, typename ValType>
std::tuple<KeyType, double> WAVLTree<KeyType, ValType>::firstFit(double v)
{
	Node* temp = firstFitUtil(root, v);
	//std::cout << "in firstFit function" << std::endl;
	if (temp == nullptr) {
		//std::cout << "here4" << std::endl;
		return {0, 0};
	}
	/*std::cout << "here5" << std::endl;
	std::cout << temp->key << std::endl;
	std::cout << temp->val[0] << std::endl;
	std::cout << temp->val[1] << std::endl;*/
	return {temp->key, temp->val[0]};
}


// add definitions for any public/private members if needed

#endif /* WAVLTREE_H */
