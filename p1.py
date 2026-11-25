def classificar_aluno(notas):
    media = sum(notas) / len(notas)
    if media < 5:
        status = 'Reprovado'
    elif media < 7:
        status = 'Recuperação'
    else:
        status = 'Aprovado'
    return round(media, 2), status

turma = {
    "Ana": [8.5, 7.0, 9.0],
    "Bruno": [4.0, 5.5, 4.5],
    "Carla": [6.0, 6.5, 5.5]
}

for aluno, notas in turma.items():
    media, situacao = classificar_aluno(notas)
    print(f"Aluno: {aluno} | Média: {media:.2f} | Status: {situacao}")
