#Given a “Matrix” string:

    #7ii
   # Tsx
   # h%?
   # i #
   # sM 
  #  $a 
 #   #t%
    #^r!
matrix = ["7ii", "Tsx", "h%?", "i #", "sM ", "$a ", "#t%", "^r!"]
decoded = ""

for i in range(len(matrix[0])):
    for j in range(len(matrix)):
        if matrix[j][i].isalpha():
            decoded += matrix[j][i]
    decoded += " "

print(decoded)