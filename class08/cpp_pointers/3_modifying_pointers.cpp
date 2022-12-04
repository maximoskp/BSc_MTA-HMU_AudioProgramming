# include <iostream>
using namespace std;

int main(){
    int x = 5;
    cout << "value of x is: " << x << endl;
    // getting address via a pointer
    int *pointer_to_x = &x;
    // modify the content of a pointer - modify the actual variable
    *pointer_to_x = *pointer_to_x+1;
    cout << "new value of x: " << x << endl;
}