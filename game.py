import random

WORD = ["Chev", "giraffe", "roadtrip", "dynamite", "eternal"]

word = random.choice(WORD)
correct = word

clue = word[0] + word[(len(word)-1):(len(word))]
letter_guess = ''
word_guess = ''
store_letter = ''
count = 0
limit = 7

print('guess the secret word!')
print('you have 7 tries')

while count < limit:
    letter_guess = input('guess a letter: ')

    if letter_guess in word:
        print('correct')
        store_letter += letter_guess
        print(letter_guess)
        count += 1

    if letter_guess not in word:
        print('no')
        count += 1

print('\n')
print('you have guessed',len(store_letter),'letters correctly.')
print('the letters are: ', store_letter)

word_guess = input('now try and guess the whole word: ')
while word_guess:
    if word_guess.lower() == correct:
        print('yay! good job!')
        break

    elif word_guess.lower() != correct:
        print('wrong! The answer was,', word)
        break
