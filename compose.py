import os
import re
import string
import random
from graph import Graph, Vertex

# Função recebe o caminho para um arquivo de texto como argumento. Lê o arquivo, remove espaços em branco e converte em texto.


def get_words_from_text(text_path):
    with open(text_path, 'rb') as file:
        text = file.read().decode("utf-8")
        text = ' '.join(text.split())
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split()

    words = words[:1000]

    return words

# Recebe a lista, cria o gráfico e gera o mapeamento de probabilidades.


def make_graph(words):
    g = Graph()
    prev_word = None

    for word in words:
        word_vertex = g.get_vertex(word)
        if prev_word:
            prev_word.increment_edge(word_vertex)

        prev_word = word_vertex

    g.generate_probability_mappings()

    return g

# Armazenar as palavras da composição e escolhe aleatoriamente. Retorna a composição como uma lista.


def compose(g, words, length=50):
    composition = []
    word = g.get_vertex(random.choice(words))
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)

    return composition

# Chama a função.


def main():
    words = get_words_from_text('texts/Hamelt.txt')

    g = make_graph(words)

    composition = compose(g, words, 100)
    print(' '.join(composition))


if __name__ == '__main__':
    main()
