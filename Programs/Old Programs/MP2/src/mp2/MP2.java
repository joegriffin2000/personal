package mp2;

import java.io.File;
import java.io.FileNotFoundException; 
import java.io.PrintWriter; 
import java.util.Scanner;

public class MP2 
{
    
    public static void main(String[] args) throws FileNotFoundException
    {
    
    //PRIMING
    File inputFile = new File("mp2.txt");
    Scanner fileInput = new Scanner(inputFile);
    PrintWriter out = new  PrintWriter("mp2.out.txt");
    
    //MY NAME IS WHAT
    String name = fileInput.nextLine();
    System.out.println(name);
    
    //READING DECIMALS
    Double first = fileInput.nextDouble();
    Double second = fileInput.nextDouble();
    Double third = fileInput.nextDouble();
  
    //SUM 
    double sum = first + second + third;
    
    //PRINTING DECIMALS & SUM
    System.out.println(first);
    System.out.println(second);
    System.out.println(third);
    
    System.out.println("");
    System.out.print("Sum: ");
    System.out.println(sum);
    
    fileInput.close();
    
    out.println(name);
    out.println(first);
    out.println(second);
    out.println(third);
    out.println("");
    out.print("Sum:");
    out.println(sum);
    out.close();
    
    }
    
}
