def main(user):
    if user > 25:
        print("Error")
    else:
        for i in range(user, 26):
            print(f"Inside the loop, my variable is {i}")
main(int(input("Enter a number less than 25 \n")))