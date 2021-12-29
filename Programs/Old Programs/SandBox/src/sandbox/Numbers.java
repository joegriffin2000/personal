package sandbox;

import java.awt.Color;              
import javax.swing.JComponent;     
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.geom.Rectangle2D;

public class Numbers 
{
    private int width;
    private int height;
    private int u;
    private int v;
    private int w;
    private int x;
    private int y;
    private int z;
    
    public Numbers()
    {
    u = 0;
    v = 0;
    w = 0;
    x = 0;
    y = 0;
    z = 0;
    }
    
    //parameter
    public Numbers(int inu, int inv, int inw, int inx, int iny, int inz, int inwidth, int inheight)
    {
    int u = inu;
    int v = inv;
    int w = inw;
    int x = inx;
    int y = iny;
    int z = inz;
    }
    
    //Accessors
    public int getu()
    { return (u); }
    public int getv()
    { return (v); }
    public int getw()
    { return (w); }
    public int getx()
    { return (x); }
    public int gety()
    { return (y); }
    public int getz()
    { return (z); }
    
    
    //Mutators
    
    public void setu(int inu)
    { u = inu; }
    public void setv(int inv)
    { v = inv; }
    public void setw(int inw)
    { w = inw; }
    public void setx(int inx)
    { x = inx; }
    public void sety(int iny)
    { y = iny; }
    public void setz(int inz)
    { z = inz; }
    
}
