import random

name = input("Enter your name : ")

print(f"Hii, {name} welcome to the game")

words = [
    'algorithm', 'database', 'function', 'variable', 'constant', 'array',
    'loop', 'recursion', 'stack', 'queue', 'binary', 'decimal', 'hexadecimal',
    'bit', 'byte', 'kilobyte', 'megabyte', 'gigabyte', 'terabyte', 'petabyte',
    'compiler', 'interpreter', 'syntax', 'semantics', 'parsing', 'token', 'tree',
    'graph', 'node', 'edge', 'vertex', 'weight', 'path', 'search', 'sort',
    'insert', 'delete', 'update', 'select', 'join', 'merge', 'split', 'encrypt',
    'decrypt', 'hash', 'cipher', 'key', 'protocol', 'network', 'internet', 'intranet',
    'extranet', 'firewall', 'router', 'switch', 'hub', 'modem', 'bandwidth', 'latency',
    'throughput', 'packet', 'frame', 'data', 'information', 'knowledge', 'wisdom',
    'software', 'hardware', 'firmware', 'middleware', 'application', 'system',
    'security', 'privacy', 'authentication', 'authorization', 'integrity', 'availability',
    'confidentiality', 'nonrepudiation', 'phishing', 'malware', 'virus', 'worm', 'trojan',
    'spyware', 'adware', 'ransomware', 'backup', 'restore', 'recovery', 'redundancy',
    'scalability', 'performance', 'optimization', 'efficiency'
]

# Function will choose one random word from this list of words
word = random.choice(words)

print("Guess the characters:")

guesses = ""

turns = 20

while turns > 0:
    failed = 0

    # Printing the word with guessed characters
    for char in word:
        if char in guesses:
            print(char, end="")
        else:
            print("_", end="")
            failed += 1

    print()

    if failed == 0:
        print("You win!")
        print("The word is:", word)
        break

    # Taking input from the user
    guess = input("Guess a character: ")
    guesses += guess

    # Checking if the guessed character is not in the word
    if guess not in word:
        turns -= 1
        print("Wrong")
        print(f"You have {turns} more guesses")

    # Checking if the user has run out of turns
    if turns == 0:
        print("You lose")
        print(f"The word was: {word}")

