# Função para calcular a média das notas
def calcular_media(notas):
    return sum(notas) / len(notas)

# Função para verificar se o aluno foi reprovado
def verificar_reprovacao(media):
    return media < 6

# Função para imprimir os dados dos alunos reprovados
def imprimir_alunos_reprovados(dados_alunos, matriculas_reprovados):
    for matricula in matriculas_reprovados:
        aluno = dados_alunos[matricula]
        print(f'Aluno Reprovado: {aluno["nome"]} – Matrícula: {matricula} – Média Final: {aluno["media"]:.2f}')
