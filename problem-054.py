#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Poker
# The file, poker.txt, contains one-thousand random hands dealt to two players.
# How many hands does Player 1 win?

# 1. High Card
# 2. One Pair + High Card
# 3. Two Pairs + High Card
# 4. Three of a Kind
# 5. Straight
# 6. Flush
# 7. Full House
# 8. Four of a Kind
# 9. Straight Flush / Royal Flush

import sys
import time
ti=time.time()

# ==============================================================================

class Card():
    pic = None
    suit = None
    val = None

    def __init__(self, pic):
        self.pic = pic
        self.val = self.value(pic[0])
        self.suit = pic[1]

    def value(self, x):
        hm = { 'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10 }
        if x in hm:
            return hm[x]
        else:
            return int(x)

# ==============================================================================

class Hand():
    cards = None
    cards_group_by_kind = None
    statistics = None
    
    def __init__(self):
        self.cards = []
        self.cards_group_by_kind = {}
        
        self.statistics = {
            'one_pair': None,
            'two_pairs': None,
            'three_of_a_kind': None,
            'straight': None,
            'flush': None,
            'four_of_a_kind': None,
            'full_house': None,
            'straight_flush': None
        }
        
    def has_one_pair(self, card):
        return len(self.cards_group_by_kind[card.val]) == 2

    def has_three_of_a_kind(self, card):
        return len(self.cards_group_by_kind[card.val]) == 3

    def has_four_of_a_kind(self, card):
        return len(self.cards_group_by_kind[card.val]) == 4
    
    def has_flush(self):
        suits = map(lambda c: c.suit, self.cards)
        return all(x == suits[0] for x in suits)

    def has_straight(self):
        vals = map(lambda c: c.val, self.cards)
        vals.sort()

        counter = 0
        for idx, v in enumerate(vals[:-1]):
            if (v + 1) != vals[idx+1]:
                break
            counter += 1
        
        # with exceptional case [2 3 4 5 A]
        if counter == 4 or (counter == 3 and vals[-1] == 14 and vals[0] == 2):
            return True

        return False

    def is_one_pair_exist(self):
        return self.statistics['one_pair'] is not None
    
    def is_two_pairs_exist(self):
        return self.statistics['two_pairs'] is not None
    
    def is_three_of_a_kind_exist(self):
        return self.statistics['three_of_a_kind'] is not None
    
    def got_one_pair(self, card):
        self.statistics['one_pair'] = self.cards_group_by_kind[card.val][:]
        
    def got_two_pairs(self, card):
        pair1_v = card.val # 1st pair value
        pair2_v = self.statistics['one_pair'][0].val # 2nd pair value
        
        self.statistics['two_pairs'] = {}
        self.statistics['two_pairs'][pair1_v] = self.cards_group_by_kind[card.val][:]
        self.statistics['two_pairs'][pair2_v] = self.statistics['one_pair'][:]
        # # remove
        self.statistics['one_pair'] = None
    
    def got_three_of_a_kind(self, card):
        self.statistics['three_of_a_kind'] = self.cards_group_by_kind[card.val][:]
        self.statistics['one_pair'] = None
    
    def got_full_house_to_the_three_of_a_kind_hand(self, card):
        fh_three = self.statistics['three_of_a_kind'][:]
        fh_two = self.cards_group_by_kind[card.val][:]
        self.statistics['full_house'] = { 3: fh_three, 2: fh_two }
        # remove
        self.statistics['three_of_a_kind'] = None
    
    def got_full_house_to_the_two_pairs_hand(self, card):
        self.statistics['full_house'] = { 3: None, 2: None }
        for v in self.statistics['two_pairs']:
            k = 3 if v == card.val else 2
            self.statistics['full_house'][k] = self.statistics['two_pairs'][v][:]
        # remove
        self.statistics['two_pairs'] = None
    
    def got_four_of_a_kind(self, card):
        self.statistics['four_of_a_kind'] = self.cards_group_by_kind[card.val]
        self.statistics['three_of_a_kind'] = None
    
    def got_straight(self):
        self.statistics['straight'] = self.cards

    def got_flush(self):
        self.statistics['flush'] = self.cards
    
    def got_straight_flush(self):
        self.statistics['straight_flush'] = self.cards
        self.statistics['straight'] = None
        self.statistics['flush'] = None

    def analyse(self, card):

        if self.has_one_pair(card):
            # got [Two Pairs]
            if self.is_one_pair_exist():
                self.got_two_pairs(card)
            # got [Full House]
            elif self.is_three_of_a_kind_exist():
                self.got_full_house_to_the_three_of_a_kind_hand(card)
            # got [One Pair]
            else:
                self.got_one_pair(card)

        elif self.has_three_of_a_kind(card):
            # got [Full House]
            if self.is_two_pairs_exist():
                self.got_full_house_to_the_two_pairs_hand(card)
            # got [Three of a Kind]
            elif self.is_one_pair_exist():
                self.got_three_of_a_kind(card)
        
        elif self.has_four_of_a_kind(card):
            # got [Four of a Kind]
            self.got_four_of_a_kind(card)
        
        if len(self.cards) == 5:
            if self.has_flush():
                self.got_flush()
            elif self.has_straight():
                self.got_straight()

            if self.has_flush() and self.has_straight():
                self.got_straight_flush()

    def add_card(self, card):
        if card.val not in self.cards_group_by_kind:
            self.cards_group_by_kind[card.val] = []

        self.cards.append(card)
        self.cards_group_by_kind[card.val].append(card)
        # update [statistics]
        self.analyse(card)

    def bits_to_num(self, bits):
        return int(str(bits[0]).zfill(2) + str(bits[1]).zfill(4) + str(bits[2]).zfill(6))
        
    def best(self):
        bits = [0,0,0]
        
        k = 'high_card' # default
        for item in self.statistics:
            if self.statistics[item] is not None:
                k = item
        
        if k == 'straight_flush' or k == 'flush' or k == 'straight' or k == 'high_card':
            vals = map(lambda c: c.val, self.cards)
            vals.sort(reverse=True)
            
            bits[1] = vals[0] # high

            if k == 'straight':
                bits[0] = 5
            elif k == 'flush':
                bits[0] = 6
            elif k == 'straight_flush':
                bits[0] = 9
            elif k == 'high_card':
                bits[0] = 1
                bits[1] = str(vals[0]).zfill(2) + str(vals[1]).zfill(2)
                bits[2] = str(vals[2]).zfill(2) + str(vals[3]).zfill(2) + str(vals[4]).zfill(2)
            
        elif k == 'four_of_a_kind':
            bits[0] = 8
            bits[1] = self.statistics[k][0].val
            
        elif k == 'full_house':
            bits[0] = 7
            bits[1] = self.statistics[k][3][0].val
        
        elif k == 'three_of_a_kind':
            bits[0] = 4
            bits[1] = self.statistics[k][0].val

        elif k == 'one_pair':
            
            bits[0] = 2
            bits[1] = self.statistics[k][0].val
            
            pic1 = self.statistics[k][0].pic
            pic2 = self.statistics[k][1].pic
            
            rest_vals = []
            for c in self.cards:
                if c.pic != pic1 and c.pic != pic2:
                    rest_vals.append(c.val)
            
            rest_vals.sort(reverse=True)
            
            bits[2] = ''
            for v in rest_vals:
                bits[2] += str(v).zfill(2)
            
        elif k == 'two_pairs':
            bits[0] = 3
            
            pl = []
            high = 0
            
            for p in self.statistics[k]:
                pl.append(p)
            p1 = max(pl)
            p2 = min(pl)
            
            for c in self.cards:
                if c.val != p1 and c.val != p2:
                    high = c.val
                
            bits[1] = str(p1).zfill(2) + str(p2).zfill(2)
            bits[2] = high
            
        return self.bits_to_num(bits)

# ==============================================================================

def build_hand(cards_str):
    hand = Hand()
    for s in cards_str.split(' '):
        hand.add_card(Card(s))
    return hand

# ==============================================================================

def solution(file_path):
    lines = open(file_path, 'r').read().strip().split('\n')
    wins = 0
    
    for row in lines:
        
        player1 = row[0:14]
        player2 = row[15:]
        
        hand1 = build_hand(player1)
        hand2 = build_hand(player2)
        
        b1 = hand1.best()
        b2 = hand2.best()
        win = b1 > b2
        
        # print player1, ' vs ', player2, (' -> Win' if win else ' -> Lost')
        
        wins += (1 if win is True else 0)

    return wins

# ==============================================================================

if __name__ == '__main__':
    print 'Answer is:', solution('data/p054_poker.txt')
