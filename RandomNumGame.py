"""RandomNumGame"""

def main():
    """Random num"""
    from random import randrange
    x_num = randrange(1000)
    while True:
        put_num = int(input())
        if x_num == put_num:
            print("Correct!")
            break
        if x_num < put_num:
            print("Smaller")
        else:
            print("Bigger")
main()
