package assignment2;            //Joe Griffin
import java.util.Scanner;       //April 14,2018
import java.lang.Math;          //Assignment 2
public class Assignment2        //Mr Ritter
{

    public static void main(String[] args) 
    {
        Scanner Scanner = new Scanner(System.in);
        
        int x = 0;
        
        do
        {
        System.out.println("");
        System.out.println(" Part 1: Investment Calculator  =  1 ");
        System.out.println(" Part 2: Multiplication Range   =  2 ");
        System.out.println(" Part 3: The Upper Prime List   =  3 ");
        System.out.println(" Part 4: Time Conversion        =  4 ");
        System.out.println("");
        System.out.println(" Exit The Program               =  5 ");
        System.out.println("");
        System.out.print(" |====|: ");
        int usermenu = Scanner.nextInt();
        System.out.println("");
        
        for (int space = 0; space <14; space++ )     //Clear Page Input
            {
                System.out.println("");
            }
        
        if (usermenu == 1)                              //Initial Investment
            {
            
            System.out.print(" Initial Investment: ");
            int inv = Scanner.nextInt();
            System.out.print(" Number of Years: ");
            int years = Scanner.nextInt();
            System.out.print(" Start Rate: ");
            int Irate = Scanner.nextInt();
            System.out.print(" End Rate: ");
            int Erate = Scanner.nextInt();
            System.out.println(" __________________________________________________________");
            System.out.println("  ");
            double g = (int)Irate;
            
            while (g <= Erate)
                {      
                System.out.print(" "+g);
                g = g/100;

                double product = 0;
                product = inv;
                for (int y=0; y<years; y++)
                    {
                    double wow1 = (1+(g/365));              //calculating investment here
                    double wow2 = 365*y;
                    product = product* Math.pow(wow1,wow2);
                    
                    product = product*100;
                    product = Math.round(product);      //me figuring out how to get a good rounded number for printing
                    product = product/100;
                    System.out.print("  $"+ product);
                    };
                    
                System.out.println(" "); 
                
                g*=100;
                g++;
                };
            System.out.println(" __________________________________________________________");
            System.out.println("");
        }
        else if (usermenu == 2)                         // Multiplication Table
            {
                
            int product = 0;
        
            System.out.print(" First Number: ");
            int w = Scanner.nextInt();
            System.out.print(" Second Number: ");
            int z = Scanner.nextInt();

            System.out.println(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
            System.out.print("  ");
            int s =w;
            
            while(s<z)
                {
                System.out.print(" "+ s);
                s++;
                }
            System.out.println("");
            
            while (s<z)
                {
                System.out.print("~~");
                s++;
                }
            
            for (int a=w; a <= z; a++)
                {
                System.out.print(" "+a+"|");
                for(int y=w; y <= z; y++)
                    {
                  
                    product = a * y;
                    System.out.print(" "+ product +" ");
                    }

                System.out.println("");
                }

            }
        else if (usermenu == 3)                             // The Upper Prime List
            {
            PrimeGenerator prime = new PrimeGenerator();

            System.out.print(" Upper Prime: ");
            prime.upperprime = Scanner.nextInt();
            System.out.println(" ");
            
            boolean isitprime = prime.getisprime();
            String list = prime.getprimelist();
            
            System.out.print(" " + prime.getupperprime());
            if (isitprime == false)
            { 
                System.out.println(" is Not Prime");
            }
            else
            { 
                System.out.println(" is Prime");
            }
            System.out.println(list);
        }       
        
        else if (usermenu == 4)                             // Time Conversion
            {
            
            Time time = new Time();
            System.out.print("Number of Seconds: ");
            time.time = Scanner.nextInt();
            System.out.println(" ");
            System.out.println(" ");
            int seconds = time.getseconds();
            double minutes = time.getminutes();
            double hours = time.gethours();
            double days = time.getdays();
            
            System.out.println("———————————————————————–");
            
            System.out.println(" Seconds: " + seconds);
            System.out.println(" Minutes: " + Math.rint(minutes));
            System.out.println(" Hours: " + Math.rint(hours));
            System.out.println(" Days: " + Math.rint(days));
            }
        
        else if ( usermenu == 5)            //Exit Program
        {break;}
        
        else                                                 // Non Recognized Input
            {
            System.out.println(" " + usermenu + " is Not a Recognized Input");
            System.out.println("");
            }
        
        System.out.println("  ");
        System.out.println(" Press Any Button and Enter to Continue ");
        String enter = Scanner.next();
        
        for (int space = 0; space <14; space++ )     //Clear Page Input
            {
            System.out.println("");
            }
        
        x++;
        } 
        while (x < 100);      
    }
    
}
