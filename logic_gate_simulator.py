print("DIGITAL LOGIC GATE SIMULATOR")

def AND(a,b):
    return a and b

def OR(a,b):
    return a or b

def NOT(a):
    return not a

def NAND(a,b):
    return not (a and b)

def NOR(a,b):
    return not (a or b)

def XOR(a,b):
    return a ^ b

while True:

    print("\n1 AND")
    print("2 OR")
    print("3 NOT")
    print("4 NAND")
    print("5 NOR")
    print("6 XOR")
    print("7 Truth Table")
    print("8 Exit")

    choice = int(input("Enter choice: "))

    if choice == 8:
        break

    if choice == 7:
        print("\nA B | AND OR NAND NOR XOR")

        for a in [0,1]:
            for b in [0,1]:
                print(a,b,"|",
                      int(AND(a,b)),
                      int(OR(a,b)),
                      int(NAND(a,b)),
                      int(NOR(a,b)),
                      int(XOR(a,b)))
        continue

    if choice == 3:
        a = int(input("Enter A: "))
        print("Output:", int(NOT(a)))
        continue

    a = int(input("Enter A: "))
    b = int(input("Enter B: "))

    if choice == 1:
        print("AND:", int(AND(a,b)))
    elif choice == 2:
        print("OR:", int(OR(a,b)))
    elif choice == 4:
        print("NAND:", int(NAND(a,b)))
    elif choice == 5:
        print("NOR:", int(NOR(a,b)))
    elif choice == 6:
        print("XOR:", int(XOR(a,b)))