import System.Random
import System.Random.Shuffle
import Data.List
import Control.Monad ( foldM )

-- Define data types for suits, ranks, cards, players, and the game
data Suit = Hearts | Diamonds | Clubs | Spades deriving (Show, Eq, Enum)
data Rank = Two | Three | Four | Five | Six | Seven | Eight | Nine | Ten | Jack | Queen | King | Ace deriving (Show, Eq, Enum)
data Card = Card { suit :: Suit, rank :: Rank } deriving (Show, Eq)
data Player = Player { playerName :: String, playerHand :: [Card], discardedHand :: [Card] } deriving (Show)
data Game = Game { players :: [Player], deck :: [Card] } deriving (Show)

-- Generate a standard deck of cards
generateDeck :: [Card]
generateDeck = [Card s r | s <- [Hearts .. Spades], r <- [Two .. Ace]]

-- Shuffle a deck using Fisher-Yates algorithm
shuffleDeck :: [Card] -> IO [Card]
shuffleDeck deck = do
    gen <- getStdGen
    return $ take (length deck) $ nub $ shuffle' deck (length deck) gen

-- Deal cards to players
dealCards :: [Card] -> Int -> ([Card], [Player])
dealCards deck numPlayers = (remainingDeck, players)
  where
    playerHands = chunkList numPlayers remainingDeck
    players = map (\(name, hand) -> Player name hand []) $ zip playerNames playerHands
    remainingDeck = drop (numPlayers * 7) deck

-- Chunk a list into sublists of a given size
chunkList :: Int -> [a] -> [[a]]
chunkList _ [] = []
chunkList n xs = take n xs : chunkList n (drop n xs)

-- Player names for a two-player game
playerNames :: [String]
playerNames = ["Player 1", "Player 2"]

-- Function to simulate a Go Fish game
playGoFish :: IO ()
playGoFish = do
    shuffledDeck <- shuffleDeck generateDeck
    let (remainingDeck, initialPlayers) = dealCards shuffledDeck 2
        initialGame = Game initialPlayers remainingDeck
    finalGame <- playTurns initialGame
    putStrLn "Game Over!"
    putStrLn $ "Final Scores: " ++ show (calculateScores finalGame)

-- Function to calculate scores at the end of the game
calculateScores :: Game -> [(String, Int)]
calculateScores game = map (\player -> (playerName player, length (discardedHand player) `div` 2)) (players game)

-- Function to play turns in the game
playTurns :: Game -> IO Game
playTurns game = do
    putStrLn $ "Current State: " ++ show game
    if null (deck game) && all (null . playerHand) (players game)
        then return game
        else do
            newGame <- playTurn game
            playTurns newGame

-- Function to play a single turn
playTurn :: Game -> IO Game
playTurn game = do
    putStrLn "-------------------------------"
    putStrLn "Next Turn:"
    (newGame, _) <- foldM playPlayer (game, 0) (players game)
    return newGame

-- Function to handle a player's turn
playPlayer :: (Game, Int) -> Player -> IO (Game, Int)
playPlayer (game, penalty) player = do
    putStrLn $ playerName player ++ "'s turn."
    putStrLn $ "Hand: " ++ show (playerHand player)
    putStrLn "Ask another player for a card (Rank):"
    rankInput <- getLine
    let rankAskedFor = read rankInput
    case filter (\p -> not (null (playerHand p)) && any (\c -> rank c == rankAskedFor) (playerHand p) && p /= player) (players game) of
        [] -> do
            putStrLn "Go Fish! Penalty!"
            let (newDeck, drawnCard) = drawCard (deck game)
                newPenalty = if rank drawnCard == rankAskedFor then penalty + 1 else penalty
                newPlayerHand = drawnCard : playerHand player
                newPlayer = player { playerHand = newPlayerHand }
                newGame = game { deck = newDeck, players = replacePlayer player newPlayer (players game) }
            return (newGame, newPenalty)
        (otherPlayer:_) -> do
            putStrLn $ "Player has the card. Go again!"
            let (newOtherPlayerHand, drawnCard) = drawCard (playerHand otherPlayer)
                newPlayerHand = drawnCard : playerHand player
                newOtherPlayer = otherPlayer { playerHand = newOtherPlayerHand }
                newPlayer = player { playerHand = newPlayerHand }
                newGame = game { players = replacePlayer otherPlayer newOtherPlayer $ replacePlayer player newPlayer (players game) }
            if length (filter (\c -> rank c == rankAskedFor) (playerHand otherPlayer)) > 1
                then do
                    putStrLn $ "Player completed a pair! Cards added to discarded hand."
                    let updatedGame = game { players = replacePlayer otherPlayer (otherPlayer { discardedHand = drawnCard : drawnCard : discardedHand otherPlayer }) (players game) }
                    return (updatedGame, penalty)
                else return (newGame, penalty)

-- Function to draw a card from a deck
drawCard :: [Card] -> ([Card], Card)
drawCard [] = error "Deck is empty!"
drawCard (c:cs) = (cs, c)

-- Function to replace a player in the list of players
replacePlayer :: Player -> Player -> [Player] -> [Player]
replacePlayer oldPlayer newPlayer playersList = map (\p -> if p == oldPlayer then newPlayer else p) playersList

-- Main function to start the game
main :: IO ()
main = playGoFish