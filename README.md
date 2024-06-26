[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14588397&assignment_repo_type=AssignmentRepo)

# The Road Trip
## CS110 Final Project   Spring, 2024 

## Team Members

Jeremy Luk

## Project Description

I want to create a game similar to Oregon Trail where the player is trying to reach a destination and at certain locations,the player will encounter different options that will impact their progress. Some choices can impact future choices and some choices are randomized and based on luck. 

## GUI Design

### Initial Design

![initial gui](assets/gui.png)

### Final Design

![final gui](assets/finalgui.png)

## Program Design

### Features

1. Character moves around
2. Interactable Choices
3. Buttons as a roll mechanism
4. Score keeping and displaying score at end
5. Menu to keep playing or to quit

### Classes

- 

    Controller:
        The Controller class is responsible for the main looping of the game and to control the menu. This class defines when the game state is in menu or game. If the game state is menu, this class will draw a menu that allows the user to continue the game or stop the game. When the game state is in game, this class updates the events and class on other classes to handle events based on the game events. 
- 

    Initialize:
        The Initialize class creates the screen and the objects on the screen such as the scoreboard, the wheel, and the player icon. This class also controls the score count when the user clicks on the roll circle. At specific score counts, this class will call on the game class to perform functions. After the game class changes the game state to game, the Initialize class will continue the game and continuously redrawing the screen so that the game functions properly. 
- 

    Game:
        The Game class handles user inputs and the choices the user makes during the game. When the class game is called, it will display text and boxes on the screen depending on how the class is called. When the user clicks on of these boxes, it will trigger changes to the score or the screen depending on which choice the user makes. 
- 

    Movement:
        This class controls the movement of the user when the user clicks the roll circle. This class ensures that the user moves to the right based on the number that they roll and stops the movement if the user icon moves off the screen.
-

    Context:
        Creates a short paragraph introduction about the game and what the user is expected to do. This class also fills in the color of the background and creates a rectangle which the user is supposed to click to allow the game to continue to the next part. 
## ATP

Test Case 1: User Movement

    Test Description: Verifies the user moves to the right after click

    Test Steps:
        1. Start the game
        2. Click to continue through the intro and first choice
        3. Click the circle in the center of the screen
        4. Verify that the user moves to the right in a horizontal line

    Expected Outcome: The user moves to the right by the amount set by the click.

Test Case 2: Menu Options

    Test Description: Verifies each option in the menu is able to be selected

    Test Steps:
        1. Start the game
        2. Click "Play"
        3. Verify the game starts and the intro screen is presented
        4. Close and restart the game
        5. Click "Quit"
        6. Verify the game closes 
    
    Expected Outcome: The menu should either allow the user to play the game or quit the game depending on which button the user selects.

Test Case 3: Play Again

    Test Description: Confirms that the user is able to play again when the game ends.

    Test Steps:
        1. Start the game
        2. Click through the intro and click the circle and choices until another menu pops out stating "Game Over"
        3. Click the button, "Play Again"
        4. Verify the game restarts 

    Expected Outcome: When the user reaches the end and clicks "Play Again", the game restarts and the user can replay the game.

Test Case 4: Select Choices

    Test Description: Confirms that the user is presented with choices and can select one.

    Test Steps:
        1. Start the game
        2. Click continue through the intro
        3. Click one of two options presented (red box or blue box)
        4. Verify the turn count increases (initially at 0) and the screen with the user icon redisplays

    Expected Outcome: When the user selects an option, the game will continue to run until the end. 

Test Case 5: Error Clicks

    Test Description: Verifies that if the user clicks on a different part of the screen than intended, the game does not respond.

    Test Steps:
        1. Start the game
        2. Click outside the pink box in the intro
        3. Verify the game does not continue
        4. Click continue to move on to a green screen with two colored boxes
        5. Click outside the boxes to verify the game does not continue
    
    Expected Outcome: The game should not continue and should not move to a different screen if the user does not click in the approriate locations. 
