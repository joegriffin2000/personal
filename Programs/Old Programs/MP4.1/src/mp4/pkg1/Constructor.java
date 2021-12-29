package mp4.pkg1;                   //Joe Griffin
                                    //Intro to Java
import java.awt.Color;              //Mr. Ritter
import javax.swing.JComponent;      //May 9, 2018
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Rectangle;
import java.awt.geom.Ellipse2D;

public class Constructor 
{
    private int x;
    private int y;                  //Initialized Variables
    private int dx;
    private int dy;
    private int radius;
    private Color FillColor;
    private Ellipse2D.Double Circle;
    
    public Constructor()
    {
    x = 0;
    y = 0;                          // Default Constructor
    radius = 0;
    FillColor = Color.RED;
    Circle = new Ellipse2D.Double();
    }
    
    //parameter
    public Constructor(int inx, int iny, int inradius, Color inColor)
    {
    x = inx;
    y = iny;
    radius = inradius;              // Parameter Constructor
    FillColor = inColor;
    Circle = new Ellipse2D.Double(x, y, radius, radius);
    }
    
    //Accessors
    public int getx()
    {
    return (x);
    }
    
    public int gety()
    {
    return (y);
    }
    
    public int getradius()
    {
    return (radius);
    }
    
    public Color getFillColor()
    {
    return (FillColor);
    }
    
    public Ellipse2D.Double getCircle()
    {
    return (Circle);
    }
    
    
    //Mutators
    public void setx(int inx)
    {
    x = inx;
    Circle.setFrame(x,y,radius,radius);
    }
    
    public void sety(int iny)
    {
    y = iny;
    Circle.setFrame(x,y,radius,radius);
    }
    
    public void setradius(int inradius)
    {
    radius = inradius;
    Circle.setFrame(x,y,radius,radius);
    }
    
    public void setFillColor(Color inColor)
    {
    FillColor = inColor;
    }
    
}
