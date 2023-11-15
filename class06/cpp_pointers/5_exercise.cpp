# include <iostream>
using namespace std;

int main(){
    // 1. begin with a float with value 0.5
    float x = 0.5;
    // 2. make a pointer to it
    float* p = &x;
    // 3. create a for loop to fill in the next 3 addresses with increment 0.1
    for (int i=1; i<=3; i++){
        *(p+i) = *(p+i-1) + 0.1;
    }
    // 4. create an array (another pointer) that shows to the pointer of the initial float
    float* a = p;
    // 5. check the third item (index 2) of the array (should be 0.7)
    cout << "a[2] =   " << a[2] << endl;
    cout << "p[2] =   " << p[2] << endl;
    cout << "*(a+2) = " << *(a+2) << endl;
    cout << "*(p+2) = " << *(p+2) << endl;
}