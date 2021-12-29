#include <stdio.h>

int main( int argc, char* argv[] )
{
   int twenties = 0 ;
	int tens = 0 ;
	int fives = 0 ;
	int ones = 0 ;
	
	int user	;
	printf( "Enter a dollar amount => ") ;
	scanf("%d",&user);

	while (user >= 20)
	{
		twenties += 1;
		user -= 20;
		}
	while (user >= 10)
	{
		tens += 1;
		user -= 10;
		}
	while (user >= 5)
	{
		fives += 1;
		user -= 5;
		}
	while (user > 0)
	{
		ones += 1;
		user -= 1;
		}

   printf( "$20 bills: %d\n",twenties ) ;
	printf( "$10 bills: %d\n",tens ) ;
	printf( "$ 5 bills: %d\n",fives ) ;
	printf( "$ 1 bills: %d\n",ones ) ;

   return 0 ;
}
