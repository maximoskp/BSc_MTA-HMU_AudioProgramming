#include "MyClass.h" // header has to be included in source

MyClass::MyClass(){
    my_private_int = 5;
    my_public_int = 6;
}

MyClass::MyClass(int x){
    my_private_int = x;
    my_public_int = 6;
}

MyClass::~MyClass(){
    // can be left empty if there is nothing to destruct
}

void MyClass::my_public_function(){
    cout << "calling public function" << endl;
    cout << "public int: " << my_public_int << endl;
    cout << "private int: " << my_private_int << endl;
    cout << "private function can be called from within the class" << endl;
    my_private_function();
}

void MyClass::my_private_function(){
    cout << "cannot be called from outside the class..." << endl;
}