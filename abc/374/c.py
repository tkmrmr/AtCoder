import itertools


def split_groups(people):
    n = len(people)
    # 全ての人が1つのグループにいるのを避けるため、Aグループのサイズは1〜n-1
    all_splits = []
    for i in range(1, n):
        for group_a in itertools.combinations(people, i):
            group_b = tuple(p for p in people if p not in group_a)
            all_splits.append((group_a, group_b))
    return all_splits


# 5人のリスト
people = ["Person1", "Person2", "Person3", "Person4", "Person5"]

# 分け方を取得
splits = split_groups(people)

# 結果を表示
for group_a, group_b in splits:
    print(f"Group A: {group_a}, Group B: {group_b}")
