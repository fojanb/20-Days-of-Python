def get_user_input():
    print("\n========== Welcome to this beautiful app ==========\n")
    user_input = input("Please enter an integer positive number:\n")
    return int(user_input)

def generate_fibonacci():
    print("-------------- ✿ --------------")
    fibo = [1,1]
    for i in range(first_n_fibonacci - 2):
        fibo.append(fibo[i] + fibo[i+1])
    print(f"The first {first_n_fibonacci} numbers in Fibonacci: {fibo}")
    print("-------------- ✿ --------------\n")

first_n_fibonacci = get_user_input()
generate_fibonacci()
print("========== The End ==========\n")
