// header (.h) files are used for declaration of variables and functions
// source (.cpp) files implement them

# include <iostream>
using namespace std;

// the following are precompiler commands
#ifndef MYCLASS_H
#define MYCLASS_H

class MyClass{
    private:
        // private variables and functions are not visible to the outside world
        int my_private_int;
        void my_private_function();

    public:
        // constructor and desctructor has to be public
        MyClass();
        MyClass(int x); // could have multiple constructors
        ~MyClass();

        // public variables and functions are visible to the outside world
        int my_public_int; // it is a good practice to have variables only as private
        void my_public_function();
};

#endif