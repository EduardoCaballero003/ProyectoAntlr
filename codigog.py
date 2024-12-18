def main():
    numeros = [1,2,3,4,5]
    print('El primer número es: ',numeros[0])
    numeros.append(6)
    print('Los números después de agregar 6: ',numeros)
    numeros.remove(3)
    print('Los números después de eliminar el 3: ',numeros)
    del numeros[0]
    print('Los números después de eliminar el primero: ',numeros)
    numeros.insert(0,6)
    print('Los números después de insertar el primero: ',numeros)
    ultimoLista = numeros[-1]
    print('Ultimo elemento de la lista: ',ultimoLista)

if __name__ == '__main__':
    main()