# Final Project 1

Basic App that allows CRUD of game reviews

# Basic Usage

Everytime the application is started please follow these steps:
1. pip3 install -r requirements.txt
2. export CREATE_SCHEMA=true
3. export DATABASE_URI=mysql+pymysql://root:"password of db"@"private ip of db"/"name of db"
4. python3 create.py
5. python3 -m venv venv
6. source venv/bin/activate
7. python3 app.py

# Current outstanding issues with code

At the moment all functionality works i.e. create, read, update and delete. However, currently with create function all creates after the intial will produce extra entries i.e. if you put your first entry it works but the second entry will produce an additional first entry and an additional second entry and for a third entry it will produce a third first and third second entry as well as three third entries. As of now this is still an issue.

# User Story

* As a reviewer, I want to be able to write a review for others to see my opinion on a particular game
* As a reviewer, I want to be able to edit that review in case my mind chnages on a game due to subsequent playthroughs
* As a reviewer, I want to be able to see the reviews I have uploaded to the website as well as the reviews of others
* As a reviewer, I want to be able to delete a review if I do not want others to see it

# Risk Assessment

# Entity Relationship Diagram

