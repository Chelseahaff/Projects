Using system;
namespace CodeSample
{
	class Program
	{
		static void Main(string[] args)
		{
			int A;   //declare an int variable
		}
	}
}

using system;
namespace CodeSample
{
	class Program
	{
		static void Main(string [] args)
		{
			double A;        //declare a decimal variable 
		}
	}
}

using system;
namespace CodeSample
{
	class Program
	{
		static void Main(string [] args)
		{
			double A = 1.2;
			double B = -10.62;       //declaring decimals
			double C = 0;
		}	
	}
}

using system;
namespace CodeSample
{
	class program
	{
		static void main(string[] arg)
		{
			string A;                  //delare a string
		}
	}
}

using system;
namespace CodeSample
{
	class Program
	{
		static void Main(string[] args)
		{
			int A = 10;
			double B = 0;
			b= A + 10;    //addition 
		}
	}
}

int c=5;          
c++;         //increaase c by 1

int a = 10;
a--;        //decrease by 1

using system;

namespace consoleapp
{
	class program
	{
		static void main (string [] arg)
		{
			char x = 'a';           //declaring x as char 
			int i = (int)x;           //delcaring i as int and converting x to int
			console.WriteLine(i);       //printing i
		}
	}
}


using system;
namespace ConsoleApp
{
	class program
	{
		static void main(string [] args)
		{
			string name = 'john';
			string surname = 'doe';
			string fullname = name + " " + surname;      //adding strings together
			console.writeline(fullname);    // john doe
		}
	}
}


using system;

namespace ConsoleApp
{
	class program
	{
		static void main (string [] args)
		{
			string word= "friend";
			char character = word[0];    //using the string as an array
			
			console.writeline(character);
		}
	}
}

int a = 58;
string sentence = "a equals" + a.ToString():     //converting a to a string format
console.writeline(sentence);


using system;

namespace ConsoleApp
{
	class program
	{
		static void main (string []0 args)
		{
			string a;
			a = console.readline();
		}
	}
}

using system;
namespace consoleapp
{
	class program
	{
		static void main (string [] args)
		{
			double a;
			a= double.parse(console.readline());   //caught input
			console.writeline(a);       //turned into output
		}
	}
}


int A = 15;
int B = 15;
int C = 20;
if( A== B && C > B){
	console.writeline("A & B are equal, and C is greater than B");
}

for(int 1= 0; i<10; 1++)  //for loop
{
	for(int j = 0; j<5, j++)  //embedded for loop
	{
		//task to be repeated
	}
}

int a = 5;
while(a<= 25)   //while loop
{
	a=a+5;    //in increments of 5
	console.writeline(a);   //output a 
}

		
using system;
namespace consoleapp
{
	class program
	{
		static void main (string[] arg)
		{
			Console.writeline("How many students attended class today:";
				int c = int.Parse(Console.ReadLine());
				string[] students = new string[c];  //create array
				for(int i = 0; i < c ; i++)
				{
					console.writeline("Name of student:");
					student[i] = Console.ReadLine();
				}
				Console.WriteLine("Attended to school today:");
				for(int i = 0; i < c; i++)
				{
					console.writeline(students[i]0;
				}
		}
	}
}

//arrays

static void main(string[] args)
{
	int elements = 5;      //declare the number of elements
	double[] numbers = new double[elements];  //initialize array named numbers
	numbers[0] = 10;    //placing value in index 0
	numbers[1] = 25;
	numbers[2] = 27;
	for(int i = 0; i< elements; i ++)  
	{
		console.writeline(numbers[i]);  //printing array values   10 25 27
	}
}


static void main(string[] args)
{
	int elements = 3;
	string[] words = new string[elements];
	words[0]="Have";
	words[1]="some";
	words[2]="coffee";
	for(int i = 0; i < elements; i++) //iterating through each index space
	{
		console.writeline(words[i]);      //output have some coffee
	}
}

static void main(string[] args)
{ 
	int elements = 3;
	string[] words = new string[elements];
	words[0] = "Have";
	words[1] = "some";
	words[2] = "coffee";
	string WORD = words[2];      //assign str word value of index 2
	console.writeline(WORD);    //output coffee
}

//functions

class program
{
	static void main(string[] args)
	{
		int c = -5;
		int x = 2;
		int y = 8;
		while(c<= 250)
		{
			c = c + DoMath(x,y);
		}
	}
	static int DoMath(int a, int b)
	{
		int variable = 52;
		int variable1 = a + b + variable;
		variable1 = variable1 * 2;
		return variable;
	}
}

class program
{ 
	static void main(string[] arg)
	{ 
		int c = -5;
		int x = 2;
		int y = 8;
		while(c <= 250)
		{
			c= c + DoMath(x,y)
			for(int i = 5; i < 8; i++)
			{
				c= c + DoMath(x,y);
			}
		}
	}
	static int DoMath(int a, int b)
	{
		int variable= 52;
		int variable1 = a + b + variable;
		variable1 = variable1 * 2;
		return variable;
	}
}



	


	
	
				


