
package mpweight;

public class Constructor 
{
    private int weight;
    private double mercury;
    private double venus; 
    private double mars;
    private double jupiter;
    private double saturn;
    private double uranus;
    private double neptune;
    
    //Set Weight to Zero
    public Constructor()
    {
    weight = 0;
    mercury = 0;
    venus = 0;
    mars = 0;
    jupiter = 0;
    saturn = 0;
    uranus = 0;
    neptune = 0;
    }
    
    //Set New Variable for Weight
    public Constructor(int freeweight, int freemercury, int freevenus, int freemars, int freejupiter, int freesaturn, int freeuranus, int freeneptune)
    {
    weight = freeweight;
    mercury = freemercury;
    venus = freevenus;
    mars = freemars;
    jupiter = freejupiter;
    saturn = freesaturn;
    uranus = freeuranus;
    neptune = freeneptune;
    }
    
    public int Getfreeweight()
    {   return (weight);    }
    
    public double Getfreemercury()
    {   return (mercury);   }
    
    public double Getvenus()
    {   return (venus);    }
    
    public double Getfreemars()
    {   return (mars);    }
    
    public double Getjupiter()
    {   return (jupiter);    }
    
    public double Getsaturn()
    {   return (saturn);    }
    
    public double Geturanus()
    {   return (uranus);    }
    
    public double Getneptune()
    {   return (neptune);    }
       
   //Mutators but maybe not working
   public void setWeight (int freeweight)
   {    weight = freeweight;    }
   
   public void setmercury (int freemercury)
   {    mercury = freemercury;    }
   
   public void setvenus (int freevenus)
   {    venus = freevenus;    }
   
   public void setmars (int freemars)
   {    mars = freemars;    }
    
   public void setjupiter (int freejupiter)
   {    jupiter = freejupiter;    }
   
   public void setsaturn (int freesaturn)
   {    saturn = freesaturn;    }
   
   public void seturanus (int freeuranus)
   {    uranus = freeuranus;    }
   
   public void setneptune (int freeneptune)
   {    neptune = freeneptune;    }   
}