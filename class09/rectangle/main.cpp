#include<iostream>
#include"Rectangle.h"

using namespace std;

int main() {
	Rectangle r = Rectangle(45,37);
	Rectangle* p = new Rectangle(45, 37);
	Rectangle* x[10];
	for (int i = 0; i < 10; i++) {
		x[i] = new Rectangle(1+rand()%10, 1+rand()%10);
		//cout << x[i].get_area()<< endl;
	}
	/*cout << "sizeof(r) = " << sizeof(r) << endl;
	cout << "sizeof(p) = " << sizeof(p) << endl;*/
	return 0;
}