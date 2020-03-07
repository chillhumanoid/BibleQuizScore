# Developer Info

until I get more work done, I won't have a project page just yet or open issues. 

Right now i'm working through getting all the UI for the scoresheet out, eventually I plan to make it so that the workflow is as follows:

Create meet, specific location and set home team (your team), specificy how many rounds and the date of the meet (if creating in advance) (there will also be an option to add each round one at a time)

Meet page will have tab per round, each round will call the Scoresheet class. On any update to the scoresheet, the program will save the data in a specific way. (I haven't determined save structure or file type, most likely sql)

## Scoresheet.py structure

after __init__ -> initUI

### initUI: 
 - createGridLayout (name changing) - This is the top section of the scoresheet
 - createHomeTeam                   - this is the part of the scoresheet for scoring your team
 - createAwayTeam                   - This is the part of the scoresheet for scoring the other team
 Everything else is self explanatory in here this function

### createHomeTeam
 naming convention - h#%$ - h = Home, #=seat number, % = (q)uizzer or (s)ub, $=Question number
 
 creates a grid layout for this section, and then creates the dropdowns for each question.
 - createTeam                       - creates the info in the dropdowns

### createAwayTeam
 naming convention - a#%$ - a = Away, #=seat number, % = (q)uizzer or (s)ub, $=Question number
 
  same as hometeam but for away team

  - createTeam                      - creates the info in the dropdowns

### createGridLayout
   naming convention: 
   variables start with q for question (unlike quizzer above) and # for question number
   q#Label is the text for each question, single digit numbers get a leading 0 for symetry
   q#Point is for point values (nothing, 10, 20, 30), set in createDropDown
   q#Type  is for question types, set in createDropDown
   q#Part  is for parts of the question (2 part answer, 2 part question 2 part answer, etc.)
   q#note  is for the notes edit line
   
   - createDropDown                 - populates the dropdowns and formats everything correctly

#### createDropDown
   Takes: 
   * position (1-23)
   * all the things created for each question, difference is that there's no question number (to allow for reusability)
   
   variables: 
   * points - list - point values - nothing, 10, 20, 30
   * types  - list - question types - follows Meddaugh's method
   * parts  - list - question parts - follows meddaugh's method

   if position is above 20 it's an overtime question, and doesn't have a dropdown, so it gets set to teh label, that label is centered
   
   set the width of all parts of the scoresheet so far to 55, this will exclude spots for names, and things that need to be smaller, but everything in the center is 55.
   set alignment of all labels to center. 
   
   add the widgets to the scoreLayout variable

### createTeam
   Takes: 
   * position (1-23)
   * layout - this is needed because it's re-used for both home and away
   * all the things created for each question, but for reusability, use t instead of h/a (for team), and don't include question number or Point.
   
   * if position is over 20, set point list to nothing, 10, -5, otherwise set it to nothing, + , and - (point values will be adjusted when the question value is changed, this method is only called in the beginning)
   * add the points to each quizzer, and then set the width to 55(see above)
   
   * add widgets to layout. 
