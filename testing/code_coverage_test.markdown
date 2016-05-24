# Code Coverage Test

## Concept
Want to know what portion we have tested? The term is "coverage", and we have a library to test that.

## Install
If you don't have it yet, install the code coverage test library by

```
sudo pip install coverage
```

## Use Coverage
In terminal, type this:

```
coverage run tests.py
```

It will run the tests as usual, but coverage will record statistics. To see those statistics, run

```
coverage report
```

You'll see something like this:

```
Name      Stmts   Miss  Cover                                                                    
-----------------------------                                                                    
dice.py      50     30    40%                                                                    
test.py      28     15    46%                                                                    
-----------------------------                                                                    
TOTAL        78     45    42% 
```

The percentage for `test.py` is not important. We pay attention to the line for `dice.py`.

To see more about which lines we missed, run

```
coverage report -m
```

You'll see something like this:

```
Name      Stmts   Miss  Cover   Missing                                                          
---------------------------------------                                                          
dice.py      50     30    40%   11-17, 20, 23, 26, 29, 32, 35, 43-54, 57, 60, 63, 66, 69, 72-75  
test.py      28     15    46%   8-9, 12-13, 16, 21-22, 25, 28, 31-33, 36-37, 40                  
---------------------------------------                                                          
TOTAL        78     45    42%                                                     
```

Aim for 90% and higher.

## Visual Representation
The tables above is helpful, but there is a better way: visualize the results in a webpage.

Do this:

```
coverage html
```

Now the generated files are in htmlcov/ directory.

Click the file you want to test; you'll see something amazing. 
