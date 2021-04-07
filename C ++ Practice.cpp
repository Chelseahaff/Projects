#include <iostream>
using namespace std;

int main() {
    cout<<"Hello!";
	return 0;
	}
	
int main() { 
	char grade= 'D';
	
	switch(grade) {
		case 'A';
			cout << "Excellent!" << end1;
			break;
		case 'B';
		case 'c';
			cout << "Well done!" << end1;
			break;
		case 'D';
			cout << "You Passed" << endl;
			break;
		case '';
			cout << "You failed" ,, end1;
			break;
		default;
			cout << " Invalid grade" << end1;
	}
	cout << "Your grade is " << grade << end1;
	
	return 0;
}

#include <iostream>
using namespace std;

int main() {
	for (int a= 10; a < 20; a= a+1){
	count << "value of a : "<<a<< end1;
	}
	return 0;
}

#include <iostream>
using namespace std;

	int main(); {
		int a = 10;
	
		while (a <20) {
			count << "value of a: - << a << end1;
			a ++;
		}
		return 0;
	}
		
#include <iostream>
using namespace std;

	int main () {
		int a = 10;
		
		do{
			count ,, " value of a: - << a << end1;
			a= a+1;
		} while (a < 20);
		
		return 0;
	}




	int i = 0;
	for(i=1; i <= 10; i + = 2) {
		cout << i<< "
		";
	}
	
	//factorial
	
int number, i = 1, factorial=1;
cout << "Enter a positive integer:";
cin >> number;
while ( i < number) {
	factorial *= i;
	++i;
}
cout << "Factorial of" << number<< "=" << factorial;

//array

int roll_no[5];
	roll_no[0]=45;
	roll_no[1]=89;
	roll_no[2]=16;
	roll_no[3]=10;
	roll_no[4]=23;
	
int roll_no[5]={45,89,16,10,23};
for(int i = 0, i<5; i++){
	cout << "Element at index" << i << "is" << roll_no[i] << end1;
}

//declaring a new variable

int greater( int num1, int num2) {
	int result;
	if (num1 > num2){
	result=num
	}
		else{
			result=num2;
		}
		return result;
}


int main() {
	int a = 100;
	int b = 200;
	int ret;
	ret = max(a,b);
	cout << " greater value of the two is:" << ret<<endi;
	return 0;
}


