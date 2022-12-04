# include <iostream>
using namespace std;

int main(){
    int array_of_ints[3] = {11, 22, 33};
    cout << "access an element: " << array_of_ints[1] << endl;
    // actual value of variable
    cout << "value of variable representing the array: " << array_of_ints << endl;
    // pointer of first element of the array
    int *pointer_to_first = &array_of_ints[0];
    cout << "value of pointer to the first element   : " << pointer_to_first << endl;
    // modify element via array index:
    array_of_ints[2] = 42;
    cout << "modified via index: " << array_of_ints[2] << endl;
    // modify via variable-as-pointer
    *(array_of_ints + 2) = 43;
    cout << "modified via variable-as-pointer: " << array_of_ints[2] << endl;
    // modify via pointer
    *(pointer_to_first + 2) = 44;
    cout << "modified via pointer: " << array_of_ints[2] << endl;
    // modify via pointer-as-array
    pointer_to_first[2] = 45;
    cout << "modified via pointer-as-array: " << array_of_ints[2] << endl;
    // therefore, an array is a pointer to the first element
    // check next exercise for more...
}