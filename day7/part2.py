CARDS = 'J23456789TQKA'
NEW_CARDS = 'ABCDEFGHIJKLM'

def main():
    data = []
    with open('input.txt') as infile:
        for line in infile.read().splitlines():
            record = line.split(' ')
            # Convert the hand so that it can be directly compared
            record[0] = hand_type(record[0]) \
                    + record[0].translate(str.maketrans(CARDS, NEW_CARDS))
            record[1] = int(record[1])
            data.append(record)

    data.sort()
    total = 0
    i = 1
    for record in data:
        total += i * record[1]
        i += 1
    print(total)

def hand_type(hand):
    card_count = {}
    for card in hand:
        if card in card_count:
            card_count[card] += 1
        else:
            card_count[card] = 1

    if 'J' in card_count:
        # Substitute wild cards
        num_wild = card_count.pop('J')
        nums = sorted(list(card_count.values()))
        # Add wild cards to the largest group
        try: nums[-1] += num_wild
        # All wild
        except IndexError: nums.append(5)
    else:
        nums = list(card_count.values())
        
    if 5 in nums:
        # Five of a kind
        return '6'
    if 4 in nums:
        # Four of a kind
        return '5'
    if 3 in nums:
        if 2 in nums:
            # Full house
            return '4'
        # Three of a kind
        return '3'
    # Two pair, one pair, or high card
    return str(list(nums).count(2))

main()
