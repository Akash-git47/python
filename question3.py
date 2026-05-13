# Social Media Hashtag Tracker

hashtags = ["#fun", "#python", "#fun", "#code", "#python"]

# Frequency of each hashtag
frequency = {}

for tag in hashtags:
    if tag in frequency:
        frequency[tag] += 1
    else:
        frequency[tag] = 1

# Most repeated hashtag
most_repeated = max(frequency, key=frequency.get)

# Unique hashtags
unique_hashtags = list(set(hashtags))

# Remove duplicate hashtags
no_duplicates = []

for tag in hashtags:
    if tag not in no_duplicates:
        no_duplicates.append(tag)

print("Frequency of hashtags:", frequency)
print("Most repeated hashtag:", most_repeated)
print("Unique hashtags:", unique_hashtags)
print("List after removing duplicates:", no_duplicates)