# Cardboard Craic
Phillip Healy's Milestone Project 3: Data-centric full stack site.
Cardboard Craic is a site for all things boardgame related. Register to leave a review of a game you love or hate, check out news about what's going on in 
the world of boardgames!

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

I chose to have the site be open and clean to have a great user experience. Keeping focus on the content the user has come for, while providing easy navigation
 to and from every part of the site. I went with a healthy green colour which is traditionally associated with the environment and success.

For the font I chose Poppins; a free Google Font. Poppins is an internationalist take on geometric sans. Each letterform is nearly monolinear, 
 with optical corrections applied to stroke joints where necessary to maintain an even typographic color. The Devanagari base character height 
 and the Latin ascender height are equal; Latin capital letters are shorter than the Devanagari characters, and the Latin x-height is set rather high (https://fonts.google.com/specimen/Poppins#about).
 I found this Font to be clean and clear at all font-weights, which is what I wanted in my consistent vision across the site.


## Features

### Existing Features

### Future Features


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
- When building the nav bar the logo was overflowing bellow the header with materialize template. This looked sloppy so I applied an id and style to it just for mobile to fix it.

### Registration

### Log in/out

### Access Control

### Games

### Genres

### Support

### Bugs Encountered


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

## Credits

### Content

### Media

### Acknowledgements
