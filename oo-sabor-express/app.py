from modelos.restaurante import Restaurante


def main():
    restaurante1 = Restaurante('Pizza Hut', 'Italiana')
    restaurante1.receber_avaliacao('Alice', 9)
    restaurante1.receber_avaliacao('Bob', 10)
    restaurante1.receber_avaliacao('Charlie', 4)
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()