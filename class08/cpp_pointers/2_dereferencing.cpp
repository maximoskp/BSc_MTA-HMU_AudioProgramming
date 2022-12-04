# include <iostream>
using namespace std;

int main(){
    int x = 5;
    cout << "value of x is: " << x << endl;
    // getting address via a pointer
    int *pointer_to_x = &x;
    // value of a pointer is the address of a variable
    cout << "value of pointer_to_x (address of x): " << pointer_to_x << endl;
    // dereferencing pointer, means accessing the value it points to
    cout << "content of pointer_to_x (actual value of x): " << *pointer_to_x << endl;
}