from abc import ABC, abstractmethod
from random import randint, choice
import pokemon
import Round

class Jogador: 
    def __init__(self):
        self.pokemon_atual = None
        
    def Listar_pokemon_usuario(self):
        # usuario vai selecionar o pokemon que irar jogar 
        print(" Pokémons disponivéis: ")
        for p in pokemon.Lista_pokemon:
            print(f"\t\n=========================\n ID: {p['ID']}\t\nNome: {p['Nome']}\t\nTipo: {p['Tipo']}\t\nHP: {p['Hp']}\t\nDano mínimo: {p['Dano']}\t\n=========================")
      
    def escolher_pokemon(self):
        self.Listar_pokemon_usuario()
        while True:
            try:
                escolhido= input("Escolha o ID do pokémon que você deseja usar: ").strip()
                if not escolhido.isdigit():
                    raise ValueError(" ID deve ser um número")
                
                escolhido = int(escolhido)
                self.pokemon_atual = next(p for p in pokemon.Lista_pokemon if p["ID"] == escolhido)
                print(f'\t\n==================================================\n Você escolheu: {self.pokemon_atual["Nome"]}')
                break
            except ValueError as e:
                print(f"Entrada invalida:{e} !!!")
            except StopIteration:
                print("ID invalido, digite novamente ")
                
class Jogo:
    def __init__(self):
        self.jogador = Jogador()
    
    def iniciar(self):
        self.jogador.escolher_pokemon()
        while True:
            rival = pokemon.Oponente()
            if not rival:
                print("Não há mais oponentes disponíveis!")
                break
            input(f"\t\n Você está enfrentando: {rival['Nome']}. Pressione Enter para continuar...\n ==================================================")
            
            combate = Round.Round(self.jogador, rival)
            
            while True:
                if combate.perdeu_XP():# pokemon do usuario morreu durante o combate 
                    combate.perdeu()
                    return

                if combate.atacou():
                    combate.ganhou()
                    break
                
                if self.jogador.pokemon_atual['Hp'] <= 0:# pokemon do usuario morreu ao final do combate 
                    combate.perdeu()
                    return
               
jogo = Jogo()
jogo.iniciar()