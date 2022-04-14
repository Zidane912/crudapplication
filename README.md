# Architecture

This is a basic CRUD application that accepts user input of video games and reviews. It comprises of two tables in the mysql database,
* Games
* Reviews
This uses a one-to-many relationship where one game can be reviewed by many people however only one entry can review one game hence reviews contains a foreign key referencing to the games table. Initially, I tried to develop this app where several games could be reviewed by several people however after realising this was a many-to-many relationship so would require three tables.

As for the application itself, it comprises of an application folder which contains a templates, routes.py, models.py and forms.py. The routes deals with the various functions create, read, update and delete on the web application, committing to and deleting from the sql and linking the form and the tables together. The models is used in tandem with the create.py file (which is in the root of the directory) in the root to create the database and tables. Forms was used to model the form used for and display onto the web pages. As for the templates folder this contains the various html files used to display and interact with the user.

app.py was used to run the "python3 app.py" command on the command line to run the web application on the virtual environment.

# Setup

Everytime the application is started please follow these steps:
1. Ensure vm and db instances have been started
2. pip3 install -r requirements.txt
3. export CREATE_SCHEMA=true
4. export DATABASE_URI=mysql+pymysql://root:"password of db"@"private ip of db"/"name of db"
5. python3 create.py
6. python3 -m venv venv (if there is no venv folder)
7. source venv/bin/activate
8. python3 app.py

# Current outstanding issues with code

At the moment all functionality works i.e. create, read, update and delete. However, currently with create function, all creates after the intial create will produce extra entries i.e. if you put your first entry it works but the second entry will produce an additional first entry and an additional second entry and for a third entry it will produce a third first and third second entry as well as three third entries. As of now this is still an issue.

# User Story

* As a reviewer, I want to be able to write a review for others to see my opinion on a particular game
* As a reviewer, I want to be able to edit that review in case my mind chnages on a game due to subsequent playthroughs
* As a reviewer, I want to be able to see the reviews I have uploaded to the website as well as the reviews of others
* As a reviewer, I want to be able to delete a review if I do not want others to see it

# Kanban Board

Please refer to the github projects board on the page of this repository.

# Risk Assessment



# Entity Relationship Diagram
![ERD1](https://user-images.githubusercontent.com/96538941/163391253-9fdc32ea-a0b9-464f-9216-d7229ef6870f.jpg)
