#include <iostream>
#include <vector>
using namespace std;

// array implementation of a integer max-heap in C++

class IntMaxHeap {
private:
    vector<int> vect;
    int _size;

    int parent(int i) {
        return i>>1;
    }
    int l_child(int i) {
        return i<<1;
    }
    int r_child(int i) {
        return (i<<1) + 1;
    }

    void shift_up(int i) {
        if(i >_size) return;

        if(i == 1) return;

        if (vect[parent(i)] < vect[i]) {
            swap(vect[parent(i)], vect[i]);
            shift_up(parent(i));
        }
    }

    void shift_down(int i) {
        if(i > _size) {
            return;
        }

        int l = l_child(i);
        int r = r_child(i);
        int largest = i;
        if (l<_size && vect[l] > vect[largest]) {
            largest = l;
        }
        if (r<_size && vect[r] > vect[largest]) {
            largest = r;
        }
        if (largest != i) {
            swap(vect[largest], vect[i]);
            shift_down(largest);
        }
    }

public:
    IntMaxHeap() {
        this->_size = 0;
        this->vect.push_back(0);
    }

    bool empty() {
        return _size==0;
    }
    int size() {
        return _size;
    }
    int top() {
        return vect[1];
    }
    void push(int value);
    void pop();
    void print();
};

void IntMaxHeap::push(int value) {
    if (_size + 1 >= (int)vect.size()) {
        vect.push_back(0);
    }
    _size++;
    vect[_size] = value;
    shift_up(_size);
}

void IntMaxHeap::pop() {
    swap(vect[1], vect[_size--]);
    shift_down(1);
}

void IntMaxHeap::print() {
    if (this->empty()) {
        cout << "empty heap" << endl;
        return;
    }

    cout << "[";
    for(int i=1; i<_size; i++) {
        cout << vect[i] << ", ";
    }
    cout << vect[_size] << "]" << endl;
}

int main() {
    IntMaxHeap heap;
    heap.push(1);
    heap.push(3);
    heap.push(7);
    heap.push(10);
    heap.push(5);
    heap.print();
    heap.pop();
    heap.print();
    heap.pop();
    heap.print();
}