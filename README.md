Assignment 1: Shall we play a game?¶
By using Object-Oriented Programming (OOP), you will create a program called WordyPy. In WordyPy, the bot you create must try to guess a five-letter secret word based on feedback given from the game engine. For each word guess your bot makes, the WordyPy game engine will give detailed feedback which your bot can use to increase its chances of winning.

Requirements
The rules of WordyPy are as follows:

Each guess must be a five letter English word. Only the 26 letters of the English alphabet are used, and case does not matter.
The game engine, which is written for you, generates a hidden 5 letter word called the target word.
The bot, which you must write, attempts to guess that word. It will get up to six tries.
The bot will be given the location of a datafile which has a list of allowable words (one per line). Your bot must read in this datafile and only make guesses from this datafile.
After each guess the system provides feedback indicating if each character is in the correct position for the target word, and if not, if the character is in the target word but in the wrong position.
The bot must be "smart" in that once it has identified the correct location of a letter in a word it must only guess future words where that letter is in the same position.
We have written tests for these requirements; you must pass those tests to pass the assignment.
Architecture
In order for your bot to play WordPy, you must implement two classes shown in the figure below (Letter and Bot) and write the python logic for each method of the two classes.

Architecture Diagram of WordyPy

A Letter indicates a single English letter from a guess, and has methods and attributes to describe whether the letter was in (or in the correct place) in the hidden target word.

The Bot class is your game playing agent! This class has two substantive methods in it:

make_guess which returns a string that is evaluated by the GameEngine and
record_guess_results which takes the evaluation done by the GameEngine in order to ensure that the same guess is never made twice and that your bot "learns" from previous guesses.
The GameEngine, given to you at the bottom of this notebook, will control the game play. You don't have to write the GameEngine – we've done that for you. However, the GameEngine will not work until you have correctly defined the Letter and Bot classess, including their methods. You will work on those!

How to Test Your Bot
Once you have created the neccessary classes you should be able to test your bot by running this notebook. To verify it is passing our grading criteria, press the validate button on the toolbar. Once you have verified this you can try submitting to the autograder, which will evaluate our additional hidden unit tests and give you a grade -- don't worry, you can submit to the autograder as many times as you would like!

You may wish to debug your Bot by playing a game with a shorter word list. We've included code for that at the bottom of this notebook for testing, but be aware that it will not work until your Letter and Bot classes have been implemented. Also, our final grader script will use a bigger dictionary of allowable words, so make sure you are thinking more generally about the problem and not hard coding any example words into your work!

Worked Example
Here is the output from an example run using the testing code provided. In this example five words were put into a text file called temp_file.txt. The game engine randomly picked a target word of DOGGY and the bot made three guesses.

The first guess was the word DRIVE and the GameEngine provides the output of D???? indicating that the first letter is in the word and is in the correct position and the last four letters are not in the word anywhere.
The bot then made the guess of DADDY and the GameEngine provides the output of D?**Y indicating that the first and the last letters are in the word and in the correct location, the second letter from DADDY is not in the word anywhere, and the third and fourth letters from DADDY are in the target word but not in those positions.
The final guess made by the bot is the word DOGGY, which the game engine identifies as correct and finishes WordyPy.
Example of Playing WordyPy

Hint 1: Don't forget the Types!

In the architecture diagram we have used the format that python uses for type annotations. For example, in the Letter class, there are three methods. The constructor method, __init__, takes two input parameters, letter, which is of type string, and index, which is of type integer. The __init__ method returns None. The diagram also indicates that the third attribute, in_word, is a boolean value and has a default value of False and you need to set this value appropriately.

For a refresher on interpreting these type annotations, please consult [TODO: INCLUDE LINK TO COURSE 2 MATERIAL ON TYPE HINTING HERE]

Hint 2: Planning your Approach

It can be a bit overwhelming to tackle the whole assignment at one time, so consider breaking it down into steps. The steps I would take with this assignment would be:

Create the Letter class and ensure it passes all of the tests (both validation and assignment grading tests)
Create an initial Bot class based on the architecture diagram
Update the Bot class to make random guesses with the test words I provided
Update the Bot class to track the letters whose positions are identified correctly
Update the Bot class to track the letters which are not used at all and not use them in the next guesses. In short, ensure it keeps track of past guesses and makes a "smart" guess






Hint 3: Considering an Algorithm for Smart Guesses

One of the hardest parts of this assignment is making a "smart" guess. The assignment requires your bot to keep track of what it has learned, and the GameEngine provides feedback to your bot using the record_guess_results() method. In solving this part of the assignment consider the following:

You only need to keep track of which Letter objects have an is_in_correct_place() of True, so feel free to ignore other information about Letter objects such as whether is_in_word() is true
You don't need to keep track of all of your previous guesses if they are removed from your word_list
You may want to add additional attributes to your Bot which don't appear in the architecture diagram
