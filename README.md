# Learn_Python_Hard_Way
Summary of excercises for book Learn Python the Hard Way

## Escape Sequences reference

| Escape                                  |                            What it does |
| --------------------------------------- | --------------------------------------- |
| \\                                      |                            Backslash(\) |
| \'                                      |                         Single-quote(') |
| \"                                      |                         Double-quote(") |
| \a                                      |                        ASCII bell (BEL) |
| \b                                      |                    ASCII backspace (BS) |
| \f                                      |                     ASCII formfeed (FF) |
| \n                                      |                     ASCII linefeed (LF) |
| \N{Name}                                |  Character named name in the Unicode database (Unicode only) |
| \r                                      |              ASCII carriage return (CR) |
| \t                                      |              ASCII Horizontal tab (TAB) |
| \uxxxx                                  | Character with 16-bit hex value xxxx (Unicode only) |
| \Uxxxxxxxx                              | Character with 32-bit hex value xxxxxxxx (Unicode only) |
| \V                                      |                 ASCII vertical tab (VT) |
| \ooo                                    |           Character with octal value oo |
| \xhh                                    |             Character with hex value hh |


## To Check documentation
python -m pydoc *function* 

## Reading and Writing files
* file.close() -> Close the file
* file.read() -> Read content of file, you can assign the result to a variable
* file.readline() -> Reads just one line of a text file
* file.truncate() -> Empties the file. Watch out if you care about the file
* file.write(stuff) -> Writes stuff to the file
