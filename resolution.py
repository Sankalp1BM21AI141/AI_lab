def resolve(clause1, clause2):
    # Find resolvent by removing complementary literals from both clauses
    resolvent = [literal for literal in clause1 if literal not in clause2]
    resolvent += [literal for literal in clause2 if literal not in clause1]
    return resolvent

def resolution(KB, query):
    KB.append(["~" + literal for literal in query])  # Add negation of query to the knowledge base

    while True:
        new_clauses = []

        for i in range(len(KB)):
            for j in range(i + 1, len(KB)):
                c1, c2 = KB[i], KB[j]
                for literal in c1:
                    if "~" + literal in c2:
                        resolvent = resolve(c1, c2)
                        if not resolvent:
                            return True  # Contradiction found
                        if resolvent not in new_clauses:
                            new_clauses.append(resolvent)

        if not new_clauses:
            return False  # No new clauses can be generated

        KB.extend(new_clauses)

# Example usage:
KB = [["A", "B", "C"], ["~A", "D"], ["~B", "~D"]]
query = ["C"]
result = resolution(KB, query)
print("Query is provable:", result)
