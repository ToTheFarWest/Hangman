import random
guesses_left = 10
words = ["hippocampus", "Trump", "Truman", "Pogo", "Domination", "Hitler", "hippopotomonstrosesquippedaliophobia", "Satan", "Freshmen", "Cancer", ]
wrong = []
def main():
    secret_word = random.choice(words)
    secret_word = secret_word.lower()
#    print(secret_word)
    print("The word is %d letters long" % len(secret_word))
    dashes = ""
    dashes = dashes.ljust(len(secret_word),'-')
#    print(len(dashes))
    done = False
    while not done:
        print(str(guesses_left) + " incorrect guesses left.")
        print(dashes + '        ' + str(wrong))
        guess = get_guess(secret_word)
        dashes = update_dashes(secret_word, dashes, guess)
        if dashes == secret_word:
            print("CONGRATS U WON")
            print("The word was " + secret_word)
            done = True
        if guesses_left == 0:
            print("MISSION FAILED WE SHALL GET ZEM NEXT TOIME!")
            done = True
           
def get_guess(word):
    global wrong
    global guesses_left
    while True:
        guess = input("Guess: ")
        guess = guess.lower()
        if guess=='debug()':
            print(word)
        elif len(guess) != 1:
            print("Your guess must have exactly one character!")
        elif not guess.isalpha():
            print("Your guess must be a letter!")
        elif guess not in word:
            print("That letter is not in the secret word!")
            guesses_left -= 1
            wrong.append(guess)
            break
        else:
            print("That letter is in the secret word!")
            return guess
            break
        
def update_dashes(word,dashes,guess):
    for i in range(len(word)):
#DEBUG        print i
        if word[i] == guess:
#DEBUG            print("Called!")
            new = dashes[:i]+guess+dashes[i+1:]
            dashes = new
#DEBUG            print(dashes)
    return dashes
        
    
if __name__ == "__main__":
    main()
