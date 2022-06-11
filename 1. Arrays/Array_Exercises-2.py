# You have a list of your favourite marvel super heros.

heros=['spider man','thor','hulk','iron man','captain america']
# 1. Length of the list
print(len(heros))
# OP: 5

# 2. Add 'black panther' at the end of this list
heros.append('black panther')
print(heros)
# OP: ['spider man', 'thor', 'hulk', 'iron man', 'captain america', 'black panther']

# 3. You realize that you need to add 'black panther' after 'hulk', so remove it from the list first and then add it after 'hulk'
heros.remove('black panther')
heros.insert(3, 'black panter')
print(heros)
# OP: ['spider man', 'thor', 'hulk', 'black panter', 'iron man', 'captain america']

# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
heros[1:2] = ['doctor strange']
print(heros)
