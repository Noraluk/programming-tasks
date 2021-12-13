input()
p_score = {'Adrian': 0, 'Bruno': 0, 'Goran': 0}
p_answer = {'Adrian': 'ABC', 'Bruno': 'BABC', 'Goran': 'CCAABB'}

for i, cha in enumerate(str(input())):
    for j, v in p_answer.items():
        if v[i % len(v)] == cha:
            p_score[j] += 1

m = max(p_score.values())
print(m)
for p, score in p_score.items():
    if score == m:
        print(p)
