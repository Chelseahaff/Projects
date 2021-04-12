var num = 2;    //declaring a variable
document.write(num);   //printing

var x = 1;        //conditional statement
var y = 3;
if ( x > y) {
	document.write("true")
} else { document.write("false") }

var students = ["peter" , " sam", "shelby" , "chelsea" , "amelia"];  //creating an array
students[0]  //peter is at index 0

var i;   //declaring a variable without value
for(i=1;i<10;i++){    //creating a for loop that loops 10 times with counter
	document.write("Not Today");
}

var i = 1;
do{    //creating a do while loop
	document.write("Not today!";        
	i=i+1;      //increments
}
while(i<=10);   //while condition

function add(num1, num2){   //declaring a new function that takes parameters
	var result = num1+num2;    // declaring a function that adds parameters
	document.write(result);
}
add(2,3);    //calling function

function localFunction(){       //defines new local function
	var localVar=50;     //declares the value of local variable
	console.log(localVar);    //prints variable
}
localFunction();             //will call function to print the variable

var globalVar=5;        //declaring a global variable

function globalFunction(){     //declaring a global function
	console.log(globalVar);          
}
console.log(globalVar);    //print global variable

newFunction();               //calls function to print global variable again
 
