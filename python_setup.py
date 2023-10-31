# A function named hello() that prints a greeting to the user.
def hello():
    print("Hello, user!")

# A function named pack() that accepts three arguments, 
# and returns a single list with the three arguments inside as list elements.
def pack(arg1, arg2, arg3):
    return [arg1, arg2, arg3]

# A function called eat_lunch().
def eat_lunch(lunch_list):
    if len(lunch_list) == 0:
        print("My lunchbox is empty!")
    else:
        print(f"First I eat {lunch_list[0]}")
        for food in lunch_list[1:]:
            print(f"Next I eat {food}")

# Test the functions
if __name__ == '__main__':
    hello()
    packed_list = pack("apple", "banana", "carrot")
    print(f"The output of pack() is: {packed_list}")
    eat_lunch(["sandwich", "chips", "cookie"])
    eat_lunch([])