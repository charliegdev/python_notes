# Teach Yourself Python in 24 Hours Notes

## Formatting Ouput

### Style 1
```python
greeting = "Good {}, {}. How are you doing?"

name = "Hannah"
time = "morning"

print greeting.format(time, name)
```

### Style 2
```python
specials_text = "Good {time}! Today's specials are: {special1} and {special2}."

time = "afternoon"
food1 = "spam with eggs"
food2 = "eggs with spam"

print specials_text.format(time=time, special1=food1, special2=food2)
```

### Style 3
```python
line = "Cities with Python meet-ups: {0}, {1}, {2}"

print line.format("Victoria", "Vancouver", "Alberta")
