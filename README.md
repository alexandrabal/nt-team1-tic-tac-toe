# Tic-Tac-Toe [Team 1]

## Python Development

This is a Tic-Tac-Toe game developed by **Team 1** during the Python Development course within Scoala Informala de IT.

### Requirements:
1. Inlocuire mesaje `print` si `logging` pentru a nu le rescrie.
2. Adaugare functionalitate de introducere de la tastatura a numelor celor 2 jucatori.
3. Adaugare functionalitate de introducere a unui sistem de joc:
	- adaugare suport pentru un singur joc
	- adaugare suport pentru joc 2/3 (castigatorul va fi cel care va castiga 2 jocuri dintr-un maxim de 3)
	- adaugare suport pentru joc 3/5 (castigatorul va fi cel care va castiga 3 jocuri dintr-un maxim de 5)
4. Adaugare functionalitate de personalizare a semnului cu care fiecare jucator va juca:
	- trebuie sa fie ales UN SINGUR caracter (validare ca este caracter)
	- se va folosi "litera mica" a caracterului ales (ex: daca aleg 'A', jocul va folosi 'a')
5. Generare posibilitate de inregistrare/autentificare inainte de inceperea unui joc.
	- se va folosi un fisier JSON (data/credentials.json)
	- fiecare jucator va avea creat un cont
	- rolul functionalitatii este sa se implementeze un sistem de autentificare si unul de inregistrare
	- jucatorii nu isi vor mai alege doar numele ci vor avea conturi cu ajutorul carora putem tine cont de statistici
	- in momentul in care este rulat programul, Player 1 are doua optiuni:
		- creare cont (dupa inregistrare jucatorul este autentificat automat)
		- autentificare (pe baza de email si parola)
	- acelasi lucru se va repeta pentru Player 2
	- pentru inregistrare fiecare utilizator va avea de completat urmatoarele campuri:
		- first_name
		- last_name
		- email (unic in fisierul data/credentials.json)
		- parola
		- confirmare parola
5. Generare sistem de gestionare a datelor asemanator stocarii intr-o baza de date.
	- se va folosi un fisier JSON (data/db.json)
	- se va genera un ID unic (folosind uuid.uuidv4())
	- fiecare jucator va avea deja datele de la functionalitatea anterioara.
	- sa se adauge functionalitate astfel incat in JSON sa se reflecte urmatoarele date:
		- numarul total de jocuri in sistem single ale unui utilizator (se contorizeaza dupa fiecare joc)
		- numarul total de jocuri castigate in sistem single ale unui utilizator (se contorizeaza dupa fiecare joc)
		- numarul total de jocuri in sistem 2/3 ale unui utilizator (se contorizeaza dupa fiecare serie de 2/3)
		- numarul total de jocuri castigate in sistem 2/3 de utilizator (se contorizeaza dupa fiecare serie de 2/3)
		- numarul total de jocuri in sistem 3/5 ale unui utilizator (se contorizeaza dupa fiecare serie de 3/5)
		- numarul total de jocuri castigate in sistem 3/5 de utilizator (se contorizeaza dupa fiecare serie de 3/5)
6. Testare functii existente.

**TBA:** Programare orientare pe obiecte
**TBA:** tkinter (interfata grafica - GUI)
