# Strings

## Scorers

I get uncalled-for parentheses in my output.
I get uncalled for apostrophes in my output.
I get uncalled-for commas in my output.

By converting the integers to strings, I no longer get the uncalled-for parentheses and commas.
I was able to include spaces within between scorer names and minutes by explicitely adding <' '>, but am unsure whether maybe there's a more elegant way to add the spaces.

I initially used specific strings for Py to find for me, but there's a more generic method that's not dependant on the content of the string it's retrieving from:

~~~py
first_name = player[:player.find(" ")]
last_name = player[player.find(" ") +1:]
~~~

### Previous attempts

~~~~py
scorers = (score1) + ', ' + (score2)

scorers = (scorer_1_full_name, goal_0) + (scorer_2_full_name, goal_1)
~~~~

## Report

I must use an f-string, but don't know how to make it.

I finally made the f-string by having an F before the string (without a space after the F).
I made it into a multi-line string by having everything after the F in triple double-quotes.

The multi-line string led to the output of the second score report ending up after a vertical line. I must fix this.
By removing the '\n' command and just breaking the second score report into a new line, the vertical line to the left was avoided.

I made it happen, I got the 'F. Rijkaard', but on my way to it I've had to jump through a few hoops just to make Py get me the last name (incl a subtraction). There must be a more elegant way.
I've asked about it in Slack. We'll see.

### Split

By using the following, I make Py retrieve the 0th or 1st (or any'th word within a variable):

~~~~py
first_name = (player.split()[0])
last_name = (player.split()[1])
~~~~

It's a super elegant shortcut to isolating a word within a variable. (thanks Ezra Leeuwenhage!)

### Double brackets

~~~~py
chant = ((F"{first_name}! ") *first_name_len) [:-1]
~~~~

Without the brackets that enclose the f-string and the multiplication, I'd have to use multiple lines just to remove the final character in the variable (the space after the last exclamation mark).
The double enclosing brackets save me 2 lines of code and make the 'good_chant' line redundant.
In the case of this assignment I'll go back to using first_name_len and good_chant, cause WincPy wants to see that variable, but in real life this saves lots of time and memory in projects! (again, thanks Ezra :D)
