package freetime;

import java.awt.Color;
import java.util.Scanner;

public class Freetime {

    public static void main(String[] args) 
    {
         Scanner in = new Scanner(System.in);
         
         System.out.println("");
         System.out.print(" Write Username: ");
         String name = in.next();
         System.out.println("");
         
         System.out.println(" Okay " +name+ ", Please input the values for the color"); //(every value will need to be a value from 1-255)
         System.out.println(" (Every value will need to be a value from 1-255)");
         System.out.print(" Value 1 : ");
         int x1 = in.nextInt();
         System.out.print(" Value 2 : ");
         int x2 = in.nextInt();
         System.out.print(" Value 3 : ");
         int x3 = in.nextInt();
         
         Color randcolor = new Color(x1,x2,x3);
    }
        
}
