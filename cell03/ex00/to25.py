def main(user):
    if user > 25:
        print("Error")
    else:
        for i in range(int(user)+1):
            print(f"Inside the loop, my variable is {i}")
main(float(input("Enter a number less than 25 \n")))