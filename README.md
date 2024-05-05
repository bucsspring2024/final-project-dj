[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14588390&assignment_repo_type=AssignmentRepo)

:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# << Boss Fight >>
## CS110 Final Project  << Semester, Year >>

## Team Members

<< Jayden Feliz, Damian Chang >>

***

## Project Description

<< Maybe a boss fight >>

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. << Start Menu >>
2. << Power up item >>
3. << Winning Animation and losing>>
4. << Shaking Background>>
5. << End Menu (Win/Lose)>>

### Classes

- << You should have a list of each of your classes with a description >>
- Controller Class: controls player actions such as moving left, right, jumping, and crouching.
- MainMenu Class: handles the main menu interface and interactions.


## ATP

Test Case 1: Player Movement Interaction

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Press left arrow key | Player moves left |
|  2                   | Press right arrow key   | Player moves right |
|  3                   | Press up arrow key   | Player jumps |
|  4                   | Press down arrow key   | Player crouches |

Test Case 2: Button Interaction in Main Menu

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Hover the mouse pointer over each button  | Buttons highlight upon mouse hover |
|  2                   | Click on the "Start Game" button | Clicking on the "Start Game" button transitions to the game screen |
|  3                   | Click on the "Quit" button | Clicking on the "Quit" button closes the game application without issues |

Test Case 3: Attack Mechanism in Game

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Select "Rock" option | Game displays appropriate outcome based on the selected option |
|  2                   | Select "Paper" option   | Game displays appropriate outcome based on the selected option |
|  3                   | Select "Scissors" option   | Game displays appropriate outcome based on the selected option |

Test Case 4: Display of Win/Lose Screens

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Run Counter Program  |GUI window appears with count = 0  |
|  2                   | click count button   | display changes to count = 1      |
etc...

Test Case 5: Enemy and Player Character Scaling

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Start the Game | Game starts |
|  2                   | Verify that the player and enemy characters are displayed on the screen with the correct sizes, positions, and proportions. | The player and enemy character imagse are scaled according to the specified dimensions and appear correctly on the screen. |