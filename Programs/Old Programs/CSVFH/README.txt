CSV File Handler Test Application Instructional Guide


[1] Introduction
This is a small README document offering instructions on how to use the test application. If any concerns arise regarding the design or operation of the CSV File Handler program, users are recommended to visit the Software Requirement Specification document or the Software Design Document. 
[2] Launching the Program
A step by step process for running the CSV File Handler program is stated below.


1. Before initiating the CSV File Handler program, it is essential that two things are completed first:
   1. The desired CSV file for handling has been placed in the CSV File Handler folder alongside this file
   2. The device that this program runs has Python and Bash capabilities(this is usually standard with most computers).
2. Activate either a command prompt or terminal depending on your operating system and navigate to the CSV File Handler Folder. 
3. When you are in the CSV File Handler program, run the launcher script “CSVFH” followed by the file name of the CSV file to be handled.
4. If these steps do not work it is recommended to check if all needed files are present. A list of the files are as follows:
   1. CSVFH (Launcher Application)
   2. srcecode.py
   3. Srcebank.py
[3] FAQ Section
1. Is a command prompt or terminal needed to run this program?
   1. Yes. This program runs through scripts and if a method other than the command prompt/terminal is used, it could make the displays not print out correctly thus affecting the visuals of the program
2. Can the program really handle files of any size?
   1. Yes! This program can handle larger data sets with ease; however, python has a known limit to how much data can be sent around at any given time so I would try not over loading the program!