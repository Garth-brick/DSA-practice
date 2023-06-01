#include <iostream>
#include <vector>
using namespace std;

// array implementation of a generic max-heap in C++

template <typename T>
class Heap {
private:
    T dummy;
    vector<T> vect = {dummy}; 
    int _size;

    int parent(int i) {
        return i>>1;
    }
    int l_child(int i) {
        return i<<2;
    }
    int r_child(int i) {
        return (i<<2) + 1;
    }
    void shift_up(int i) {
        if (i > _size) return;
        if (i == 1) return;

        if (vect[parent(i)] < vect[i]) {
            swap(vect[parent(i)], vect[i]);
            shift_up(parent(i));
        }
    }
    void shift_down(int i) {
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
            swap(vect[i], vect[largest]);
            shift_down(largest);
        }
    }

public:
    Heap() {
        this->_size = 0;
    }

    bool empty() {
        return _size==0;
    }
    int size() {
        return _size;
    }
    T top() {
        return vect[1];
    }
    void push(T value) {
        if (_size+1 >= (int)vect.size()) {
            vect.push_back(dummy);
        }
        _size++;
        vect[_size] = value;
        shift_up(_size);
    }
    void pop() {
        swap(vect[1], vect[_size--]);
        shift_down(1);
    }
    void print() {
        if (_size == 0) {
            cout << "Empty heap" << endl;
            return;
        }
        cout << "[";
        for (int i=1; i<_size; i++) {
            cout << vect[i] << ", ";
        }
        cout << vect[_size] << "]" << endl;
    }
};


int main() {
    Heap<char> heap;
    heap.push('a');
    heap.push('d');
    heap.push('b');
    heap.print();
}