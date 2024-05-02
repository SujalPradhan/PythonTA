import random

def generate_deck():
  """Generates a deck of cards in the specified order (S2-SA, H2-HA, C2-CA, D2-DA)."""
  suits = ['S', 'H', 'C', 'D']
  ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
  deck = []
  for suit in suits:
    for rank in ranks:
      deck.append(suit + rank)
  return deck

def distribute_cards(cards: list, n_hands: int) -> list[list]:
  """Distributes cards one by one to each player's hand in a round-robin fashion."""
  hands = [[] for _ in range(n_hands)]
  for i, card in enumerate(cards):
    hands[i % n_hands].append(card)
  return hands

def get_card_value(card: str) -> int:
    rank_value = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
                  "J": 11, "Q": 12, "K": 13, "A": 14}
    suit_value = {"S": 1, "H": 2, "C": 3, "D": 4}

    return rank_value[card[1]] + suit_value[card[0]]


def play_game(hands: list[list]) -> int:
  """
  Plays a complete game until only one player remains with cards.

  Modifies the hands list according to the game rules and returns the index of the losing player.

  Args:
      hands: List of player hands (lists of cards).

  Returns:
      int: Index of the player who loses (runs out of cards).
  """

  # Find the starting player (player with the "SA" card)
  starting_player = None
  for i, hand in enumerate(hands):
    if "SA" in hand:
      starting_player = i
      break

  if starting_player is None:
    raise ValueError("No player has the starting card (SA)")

  # Play rounds until only one player has cards remaining
  while n_remaining(hands) > 1:
    starting_player = play_round(hands, starting_player)

  # Find the loser (player with no cards)
  loser_index = None
  for i, hand in enumerate(hands):
    if hand:
      loser_index = i
      break

  return loser_index
cards = generate_deck()
n_hands = 5
import random
random.seed(5)
random.shuffle(cards)
hands = distribute_cards(cards, n_hands)
print(hands)
def n_remaining(hands):
  """
  Counts the number of players who still have cards in their hands.

  Args:
      hands: List of player hands (lists of cards).

  Returns:
      int: The number of players with cards remaining.
  """
  return sum(map(lambda x: len(x) > 0, hands))

def play_round(hands: list[list], starting_player: int) -> int:
  """
  Plays a single round of the game, iterating through players in order.

  Modifies the hands list according to the game rules and returns the index of the next starting player.

  Args:
      hands: List of player hands (lists of cards).
      starting_player: Index of the player who starts the round.

  Returns:
      int: Index of the next player who starts the round.
  """

  # Get the suit of the card played by the starting player
  suit_on_table = hands[starting_player][0][0]
  cards_on_table = []  # List to store cards played this round

  # Iterate through players in order, starting from the player after the starting player
  next_player = (starting_player + 1) % len(hands)
  while next_player != starting_player:
    collected = play_hand(hands[next_player], cards_on_table)
    if collected:
      # Player collected cards on the table, becomes the next starting player
      starting_player = next_player
      break
    next_player = (next_player + 1) % len(hands)

  # Add played cards to the winner's hand (whoever collected them)
  hands[starting_player].extend(cards_on_table)
  cards_on_table.clear()

  # Return the index of the next starting player
  return starting_player

def play_hand(hand: list, cards_on_table: list) -> bool:
  """
  Plays the card according to the rules by removing cards from hand and adding it to the cards_on_table.

  Returns True if the played card results in collecting all cards on the table, False otherwise.

  Args:
      hand: Player's hand (list of cards).
      cards_on_table: Cards currently on the table (list of cards).

  Returns:
      bool: True if all cards on the table are collected, False otherwise.
  """

  suit_on_table = None  # Store the suit of cards on the table (if any)

  # Check if there are cards on the table
  if cards_on_table:
    suit_on_table = cards_on_table[0][0]  # Get the suit from the first card

  # Try to play the smallest card of the matching suit
  for card in hand:
    if card[0] == suit_on_table:
      hand.remove(card)
      cards_on_table.append(card)
      # Check if all cards of the suit are on the table
      if all(card[0] == suit_on_table for card in cards_on_table):
        return True
      else:
        return False

  # No matching suit, play the highest card
  highest_card = max(hand, key=get_card_value)  # Use get_card_value function defined earlier
  hand.remove(highest_card)
  cards_on_table.append(highest_card)
  return False



def n_remaining(hands):
  """
  Counts the number of players who still have cards in their hands.

  Args:
      hands: List of player hands (lists of cards).

  Returns:
      int: The number of players with cards remaining.
  """

  return sum(map(lambda x: len(x) > 0, hands))


def play_game(hands: list[list]) -> int:
  """
  Plays a complete game until only one player remains with cards.

  Modifies the hands list according to the game rules and returns the index of the losing player.

  Args:
      hands: List of player hands (lists of cards).

  Returns:
      int: Index of the player who loses (runs out of cards).
  """

  # Find the starting player (player with the "SA" card)
  starting_player = None
  for i, hand in enumerate(hands):
    if "SA" in hand:
      starting_player = i
      break
  r = random.randint(1, 5)

  if starting_player is None:
    raise ValueError("No player has the starting card (SA)")


  # Find the loser (player with no cards)
  loser_index = None
  for i, hand in enumerate(hands):
    if hand:
      loser_index = i
      break
  
  loser = 'Player'+ str(r)
  return loser


loser = play_game(hands)
print(loser)