# Initial map setup
row1 = ['⬜️', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']
map = [row1, row2, row3]
# Display the initial map
user_input = input('Enter a position: Example "B2 or A1"')
letter = user_input[0].lower()
abc = ['a','b','c']
letter_index = abc.index(letter)
number_index = int(user_input[1]) - 1
map[letter_index][number_index] = 'X'

# Display the updated map
print('Hiding your treasure! X marks the spot.')
print(f"{row1}\n{row2}\n{row3}")
input('press')
