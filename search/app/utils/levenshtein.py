def levenshtein(a: str, b: str) -> int:
    if a == b:
        return 0
    if not a:
        return len(b)
    if not b:
        return len(a)

    prev_row = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur_row = [i]
        for j, cb in enumerate(b, 1):
            insert_cost = prev_row[j] + 1
            delete_cost = cur_row[j - 1] + 1
            replace_cost = prev_row[j - 1] + (ca != cb)
            cur_row.append(min(insert_cost, delete_cost, replace_cost))
        prev_row = cur_row
    return prev_row[-1]
