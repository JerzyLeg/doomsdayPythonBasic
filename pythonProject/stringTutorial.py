def checkIfPalindrom(word):
    length = len(word)

    # odd
    if length % 2 == 1:
        mid = length//2
        i = 1
        while i <= mid:
            if word[mid+i] == word[mid-i]:
                i = i+1
            else:
                print(word + " is not palindrom")
                return False
        print(word + " is palindrom")
        return True

    # even
    else:
        mid = length//2
        i = 1
        j = 0
        while i <= mid:
            if word[mid-i] == word[mid+j]:
                i = i+1
                j = j+1
            else:
                print(word + " is not palindrom")
                return False
        print(word + " is palindrom")
        return True


name = "Jurek"
age = 22

# \" pozwala dodawać w stringu cudzysłów
print("Hi, my \"name\" is " + name.upper() + ",\nand I am " + str(age) + ".")

# imię drukowanymi, alternatywnie małymi .lower()
name = name.upper()

# sprawdzenie jak jest zapisane imię
if name.isupper():
    print(name + " is upper")
else:
    print(name + " is lower")

# Jaka długość imienia JUREK = 5
print("Length of your name is " + str(len(name)))
# Indeksowanie znaków w stringu 0 ... len(name)-1
firstLetter = name[0]
lastLetter = name[4]

print("Your name reversed looks like this ", end="", flush=True)

# Wyświetlanie imienia od tyłu, print domyślnie jako znak kończący ustawia nową linię, więc tutaj ustawiam end="",
# żeby kończył printa pustym znakiem, flush=True drukuje instant, od razu
i = 4
while i >= 0:
    print(name[i], end="", flush=True)
    i = i-1
# Zapamiętywanie indeksu danego znaku w stringu
print("\nIndex of letter " + "\"" + lastLetter + "\" " + "is " + str(name.index(lastLetter)))

# Wypisanie indeksu, gdzie znajduje się pierwsza litera z ciągu znaków
print("Index of letter \"R\" is " + str(name.index("R")))
# Zamiana pierwszej i ostatniej litery
name = name.replace(firstLetter, lastLetter)
print(name)

# Sprawdzenie czy imie jest palindromem
checkIfPalindrom(name)

# Zamiana KUREK na KEREK
name = name.replace("U", "E")

# Sprawdzenie czy imie jest palindromem
nameIsPalindrom = checkIfPalindrom(name)