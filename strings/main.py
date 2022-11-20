# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# Part 1

## Score

scorer_1_full_name = 'Ruud Gullit'
scorer_2_full_name = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = scorer_1_full_name + ' ' + str(goal_0) + ', ' + scorer_2_full_name + ' ' + str(goal_1)

print (scorers)
print ()

## Reporting

report = F"""{scorer_1_full_name} scored in the {goal_0}nd minute
{scorer_2_full_name} scored in the {goal_1}th minute"""

print (report)

print()

# Part 2

player = 'Frank Rijkaard'

"""
first_name = (player.split()[0])
last_name = (player.split()[1])

print(first_name)
print(last_name)
"""

#first_name_start = player.find('Frank')
first_name = player[:player.find(" ")]
#first_name = player [0:5]
print(first_name)

#last_name_start = player.find('Rijkaard')
#print(last_name_start)

last_name_len = len('Rijkaard')
print(last_name_len)

#print(last_name_start + last_name_len)

#last_name = player [6:14]
#print(last_name)

last_name = player[player.find(" ") +1:]
print(last_name)

print()

## Chant

first_name_initial = first_name [0]

name_short = F"{first_name_initial}. {last_name}"
print(name_short)

print()

first_name_len = len(first_name)
print(first_name_len)

# chant = ((F"{first_name}! ") *first_name_len) [:-1]

chant_name = F"{first_name}! "
chant_beta = chant_name *first_name_len

chant = chant_beta [:-1]
print(chant)

good_chant = chant [-1] != ' '
print(good_chant)
