import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T


.       - Any Character Except New Line
\d      - Digit (0-9)
\D      - Not a Digit (0-9)
\w      - Word Character (a-z, A-Z, 0-9, _)
\W      - Not a Word Character
\s      - Whitespace (space, tab, newline)
\S      - Not Whitespace (space, tab, newline)

\b      - Word Boundary
\B      - Not a Word Boundary
^       - Beginning of a String
$       - End of a String

[]      - Matches Characters in brackets
[^ ]    - Matches Characters NOT in brackets
|       - Either Or
( )     - Group

Quantifiers:
*       - 0 or More
+       - 1 or More
?       - 0 or One
{3}     - Exact Number
{3,4}   - Range of Numbers (Minimum, Maximum)


#### Sample Regexs ####

[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+
'''

sentence = 'Start a sentence and then bring it to an end'

"""
    re.ASCII (re.A) --> perform ASCII-only matching instead of full Unicode matching.
                        This is only meaningful for Unicode patterns, and is ignored for byte patterns.
    re.DEBUG  --> Display debug information about compiled expression.
    re.IGNORECASE(re.I) --> Perform case-insensitive matching; expressions like [A-Z] will also match lowercase letters.
                            Full Unicode matching (such as Ü matching ü) also works unless the re.ASCII flag is used to disable non-ASCII matches.
    re.LOCALE(re.L) -->
    re.MULTILINE(re.M) --> When specified, the pattern character '^' matches at the beginning of the string and at the beginning of each line (immediately following each newline);
                            and the pattern character '$' matches at the end of the string and at the end of each line (immediately preceding each newline).
                            Corresponds to inline flag(?m).
    re.DOTALL(re.S) --> Make the '.' special character match any character at all, including a newline; without this flag, '.' will match anything except a newline.
                        Corresponds to the inline flag (?s).
    re.VERBOSE(re.X) --> This flag allows you to write regular expressions that look nicer and are more readable by allowing you to visually separate logical sections of the pattern and add comments.

"""
pattern = re.compile(r'e.d', re.I)

phones = re.compile(r'[0-9][0-9][0-9].')

matches = phones.finditer(text_to_search)

for match in matches:
    print(match)
    
