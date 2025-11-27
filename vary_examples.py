import re
from collections import defaultdict

# Read the file
with open('EnglishPatterns300.txt', 'r') as f:
    lines = f.readlines()

# Group phrases by tag
groups = defaultdict(list)
for line in lines:
    parts = line.strip().split(';')
    if len(parts) == 3:
        front, back, tag = parts
        phrase = front.split('. ', 1)[1]  # Remove number.
        groups[tag].append((front, back, tag, phrase))

# Now, for each group, prepare prompt
for tag, items in groups.items():
    phrases = [item[3] for item in items]
    prompt = f"For the category '{tag}', generate 4 varied example sentences for each of the following phrases. Make sure the examples are realistic, natural, and different from each other. Use the phrase at the beginning or appropriately in the sentence. Return in the format:\nphrase1: sentence1<br>sentence2<br>sentence3<br>sentence4\nphrase2: ...\n\nPhrases:\n" + '\n'.join(phrases)
    
    # Call subagent
    # But since I can't call subagent here, I'll print the prompt for now
    print(f"Tag: {tag}")
    print(prompt)
    print("\n" + "="*50 + "\n")

# For now, just print, later replace with subagent calls