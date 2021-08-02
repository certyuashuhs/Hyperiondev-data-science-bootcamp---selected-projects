import sqlite3

# creating new java database file (storing in memory for this exercise to avoid that it indicates db already exists error)
db = sqlite3.connect(':memory:')

# adding a cursor object
cursor = db.cursor()

# executing creation of the table
cursor.execute('''CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY,
    Title TEXT,
    Author TEXT,
    Qty INTEGER)''')

# adding initial values to the table
books_ = [(3001, 'A Tale of Two Cities', 'Charls Dickens', 61),(3002, 'Harry Potter and the Philosopher\'s Stone', 'J.K. Rowling', 40),
          (3003, 'The Lion, the Witch and the Wardrobe', 'C.S Lewis', 25),(3004,'The Lrd of the Rings','J.R.R Tolkien', 37),
          (3005, 'Alice in Wonderland', 'Lewis Caroll', 12)]

cursor.executemany('''INSERT INTO books(id, Title, Author, Qty) VALUES (?,?,?,?)''', (books_))

db.commit()

def enter_newbook():
    """
    Function to add new rows to the current books database
    """
    try:
        identity = int(input('provide id for new book entry '))
        title = input('provide title for new book entry ')
        author = input('provide author for new book entry ')
        qty = input('provide qty for new book entry ')
    
        cursor.execute('''INSERT INTO books(id, Title, Author, Qty) VALUES (?,?,?,?)''', (identity, title, author, qty))
        db.commit()

    except Exception as e:
        db.rollback()
        raise e
    
def update_book():
    """
    Function to update specific columns, based on the id(primary key) provided
    """    
    choice = (input('What would you like to update?  \n    Title (press 1) \n    Author (press 2) \n    Qty (press 3)\n'))
        
    if choice == '1':
        
        try:

            id = int(input('Please enter the id of the book you would like to update: '))
            title_change = input('Please enter a new title ')
            cursor.execute('''UPDATE books SET Title = ? WHERE id = ?''',(title_change, id))
            db.commit()

        except Exception as e:
            db.rollback()
            raise e
        
    elif choice == '2':

        try:

            id = int(input('Please enter the id of the book you would like to update: '))
            author_change = input('Please enter a new author ')
            cursor.execute('''UPDATE books SET Author = ? WHERE id = ?''',(author_change, id))
            db.commit()

        except Exception as e:
            db.rollback()
            raise e

    elif choice == '3':
        
        try:
            id = int(input('Please enter the id of the book you would like to update: '))
            qty_change = int(input('Please enter a new quantity '))
            cursor.execute('''UPDATE books SET Qty = ? WHERE id = ? ''',(qty_change, id))
            db.commit()

        except Exception as e:
            db.rollback()
            raise e

    else: 

        print('Oops, incorrect input, program will reset')

def delete_book():
    """
    Function to rows rows to the current books database
    """
    try:

        deletion = int(input('Please select the id (primary key) of the row you want to delete '))
        cursor.execute('''DELETE FROM books WHERE id = ? ''', (deletion,))

    except Exception as e:
            db.rollback()
            raise e
        
def search_books():
    """
    Function to search books in the database
    """
    choice = (input('What would you like to view?  \n    Whole table (press 1)\n    A specific row (press 2) \n    The Title field (press 3) \n    The Author field (press 4) \n    The Qty field (press 5)\n'))
        
    if choice == '1':

        cursor.execute('''SELECT * FROM books''')
        rows = cursor.fetchall()
        for row in rows:
            print('{0} : {1} : {2} : {3}'.format(row[0], row[1], row[2], row[3]))
   
    elif choice == '2':
    
        id = int(input('Please enter the id of the row you would like to view: \n'))
        cursor.execute('''SELECT * FROM books WHERE id = ?''', (id,))
        print(cursor.fetchone())
        print()

    elif choice == '3':
            
        cursor.execute('''SELECT Title FROM books''')
        rows = cursor.fetchall()
        for row in rows:
            print('{0}'.format(row[0]))
        print()

    elif choice == '4':

        cursor.execute('''SELECT Author FROM books''')
        rows = cursor.fetchall()
        for row in rows:
            print('{0}'.format(row[0]))
        print()
    
    elif choice == '5':
            
        cursor.execute('''SELECT Qty FROM books''')
        rows = cursor.fetchall()
        for row in rows:
            print('{0}'.format(row[0]))
        print()
    else: 

        print('Oops, incorrect input')
        print()

def show_current_ids():
    """
    Function to show id row for purposes of user being able to know available ids in table
    """   
    print('current available id\'s:')
    cursor.execute('''SELECT * FROM books''')
    
    rows = cursor.fetchall()
    for row in rows:
        print('{0}'.format(row[0]))
    print()    

# creating a  while loop for user to make selections on whether to add, update, search or delete things within the db (relevant function carried out based on selection)
user_input = ""

while user_input != '5':

    user_input = input('What would you like to do: \n    1.Enter book (press 1) \n    2.Update book (press 2) \n    3.Delete book (press 3) \n    4.Search books (press 4) \n    5.Exit\n ').capitalize()
    
    if user_input == '1':

        # when the user wants to add a new books , a list of available id's (primary key) will be provided to enusre user is aware if id's already taken
        show_current_ids()
        # executing function to add new row with values if the user presses 1
        enter_newbook()

    elif user_input == '2':
        
        # when the user wants to update a specific record, a list of available id's (primary key) will be provided
        show_current_ids() 
        # function to execute the update will occur after view of the available ids
        update_book()      

    elif user_input == '3':
        
        # when the user wants to delete a specific row, a list of available id's (primary key) will be provided so that it is aware what is available
        show_current_ids()
        # delete books/row function executed
        delete_book()
        print('row deleted')

    elif user_input == '4':

        # when the user wants to view a specific row, a list of available id's (primary key) will be provided 
        show_current_ids()
        # function executed to view whole table, or per row, or per column 
        search_books()

    elif user_input == '5':

        print('bye')
        break

    else:
        
        print('Incorrect input, please try again')

print()

print('view of table after changes made\n')
cursor.execute('''SELECT * FROM books''')

# printing whole table after user made changes (while being in the while loop) to show how table looks after all changes if he did not view the entire table before.
rows = cursor.fetchall()
for row in rows:
    print('{0} : {1} : {2} : {3}'.format(row[0], row[1], row[2], row[3]))

# closing the db
db.close()