import re

#* Metacharacters (Need to be escaped)
#    . ^ $ * + ? { } [ ] \ | ( )

# @ This is to specify the char
# . -Any Char Except Newln
#\d -digit(0-9)
#\D -Not a Digit
#\w -Word Char (a-z, A-z ,0-9 ,_)
#\W -Not Word Char
#\s -Whitespace (space, tab, newline)
#\S -Not Whitespace
#[] -thing in the []

# @ This is to combline with the upper collumn to specify the char
#\b -Word Boundaly(The char after space)
#\B -Not a Word Boundary
# ^ -Beginning of a String
# $ -Ending of String

# Tester@1

Searchset="""abcdefghijklmnopqurstuvwxyz
ABCDEFGHIJKLMNOPQURSTUVWXYZ
Bombier Gradier
11587-9855-654
Microsoft
KIEJ AL A8
HAA HA HAAA 84 """

pattern = re.compile(r'A[0-9]')
matches = pattern.finditer(Searchset)
for match in matches:
    print (match)