package mp3;                        //Joe Griffin
                                    //Mr. Ritter
import java.util.Scanner;           //MP3
import java.util.Random;            //Wednesday, March 6, 2018

public class MP3 {

    private static String Dead = "Nice try, and Thanks for playing my game! Run the program again for another try to win."; // Preset message for when people die
    private static String Win = "Good Job on Winning! Also thanks for playing my game. Run the program again if you want a different outcome."; //preset message for when people win
    
    public static void main(String[] args) 
    {
        
    Scanner in = new Scanner(System.in);//Reading keyboard input from here on out
    System.out.println("Dean Duncan has been infected by Vile X, an expiremental drug that alters his skin pigment and causes mad hallucinations.");
    System.out.println("Now is your time to escape as you find yourself currently in the Computer Lab, room S208");
    System.out.println("");
    System.out.println("Here are your choices:");                           //Providing path choices after telling them the situation they are in
    System.out.println("1. Leave the Computer Lab and go to Mewbourne");    //Path Choice 1   
    System.out.println("2. Search the Computer Lab for anything");          //Path Choice 2
    System.out.println("Enter number 1 or 2 for your decision");    
    System.out.print(":");
    int first = in.nextInt();                                               //Reading input saving it as variable first
    System.out.println("");
    System.out.println("");
    
    if(first == 1) //If statement for leaving The Computer Lab AKA Imminent doom
    {
        System.out.println("You leave the Computer Lab and go to the 2nd floor of the Oculus. ");
        System.out.println("Here are your choices:");                   //Providing path choices after telling them the situation they are in
        System.out.println("1. Go through into 2nd floor Mewbourne");   //Path Choice 1
        System.out.println("2. Go upstairs to 3rd floor Mewbourne");    //Path Choice 2
        System.out.println("Enter number 1 or 2 for your decision");    
        System.out.print(":");
        int second = in.nextInt();                                      //Reading input saving it as variable second
        System.out.println("");
        System.out.println("");
      
        if (second == 1) //If statement for going through into 2nd floor
        {
            System.out.println("The doors are locked. Do you want to go upstairs?");    //Providing path choices after telling them the situation they are in
            System.out.println("1. Accept your fate");                                  //Path Choice 1
            System.out.println("2. Go upstairs to 3rd floor Mewbourne");                //Path Choice 2
            System.out.print(":");
            int third = in.nextInt();                                                   //Reading input saving it as variable third
            System.out.println("");
            System.out.println("");
            
            if (third == 1) // If statement for accepting your fate
            {
                System.out.println("You accept your fate and let Dean Duncan kill you.");
                System.out.println("");
                System.out.println(Dead);           //This branch kills you so I put in my variable dead to read the message
            }
            else //Else statment for going upstairs to 3rd floor Mewbourne
            {
                System.out.println("The 3rd floor Mewbourne doors are also locked, if you only had some way to unlock them.");
                System.out.println("Dean Duncan catches up to you and kills you.");
                System.out.println("");
                System.out.println(Dead);           //Again this branch kills you so i put in the obligatory variable dead
            };
                
            }
        else //Else statment for going upstairs to 3rd floor Mewbourne
            {
                System.out.println("The 3rd floor Mewbourne doors are also locked, if you only had some way to unlock them.");
                System.out.println("Dean Duncan catches up to you and kills you.");
                System.out.println("");
                System.out.println(Dead);       //Again this branch kills you so I put in the obligatory variable dead
            }; 
            
    }
    else //Else statment for staying in the Computer Lab aka you have a chance to survive
    {
        System.out.println("You stay at the Computer Lab and search the room. You find a set of keys on Mr. Ritter's podium, they might be useful later.");
        System.out.println("Here are your choices:");                           //Providing path choices after telling them the situation they are in
        System.out.println("1. Leave the Computer Lab and go to Mewbourne");    //Choice Path 1
        System.out.println("2. Stay in the Computer Lab and hide");             //Choice Path 2
        System.out.println("Enter number 1 or 2 for your decision");            
        System.out.print(":");
        int search = in.nextInt();                                              //Reading input saving it as variable search
        System.out.println("");
        System.out.println("");
      
        if(search == 1) //If statement for leaving the Computer Lab and going to Mewbourne
        {
            System.out.println("You leave the Computer Lab and go to the 2nd floor of the Oculus. ");
            System.out.println("Here are your choices:");                       //Providing path choices after telling them the situation they are in
            System.out.println("1. Go through into 2nd floor Mewbourne");       //Choice Path 1
            System.out.println("2. Go upstairs to 3rd floor Mewbourne");        //Choice path 2
            System.out.println("Enter number 1 or 2 for your decision");
            System.out.print(":");
            int find = in.nextInt();                                            //Reading input saving it as variable find
            System.out.println("");
            System.out.println("");
        
            if (find == 1) //Through to 2nd floor Mewbourne
            {
                System.out.println("You unlock the doors and go down the hall. You go down the hall but the doors at the other end are unreachable because of a stack of math textbooks.");
                System.out.println("Dean Duncan catches up to you and kills you.");
                System.out.println("");
                System.out.println(Dead);
            }
            
            else //Go upstairs to 3rd floor Mewbourne
            {
                System.out.println("You go upstairs and unlock the doors to 3rd floor Mewbourne.");
                System.out.println("The window at the end of the hall is busted open and the Science and Engineering teachers has constructed a working helicopter and ");
                System.out.println("they have one more spot but they don't know whether to take you or Dr. Raulston.");
                System.out.println("Here are your choices:");                   //Providing path choices after telling them the situation they are in
                System.out.println("1. Take the seat for yourself");            //Choice Path uno
                System.out.println("2. Let Dr Raulston have the seat");         //Choice Path dos
                System.out.println("Enter number 1 or 2 for your decision");
                System.out.print(":");
                int win = in.nextInt();                                         //Reading input and setting it to the variable win 
                System.out.println("");
                System.out.println("");
                
                if (win == 1)                                                   //If statement for taking His Seat (you for sure win)
                {
                    System.out.println("You win and escape St.Johns... but at what cost?");
                    System.out.println("");
                    System.out.println(Win);                                    //Win so I put in the obligatory win message
                }
                
                else                                                            //Else statement for letting him have the seat (you can still win but not as likely)
                {
                   Random generator = new Random();             //Random Nummber Generator Class
                   int d = generator.nextInt(2);                //Recieves the random number from the class
                   
                   System.out.println("You tell Dr. Raulston he can have the seat. He thanks you for your kindness. The helicopter leaves and you see Dean Duncan.");
                   
                   if (d == 0)          //Dean Duncan is a nice guy and lets you escape 
                   {  
                   System.out.println("Even as a monster he can respect a kind hearted person. He lets you escape and you win.");
                   System.out.println("");
                   System.out.println(Win);                 //Win message cause you got lucky and won
                   };
                   
                   if (d == 1)          //Dean Duncan kills you sorry
                   {
                   System.out.println("Dean Duncan kills you where you stand.");
                   System.out.println(Dead);                //Unlucky and you lose so i put in the dead message
                   };
                   
                   if (d == 2)          //Dean Duncan passes out out of shock
                   {
                   System.out.println("Dean Duncan is so surprised after all of this you still were selfless enough to let Dr. Raulston go in front of you.");
                   System.out.println("Dean Duncan passes out, leaving you plenty of time to escape.");
                   System.out.println(Win);                 //Win message cause you won
                   };
                };
            };
            
        }
        else //Stay in the Computer Lab
        {
            System.out.println("You hide under a desk next to the window into the hall. Dean Duncan walks in and sees your foot. He kills you.");
            System.out.println("");
            System.out.println(Dead);               //Just a bad outcome why did you choose this path you aren't invisible and death message
        };
      };
    }
}
