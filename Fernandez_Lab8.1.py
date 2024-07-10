##Robert Fernandez
##Complete
##This program will read the file text.txt and count the number of uppercase letters, lowercase letters, digits, and whitespace characters in the file.

def main():
  #open the file
  infile = open('text.txt', 'r')

  #read the file
  contents = infile.read()

  #close the file
  infile.close()

  #initialize the counters
  uppercase = 0
  lowercase = 0
  digits = 0
  whitespace = 0

  #loop through the characters in the file
  for ch in contents:
    if ch.isupper():
      uppercase += 1
    elif ch.islower():
      lowercase += 1
    elif ch.isdigit():
      digits += 1
    elif ch.isspace():
      whitespace += 1

  #display the results

  print('Uppercase letters:', uppercase)
  print('Lowercase letters:', lowercase)
  print('Digits:', digits)
  print('Whitespace characters:', whitespace)

#call the main function
main()  
