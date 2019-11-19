#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def Menu():
    print('--------------')
    print('Bookmar MENU')
    print('1. Add Bookmark')
    print('2. Edit Bookmark')
    print('3. Delete Bookmark')
    print('4. View Bookmark')
    print('5. exit')
    print('--------------')

bookmarks =[]

index2 = 0
exit = False

while(exit != True):
    index2 = 0
    
    Menu()
    
    input1 = input("Choose a Menu: ")
    
    if input1 == '1':
        
        input_bookmark = input("Enter a bookmark: ")
        bookmarks.append(input_bookmark)
        
    elif input1 =='2':
        
        for books in bookmarks:
            index2+=1
            print(index2,'.', books)
        choose_bookmark = input("Enter a bookmark: ")
        index = bookmarks.index(choose_bookmark)
        
        if choose_bookmark in bookmarks:
            
            bookmarks.remove(choose_bookmark)
            edit_bookmark = input('enter the new bookmark')
            bookmarks.insert(index, edit_bookmark)
            print(bookmarks)
        for books in bookmarks:
            index2+=1
            print(index2,'.', books) 
        
    
    elif input1 =='3':
    
        for books in bookmarks:
            index2+=1
            print(index2, books)
        choose_bookmark = input("Enter a bookmark: ")
        
        bookmarks.remove(choose_bookmark)
        for books in bookmarks:
            index2= bookmarks.index(books)
            print(index2,'.', books)
            
    elif input1 =='4':
        
        for books in bookmarks:
            index2+=1
            print(index2,'.', books)
   
    elif input1 =='5':
        
        exit = True
    

