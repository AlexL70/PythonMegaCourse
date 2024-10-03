import json

score: int = 0
with open("files/bonus15.json", 'r') as jf:
    content = jf.read()
data = json.loads(content)
for item in data:
    print(item["question_text"])
    for i, alt in enumerate(item["alternatives"]):
        print(f"{i + 1} - {alt}")
    opt = int(input("Enter the number of the option: "))
    item["answer"] = opt
    if opt == item["correct_answer"]:
        score += 1

for item in data:
    alt = item["alternatives"]
    y_a: str = alt[(item['answer'] - 1)]
    c_a: str = alt[(item['correct_answer'] - 1)]
    correct = y_a == c_a
    print(f"Your answer: \"{y_a}\". Correct answer: \"{c_a}\". "
          f"{'Success' if correct else 'Fail'}.")
print(f"Total score is {score} of {len(data)}")