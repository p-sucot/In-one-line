from functools import reduce
# 1:
# Print an impressive minimum by reduce
li1 = [6, 2, 8, 12, 4]
print("the minimum is:")
print(reduce(lambda x, y: y if x > y else x, li1))


# 2:
# A function that prints a sequence of numbers with a currency mark
def combine_coins(coin, numbers):
    return ", ".join(list(map((lambda num:coin + str(num)), numbers)))

# For example
print(combine_coins("$", range(6)))


# 3:
# Prints the total number of letters of all words greater than 4 letters
list_nams = ["Yoav", "Ron", "Aviva", "Ronen", "Dan", "Galit"]
print(sum(filter(lambda x: x > 4, (list(map(lambda x: len(x), list_nams))))))

# You can also use reduce
print(reduce(lambda a, b: a+b,
      (filter(lambda x: x > 4, (list(map(lambda x: len(x), list_nams)))))))
