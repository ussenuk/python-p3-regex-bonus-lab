import re


FINDALL_STRING = """
    It's such a lovely day today.
    Where'd all the time go?
    Some weather we're having today, huh?
    Tomorrow never knows!
    Maybe today's just not my day.
    It's clobbering time!
"""

text = "It's such a lovely day today."
text2 = "Some weather we're having today, huh?"
text3 ="Maybe today's just not my day."
my_pattern = r"^It's .*$"
my_pattern2 = r".*"
my_pattern3 = r".*"
my_pattern4 = r"(It's such a lovely day today\.|Some weather we're having today, huh\?|Maybe today's just not my day\.)"

my_regex = re.compile(my_pattern)
my_regex = re.compile(my_pattern2)
my_regex = re.compile(my_pattern3)
my_regex = re.compile(my_pattern4)





match = my_regex.search(text)
match2= my_regex.search(text2)
match3= my_regex.search(text3)
match4= my_regex.findall(FINDALL_STRING)


print(match)
print(match2)
print(match3)
print(match4)


