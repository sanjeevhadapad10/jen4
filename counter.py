import sys

if len(sys.argv) < 2:
    print("Usage: python even_odd_counter.py num1 num2 num3 ...")
    sys.exit(1)

numbers = [int(arg) for arg in sys.argv[1:]]

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
      
print("\n--- Even and Odd Counter ---")
print(f"Count of Even Numbers: {even_count}")
print(f"Count of Odd Numbers: {odd_count}")
