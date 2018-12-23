# Black_Jack_In_Python

This is a simple version game of Black Jack.

We have the computer dealer, and then the human player at the keyboard and a deck of 52 cards.

# Special rules
An ACE can be worth either 11 or 1, automatically picked to give the best possible combination. 
Any face card (J,Q,K) is worth 10, and any other card is worth is nominal value.

# Flow
• Make a bet (deal start)

• Dealer give you two cards, which form your hand, and two cards to themselves. one of the dealer's cards will be hidden at first. To win, you need to ensure the combined value of your cards is greater than of the dealer.

• You can add more cards, one by one, by choosing to HIT, but be wary: you must never exceed 21. Whoever gets more than 21 loses automatically. Once you're ready to play the hand, click STAND. Dealer will then reveal their hidden card, and must always Hit until game over.

• Whoever gets exactly 21, in most cases, wins. A tie (PUSH) will simply refund the bet to the player. Going over 21 (busting) is an instant loss.

• You win by making the dealer go over 21 or by having a higher value, such as 20 against the dealer's 19. BlackJack, a natural 21 (with the two initial cards) beats any combination except another Blackjack, even a non-Blackjack 21.

• Winning will reward you with double your bet - for example, $2000 for a bet of $1000, to $1000 of pure benefit. A Blackjack has a slightly higher payoff of 3 to 2, such as $2500 for a bet of $1000, or $1500 of a pure benefit.


The above functions finished, below funcs may be added into a future version...
---
• Unlike the dealer, you can DOUBLE your bet once cards are dealt (but before you Hit or Stand). You will have to take exactly one more card, and then immediately Stand. If you get two cards of the same value (such as 7 and 7, A and A, or even 10 and K), you can play that hand, or choose to SPLIT.

When you Split, you make two new hands, each with the bet equal to your initial bet, composed of one of your duplicate cards and one new card each. Once Split, each new hand will be played like usual, against the same hand of the dealer, with separate win or loss. You can even Split again if possible, up to 3 times per deal. Both Double and Split again if possible, up to 3 times per deal. Both Double and Split can only be done if you have enough money in the bank to increase your bet.
