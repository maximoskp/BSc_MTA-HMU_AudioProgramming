# include <iostream>
using namespace std;

int main(){
    // begin with a float with value 0.5
    float x = 0.5;
    // make a pointer to it
    float *p = &x;
    // create a for loop to fill in the next 3 addresses with increment 0.1
    for (int i=1; i<4; i++){
        *(p+i) = *(p+i-1) + 0.1;
    }
    // create an array that shows to the point of the initial float
    float *a = p;
    // check the third item (index 2) of the array (should be 0.7)
    cout << "a[2]: " << a[2] << endl;
}