#include <stdio.h>

int main( int argc, char* argv[] )
{	
	//Globals
   double tax = .07 ;
   double tip = .22 ;

	//Grabbing User Input (fragile)
   double user ;
   printf( "Enter a dollar amount. \n=> ") ;
   scanf("%lf",&user);

	//Calculating Tax & Tip
	tax = tax * user;
	tip = tip * user;

	//Displaying The Amount
	printf( "Subtotal: %.2lf\n",user) ;
   printf( "Tax: %.2lf\n",tax ) ;
	printf( "Tip: %.2lf\n",tip ) ;
	double total = user + tax + tip;
	printf("\n"); //Extra Line For Clarity 
	printf( "Total: %.2lf\n",total); //Amount To Be Paid!!!

   return 0 ;
}
