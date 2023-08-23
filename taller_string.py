text = "X-DSPAM-Confidence:    0.8475"

x = text.find(':')+5
print(x)
y = text.find('.')+5
print(y)

value = text[x:y]
value = float(value)
print(value)
