import copy

# STEP 1: DATA GENERATION
def generate_data():
    users = [
        {
            "id": 1,
            "data": {"files": ["a.txt", "b.txt"], "usage": 500}
        },
        {
            "id": 2,
            "data": {"files": ["c.txt"], "usage": 300}
        }
    ]
    return users


# STEP 2: REPLICATION
def replicate_data(original):
    assigned = original                      
    shallow = copy.copy(original) 
    deep = copy.deepcopy(original) 
    return assigned, shallow, deep


# STEP 3: MODIFY DATA (ODD ROLL)
def modify_data(data, label):
    print(f"\n--- Modifying {label} ---")

    for user in data:
        if user["data"]["files"]:
            removed = user["data"]["files"].pop(0)

        user["data"]["usage"] += 100

        print(f"User {user['id']} removed file: {removed}")


# STEP 4: INTEGRITY CHECK
def check_integrity(original_before, original_after, shallow, deep):
    leakage_count = 0
    safe_count = 0
    overlap_count = 0

    print("\n--- Integrity Analysis ---")

    for i in range(len(original_before)):
        before_files = original_before[i]["data"]["files"]
        after_files = original_after[i]["data"]["files"]
        shallow_files = shallow[i]["data"]["files"]
        deep_files = deep[i]["data"]["files"]

        if before_files != after_files:
            leakage_count += 1
            print(f"Leakage detected in user {original_after[i]['id']}")

        if before_files == deep_files:
            safe_count += 1

        overlap = set(after_files) & set(shallow_files)
        overlap_count += len(overlap)

    return (leakage_count, safe_count, overlap_count)


# MAIN EXECUTION
def main():
    original = generate_data()

    original_before = copy.deepcopy(original)

    assigned, shallow, deep = replicate_data(original)

    print("===== BEFORE MODIFICATION =====")
    print("Original:", original)
    print("Shallow:", shallow)
    print("Deep:", deep)

    modify_data(shallow, "SHALLOW COPY")

    print("\n===== AFTER MODIFICATION =====")
    print("Original:", original)
    print("Shallow:", shallow)
    print("Deep:", deep)

    report = check_integrity(original_before, original, shallow, deep)

    print("\n===== FINAL REPORT =====")
    print("Tuple (leakage_count, safe_count, overlap_count):")
    print(report)

main()