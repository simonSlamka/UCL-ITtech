# Week 46 questions and answers
## RegEx

### Questions
1. What is grep capable of ?
2. What are regular expressions ?
3. What Python library can be used for regular expressions ?
4. Explain what character matching in regular expressions does ?
5. What does the re.search() method return ?
6. What does the re.findall() method return ?
7. What is the escape character used for in regular expressions ?
8. What does the $ match ?

### Answers
1. Searching, expression matching (mainly under Linux/Darwin)
2. Advanced string search functions
3. "_re_" (_import re_)
4. It parses characters and finds matches, returns matching strings, wildcards ('.') supported (fx "a.c" would return true for "a c", "abc", "agc", but not "ac")
5. It returns an object of the _re.Match_ class
6. A list of patterns that we're looking for (if pattern = "_abc_" in str "_abcdefgh_", then it would return list = ["abc"] only)
7. The backslash "_\_" is used for _escaping_ regular expression matching (differentiates between pattern and the point where we actually want to stop matching)
8. It matches the _the position_ **before** the end of the first newline ("_\n_")
