# include <iostream>
using namespace std;

int n;
float x;
char c;
bool b;
string s; // from std

int main(){
    n = 5;
    x = 6.0;
    c = 'x';
    b = true;
    s = "hello!";
    cout << "n = " << n << '\n'; // '\n' is the "new line" character
    cout << "x = " + to_string(x) << '\n';
    cout << "b = " << b << '\n';
    cout << "c = " << c << '\n';
    cout << "s = " + s << '\n';
    return 0;
}