package assignment2;            //Joe Griffin      
import java.lang.Math;          //April 14,2018
                                //Assignment 2
public class PrimeGenerator     //Mr Ritter
{                               
    //Initialization
    public int upperprime;
    public String primelist;
    public boolean isprime;
    
    //Default Constructor
    public PrimeGenerator()
    {
        upperprime = 0;
        primelist = "";
        isprime = true;
    }
    
    //Parameter Constructor
    public PrimeGenerator(int inupperprime,String inprimelist)
    {
        upperprime = inupperprime;
        primelist = inprimelist;
        isprime = true;
    }
    
    //Accessors
    public int getupperprime()
    {
        return upperprime;
    }
    
    public String getprimelist()
    {
        primelist = " 2";
        for (int x=2; x<upperprime; x++)
        {
            int y=1;
            
            do
            { y++;
                if(Math.round(x%y) ==0)
                {
                break;
                }
                else
                {
                primelist += " " + x;
                break;
                } 
                
            }while (y<x);
        }
        return primelist;
    }
    
    public boolean getisprime()
    {
        if (upperprime == 2)
            {
            return (isprime);
            }
        for(int x=2;x<upperprime;x++)
        {
            if (upperprime%x == 0)
            {
                isprime = false;
                break;
            }
        }
        return isprime;
    }
    
    //Mutators
    public void setupperprime(int inupperprime)
    {
        upperprime = inupperprime;
    }
    
    public void setprimelist(String inprimelist)
    {
        primelist = inprimelist;
    }
    
    public void setisprime(boolean inisprime)
    {
        isprime = inisprime;
    }
}
