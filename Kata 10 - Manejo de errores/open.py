def main():    
    try:
        open('config.txt')
    except FileNotFoundError:
        print("No se puedo encontrar el archivo 'config.txt'")

if __name__ == '__main__':
    main()