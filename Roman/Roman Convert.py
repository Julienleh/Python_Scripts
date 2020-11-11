# Python_Scripts
#  Posted from EduTools plugin
# put your python code here
# On definie les variables
# On met des les regles par groupe
# puis on les combine pour faire les chiffres yeah!

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000


def Roman_five(number):
    if int(number) % 5 == 0 :
        if int(number) % 10 != 0:
            roman_number= "V"
        else:
            roman_number = ""
    else:
        if int(number) % 5 <4 :
            roman_number = int(number)%5*"I"
        else :
            roman_number = "IV"
    return(roman_number)

def Roman_ten(number):
    if int(number) % 10 == 0 :
        if int(number) % 50 != 0:
            if int(number) % 50 == 40:
                roman_number= ""
            else:
                roman_number= int(int(number)/10)*"X"
        else:
            roman_number = ""
    else:
        if int(number) % 10 <6:
            roman_number = int((int(number)/10))*"X" + Roman_five(int(number))
        else :
            if int(number) % 10 <9 :
                roman_number = int((int(number)/10))*"X" + "V" + (int(number) % 5)*"I"
            else :
                if int(number) %10 == 9:
                    roman_number = "IX"
                else :
                    roman_number = "X"
    return(roman_number)

def Roman_fifty (number):
    if int(number) % 50 == 0:
       if int(number) % 100 !=0:
            roman_number= "L"
       else :
            roman_number=""
    else:
        if int(number) % 50 < 40:
            roman_number= int(int(number)/50)*"L" + Roman_ten(int(number)%50)
        else :
            roman_number = "XL"+ Roman_ten((int(number)-40) % 50)
    return(roman_number)

def Roman_hundred(number):
    if int(number) % 100 == 0 :
        if int(number) % 500 != 0:
            if int(number) % 500 == 400:
                roman_number= ""
            else:
                roman_number= int(int(number)/100)*"C"
        else:
            roman_number = ""
    else:
        if int(number) % 100 <50:
            roman_number = int((int(number)/100))*"C" + Roman_fifty(int(number))
        else :
            if int(number) % 100 <90 :
                roman_number = int((int(number)/100))*"C" + "L" + Roman_fifty(int(number) % 50)
            else :
                roman_number = int((int(number)/100))*"C" + "XC" + Roman_ten(int(number)%10)
    return(roman_number)

def Roman_fivehundreds (number):
    if int(number) % 500 == 0:
       if int(number) % 1000 !=0:
            roman_number= "D"
       else :
            roman_number=""
    else:
        if int(number) % 500 < 400:
            roman_number= Roman_hundred(int(number)%500)
        else :
            roman_number = "CD"+ Roman_hundred((int(number)-400) % 500)
    return(roman_number)

def Roman_thousand(number):
    if int(number) % 1000 == 0 :
        roman_number= int(int(number)/1000)*"M"
    else:
        if int(number) % 1000 <500:
            roman_number = int((int(number)/1000))*"M" + Roman_fivehundreds(int(number))
        else :
            if int(number) % 1000 <900 :
                roman_number = int((int(number)/1000))*"M" + "D" + Roman_fivehundreds(int(number) % 500)
            else :
                roman_number = int((int(number)/1000))*"M" + "CM" + Roman_hundred(int(number)%100)
    return(roman_number)


test_number = input ()
roman_number_result = Roman_thousand(test_number)
print(roman_number_result)

