# include <iostream>
using namespace std;

// declaring functions
void no_in_no_out(){
    cout << "no_in_no_out" << '\n';
}
float no_in_yes_out(){
    cout << "no_in_yes_out" << '\n';
    float x = 3.14;
    return x;
}
float yes_in_yes_out(int x){
    cout << "yes_in_yes_out" << '\n';
    float y = (float)x/2.; // casting: while x is an integer, (float)x is the float version of it, i.e. 7.
    return y;
}

// main program
int main(){
    // calling functions
    no_in_no_out();
    float y = no_in_yes_out();
    cout << "returning y = " << y << "\n\n";
    // cout << "returning y = " << no_in_yes_out() << "\n\n";
    float z = yes_in_yes_out(7);
    cout << "returning z = " << z << '\n';
    return 0;
}