package mp4.pkg1;                       //Joe Griffin
                                        //Intro to Java
import java.awt.Color;                  //Mr. Ritter
import java.util.Random;                //May 9, 2018
import java.awt.geom.Ellipse2D;
import java.awt.BorderLayout;
import java.util.Scanner;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JButton;           //LOOK AT ALL THESE IMPORTS LIKE OH MY GOD
import javax.swing.JMenuBar;
import javax.swing.JMenu;
import javax.swing.JMenuItem;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.Timer;
import java.awt.event.MouseListener;
import java.awt.event.MouseEvent;
import javax.swing.JOptionPane;
import java.lang.Math;

public class MP41 
{
    public static void main(String[] args) 
    {
        Color FillColor = Color.RED;
        int width = 750;
        int height = 700;
        int x = 50;
        int y = 50;
        int radius = 50;
        
        Scanner in = new Scanner(System.in);
        JFrame frame = new JFrame();            //frame 
        JPanel panel = new JPanel();            //panel for buttons
        JMenuBar menubar = new JMenuBar();      //menu bar
        
        frame.setSize(width,height);
        frame.setLayout(new BorderLayout());
        
        JMenu file = new JMenu("File");
        JMenu edit = new JMenu("Edit");      //menus menu bar
        JMenu help = new JMenu("Help");
        menubar.add(file);
        menubar.add(edit);       //menus added to menubar
        menubar.add(help);
        
        JMenuItem exit = new JMenuItem("Exit");     //menu items for the file menu
        file.add(exit);                             //file menu items added
        
        JMenuItem red = new JMenuItem("Red");
        JMenuItem blue = new JMenuItem("Blue");     //menu items for the edit menu
        JMenuItem green = new JMenuItem("Green");
        JMenuItem random = new JMenuItem("Random");
        edit.add(red);
        edit.add(blue);             //edit menu items added
        edit.add(green);   
        edit.add(random);
        
        JMenuItem about = new JMenuItem("About");       //menu items for the help menu
        JMenuItem helpme = new JMenuItem("Help");
        help.add(about);
        help.add(helpme);                           //  help menu items added
        
        JButton buttonred = new JButton(" Red ");
        JButton buttonblue = new JButton(" Blue ");
        JButton buttongreen = new JButton(" Green ");       //all my panel buttons created
        JButton buttonrandom = new JButton(" Random ");
        JButton buttonupspeed = new JButton(" Speed Up ");
        JButton buttondownspeed = new JButton(" Speed Down ");
        
        panel.add(buttonred);                   
        panel.add(buttonblue);
        panel.add(buttongreen);
        panel.add(buttonrandom);        //all my buttons added
        panel.add(buttonupspeed);
        panel.add(buttondownspeed);
        
        Constructor circle = new Constructor(x, y, radius, FillColor);
        Paint paint = new Paint(circle, frame);
        
        class RANDOM implements ActionListener
            {
                public void actionPerformed(ActionEvent event)
                {
                Random generator = new Random();
                int rand1 = generator.nextInt(255);
                int rand2 = generator.nextInt(255);
                int rand3 = generator.nextInt(255);
                
                Color randcolor = new Color(rand1,rand2,rand3);
                
                circle.setFillColor(randcolor);
                paint.rePaint();
                }
            }
        ActionListener randomlistener = new RANDOM();
        Timer randomtimer = new Timer(400,randomlistener);  //random timer
        
        class Movement implements ActionListener    //calling the move method from my paint class
            {
                public void actionPerformed(ActionEvent event)
                {
                paint.Move();
                }
            }
        ActionListener movement = new Movement();
        Timer moving = new Timer(20,movement);      //movement timer
        moving.start();
        
            class ClickRED implements ActionListener
            {
                public void actionPerformed(ActionEvent event)
                {
                randomtimer.stop();
                circle.setFillColor(Color.RED);
                paint.rePaint();
                }
            }
        ActionListener redlistener = new ClickRED();
        buttonred.addActionListener(redlistener);       //red button on the panel ssigned to this listener
        red.addActionListener(redlistener);             //red button in the menu assigned to this listener
        
            class ClickBLUE implements ActionListener
            {
                public void actionPerformed(ActionEvent event)
                {
                randomtimer.stop();
                circle.setFillColor(Color.BLUE);
                paint.rePaint();
                }
            }
        ActionListener bluelistener = new ClickBLUE();
        buttonblue.addActionListener(bluelistener);     //blue button on the panel assigned to this listener
        blue.addActionListener(bluelistener);           //blue button in the menu assigned to this listener
        
            class ClickGREEN implements ActionListener
            {
                public void actionPerformed(ActionEvent event)
                {
                randomtimer.stop();
                circle.setFillColor(Color.GREEN);
                paint.rePaint();
                }
            }
        ActionListener greenlistener = new ClickGREEN();
        buttongreen.addActionListener(greenlistener);   //green button on the panel assigned to this listener
        green.addActionListener(greenlistener);         //green button in the menu assigned to this listener
        
        class ClickRANDOM implements ActionListener     //random button starting it's timer
            {
                public void actionPerformed(ActionEvent event)
                {
                randomtimer.start();
                }
            }
        ActionListener randombutton = new ClickRANDOM();
        buttonrandom.addActionListener(randombutton);   //random button on the panel assigned to this listener
        random.addActionListener(randombutton);         //random button in the menu assigned to this listener
        
        class ClickUPSPEED implements ActionListener    //The action for the speed up button
            {
                public void actionPerformed(ActionEvent event)
                {
                    if (paint.getdx() != 64 && paint.getdx() != -64)    //increases the speed by 2
                    {
                    paint.setdx(paint.getdx()*2);
                    paint.setdy(paint.getdy()*2);
                    }
                }
            }
        ActionListener uplistener = new ClickUPSPEED();
        buttonupspeed.addActionListener(uplistener);
        
        class ClickDOWNSPEED implements ActionListener  //The action for the speed down button
            {
                public void actionPerformed(ActionEvent event)
                {
                    if (paint.getdx() != 1 && paint.getdx() != -1) //decreases the speed by half
                    {
                    paint.setdx(paint.getdx()/2);
                    paint.setdy(paint.getdy()/2);
                    }
                }
            }
        ActionListener downlistener = new ClickDOWNSPEED();
        buttondownspeed.addActionListener(downlistener);
        
        
        class MousePressListener implements MouseListener  //mouse listener
        {
            private int x1;
            private int x2;
            private int y1;
            private int y2;
            private int Cradius;
            private int Eradius;
            
            public void mousePressed(MouseEvent event) //When you first press the button
            {
                moving.stop();
                x1 = event.getX();
                y1 = event.getY();
                Cradius = event.getX();
                
                circle.setx(x1-circle.getradius()/2);
                circle.sety(y1-circle.getradius());
                
                
            }
            public void mouseReleased(MouseEvent event) //when you release the button and it draws the new circle
            {
                Eradius = event.getX();
                
                if (Eradius > Cradius){
                circle.setradius(Eradius-Cradius);}             
                
                if (Cradius > Eradius){
                circle.setradius(Cradius-Eradius);}
                
                moving.start(); 
            }
            public void mouseClicked(MouseEvent event){}    //do nothing methods
            public void mouseEntered(MouseEvent event){}
            public void mouseExited(MouseEvent event){}
        }
        MouseListener mouse = new MousePressListener();
        frame.addMouseListener(mouse);
        
        class Exit implements ActionListener //exit class for the button
            {
                public void actionPerformed(ActionEvent event)
                {
                System.exit(0);
                }
            }
        ActionListener exitlistener = new Exit();
        exit.addActionListener(exitlistener);
        
        class ABOUT implements ActionListener   //the about pop up for the help menu
            {
                public void actionPerformed(ActionEvent event)
                {
                JOptionPane.showMessageDialog(null, "This is the Bouncing Ball Program created by Joe Griffin. This program was due May 9, 2018 for Mr. Ritter's Introduction to Java class.");
                }
            }
        ActionListener aboutlistener = new ABOUT();
        about.addActionListener(aboutlistener);
        
        class HELP implements ActionListener    //the help pop up for the help menu
            {
                public void actionPerformed(ActionEvent event)
                {
                JOptionPane.showMessageDialog(null, " Each button that has a color on it will change the ball to that color. The speed up and speed down buttons will increase and decrese the speed of the ball. Random will constantly change the ball color to different colors.");
                }
            }
        ActionListener helplistener = new HELP();
        helpme.addActionListener(helplistener);
        
        frame.setTitle("The Open Frame");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(panel, BorderLayout.SOUTH);           //all this stupid stuff
        frame.setJMenuBar(menubar);
        frame.add(paint);
        frame.setVisible(true);
    }
    
}