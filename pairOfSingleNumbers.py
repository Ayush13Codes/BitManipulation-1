def singleNumbers(nums):
    # T: O(n), S: O(1)
    # Get XOR of all elements
    xor_all = 0
    for num in nums:
        xor_all ^= num

    # Find the rightmost bit that is 1 in the XOR result
    # This bit is different in our two target numbers
    rightmost_bit = xor_all & -xor_all  # or: xor_all & (~xor_all + 1)

    # Divide elements into two groups based on this bit
    # Perform XOR in each group
    x, y = 0, 0
    for num in nums:
        if num & rightmost_bit:  # Bit is 1
            x ^= num
        else:  # Bit is 0
            y ^= num

    return [x, y]
