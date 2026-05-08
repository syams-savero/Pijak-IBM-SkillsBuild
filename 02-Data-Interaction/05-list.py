x = [1, 2.2, 'Dicoding']
x[0] = 'Indonesia'
print(x)

"""
Output:
['Indonesia', 2.2, 'Dicoding']
"""

x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(x[0])
print(x[2])
print(x[-1])
print(x[-3])


"""
Output:
laptop
mouse
microphone
keyboard
"""

#slicing
x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(x[0:5:2])
print(x[1:])
print(x[:3])

"""
Output:
['laptop', 'mouse', 'keyboard']
['monitor', 'mouse', 'mousepad', 'keyboard', 'webcam', 'microphone']
['laptop', 'monitor', 'mouse']

"""