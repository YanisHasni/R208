import sys, os
if __name__ == '__main__':
    if len(sys.argv) != 2 :
        print("erreur")
    elif os.path.exists(sys.argv[1]):
        for elt in os.listdir(sys.argv[1]):
            print(elt)
    else:
        print("Le rp existe pas")
