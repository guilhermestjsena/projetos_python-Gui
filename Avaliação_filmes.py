print('Bem vindo ao sistema de avaliação de filmes!')

filme = input('Que filme você deseja avaliar? ').strip()

try:
    # Aceita tanto ponto (8.5) quanto vírgula (8,5)
    entrada_nota = input('Digite a nota do filme (0 a 10): ').replace(',', '.')
    nota_filme = float(entrada_nota)

    # Verifica se a nota passou do limite e ajusta automaticamente
    if nota_filme > 10:
        print('Aviso: O limite máximo de nota é 10! Sua nota foi ajustada para 10.0.')
        nota_filme = 10.0
    elif nota_filme < 0:
        print('Aviso: A nota mínima é 0! Sua nota foi ajustada para 0.0.')
        nota_filme = 0.0

    # Define apenas a classificação para não repetir o print
    if nota_filme == 0:
        classificacao = 'péssimo'
    elif nota_filme < 5:
        classificacao = 'ruim'
    elif nota_filme < 7:
        classificacao = 'regular'
    elif nota_filme < 9:
        classificacao = 'bom'
    else:
        classificacao = 'ótimo'

    print(f'Você avaliou o filme "{filme}" com a nota {nota_filme:.1f}.')
    print(f'Veredito: O filme é {classificacao} para você.')

except ValueError:
    print('Erro: Por favor, digite apenas números válidos para a nota.')
