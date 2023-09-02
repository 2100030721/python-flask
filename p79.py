# Importing re module
import re

# Given String
s = "I am a human being."

# Performing the subn() operation
res_1 = re.subn('a', 'x', s)
res_2 = re.subn('[a,I]','x',s)

# Print Results
print(res_1)
print(res_2)

