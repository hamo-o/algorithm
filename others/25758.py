import sys
input = sys.stdin.readline

n = int(input())
dnas = list(map(str, input().split()))

alpha = []
for i in range(ord("A"), ord("A")+26):
    alpha.append(chr(i))

visited = [0]*26
answers = set()

# 두번째에 위치한 알파벳이 몇개 있는지 확인
for dna in dnas:
    visited[ord(dna[1])-ord("A")] += 1

# 첫번째 형질 고정
for dna in dnas:
    for i in range(26):
        # 두 번째 형질로 존재하면서
        if visited[i]:
            # 두 번째 형질이 여러개 나타나거나 첫 번째 형질 바로 뒤에 붙은 두 번째 형질이 아닐 경우
            if visited[i] > 1 or dna[1] != alpha[i]:
                answer = max(dna[0], alpha[i])
                answers.add(answer)

# 정렬
sorted_list = sorted(list(answers))

print(len(sorted_list))
print(" ".join(sorted_list))
