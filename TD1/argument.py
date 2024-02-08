import sys
if __name__ == '__main__':
    if len(sys.argv) == 1:
        print(f"nombre d'arguments {len(sys.argv)}")
        print(f'{sys.argv[0]} attend au moins un argument')
    else:
        print(f"nombre d'arguments {len(sys.argv)}")
        for i in range(len(sys.argv)):
            print(" -->", sys.argv[i])
        for elt in sys.argv:
            print("     -->", elt)