# include <iostream>
# include "MyClass.h" // import class code
using namespace std;

int main(){
    cout << "Initializing class object" << endl;
    MyClass *c = new MyClass();
    c->my_public_function(); // "->"" is like a "." but it invokes a function or variable from a pointer object
    cout << "observing public variable from outside: " << c->my_public_int << endl;
    // the following would cause an error:
    // c->my_private_function();
    return 0;
}

// CAUTION: all files have to be compiled:
// g++ -o 05_classes 05_classes.cpp MyClass.cpp 