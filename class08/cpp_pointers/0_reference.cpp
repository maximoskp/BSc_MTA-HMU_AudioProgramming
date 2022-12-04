# include <iostream>
using namespace std;

int main(){
    int x = 5;
    cout << "value of x is: " << x << endl;
    cout << "memory address of x: " << &x << endl;
    // getting address via a pointer
    int *pointer_to_x = &x;
    cout << "pointer to x: " << pointer_to_x << endl;
    cout << "------------------------------------" << endl;
    // pointers to other types
    double d = 3.14;
    cout << "value of d is: " << d << endl;
    cout << "memory address of s: " << &d << endl;
    // pointer is of the same type that it is pointing to
    double *pointer_to_d = &d;
    cout << "pointer to d: " << pointer_to_d << endl;
    cout << "------------------------------------" << endl;
}