### O Quicksort é um algoritmo de ordenação altamente eficiente, também baseado em "dividir e conquistar", que escolhe um elemento como pivô e particiona a lista em torno do pivô.

```python
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivo = lista[len(lista) // 2]
        menores = [x for x in lista if x < pivo]
        iguais = [x for x in lista if x == pivo]
        maiores = [x for x in lista if x > pivo]
        return quicksort(menores) + iguais + quicksort(maiores)

# Exemplo
elementos_desorganizados = [7, 2, 1, 6, 8, 5, 3, 4]
print(quicksort(elementos_desorganizados)) # [1, 2, 3, 4, 5, 6, 7, 8]
```

## Seu desafio: Caso de Uso - Classificação de Eventos por Data

Você está organizando uma agenda e precisa classificar uma lista de **eventos por data e hora**. Cada evento é um dicionário com chaves 'nome' e 'data_hora' (onde 'data_hora' é um objeto `datetime`). Implemente uma função `organizar_eventos(eventos)` que utiliza o Quicksort para ordenar os eventos _cronologicamente_

### Agora é com você!

Esse é o momento que você vai tentar fazer o seu próprio script utilizando o que aprendeu num caso de uso da vida real. Fique tranquilo se sentir dificuldades, não se frustre, tudo é questão de prática.   
Se estiver fazendo seu script em uma outra linguagem, você tem uma desculpa a mais para dar uma olhadinha no gabarito, mas tente fazer sozinho primeiro!

## Dicas práticas

Não esqueça que o código fornecido acima não passa de um exemplo teórico de como o algoritmo funciona, não vá copiar ele literalmente, hein!

Para fazer seu algoritmo, responda às perguntas:

* Como você escolheria o "pivô" da sua lista de eventos? Lembre-se que cada "evento" é um dicionário. Você vai comparar o dicionário inteiro ou apenas uma parte dele? Qual parte?

* Seus eventos vêm com uma chave `'data_hora'` que contém um objeto `datetime`. Quando você precisa comparar dois eventos para saber qual vem "antes" ou "depois", como você faz essa comparação usando os objetos `datetime` dentro de cada dicionário?

* Ao dividir a lista em `menores`, `iguais` e `maiores` que o pivô, você deve guardar apenas a data e hora? Ou é importante manter o dicionário completo do evento (com 'nome' e 'data_hora') para que o resultado final seja uma lista de eventos completos e organizados?

* Pense no caso de haver dois ou mais eventos que acontecem na mesma data e hora. Onde esses eventos devem ir na sua divisão (`menores`, `iguais`, `maiores`)? Como o Quicksort lida com elementos que são iguais ao pivô?

* O Quicksort é um algoritmo recursivo. Qual é a condição que faz a recursão parar? Em outras palavras, quando sua função `organizar_eventos` deve parar de chamar a si mesma e simplesmente retornar a lista?

* Depois que você tem as sub-listas `menores`, `iguais` e `maiores` (já ordenadas recursivamente), como você as une de volta para formar a lista final de eventos totalmente organizada cronologicamente?


## Gabarito

Acesse o arquivo gabarito.py para visualizar a resolução em python feita por mim, você tem outra tarefa, comentar meu script explicando como o código funciona.

Cabe a você como fazer, se vai comentar linha a linha ou o script como um todo em um grande comentário.


---

Para guiar os alunos a resolverem o desafio de organizar eventos por data e hora usando Quicksort, as dicas precisam fazê-los pensar em como adaptar o algoritmo genérico para trabalhar com dicionários e objetos `datetime`.

---


