from acao import Acao
import random

class Interface:

    VITORIAS={
        Acao.pedra: [Acao.tesoura],
        Acao.tesoura: [Acao.papel],
        Acao.papel: [Acao.pedra]
    }

    def jogada_usuario(self):
        jogadas = [f"{acao.name}[{acao.value}]" for acao in Acao]
        string_jogadas = ", ".join(jogadas)
        escolha = int(input(f"Escolha sua opção ({string_jogadas}): "))
        acao = Acao(escolha)
        return acao

    def jogada_maquina(self):
        escolha = random.randint(0, len(Acao) - 1)
        acao = Acao(escolha)
        return acao

    def define_vencedor(self, acao_usuario, acao_maquina):
        derrotas = Interface.VITORIAS[acao_usuario]
        if acao_usuario == acao_maquina:
            print(f"Empate! Os dois escolheram {acao_usuario}")
        elif acao_maquina in derrotas:
            print(f"{acao_usuario} ganha de {acao_maquina}! Você ganhou!!!")
        else:
            print(f"{acao_maquina} ganha de {acao_usuario}! Você perdeu!!!")

    @staticmethod
    def main():
        jogo = Interface()
        while True:
            try:
                acao_usuario = jogo.jogada_usuario()
            except ValueError as ve:
                range_escolhas = f"[0, {len(Acao) - 1}]"
                print(f"Valores aceitos: {range_escolhas}")
                continue
            
            acao_maquina = jogo.jogada_maquina()
            jogo.define_vencedor(acao_usuario, acao_maquina)

            jogar_de_novo = input("Deseja jogar novamente? (Y/n): ")
            if jogar_de_novo.lower() != "y":
                break


if __name__ == '__main__':
    Interface.main()
