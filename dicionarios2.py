primeiro_dicionario = {
    1: {'nome': 'Maria', 'idade': 26, 'nacionalidade': 'brasileira'}
}
primeiro_dicionario.update({
    2: {'nome': 'João', 'idade': 30, 'nacionalidade': 'português'},
    3: {'nome': 'Ana', 'idade': 22, 'nacionalidade': 'espanhola'}
})
print("Dicionário atualizado:", primeiro_dicionario)

copia_dicionario = primeiro_dicionario.copy()

primeiro_dicionario.pop(2)
print("Dicionário após remoção com 'pop':", primeiro_dicionario)
primeiro_dicionario.popitem()
print("Dicionário após remoção com 'popitem':", primeiro_dicionario)
primeiro_dicionario.clear()
copia_dicionario.clear()
print("Primeiro dicionário após 'clear':", primeiro_dicionario)
print("Cópia do dicionário após 'clear':", copia_dicionario)
novo_dicionario = dict.fromkeys(['chave1', 'chave2', 'chave3'], 'valor_inicial')
print("Itens do novo dicionário:", novo_dicionario.items())
print("Chaves do novo dicionário:", novo_dicionario.keys())
print("Valores do novo dicionário:", novo_dicionario.values())
