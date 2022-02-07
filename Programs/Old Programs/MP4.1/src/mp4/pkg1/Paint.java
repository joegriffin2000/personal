package mp4.pkg1;                       //Joe Griffin
                                        //Intro to Java
import java.awt.Color;                  //Mr. Ritter
import javax.swing.JComponent;          //May 9, 2018
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Rectangle;
import java.awt.geom.Ellipse2D;
import javax.swing.JFrame;
import javax.swing.Timer;

public class Paint extends JComponent
{
    private Constructor circle;
    private JFrame frame;
    private int dx;             //Globalized Variables
    private int dy;
    
    public Paint(Constructor inCircle, JFrame inFrame)
    {
        circle = inCircle;
        frame = inFrame;
        dx = 4;                 //"default constructor" for variables
        dy = 4;
    }
    
    public void paintComponent(Graphics g)
    {
        Graphics2D graphics = (Graphics2D) g;
        
        graphics.setColor(circle.getFillColor());       //basic drawing of the circle
        graphics.fill(circle.getCircle());
        graphics.draw(circle.getCircle());
        
    }
    
    public void rePaint ()
    {
        repaint();          //Repaint method 
    }
    
    public void Move ()         //Bounds checking and moving method for the ball
    {
        if((circle.getx() + circle.getradius())>=frame.getWidth())
        {
            dx *= -1;
        }
        if((circle.gety() + circle.getradius())>=frame.getHeight()-60)
        {
            dy *= -1;
        }
        if((circle.getx())<=0)
        {
            dx *= -1;
        }
        if((circle.gety())<=0)
        {
            dy *= -1;
        }
        
        circle.setx(circle.getx()+dx);
        circle.sety(circle.gety()+dy);
        repaint();
    }
    
    
    //Extra Accessors & Extra Mutators for these values
    public int getdx ()
    {   
        return(dx);
    }
    public int getdy ()
    {   
        return(dy);
    }
    
    public void setdx (int indx)
    {   
        dx = indx;
    }
    public void setdy (int indy)
    {   
        dy = indy;
    }
}
