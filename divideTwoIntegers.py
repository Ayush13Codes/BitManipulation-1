class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # T: O(log ** 2 n), S: O(1)
        # Handle edge cases
        # The only case that can overflow is -2^31 / -1 = 2^31 (which exceeds 2^31 - 1)
        if dividend == -(2**31) and divisor == -1:
            return 2**31 - 1

        # Track the sign of the result
        is_negative = (dividend < 0) != (divisor < 0)

        # Convert to positive numbers to simplify the logic
        dividend, divisor = abs(dividend), abs(divisor)

        # Initialize the result
        result = 0

        # Perform division using bit manipulation
        while dividend >= divisor:
            temp, multiple = divisor, 1

            # Use binary left shifts to accelerate the division process
            while dividend >= (temp << 1):
                temp <<= 1  # Equivalent to temp *= 2
                multiple <<= 1  # Equivalent to multiple *= 2

            dividend -= temp
            result += multiple

        # Apply the sign to the result
        return -result if is_negative else result
