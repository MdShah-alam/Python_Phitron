
file = open ( 'words.dat' , 'w' ) 
word = ''
word =input( 'Enter a word (enter END to quit): ')
while word != '' : 
    file.write ( word + '\n' ) 
    word =input( 'Enter a word (enter END to quit): ')
file.close ( )