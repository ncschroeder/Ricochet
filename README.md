# Ricochet
A simple video game where there is a ball ricocheting around a screen and your goal 
is to prevent it from hitting the bottom by moving the paddle. The colors of the 
background, ball, and paddle are up to you, as well as the choice of an easy, medium, and
hard difficulty.

## Directions
1. Clone this repository
2. Run main.py using Python

## The beginning
This project started off as an assignment for CSC 131: Computational Thinking, which
goes over advanced Python and introductory C++. For this assignment, the only part 
I was required to do was the actual game part. When the user ran the program, the 
game would start immediately and the player would have a set number of lives and the
colors of everything were set in stone. When the lives ran out, the game would restart.

## Improvements
A while after I completed this as an assignment, I decided to make some 
improvements to this program by adding a menu and giving the user the option 
to select colors for the background, ball, and paddle. I eventually added in the 
option for the user to select a difficulty as well. Along with adding these features, 
I also improved the code. I came up with the idea of creating classes of the menu, 
game screen, ball, and paddle and then having the program have a single instance 
of each class and have those objects interact with each other during the game. 

## The graphical user interface
This project is currently using graphical user interface tool tkinter.
At one point in working on this project, I found out about a different GUI tool designed
for games in Python called pygame. After researching and learning pygame, I decided to 
stick with tkinter because it allowed for an easier creation of a game menu in my opinion.
Tkinter was also adequate for what I was doing so there wouldn't have been much to gain
by switching to pygame.

## Problems
I tried to make a two player mode where one paddle would be on the bottom of the screen
and the other on the top. The ball would ricochet around the screen and the players would
have to prevent it from hitting their side of the screen. When the ball hits the top wall,
the bottom player would get a point and vice versa. The bottom player would move their 
paddle using the Z and X keys and the top player would move their paddle using the N and 
M keys. The problem is that only one button press was able to be recognized. If the
bottom player was moving their paddle and the top player tried to move their paddle, 
it wouldn't move. I did some research on this problem and didn't find any solution to 
it, at least not any tkinter solution. I just decided to scrap this improvement idea
and get rid of all the code for it, as this problem was a dealbreaker. 
From what I remember of my research of pygame, however, there is a way in pygame to 
be able to press multiple buttons and all would be recognized. Maybe in the future 
I will try to make this game using pygame and implement my ideas of a two player game.