#include <iostream>
using namespace std;

// INCOMPLETE
// this is a node based implementation of a int binary search tree

class BST {
private:
    class Node {
    public:
        int data;
        Node * left_child;
        Node * right_child;

        Node() {
            Node(0, NULL, NULL);
        }
        Node(int data) {
            Node(data, NULL, NULL);
        }
        Node(int data, Node * left_child, Node * right_child) {
            this->data = data;
            this->left_child = left_child;
            this->right_child = right_child;
        }
    };
    Node * root;
    int _size;

public:
    BST() {
        this->_size = 0;
        this->root = NULL;
    }

    void insert(int value) {
        _size++;
        if (root == NULL) {
            root = new Node(value);
            return;
        }
        
        Node * current = root;
        while (current != NULL) {
            if (value < current->data) {
                if (current->left_child != NULL) {
                    current = current->left_child;
                    continue;
                } else {
                    current->left_child = new Node(value);
                }
            } else {
                if (current->right_child != NULL) {
                    current = current->right_child;
                    continue;
                } else {
                    current->right_child = new Node(value);
                }
            }
        }
    }

    void erase(int value) {

    }

    void count(int value) {

    }
};

int main() {

}