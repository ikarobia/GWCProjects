from random import *
line1 = ["An ocean voyage", "On a silent pond", "After the rain"]
line2 = ["It's life in the sea and murmurs", "of the magic inside you", "Sunlight dancing on waters"]
line3 = ["Blue water shimmers", "What am I", "I lay still"]
aRandomIndex1 = randint(0, len(line1)-1)
aRandomIndex2 = randint(0, len(line2)-1)
aRandomIndex3 = randint(0, len(line3)-1)
print(line1[aRandomIndex1], line2[aRandomIndex2], line3[aRandomIndex3])
