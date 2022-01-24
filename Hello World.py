Task: Print Hello, World!

print("Hello, World!")

"""
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
Print objects to the text stream file, separated by sep and followed by end. sep, end, file, and flush, if present, must be given as keyword arguments.
All non-keyword arguments are converted to strings like str() does and written to the stream, separated by sep and followed by end. 
Both sep and end must be strings; they can also be None, which means to use the default values. If no objects are given, print() will just write end.
The file argument must be an object with a write(string) method; if it is not present or None, sys.stdout will be used. 
Since printed arguments are converted to text strings, print() cannot be used with binary mode file objects. 
For these, use file.write(...) instead.
Whether the output is buffered is usually determined by file, but if the flush keyword argument is true, the stream is forcibly flushed.

sys.stdout is a built-in file object that is analogous to the interpreter’s standard output stream in Python. stdout is used to display output directly to the screen console. 
Output can be of any form, it can be output from a print statement, an expression statement, and even a prompt direct for input.
By default, streams are in text mode. In fact, wherever a print function is called within the code, it is first written to sys.stdout and then finally on to the screen.

A text stream consists of one or more lines of text that can be written to a text-oriented display so that they can be read. When reading from a text stream, 
the program reads an NL (newline) at the end of each line. 
When writing to a text stream, the program writes an NL to signal the end of a line.

Anthon made it very clear to understand, Basically, the print line technically does not run (print) until the next line has finished.
Technically the line does run it just stays unbuffered until the next line has finished running.
This might cause a bug for some people who uses the sleep function after running a print function expecting to see it prints before the sleep function started.

print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

Prints the values to a stream, or to sys.stdout by default.
Optional keyword arguments:
file:  a file-like object (stream); defaults to the current sys.stdout.
sep:   string inserted between values, default a space.
end:   string appended after the last value, default a newline.
flush: whether to forcibly flush the stream.
"""
