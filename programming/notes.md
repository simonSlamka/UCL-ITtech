Week 41 - 13.10.2021

While loops checks a condition, needs a condition true of false.



    ### How do you access individual characters in a string ?
 - With the index function

```python
string = "hendricks"
print(strings[2])
>>> n
```

    ### How can you traverse a string ?
    
Both with a _for_ loop and the _while_ loop.

    ### What is a string slice ?
Is a segment from a string
```python
string = "hendricks"
print(strings[2:-2])
>>> ndrik
```

    ### What does it mean, that strings are immutable ?
It means that you cant change an existing string (not directly atleast)

    ### How do you compare two strings ?
>, < ==, /, 

    ### What string methods do you know ?
upper(), lower(), find()

    ### How do you extract a substring from a string?
Using the find() method:[]
by cutting it with a slice operator and asignment it to a variable.



Cahpter 7

#### What is a file handle ?
- The filehandle is a _handle_ that can be used to read the data in the file
```python
filehandle = open('filename.txt')
```
#### How do you count lines in a file ?
- We can count the lines with a _for_ loop.
```python
filehandle = open('filename.txt')
for line in filehandle:
	count =+ 1
print(f"Total number if lines: {count}")
```
#### How do you search through a file ?
```python
filehandle = open('filename.txt')
for line in filehandle:
	if line.contains('Bathtub'):
		print(line)
```
#### What does the `rstrip` method do ?
```python
filehandle = open('filename.txt')
for line in filehandle:
	line = rstrip(line)
	if line.contains('navystrength'):
		print(line)
```
#### What happens if you try to open a non existing file ?
- If we try to open an non-existing file we get the traceback "FileNotFoundError" error.
#### How do you write to a file ?
If we where to write to a file, we open it as earlier, but ad a "w" to the line.
```python
filehandle = open('filename.txt', 'w')
```
Word of caution, writing to an existing file **CLEARS** the file before writing to it.
    
    



