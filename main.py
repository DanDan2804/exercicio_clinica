import os


class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario


class Enfermeira(Funcionario):
    def __init__(self, nome, cpf, salario, especialidade):
        super().__init__(nome, cpf, salario)
        self.especialidade = especialidade


class TecnicaEnfermagem(Funcionario):
    def __init__(self, nome, cpf, salario, turno):
        super().__init__(nome, cpf, salario)
        self.turno = turno


def cadastrar_enfermeira():
    nome = input("Digite o nome da enfermeira: ")
    cpf = input("Digite o CPF da enfermeira: ")
    salario = float(input("Digite o salário da enfermeira: "))
    especialidade = input("Digite a especialidade da enfermeira: ")
    enfermeira = Enfermeira(nome, cpf, salario, especialidade)
    return enfermeira


def cadastrar_tecnica_enfermagem():
    nome = input("Digite o nome da técnica de enfermagem: ")
    cpf = input("Digite o CPF da técnica de enfermagem: ")
    salario = float(input("Digite o salário da técnica de enfermagem: "))
    turno = input("Digite o turno de trabalho da técnica de enfermagem: ")
    tecnica_enfermagem = TecnicaEnfermagem(nome, cpf, salario, turno)
    return tecnica_enfermagem


def listar_funcionarios(funcionarios):
    print("==== Lista de Funcionários ====")
    for funcionario in funcionarios:
        if isinstance(funcionario, Enfermeira):
            print(f"Enfermeira: {funcionario.nome} - Especialidade: {funcionario.especialidade}")
        elif isinstance(funcionario, TecnicaEnfermagem):
            print(f"Técnica de Enfermagem: {funcionario.nome} - Turno: {funcionario.turno}")
    print("================================")


def buscar_funcionario(funcionarios, cpf):
    for funcionario in funcionarios:
        if funcionario.cpf == cpf:
            return funcionario
    return None


def atualizar_funcionario(funcionario):
    if isinstance(funcionario, Enfermeira):
        especialidade = input("Digite a nova especialidade da enfermeira: ")
        funcionario.especialidade = especialidade
    elif isinstance(funcionario, TecnicaEnfermagem):
        turno = input("Digite o novo turno de trabalho da técnica de enfermagem: ")
        funcionario.turno = turno


def excluir_funcionario(funcionarios, funcionario):
    funcionarios.remove(funcionario)


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def exibir_menu():
    print("==== Sistema de Gerenciamento de Funcionários ====")
    print("1. Cadastrar Enfermeira")
    print("2. Cadastrar Técnica de Enfermagem")
    print("3. Listar Funcionários")
    print("4. Buscar Funcionário")
    print("5. Atualizar Funcionário")
    print("6. Excluir Funcionário")
    print("0. Sair")
    print("=================================================")


def executar_opcao(opcao, funcionarios):
    if opcao == "1":
        enfermeira = cadastrar_enfermeira()
        funcionarios.append(enfermeira)
        print("Enfermeira cadastrada com sucesso!")
    elif opcao == "2":
        tecnica_enfermagem = cadastrar_tecnica_enfermagem()
        funcionarios.append(tecnica_enfermagem)
        print("Técnica de Enfermagem cadastrada com sucesso!")
    elif opcao == "3":
        listar_funcionarios(funcionarios)
    elif opcao == "4":
        cpf = input("Digite o CPF do funcionário a ser buscado: ")
        funcionario = buscar_funcionario(funcionarios, cpf)
        if funcionario:
            if isinstance(funcionario, Enfermeira):
                print(f"Enfermeira encontrada: {funcionario.nome} - Especialidade: {funcionario.especialidade}")
            elif isinstance(funcionario, TecnicaEnfermagem):
                print(f"Técnica de Enfermagem encontrada: {funcionario.nome} - Turno: {funcionario.turno}")
        else:
            print("Funcionário não encontrado!")
    elif opcao == "5":
        cpf = input("Digite o CPF do funcionário a ser atualizado: ")
        funcionario = buscar_funcionario(funcionarios, cpf)
        if funcionario:
            atualizar_funcionario(funcionario)
            print("Funcionário atualizado com sucesso!")
        else:
            print("Funcionário não encontrado!")
    elif opcao == "6":
        cpf = input("Digite o CPF do funcionário a ser excluído: ")
        funcionario = buscar_funcionario(funcionarios, cpf)
        if funcionario:
            excluir_funcionario(funcionarios, funcionario)
            print("Funcionário excluído com sucesso!")
        else:
            print("Funcionário não encontrado!")
    elif opcao == "0":
        print("Saindo...")
        return False
    else:
        print("Opção inválida!")

    return True


def main():
    funcionarios = []
    executando = True

    while executando:
        limpar_tela()
        exibir_menu()
        opcao = input("Digite a opção desejada: ")
        limpar_tela()
        executando = executar_opcao(opcao, funcionarios)
        input("Pressione Enter para continuar...")


if __name__ == "__main__":
    main()
