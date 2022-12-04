# include <iostream>
using namespace std;

int main(){
    int x = 5;
    // getting address via a pointer
    int *pointer_to_x = &x;
    // pointers to other types
    double d = 3.14;
    // pointer is of the same type that it is pointing to
    double *pointer_to_d = &d;
    
    // moving to next address
    int *next_of_x = pointer_to_x + 1;
    cout << "pointer to x: " << pointer_to_x << endl;
    cout << "next address of x: " << pointer_to_x + 1 << endl;
    cout << "size of int: " << sizeof(int) << endl;
    cout << "size of x: " << sizeof(x) << endl;
    cout << "size of pointer_to_x: " << sizeof(pointer_to_x) << endl;
    cout << "------------------------------------" << endl;
    // moving to next address
    double *next_of_d = pointer_to_d + 1;
    cout << "pointer to d: " << pointer_to_d << endl;
    cout << "next address of d: " << pointer_to_d + 1 << endl;
    cout << "size of double: " << sizeof(double) << endl;
    cout << "size of d: " << sizeof(d) << endl;
    cout << "size of pointer_to_d: " << sizeof(pointer_to_d) << endl;
    return 0;
}