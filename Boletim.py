
# recebe rotulo como string e devolve float e
# especifica que quando usar essa função
# tem q receber uma string

def ler_nota(rotulo: str) -> float:
    while True:
        # STRIP REMOVE ESPAÇO
        # TROCA A , POR PONTO
        # TENTA TRANSFORMAR O STRING EM FLOAT
        texto = input(f"{rotulo}: ").strip().replace(",", ".")
        try:
            nota = float(texto)
            if 0 <= nota <= 10:
                return nota
            print("Digite uma nota entre 0 e 10")
        except ValueError:
            print("Digite um numero válido")

def ler_nome(nome):
    texto = input(f"{nome}: ").strip().replace(",",".")
    try:
        if texto.replace(" ", "").isalpha():
          return texto
        print("Nome invalido por favor tente novamente")
    except ValueError:
      print("Nome invalido, por favor tente novamente")

# Procedimento de Boletim
while True:
    print("=== Boletim Simples ===")
    nome_aluno = ler_nome("Nome")
    if nome_aluno:
        nota1 = ler_nota("Nota 1")
        nota2 = ler_nota("Nota 2")
        nota3 = ler_nota("Nota 3")

        media = (nota1 + nota2 + nota3) / 3
        print(f"Média de {nome_aluno}: {media:.2f}")
    else:
        print("Insira o nome do aluno")