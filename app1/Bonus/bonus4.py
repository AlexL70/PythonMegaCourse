filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]

for i, fName in enumerate(filenames):
    filenames[i] = fName.replace(".", "-", 1)
print(filenames)
# Tuples are the same as lists, but parentheses are used instead of square brackets.
# And tuples are immutable. Meaning replacing the element of the tuple would cause an exception