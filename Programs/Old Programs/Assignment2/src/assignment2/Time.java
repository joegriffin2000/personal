
package assignment2;

public class Time 
{
    //Initialization
     public int time;
     public int seconds;
     public double minutes;
     public double hours;
     public double days;
     
    //Default Constructor
    public Time()
    {
        time = 0;
        seconds = 0;
        minutes = 0;
        hours = 0;
        days = 0;
    }
    
     //Parameter Constructor
        public Time(int intime, int inseconds, double inminutes, double inhours, double indays)
    {
       time = intime;
       seconds = inseconds;
       minutes = inminutes;
       hours = inhours;
       days = indays;
    }
     
     
    //Accessors
    public int gettime()
    {
        return (time);
    }
    
    public int getseconds()
    {
        seconds = time;
        return (seconds);
    }
    
    public double getminutes()
    {
        minutes = time/60;
        return (minutes);
    }
    
    public double gethours()
    {
        hours = time/3600;
        return (hours);
    }
    
    public double getdays()
    {
        days = time/86400;
        return (days);
    }
    
    //Mutators
    public void settime(int intime)
    {
    time = intime;
    }
    
    public void setseconds(int inseconds)
    {
    seconds = inseconds;
    }
    
    public void setminutes(double inminutes)
    {
    minutes = inminutes;
    }
    
    public void sethours(double inhours)
    {
    hours = inhours;
    }
    
    public void setdays(double indays)
    {
    days = indays;
    }
}
