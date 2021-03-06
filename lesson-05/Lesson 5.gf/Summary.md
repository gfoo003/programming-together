## Strings in Patterns
- string: a sequence of characters
- index value starts at zero, need to use square brackets
- len: a function that defines length of string

## Intermediate Strings
slicing strings
- does not give a traceback i.e. if you give a larger index than the string, it would just end at the last index
- colon is like the range and it is *up to but not including*

Note: *up to but not including* = range includes first but excludes last

### Different Strings
- dir(): gives u directory of the functions that you can use

Type of functions that are specific to the string function:
- find(): looking up things base on index number. '-1' if not found
strip(): removing whitespaces
    - lstrip for left, rstrip for right
- replace():

Note: remember to add the '.' to include these strings

## Files
- mode: r = read, w = write
- open(filename, mode) </br>
*Note: mode is optional*
- newline: \n </br>
*Note: '\n' is one character*

## Files as a Sequence
Counting lines:
```python
for line in filename:
    count = count+1
```
*Note: Markdown all in one extension for nice content page*

