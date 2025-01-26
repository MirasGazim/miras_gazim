import random 

SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')

NCARDS = 8

def getCard(deckListIn):
    thisCard = deckListIn.pop()  # Draw one card from the top of the deck and return it
    return thisCard

def shuffle(deckListIn):
    deckListOut = deckListIn.copy()  # Create a copy of the starting deck
    random.shuffle(deckListOut)
    return deckListOut

# Main code
print('Welcome to Higher or Lower.')
print('You have to choose whether the next card to be shown will be higher or lower than the current card.')
print('Getting it right adds 20 points; get it wrong and you lose 15 points.')
print('You have 50 points to start.')
print()

startingDeckList = [] 
for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank': rank, 'suit': suit, 'value': thisValue + 1}
        startingDeckList.append(cardDict)

score = 50

while True:  # Multiple games
    print()
    gameDeckList = shuffle(startingDeckList)  
    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']
    print('Starting card is:', currentCardRank + ' of ' + currentCardSuit)
    print()

    for cardNumber in range(0, NCARDS): 
        answer = input('Will the next card be higher or lower than the ' + currentCardRank + ' of ' + currentCardSuit + '? (enter h or l): ')
        answer = answer.casefold()  # Convert to lowercase
        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']
        print('Next card is:', nextCardRank + ' of ' + nextCardSuit)

        if answer == 'h':
            if nextCardValue > currentCardValue:
                print('You got it right, it was higher')
                score += 20
            else:
                print('Sorry, it was not higher')
                score -= 15
        elif answer == 'l':
            if nextCardValue < currentCardValue:
                print('You got it right, it was lower')
                score += 20
            else:
                print('Sorry, it was not lower')
                score -= 15

        print('Your score is:', score)
        print()
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue

    goAgain = input('To play again, press ENTER, or "a" to quit: ')
    if goAgain == 'a':
        break

print('OK bye')

# class SecondNum:
#     def __init__(self, element):
#         self.arr = element
#         self.c = None
       
#         unique_elements = list(set(self.arr))
        
#         if len(unique_elements) < 2:
#             self.c = "Недостаточно уникальных элементов для определения второго по величине." 
#             return  
      
#         unique_elements.sort() 

#         self.c = unique_elements[1] 
        

# walf = SecondNum([12, 45, 67, 34, 78, 1])
# print(walf.c)

# miras = SecondNum([348, 34590, 34643, 2323, 66])
# print(miras.c)

    
# class Cat:

#     def __init__(self, name, breed = 'pers', age = 1 , color = 'white'):   
#         print('hello new object is ', self, name, breed, age, color)
#         self.name = name 
#         self.age = age
#         self.breed = breed
#         self.color = color

# walt = Cat('miras')

# print(walt.age)