# Tic-Tac-Toe [Team 1]

## Python Development

This is a Tic-Tac-Toe game developed by **Team 1** during the Python Development course within Scoala Informala de IT.

### Requirements:
1. Rewrite `print` and `logging` so you don't have to write the messages you have to log more then once. Also rename to output logs to `games_history` instead of just `games` [the name is really confusing, sorry about that :)]
2. Add functionality to allow players to set their names before the start of the game..
3. Add functionality to allow selecting a game system:
	- add support for single game only
	- add support for 2/3 (the winner will be the one who wins 2 games out of a maximum of 3)
	- add support for 3/5 (the winner will be the one whi wins 3 games out of a maximum of 5)
4. Add functionality to allow custom sign for each player:
	- the user should be able to select EXACTLY one character (validate s/he really selected a character)
	- use the lower case of the selected character, e.g. if the users choose **A**, use the **a** instead
5. Add functionality to allow registration and authentication before a game:
	- use a JSON file (data/credentials.json)
	- each player should authenticate before playing a game based on an `username` and `password`
	- every player should have an account and we could keep track of their stats
	- when you start the program, the first player will be prompted to:
		- create an account (automatically consider the user authenticate afte the sign up succeed)
		- authenticate (use `username` and `password`)
	- the same thing will apply for the second player too.
	- in order to create an account, each player should complete the following:
		- first_name
		- last_name
		- username (unique within data/credentials.json)
		- password (at least 6 characters with at least one digit)
		- password confirmation
6. Account for the following stats:
	- total single games played (account after each game)
	- total single games won (account after each game)
	- total 2 out of 3 games played (acccount after each 2/3 series)
	- total 2 out of 3 games won (account after each 2/3 series)
	- total 3 out of 5 games played (account after each 3/5 series)
	- total 3 out of 5 games won (account after each 3/5 series)
7. Add unit tests for as many functions as possible.

**TBA:** Object oriented programming

**TBA:** tkinter (GUI - Graphical User Interface)
