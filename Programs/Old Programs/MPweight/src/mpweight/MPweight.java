package mpweight;

import java.util.Scanner;
        
public class MPweight {

    public static void main(String[] args) 
    {
        Scanner in = new Scanner (System.in);
       
        System.out.println("Hello! Welcome to My Earth-Planet Weight Conversion Program");
        System.out.println("In a couple seconds, I will ask for your weight, but first what is your name.");
        System.out.println("");
        System.out.print("=: ");
        String name = in.next();
        System.out.println("");        
        System.out.print("Excellent! Hello ");
        System.out.print(name);
        System.out.println("! Please Enter Your Weight");
        System.out.println(""); 
        System.out.print("=: ");
        int weight = in.nextInt();
        System.out.println(""); 


        System.out.println("Awesome! Here are your stats:");
        System.out.println("");
        
        Constructor getmercury = new Constructor ();
        System.out.print("Your weight on Mercury is ");
        System.out.println(weight * .38); 
 
        Constructor getvenus = new Constructor ();
        System.out.print("Your weight on Venus is ");
        System.out.println(weight * .91); 
        
        Constructor getmars = new Constructor ();
        System.out.print("Your weight on Mars is ");
        System.out.println(weight * .38);
        
        Constructor getjupiter = new Constructor ();
        System.out.print("Your weight on Jupiter is ");
        System.out.println(weight * 2.34); 
        
        Constructor getsaturn = new Constructor ();
        System.out.print("Your weight on Mercury is ");
        System.out.println(weight * 1.06); 
        
        Constructor geturanus = new Constructor ();
        System.out.print("Your weight on Uranus is ");
        System.out.println(weight * .92); 
        
        Constructor getneptune = new Constructor ();
        System.out.print("Your weight on Neptune is ");
        System.out.println(weight * 1.19); 
        
        
        //Conversions from https://www.livescience.com/33356-weight-on-planets-mars-moon.html
        
        //P.S I completely understand that this isnt the way the program was supposed to work. 
        //However, after failing at figuring out how to utilize the Constructors, Accessors, and Mutators 
        //in my Constructor.java in my tester, I decided to find out my own solution and include as much of what I 
        //could of the requirements. -Joe
    }

}
