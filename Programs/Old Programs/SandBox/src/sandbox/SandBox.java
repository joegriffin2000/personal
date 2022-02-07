package sandbox;

import java.util.Scanner;
import java.util.Random;
import java.awt.Font;
import java.awt.Color;
import java.awt.Graphics2D;
import java.lang.InterruptedException;
import java.awt.BorderLayout;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JButton;           
import javax.swing.JMenuBar;
import javax.swing.JMenu;
import javax.swing.JMenuItem;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.Timer;
import java.awt.event.MouseListener;
import java.awt.event.MouseEvent;
import javax.swing.JOptionPane;
import java.awt.geom.Rectangle2D;

public class SandBox 
{ 
    public String U;
    public String V;
    public String W;
    public String X;
    public String Y;
    public String Z;
    
    public static void main(String[] args)
    {
        Color FillColor = Color.RED;
        
        Scanner in = new Scanner(System.in);
        JFrame frame = new JFrame();             
        JPanel panel = new JPanel();            
        JMenuBar menubar = new JMenuBar();
        
        frame.setSize(800,600);
        frame.setLayout(new BorderLayout());
        
        JMenu file = new JMenu("File");
        JMenu edit = new JMenu("Edit");
        JMenu help = new JMenu("Help");
        menubar.add(file);
        menubar.add(edit);
        menubar.add(help);
        
        JMenuItem exit = new JMenuItem("Exit");
        file.add(exit);
        
        JMenuItem red = new JMenuItem("Red");
        JMenuItem blue = new JMenuItem("Blue");
        JMenuItem green = new JMenuItem("Green");
        JMenuItem reroll = new JMenuItem("Reroll");
        edit.add(reroll);
        edit.add(red);
        edit.add(blue);
        edit.add(green);
        
        JMenuItem helpme = new JMenuItem("Help");
        help.add(helpme);
        
        JButton rerollall = new JButton(" Reroll All ");
        panel.add(rerollall); 
        
        
        //PASSING VARIABLES
        Constructor dice = new Constructor(FillColor, frame);
        Numbers numbers = new Numbers();
        Paint paint = new Paint(dice, frame, numbers);
        
        
        class Exit implements ActionListener 
            {
                public void actionPerformed(ActionEvent event)
                {
                System.exit(0);
                }
            }
        ActionListener exitlistener = new Exit();
        exit.addActionListener(exitlistener);
        
        class HELP implements ActionListener    //the help pop up for the help menu
            {
                public void actionPerformed(ActionEvent event)
                {
                JOptionPane.showMessageDialog(null, "This app is made with the purpose of presenting 6 different dice and with a roll for each.");
                }
            }
        ActionListener helplistener = new HELP();
        helpme.addActionListener(helplistener);
        
        class ClickRED implements ActionListener
            {
                public void actionPerformed(ActionEvent event)
                {
                dice.setFillColor(Color.RED);
                paint.rePaint();
                }
            }
        ActionListener redlistener = new ClickRED();
        red.addActionListener(redlistener); 
        
        class ClickBLUE implements ActionListener
            {
                public void actionPerformed(ActionEvent event)
                {
                dice.setFillColor(Color.BLUE);
                paint.rePaint();
                }
            }
        ActionListener bluelistener = new ClickBLUE();
        blue.addActionListener(bluelistener);
        
        class ClickGREEN implements ActionListener
            {
                public void actionPerformed(ActionEvent event)
                {
                dice.setFillColor(Color.GREEN);
                paint.rePaint();
                }
            }
        ActionListener greenlistener = new ClickGREEN();
        green.addActionListener(greenlistener);
        
        class Reroll implements ActionListener
            {
                public void actionPerformed(ActionEvent event)
                {
                paint.Roll();
                paint.rePaint();
                }
            }
        ActionListener rerolllistener = new Reroll();
        reroll.addActionListener(rerolllistener);
        rerollall.addActionListener(redlistener);
        
        
        frame.setTitle("The Rolling Dice");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(panel, BorderLayout.SOUTH);
        frame.setJMenuBar(menubar);
        frame.add(paint);
        frame.setVisible(true);
        
    } 
    
}