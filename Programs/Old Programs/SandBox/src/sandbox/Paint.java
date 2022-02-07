package sandbox;

import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.geom.Rectangle2D;
import java.awt.geom.Ellipse2D;
import java.util.Random;
import java.awt.Font;
import java.awt.BasicStroke;
import java.awt.Color;
import javax.swing.JComponent;
import javax.swing.JFrame;

public class Paint extends JComponent 
{
    private Constructor dice;
    private Numbers numbers;
    private JFrame frame;
    private String U;
    private String V;
    private String W;
    private String X;
    private String Y;
    private String Z;
    private Font Serif;
    private Ellipse2D.Double design;
    
    
    public Paint(Constructor indice, JFrame inFrame, Numbers innumbers)
    {
        dice = indice;
        frame = inFrame;
        numbers = innumbers;
    }
    
    public void paintComponent(Graphics g)
    {
        Graphics2D graphics = (Graphics2D) g;
        graphics.setColor(dice.getFillColor());
        Font F = new Font("Arial",Font.PLAIN,20);
        Font L = new Font("Arial",Font.BOLD,24);
        
       //Background
        Rectangle2D.Double Fresh = new Rectangle2D.Double(0,0,frame.getWidth(),frame.getHeight());
        Ellipse2D.Double design = new Ellipse2D.Double();
        Color background = new Color(255,255,216);
        Color circles = new Color(238,245,210);
        
        
       //Background
        graphics.setColor(background);
        graphics.draw(Fresh);
        graphics.fill(Fresh);
        
       //Method for making the design
        graphics.setColor(circles);
        int cry = 1;
        while(cry!=9)
        {
           Random generator = new Random();
           int x = generator.nextInt(frame.getWidth());
           int y = generator.nextInt(frame.getHeight());
           int width = generator.nextInt(frame.getWidth());
           int height = generator.nextInt(frame.getHeight());
           
           design = new Ellipse2D.Double(x,y,width,height);
           graphics.draw(design);
           graphics.fill(design);
           
           if (x-width-250<0)
           { width -=250; }
           if (width-x-250<0)
           { x -=250; }
           
           cry++;
        }
        
       //Original Roll
        Roll();
        
       //Drawing Dice
        graphics.setColor(dice.getFillColor());
        graphics.setStroke(new BasicStroke(6.0f));
        graphics.draw(dice.getu());
        graphics.draw(dice.getv());
        graphics.draw(dice.getw());
        graphics.draw(dice.getx());
        graphics.draw(dice.gety());
        graphics.draw(dice.getz());
        
       //Dice Labels
        graphics.setFont(L);
        graphics.drawString("D4", dice.x*1/7, dice.y/2);
        graphics.drawString("D6", dice.x*2/7, dice.y/2);
        graphics.drawString("D8", dice.x*3/7, dice.y/2);
        graphics.drawString("D10", dice.x*4/7, dice.y/2);
        graphics.drawString("D12", dice.x*5/7, dice.y/2);
        graphics.drawString("D20", dice.x*6/7, dice.y/2);
        
       //Dice Fill Color
        graphics.setColor(Color.WHITE);
        graphics.fill(dice.getu());
        graphics.fill(dice.getv());
        graphics.fill(dice.getw());
        graphics.fill(dice.getx());
        graphics.fill(dice.gety());
        graphics.fill(dice.getz());
        
       //Printing Rolls
        graphics.setFont(F);
        graphics.setColor(Color.BLACK);
        graphics.drawString(U, frame.getWidth()*1/7, dice.y+43);
        graphics.drawString(V, frame.getWidth()*2/7, dice.y+43);
        graphics.drawString(W, frame.getWidth()*3/7, dice.y+43);
        graphics.drawString(X, frame.getWidth()*4/7, dice.y+43);
        graphics.drawString(Y, frame.getWidth()*5/7, dice.y+43);
        graphics.drawString(Z, frame.getWidth()*6/7, dice.y+43);
       
    }
    
    public void rePaint ()
    { 
        repaint(); 
    }
    
    public void Roll()
    {
        Random generator = new Random();
        int u = 1+ generator.nextInt(4);
        int v = 1+ generator.nextInt(6);
        int w = 1+ generator.nextInt(8);
        int x = 1+ generator.nextInt(10);
        int y = 1+ generator.nextInt(12);
        int z = 1+ generator.nextInt(20);
        U=String.valueOf(u);
        V=String.valueOf(v);
        W=String.valueOf(w);
        X=String.valueOf(x);
        Y=String.valueOf(y);
        Z=String.valueOf(z);
    } 
    
}

