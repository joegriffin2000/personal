{--
Previously used prompts:
can you create a function to create a deck of cards using the Card data type as previously defined?

can you create a function for shuffling a deck of cards if the deck of cards is an array of Card data types as previously defined?

can you create a function to deal cards to players using the defined data types of Player and Card?
--}

import System.Random

data Suit = Hearts | Clubs | Diamonds | Spades deriving (Show, Eq)

data Rank = Two | Three | Four | Five | Six | Seven | Eight | Nine | Ten | Jack | Queen | King | Ace deriving (Show, Eq)

data Card = Card {suit :: Suit, rank :: Rank} deriving (Show, Eq)

data Player = Player {hand :: [Card], discardedCards :: [Card]} deriving (Show)

data Game = Game {players :: [Player], deck :: [Card], currentPlayer :: Int} deriving (Show)

-- Function to create a deck of cards
createDeck :: [Card]
createDeck = [Card s r | s <- [Hearts, Clubs, Diamonds, Spades], r <- [Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten, Jack, Queen, King, Ace]]

-- Function to shuffle the deck

shuffleDeck :: [Card] -> [Card]
shuffleDeck deck = do
  let randomIndex = randomR (0, length deck - 1)
  let randomCard = deck !! randomIndex
  let remainingCards = take randomIndex deck ++ drop (randomIndex + 1) deck
  let newDeck = randomCard : remainingCards
  newDeck

main = do
  putStrLn "Welcome to Go Fish"
  print (createDeck)