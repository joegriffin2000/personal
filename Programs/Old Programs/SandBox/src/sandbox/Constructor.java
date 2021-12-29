package sandbox;

import java.awt.Color;              
import javax.swing.JComponent;     
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.geom.Rectangle2D;
import java.util.Scanner;
import javax.swing.JFrame;

public class Constructor 
{
    
    private JFrame frame;
    private Rectangle2D.Double URectangle;
    private Rectangle2D.Double VRectangle;
    private Rectangle2D.Double WRectangle;
    private Rectangle2D.Double XRectangle;
    private Rectangle2D.Double YRectangle;
    private Rectangle2D.Double ZRectangle;
    private Color FillColor;
    
    public int x = 0;
    public int y = 0;
    public int CONwidth = 80;
    public int CONheight = 80;
    
    //Default Constructor
    public Constructor()
    {
    URectangle = new Rectangle2D.Double((double)frame.getWidth()*1/7,(double)frame.getHeight()/2,CONwidth,CONheight);
    VRectangle = new Rectangle2D.Double((double)frame.getWidth()*2/7,(double)frame.getHeight()/2,CONwidth,CONheight);
    WRectangle = new Rectangle2D.Double((double)frame.getWidth()*3/7,(double)frame.getHeight()/2,CONwidth,CONheight);
    XRectangle = new Rectangle2D.Double((double)frame.getWidth()*4/7,(double)frame.getHeight()/2,CONwidth,CONheight);
    YRectangle = new Rectangle2D.Double((double)frame.getWidth()*5/7,(double)frame.getHeight()/2,CONwidth,CONheight);
    ZRectangle = new Rectangle2D.Double((double)frame.getWidth()*6/7,(double)frame.getHeight()/2,CONwidth,CONheight);
    }
    
    
    //Parameter Contsructor
    public Constructor(Color inColor, JFrame inframe)
    {
    FillColor = inColor;       //frame.getWidth()
    frame = inframe;
    }
    
    
    //Accessors
    public Rectangle2D.Double getu()
    { return (URectangle); }
    public Rectangle2D.Double getv()
    { return (VRectangle); }
    public Rectangle2D.Double getw()
    { return (WRectangle); }
    public Rectangle2D.Double getx()
    { return (XRectangle); }
    public Rectangle2D.Double gety()
    { return (YRectangle); }
    public Rectangle2D.Double getz()
    { return (ZRectangle); }
    public Color getFillColor()
    { return (FillColor); }
    
    
    //Mutators
    
    public void setu()
    {URectangle = new Rectangle2D.Double(x,y,CONwidth,CONheight);}
    public void setv()
    {VRectangle = new Rectangle2D.Double(x,y,CONwidth,CONheight);}
    public void setw()
    {WRectangle = new Rectangle2D.Double(x,y,CONwidth,CONheight);}
    public void setx()
    {XRectangle = new Rectangle2D.Double(x,y,CONwidth,CONheight);}
    public void sety()
    {YRectangle = new Rectangle2D.Double(x,y,CONwidth,CONheight);}
    public void setz()
    {ZRectangle = new Rectangle2D.Double(x,y,CONwidth,CONheight);}
    public void setFillColor(Color inColor)
    { FillColor = inColor; }
    
    
    
}
