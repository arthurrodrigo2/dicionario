# tupla
campos = ("nome", "idade", "profissao", "email")

# Dicionário
usuario = {}

# entrada de dados
for campo in campos:
    usuario[campo] = input(f"Informe o valor do campo {campo}: ")

# exibe os valores do dicionario
print("DADOS DO USUÁRIO:\n")
for campo in campos:
    print(f"{campo}: {usuario.get(campo)}.")