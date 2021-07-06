# Cardboard Craic
Phillip Healy's Milestone Project 3: Data-centric full stack site.
Cardboard Craic is a site for all things boardgame related. Register to leave a review of a game you love or hate, check out news to see what is going on in the world of boardgames!

## Brief

### Project purpose: 

In this project, you'll build a full-stack site that allows your users to manage a common dataset about a particular domain (Boardgames). 

### Value provided: 

Users make use of the site to share their own data with the community, and benefit from having convenient access to the data provided by all other members. 

My users will benefit by being able to share their opinions and experiences, as well as seeing other users expriences and opinions on various boardgames. This can help
 to guide purchasing or entertain people interested in the hobby.

The site owner advances their own goals by providing this functionality, potentially by being a regular user themselves. The site owner might also benefit 
from the collection of the dataset as a whole. 

As the site owner I will love reading the users experiences, enjoy writing about my own, and potentially make some money through affiliate links or Patreon.

### Project Requirements 

#### Main Technologies 

- HTML, CSS, JavaScript, Python+Flask, MongoDB 

- Additional libraries and external APIs 

#### Mandatory Requirements 

A project violating any of these requirements will FAIL 

1. Data handling: Build a MongoDB-backed Flask project for a web application that allows users to store and manipulate data records about a particular domain. 
 If you are considering using a different database, please discuss that with your mentor first and inform Student Care. 

2. Database structure: Put some effort into designing a database structure well-suited for your domain. Make sure to put some thought 
 into the nesting relationships between records of different entities. 

3. User functionality: Create functionality for users to create, locate, display, edit and delete records (CRUD functionality). 

4. Use of technologies: Use HTML and custom CSS for the website's front-end. 

5. Structure: Incorporate a main navigation menu and structured layout (you might want to use Materialize or Bootstrap to accomplish this). 

6. Documentation: Write a README.md file for your project that explains what the project does and the value that it provides to its users. 

7. Version control: Use Git & GitHub for version control. 

8. Attribution: Maintain clear separation between code written by you and code from external sources (e.g. libraries or tutorials). 
 Attribute any code from external sources to its source via comments above the code and (for larger dependencies) in the README. 

9. Deployment: Deploy the final version of your code to a hosting platform such as Heroku. 

10. Make sure to not include any passwords or secret keys in the project repository. 

#### Important Notes 

11. Feel free to reuse the authentication from the mini-project. The focus of this milestone project is on the data, rather than any business logic. 

## UX

### User Stories

- As an enthusiast I would like to be able to check out Boardgame news.
- As a hobbyist I want to read reviews before I buy.
- As a gamer I would like to be able to write my own reviews.
- As a perfectionist I would like to be able to come back and edit or delete my past reviews. 
- As a supporter I would like to be able to support the page.
- As a user I want to be able to register with the site.
- As a player I want to be able to sort by genre.

### Design

[Wireframes](wireframes/cardboardcraic.pdf)

[Schema](/assets/images/schema-2.1.png)

I chose to have the site be open and clean to have a great user experience. Keeping focus on the content the user has come for, while providing easy navigation
 to and from every part of the site. I went with a healthy green colour which is traditionally associated with the environment and success.

For the font I chose Poppins; a free Google Font. Poppins is an internationalist take on geometric sans. Each letterform is nearly monolinear, 
 with optical corrections applied to stroke joints where necessary to maintain an even typographic color. The Devanagari base character height 
 and the Latin ascender height are equal; Latin capital letters are shorter than the Devanagari characters, and the Latin x-height is set rather high (https://fonts.google.com/specimen/Poppins#about).
 I found this Font to be clean and clear at all font-weights, which is what I wanted in my consistent vision across the site.

## Features

### Existing Features
- A front page featuring latest news and spotlights on top 3 games.
- A page to see all games that have been reviewed on the site.
- A genres page to see the games in each genre.
- A review page to see each review.
- A log in/register page to become a user of the site.
- A profile page to show the reviews you've already left and allow you to edit/delete them.
- A form to add games, and reviews for those games.
- Have search bar for games, genres, reviews based on different terms.
- A logout button to see the site as a non-registered user or if you computer share etc.

### Future Features
- Affinity links on the games to earn money for site upkeep/future projects.
- Link to all games of a certain genre etc. when a user clicks on it.

## Technologies Used

### Python
- Python is an interpreted high-level general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant indentation. 
 Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code. (https://pythonbasics.org/)

### Flask
- Flask is a web application framework written in Python. Flask is based on the Werkzeg WSGI toolkit and the Jinja2 template engine. It is a Web 
Application Framework or a simply a Web Framework represents a collection of libraries and modules. (https://pythonbasics.org/what-is-flask-python/)

### Jinja
- Jinja2 is one of the most used template engines for Python. It is inspired by Django's templating system but extends it with an expressive language that gives 
 template authors a more powerful set of tools. (https://www.palletsprojects.com/p/jinja/)

### Werkzeug 
- Werkzeug is a comprehensive WSGI web application library. It began as a simple collection of various utilities for WSGI applications and has become one of the
 most advanced WSGI utility libraries. Flask wraps Werkzeug, using it to handle the details 
 of WSGI while providing more structure and patterns for defining powerful applications. (https://www.palletsprojects.com/p/werkzeug/)

### Bootstrap
- Bootstrap is the most popular CSS Framework for developing responsive and mobile-first websites. (https://www.w3schools.com/whatis/whatis_bootstrap.asp)

### Balsamiq
- Balsamiq Wireframes is a rapid low-fidelity UI wireframing tool that reproduces the experience of sketching on a notepad or whiteboard, but using a computer. (https://balsamiq.com/wireframes/)

### Font Awsome
- Font Awesome is a font and icon toolkit based on CSS and Less. (https://fontawesome.com)

## Testing

### Home Page
- Most recently created news item shows under logo.
- 3 most recently created games populate showcase.
- users can navigate to all other pages via nav.
- news is navigable via "go to news feed" link.
### Registration
- 
### Log in/out

### Access Control

### Games

### Genres

### Support

### Bugs Encountered
- When building the nav bar the logo was overflowing bellow the header with materialize template. This looked sloppy so I applied an id and style to it just for mobile to fix it.
- Created a "back to top" button to appear when user scrolls 30px or more on any page. fontawesome image did not apear in the button. Tried using unicode and importing fontawesome
 but this didn't work. Tried changing font color, adding a small background image, also didn't work. 
 I had put in a conflicting position value for the button vs the text, fixing this using an id resolved the issue!
- continually getting "werkzeug.routing.BuildError: Could not build url for endpoint 'register'. Did you mean 'index' instead?" error. have looked through code on each page as well as app.py. Can't see any errors that would cause this. 
 Turns out I had my __main__ above the register decorator so it was failing to call.
- Had the footer on profile page split in a strange way looking sloppy. Found an unclosed div that was causing this.
- Card action links were crowding each other. Align-right class wasn't working, used float: right on a custom class and this tidied it up.
- Genre titles were overlapping cards above them in mobile view. Applying margin to title card didn't work, possibly as position was offset. Applying just the right margin 
 to lower card helped space it out nicely.
 - Add game form has blank select input that I can't focus or change, making the form non submitable. Putting in even the most basic select/options was coming 
  up blank. Started form from scratch and found I had initialized the JQuery incorrectly. Select now working as intended.
- jinja2.exceptions.UndefinedError: 'None' has no attribute 'capitalize' after building add_news page. A test entry in the DB had a 
 null value that was causing the traceback error. Fixed that but correcting data in DB.
- Had the add buttons on each page regardless of user logged in, this caused an error if you tried submitting anything as "created_by" is recorded using session user, 
 and if you're not logged in there is no session user. An if statement fixed this.
- Default text on registration page spilling over line on mobile view. Reduced text size on mobile viewport of these elements to compensate for this.
- Footer was hanging in middle v-align on pages without much content. Flex and height: 100vh were supposed to eliminate this but didn't work. Creating containers 
 for header, body, and footer and making position of footer absolute helped, but left some overhang at bottom. Went through a dozen sites like stack overflow 
 and csswizard to try find a sollution and none were working on mobile and tablet and PC. Finally came across a sollution that calculated the window height minus
 the footer height which worked on all devices! http://martinpennock.com/blog/force-footer-bottom-page-css/ 
- News card was very large with too much white space. Fixed this to be small until clicked when the news would fill the cell.
- Kept getting PEP8 compliance errors for under-indented second lines. After a lot of trial and error I finally found the right level 
 of indentation for each part using http://pep8online.com/

## Deployment

1. Create repo "cardboard_craic" on Github based on Code-institute template.

2. Open workspace on Gitpod.

3. Install: updated pip, Flask, flask-pymongo, dnspython.

4. Create environments file env.py, and add this (and pycache) to gitignore for security.

5. create requirements.txt with pip3 freeze, create Procfile.

6. Log into MongoDB, join free cluster.

7. Create database cardboard_craic on free cluster.

8. Create collections on this database: games, genres, users, reviews as per schema.

9. Insert initial documents to these collections to test connectivity etc.

10. Back on Gitpod workspace create app.py and wire it up to the env.py.

11. Create first @app.route("/") and define a test page.

12. Go to Heroku.com and log in.

13. Create app cardboard_craic.

14. Go to Deploy and click deploy via Github. 

15. Put in Github username and repo name, make sure the correct repo opens.

16. Go to settings and click Reveal Config Vars. Add all info from env.py to this as it won't be picked up through Github (gitignore).

17. Back to deploy page click "Automatically deploy from branch: Master".

18. Wait to see this light up green. 

19. You can now "Open App" and will see the test page you created.

20. Live app:  https://cardboardcraic.herokuapp.com/

## Credits

### Content
- Back to top button modified from code taken from https://www.templatemonster.com/blog/back-to-top-button-css-jquery/
Window height calculations modified from http://martinpennock.com/blog/force-footer-bottom-page-css/

### Media
- Boardgame images taken from the original boxart as displayed on https://www.boardgamegeek.com/
- Page logo designed and created by me on https://sketch.io/sketchpad/
- Schema created on https://draw.io/app.diagrams/
### Acknowledgements
