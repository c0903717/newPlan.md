# Media Database
 
### Introduction
 
Have you ever felt frustrated that Goodreads lacks several features on Letterboxd, which lacks features that are on Goodreads? Or that you can't view a database of all of the media you’ve experienced, such as books and movies, in the same site/application? No longer will this be a problem!
 
We are going to create a graphical user interface for displaying and interacting with a database of media the user curates. The user will be able to sort through the media they have experienced, in any medium, because the interface will allow them to tag different attributes, including personal score, creator, genre, etc.
 
### Input
 
The user will be prompted to enter information in the GUI, which will then create a CSV/SQLite database specifically for the information they typed in.
 

First, the user will be prompted to choose a button for the super medium of media (Verbal or Visual), or they can choose to sort, see and/or add to their favorites section, see and/or add to their diary, or choose a folder/file to see their media database that the program will create. 
 
If the user selects the verbal media, they will be prompted to specify the type of media in another window. The verbal media will include mainly books and poems, but the user can choose to create a new type of subset. Then, the user will be prompted to make tags for each of the new types of data that they input. These tags will be created by the user, and there will be a sort function for them to view each of the tags for each of the inputs that they have made. There will also be an option to edit specific tags for the information they have input.
 
If the user selects the “visual” button, then they will again be prompted with a series of buttons allowing the user to specifically select the category of visual media they wish to access (Movies, TV shows, Documentaries, etc). If they choose the “+new” button, then they will be able to create a new category for their convenience. If they chose one of the buttons that is not “+new” then their entries of that type of visual media are displayed, and it gives the user an option to sort their entries, add new entries, add new tags, and edit their current entries. If they choose to add a new entry, then they will provide the information for the entry and it will go into the database. If they choose to edit one of their current entries, then they will simply be able to modify whichever tag they need to modify. 
 

The created CSV/SQLite file will be sorted according to the user’s preference. 
 
 
### Display
 
The application will open with an area to choose supermedium (verbal or visual), a place to view all media sorted, a place to choose database folder, a place to view favorites, and a diary section.
 
Upon choosing the supermedium, users will be prompted to choose the medium within it or create another one to log media within, such as book series and poems for verbal and films and comics for visual.
 
When creating a new medium section, users will be able to enter the name of the medium to display and an optional description.
 
When in a medium section, users will be able to sort within the display section of the media they have logged in the medium by tags, edit the tags of entries, edit the tags of the medium, and add entries.
