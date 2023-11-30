# include <iostream>
using namespace std;

int main(){
    // for in c
    for ( int i=0 ; i<10 ; i++){ // i++ means i += 1 or i = i+1
        cout << i << endl;
    }
    int j = 0;
    for( ; j<5; j++){
        cout << "j: " << j << endl;
    }
    int k = 0;
    bool exit_loop = true;
    for( ; exit_loop; k++){
        cout << "k: " << k << endl;
        exit_loop = k < 100;
    }
}