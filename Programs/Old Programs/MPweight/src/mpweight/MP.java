package mpweight;

import java.util.Scanner;

public class MP {

    public static void main(String[] args) 
    {
        Scanner in = new Scanner (System.in);
        
        Constructor weight = new Constructor();
        
        System.out.print("Enter Your Weight: ");
        int freeweight = in.nextInt();
       
        
        double mercury = freeweight * .38;
        System.out.println("You're Weight on Mercury is ");
        System.out.print(mercury);
        
    }
    
}
