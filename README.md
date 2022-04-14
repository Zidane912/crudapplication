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

Description	Evaluation	Likelihood	Impact Level	Responsibility	Response	Control Measures
Getting ill	Delays to project	Likely	Medium	Developer	Cover from colleagues	Have others trained to cover potentially ill colleagues
Late deployment of application	Delays deployment of application	Likely	Severe	Developer	Use agile methods throughout entire production lifecycle	Use of Kanban boards, realistic time scales, delegation of work
Servers going down	Affects user experience	Unlikely	Severe	Maintenance team	Implement system to get servers back up	Use Jenkins to automate server fixes
Accidental file deletion	Delays to project	Likely	Severe	Developer	Back up files	Cloud storage system like AWS
Older version of application is deployed	Likely to have bugs	Likely	Medium	Developer	Ensure most latest stable version of application is deployed	Use Jenkins to automate tests and restrict access to code of application
Virtual Machine goes down	Application is offline	Unlikely	Severe	AWS	Rebuild the infrastructure onto another virtual machine	Ensure this infrastructure is a code so that rebuilding is as efficient as possible
Password, information and Security Attacks	Information provided by user accessed by hackers	Likely	Minimal (no personal information is shared)	Cyber Security, DevSecOps	Implement security measures	Code pop ups that alert users to not share personal information
Database and Tables being deleted	User that inputs reviews will have their data deleted	Likely	Severe	Cyber Security, DevSecOps	Restrict access to code (so that attacker cannot access drop function in sql servers)	Export drop function as a environmental variable and not in the code itself
Users writing inappropriate/offensive reviews for games	Affects user experience of other reviewers	Likely	Severe	Developer	Remove ability of this reviewer to write reviews	Ban reviews from the IP address of the reviewer who wrote the inappropriate review/warn reviewer at top of the page about being respectful etc
Reviewer accidently deleting reviews from website	Affects user experience	Likely	Severe	Developer	Allow reviewers to retain deleted reviews	Implement a page for deleted reviews while coding an option to recover these deleted reviews
Leaking of sql password and IP addresses	Security Breach	Unlikely	Severe	Developer	Hide this information so those who have access to code cannot see it	Store it as an environmental variable using export … = true in the command line



# Entity Relationship Diagram

