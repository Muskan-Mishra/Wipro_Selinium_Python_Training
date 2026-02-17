#match - match the sequence

import re
from re import findall

#o/p match object - matched sequence and span()- start and index

text = "hello world"
result = re.match("hello" , text)
print(result)

      # using pattern
test_str = "12356668abchhhjjhjabcABC"
pattern = re.compile("123")
matches = pattern.finditer(test_str)
for match in matches:
    print(match)

text = "python of powerful maths powerful"
result = re.search("powerful",text)
print(result)


# raw string

a = r"\thello"
print(a)

# findall()
my_string = "abc123ABC123abc"
pattern = re.compile(r'123')
matches = pattern.findall(my_string)

for match in matches:
    print(match)

 #method of matches
test_str = "12356668abchhhjjhjabcABC"
pattern = re.compile("123")
matches = pattern.finditer(test_str)
for match in matches:
    print(match)
    print(match.span(),match.start(),match.end())
    print(match.group())




#abc matches exact text
#match exact "abc" where ever it is appearing
text = " i like abc and abcdde"
result = re.findall("abc",text)
print(result)


#[abc] or a or b or c- matches any one of the charater
#match


#a-z lowercase letters
text = " i like abc and ABCGHJHJH"
result = re.findall("[a-z]",text)
print(result)


text = " i like abc and 1234555ABCJHGJ"
result = re.findall("[0-9]",text)
print(result)


text = " i like abc and ABCGHJHJH"
result = re.findall("[A-Z]",text)
print(result)

#special character


#\d digit (0-9)\d\d
print(re.findall(r"\d", "Order 123 cost 450"))
print(re.findall(r"\d+", "Order 123 cost 450"))
#\D  Non-digit  \D
print(re.findall(r"\D", "Order 123 cost 450"))
print(re.findall(r"\D+", "Order 123 cost 450"))
#\w  Word char (a-z, A-Z, 0-9, _)   \w+
text = "python_3 version"
result = re.findall(r"\w",text)
print(result)

#\W  Non-word char  \W
text = "hello@123!"
result = re.findall(r"\W",text)
print(result)

#\s  Whitespace \s
text = "hello world\n python\t"
result = re.findall(r"\s",text)
print(result)

#\S  Non-whitespace \S
text = "hi there"
result = re.findall(r"\S",text)
print(result)

#\b  Word boundary  \bcat\b
text = "cat scatter catalog"
result = re.findall(r"\bcat\b",text)
print(result)

#\B  Not a word boundary    \Bcat
text = "cat scatter catalogcat"
result = re.findall(r"cat\B",text)
result = re.findall(r"\Bcat\B",text)
print(result)
''''
Meta - characters
have
special
meaning in regex.

Meta - character
Meaning
.Any
character
^ Start
of
string
$   End
of
string
*0 or more
+   1 or more
?   0 or 1
{n}
Exactly
n
times
{n, }
n or more
{n, m}
Between
n and m
[]
Character
set
()
Grouping
'''

import re

text = "cat dog bat 123 _var scatter singer bringing run playing sing a.b.c start end"

# \d -> digit
print(re.findall(r"\d+", text))  # numbers

# \D -> non digit
print(re.findall(r"\D+", text))  # non numbers

# \w -> word character
print(re.findall(r"\w+", text))  # words

# \W -> non word character
print(re.findall(r"\W+", text))  # spaces / symbols

# \s -> whitespace
print(re.findall(r"\s+", text))  # spaces

# \S -> non whitespace
print(re.findall(r"\S+", text))  # tokens

# \b -> word boundary
print(re.findall(r"\bcat\b", text))  # exact word cat

# \B -> inside word
print(re.findall(r"\Bing", text))  # ing inside word

# | -> OR
print(re.findall(r"cat|dog", text))  # cat or dog

# escape special character
print(re.findall(r"\.", text))  # literal dot

# ^ -> start of string
print(re.findall(r"^cat", text))  # cat only if start

# $ -> end of string
print(re.findall(r"end$", text))  # end only if last

# grouping ()
print(re.findall(r"(cat|dog)", text))  # group cat or dog

# non capturing group (?: )
print(re.findall(r"(?:cat|dog)", text))  # same but no capture group

# positive lookahead (?= )
print(re.findall(r"\w+(?=ing)", text))  # word before ing

# negative lookahead (?! )
print(re.findall(r"\b\w+(?!ing)\b", text))  # words not ending with ing

# positive lookbehind (?<= )
print(re.findall(r"(?<=\b)b\w+", text))  # words starting with b

# negative lookbehind (?<! )
print(re.findall(r"(?<!\b)b\w+", text))  # b not at word start

import re

text = "abc 123 aaa bbb cat scatter sing singer bringing start end"

# .  -> any single character
print(re.findall(r"c.t", text))  # matches cat

# ^  -> start of string
print(re.findall(r"^abc", text))  # matches abc only if at start

# $  -> end of string
print(re.findall(r"end$", text))  # matches end only if at end

# *  -> 0 or more of previous character
print(re.findall(r"a*", text))  # matches '', a, aa, aaa etc

# +  -> 1 or more of previous character
print(re.findall(r"a+", text))  # matches a, aa, aaa but not empty

# ?  -> 0 or 1 of previous character
print(re.findall(r"ab?c", text))  # matches ac or abc

# {n} -> exactly n times
print(re.findall(r"a{3}", text))  # matches aaa

# {n,} -> n or more times
print(re.findall(r"a{2,}", text))  # matches aa, aaa etc

# {n,m} -> between n and m times
print(re.findall(r"a{2,3}", text))  # matches aa or aaa

# [] -> character set
print(re.findall(r"[cs]at", text))  # matches cat or sat (if present)

# () -> grouping
print(re.findall(r"(cat)+", text))  # matches cat, catcat etc

'''
Modifier    Short  Purpose
re.IGNORECASE   re.I   Case-insensitive matching
re.MULTILINE    re.M   ^ and $ match each line
re.DOTALL   re.S   . matches newline
re.VERBOSE  re.X   Write readable regex with comments
re.ASCII    re.A   ASCII-only matching
re.DEBUG    —  Debug pattern
'''
import re
#re.IGNORECASE   re.I   Case-insensitive matching
text = "Python"
print(re.search("python",text, re.I))
#re.MULTILINE    re.M   ^ and $ match each line
text = "Hello\nPython"
print(re.findall("Hello\nPython",text, re.M))
#re.DOTALL   re.S   . matches newline
text = "Hello\nWorld"
print(re.search("Hello\nWorld",text, re.S))

#re.VERBOSE  re.X   Write readable regex with comments


#re.ASCII    re.A   ASCII-only matching
print(re.findall(r"\w+",text , re.A))
#re.DEBUG    —  Debug pattern

#assertation
"""
^ → Start of string
$ → End of string
\B → Word boundary
\B → Not word boundary
(?=...) → Positive Lookahead
(?!...) → Negative Lookahead
(?<=...) → Positive Lookbehind
(?<!...) → Negative Lookbehind
"""
# 1. ^ Start of String
# Matches pattern only if it appears at beginning of string
text1 = "Hello Python"
print(re.findall(r"^Hello", text1))

# 2. $ End of String
# Matches pattern only if it appears at end of string
text2 = "Learn Python"
print(re.findall(r"Python$", text2))

# 3. \b Word Boundary
# Matches whole word only, not inside another word
text3 = "cat scatter catalog"
print(re.findall(r"cat\b", text3))

# 4. \B Not Word Boundary
# Matches pattern only if it is inside a word
text4 = "Python"
print(re.findall(r"\Bthon", text4))

#(?=...) → Positive Lookahead
text = "user1 admin2 test"
print(re.findall(r"\w+(?=\d)",text))

#(?!...) → Negative Lookahead
text = "user1 admin2 test"
print(re.findall(r"\w+(?!\d)",text))

#(?<=...) → Positive Lookbehind
text7 = "Price ₹500"
print(re.findall(r"(?<=₹)\d+", text7))

#(?<!...) → Negative Lookbehind
# 8. (?<!...) Negative Lookbehind
# Match only if pattern is NOT preceded by given pattern
text8 = "₹500 $400 300"
print(re.findall(r"(?<!₹)\d+", text8))

print(re.findall(r"[A-Z]+", "PyTHon IS Fun"))
print(re.findall(r"(ha){2,3}", "hahaha haha hahahaha"))
print(re.findall(r"\b\w{4}\b", "This test code runs well"))
print(re.findall(r".+?", "abc"))
print(re.findall(r"\w+\B", "cat scatter dog"))
print(re.findall(r"(ab|cd)+", "ab cd abab cdcd"))
print(re.findall(r"\Acat", "cat\ncat"))
print(re.findall(r"(?<!\d)\d{2}", "123 45 6 789"))