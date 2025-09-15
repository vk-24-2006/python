'''Diamond printing @K_Vivek_13'''
def print_diamond_patternNo(n):
    if n < 3 or n % 2 == 0:
        print("Please enter an odd integer greater than or equal to 3.")
        return
    
    for i in range(1, n + 1, 2):
        print(" " * ((n - i) // 2) + "*" * i)
    
    for i in range(n - 2, 0, -2):
        print(" " * ((n - i) // 2) + "*" * i)


n = int(input("Enter an odd integer (>=3): "))
print_diamond_patternNo(n)