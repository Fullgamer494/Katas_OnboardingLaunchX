def main():
    try:
        open('config.txt')
    except FileNotFoundError:
        print("No se pudo encontrar el archivo 'config.txt'")
    except PermissionError: 
        print("Se encontró 'config.txt', pero no se tienen los permisos necesarios para acceder a este")
    except (BlockingIOError, TimeoutError):
        print("El sistema se ha sobrecargado, no se puede completar la lectura del archivo")

if __name__ == '__main__':
    main()