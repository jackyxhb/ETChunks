import re

# Read the file
with open('/Users/macbook1/work/ETChunk/ETChunks/EnglishChunks.md', 'r') as f:
    content = f.read()

# Find groups
groups = re.findall(r'### (\d+)\. (.+?) \(\d+ items\)(.+?)(?=### \d+\.|$)', content, re.DOTALL)

anki_lines = []
current_num = 1

for group in groups:
    group_num, group_title, phrases_text = group
    # Extract phrases
    phrases = re.findall(r'\d+\. (.+)', phrases_text)
    for phrase in phrases:
        front = f"{current_num}. {phrase}"
        # Determine if incomplete
        is_incomplete = phrase.endswith('…')
        # Explanation based on group
        explanations = {
            '1': "This phrase is used to introduce or express your personal opinion or view on a topic.",
            '2': "This phrase is used to show agreement or disagreement with a statement or opinion.",
            '3': "This phrase is used to describe your feelings or emotions about something.",
            '4': "This phrase is used to describe experiences or tell stories.",
            '5': "This phrase is used to explain reasons or results.",
            '6': "This phrase is used to give examples or provide additional explanations.",
            '7': "This phrase is used for transitions or to show contrasts.",
            '8': "This phrase is used to emphasize or intensify the tone.",
            '9': "This phrase is used for hesitation or to fill thinking time.",
            '10': "This phrase is used to end topics or summarize.",
            '11': "This phrase is used in daily social interactions.",
            '12': "This phrase is used to connect ideas or show logical flow."
        }
        explanation = explanations.get(group_num, "This phrase is used in conversation.")
        # Examples
        if is_incomplete:
            base = phrase[:-1]
            examples = [
                f"1: {base} this movie is great.",
                f"2: {base} we should leave now.",
                f"3: {base} it's going to rain.",
                f"4: {base} you did a good job."
            ]
        else:
            if group_num == '2':
                if 'not' in phrase.lower() or 'disagree' in phrase.lower() or 'differ' in phrase.lower() or 'contrary' in phrase.lower():
                    examples = [
                        f"1: {phrase} It's not a good idea.",
                        f"2: {phrase} That's not correct.",
                        f"3: {phrase} I disagree.",
                        f"4: {phrase} Let's not do it."
                    ]
                else:
                    examples = [
                        f"1: {phrase} It's a good idea.",
                        f"2: {phrase} That's correct.",
                        f"3: {phrase} I agree.",
                        f"4: {phrase} Let's do it."
                    ]
            elif group_num == '3':
                examples = [
                    f"1: {phrase} happy.",
                    f"2: {phrase} excited.",
                    f"3: {phrase} good.",
                    f"4: {phrase} great."
                ]
            elif group_num == '4':
                examples = [
                    f"1: {phrase} It was interesting.",
                    f"2: {phrase} We had fun.",
                    f"3: {phrase} It happened suddenly.",
                    f"4: {phrase} I remember it well."
                ]
            elif group_num == '5':
                examples = [
                    f"1: {phrase} it was raining.",
                    f"2: {phrase} we were tired.",
                    f"3: {phrase} it led to success.",
                    f"4: {phrase} that's why we won."
                ]
            elif group_num == '6':
                examples = [
                    f"1: {phrase} apples or oranges.",
                    f"2: {phrase} walking or running.",
                    f"3: {phrase} reading books.",
                    f"4: {phrase} playing games."
                ]
            elif group_num == '7':
                examples = [
                    f"1: {phrase} it's a good idea.",
                    f"2: {phrase} that's correct.",
                    f"3: {phrase} I agree.",
                    f"4: {phrase} let's do it."
                ]
            elif group_num == '8':
                examples = [
                    f"1: {phrase} interesting.",
                    f"2: {phrase} correct.",
                    f"3: {phrase} agree.",
                    f"4: {phrase} do it."
                ]
            elif group_num == '9':
                examples = [
                    f"1: {phrase} I think.",
                    f"2: {phrase} Maybe.",
                    f"3: {phrase} Perhaps.",
                    f"4: {phrase} I'm not sure."
                ]
            elif group_num == '10':
                examples = [
                    f"1: {phrase} it's a good idea.",
                    f"2: {phrase} that's correct.",
                    f"3: {phrase} I agree.",
                    f"4: {phrase} let's do it."
                ]
            elif group_num == '11':
                examples = [
                    f"1: {phrase} It's a good idea.",
                    f"2: {phrase} That's correct.",
                    f"3: {phrase} I agree.",
                    f"4: {phrase} Let's do it."
                ]
            elif group_num == '12':
                examples = [
                    f"1: {phrase} it happened.",
                    f"2: {phrase} we went.",
                    f"3: {phrase} it started.",
                    f"4: {phrase} then we did."
                ]
            else:
                examples = [
                    f"1: {phrase} It's a good idea.",
                    f"2: {phrase} That's correct.",
                    f"3: {phrase} I agree.",
                    f"4: {phrase} Let's do it."
                ]
        back = explanation + ' ' + ' '.join(examples)
        tags = f"{group_num}-{group_title}"
        line = f"{front};{back};{tags}"
        anki_lines.append(line)
        current_num += 1

# Print all lines
print('\n'.join(anki_lines))