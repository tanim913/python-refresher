def minion_game(string):
    length = len(string)
    vowel = const = 0
    for i in range(length):
        if string[i] in 'AEIOU':
            vowel = vowel + length - i
        else:
            const = const + length - i
    if (const > vowel):
        print(f"Stuart {const}")
    elif (const == vowel):
        print("Draw")
    else:
        print(f"Kevin {vowel}")
