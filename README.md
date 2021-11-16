# Programmering_1_project_J-D-A
David Salomonsson, Johan James och Alexander Holmgrens programmering 1 grupp project

16/11/2021 - Alexander H
Started writing a base for the game we are making. (First i imported sys, and time as i am going ot use those throughout the project). I started by making a function called start 
that would essentially ask the player if they want to start playing the game or not. First an input prompt asking "would you like to start the game?". If you type in yes it will 
take you to the games introduction and start the game. If you typed in no, the program will simply "say maybe next time". If however none of those conditions are filled, 
neither yes or no was typed in, the function "again()" is played that tells you to enter a valid answer (in this case yes or no). The function again also has a pause (time.sleep) 
to slow down the text and make everything a bit less sudden and making it more smooth. The function (again) then plays the function clear() that just prints a bunch of empty lines
to make the terminal less cluttered. After the clear the start function is started again. I put "lower" and "strip" at the end of the input prompt to convert any text given to 
lowercase and removing any leading or trailing whitespaces that may have been written in by accident. I then made a function called print_slow. This function essentially printed
out text slower (letter by letter) to give it more of a retro video game feeling. It takes the parameter string (the text you enter, and prints each letter out with a small break
in between each, the duration decided by the time.sleep function. The intro function, prints a series of text lines introducing the theme of the game and setting up for the first
choice. The first choice is made through a function that presents 3 choices of where to go. You are then given the choice to go one of the 3 ways. 




