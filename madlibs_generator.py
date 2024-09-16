# <name1> and <name2> saw a <adjective> <noun>. <name1> wanted to <verb1> it, but <name2> said, “Let’s just <verb2> it.”
# Tim and Lily saw a beautiful butterfly. Tim wanted to catch it, but Lilly said, "Let's just watch it."

story = "<name1> and <name2> saw a <adjective> <noun>. <name1> wanted to <verb1> it, but <name2> said, \"Let's just <verb2> it.\""

start_point = "<"
end_point = ">"
start_of_word = -1
words = set()

for i, char in enumerate(story):
    if char == "<":
        start_of_word = i

    if char == ">" and start_of_word != -1:
        words.add(story[start_of_word: i+1])

# words = sorted(words)

answer = {}
for word in words:
    answer[word] = input(f"Enter a word for {word}: ")

for word in words:
    story = story.replace(word, answer[word])

print(story)