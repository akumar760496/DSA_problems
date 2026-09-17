def sum_3(num):
    """Brute-force reference implementation that returns unique triplets.

    Kept for reference; not used by the main demo.
    """
    num_len = len(num)
    unique = set()
    for i in range(num_len):
        for j in range(i+1, num_len):
            for k in range(j+1, num_len):
                if num[i] + num[j] + num[k] == 0:
                    trip = tuple(sorted((num[i], num[j], num[k])))
                    unique.add(trip)

    return [list(t) for t in unique]


def sum_3_hash(nums):
    """Hash-based O(n^2) solution returning unique triplets that sum to 0.

    Approach:
    - Sort the input so triplets are generated in non-decreasing order.
    - For each index i, treat nums[i] as the fixed first element and look for
        pairs in the remainder that sum to -nums[i] using a hash set (seen).
    - Store found triplets as tuples in a set to ensure uniqueness.
    """
    nums = sorted(nums)
    n = len(nums)
    results = set()

    for i in range(n - 2):
        # Skip duplicate fixed elements to reduce work (optional but common)
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        target = -nums[i]
        seen = set()
        for j in range(i + 1, n):
            complement = target - nums[j]
            if complement in seen:
                # Complement was seen earlier in this inner loop, so (nums[i], complement, nums[j]) is a valid triplet
                results.add((nums[i], complement, nums[j]))
            # Record current number for future complements
            seen.add(nums[j])

    return [list(t) for t in results]


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print("Brute-force results:")
    for t in sum_3(nums):
        print(t)

    print("\nHash-based results:")
    for t in sum_3_hash(nums):
        print(t)
