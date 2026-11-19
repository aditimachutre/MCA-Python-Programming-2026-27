
nums = list(map(int, input("Enter numbers: ").split()))

nums.append(50)
nums.extend([60, 70])
nums.insert(1, 100)

print("List:", nums)

nums.remove(100)
nums.pop()

print("Updated List:", nums)

print("Ascending:", sorted(nums))
print("Descending:", sorted(nums, reverse=True))

print("Maximum:", max(nums))
print("Minimum:", min(nums))
print("Sum:", sum(nums))

print("Concatenation:", nums + [80, 90])
print("Repetition:", nums * 2)
print("Indexing:", nums[0])
print("Membership:", 10 in nums)

print("Even Numbers:", [n for n in nums if n % 2 == 0])
print("Odd Numbers:", [n for n in nums if n % 2 != 0])
print("Squares:", [n*n for n in nums])

nums.sort()
print("After Sort:", nums)

nums.reverse()
print("After Reverse:", nums)
