"""
╔══════════════════════════════════════════════════════════════╗
║          Python Essentials 1 — Cisco Networking Academy      ║
║                  Resumo Completo do Curso                    ║
╚══════════════════════════════════════════════════════════════╝

Autor: Matheus Magalhães de Faria
Conclusão: Maio de 2025
Certificação: Python Essentials 1 (PE1)

Este script reúne os principais conceitos aprendidos ao longo
do curso Python Essentials 1, com exemplos práticos e comentados.
"""

# ─────────────────────────────────────────────────────────────
# MÓDULO 1 — INTRODUÇÃO AO PYTHON
# ─────────────────────────────────────────────────────────────

print("=" * 60)
print("  MÓDULO 1 — INTRODUÇÃO AO PYTHON")
print("=" * 60)

# Python é uma linguagem de alto nível, interpretada e de propósito geral.
# A função print() exibe dados na tela.
print("Olá, Mundo!")                   # string simples
print("Cisco", "Python", "Essentials") # múltiplos argumentos
print("Linha 1\nLinha 2")             # \n = nova linha
print("A" * 3)                         # repetição de string → AAA
print(2 + 2)                           # expressão numérica


# ─────────────────────────────────────────────────────────────
# MÓDULO 2 — TIPOS DE DADOS, VARIÁVEIS E OPERADORES
# ─────────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("  MÓDULO 2 — TIPOS DE DADOS, VARIÁVEIS E OPERADORES")
print("=" * 60)

# --- Tipos de dados primitivos ---
inteiro    = 42           # int
flutuante  = 3.14         # float
booleano   = True         # bool (True / False)
texto      = "Python"     # str
nulo       = None         # NoneType

print(type(inteiro), type(flutuante), type(booleano), type(texto))

# --- Conversão de tipos (casting) ---
print(int(3.9))      # → 3  (trunca, não arredonda)
print(float(7))      # → 7.0
print(str(100))      # → '100'
print(bool(0))       # → False  (0, "", None, [] são falsy)
print(bool(42))      # → True

# --- Operadores aritméticos ---
print(10 + 3)   # adição       → 13
print(10 - 3)   # subtração    → 7
print(10 * 3)   # multiplicação→ 30
print(10 / 3)   # divisão real → 3.333...
print(10 // 3)  # divisão inteira → 3
print(10 % 3)   # módulo (resto) → 1
print(2 ** 8)   # potenciação  → 256

# --- Operadores relacionais ---
print(5 > 3)    # True
print(5 == 5)   # True
print(5 != 4)   # True
print(5 >= 5)   # True

# --- Operadores lógicos ---
print(True and False)  # False
print(True or  False)  # True
print(not True)        # False

# --- Operadores bit a bit ---
a, b = 1, 0
print(a & b)   # AND  bit a bit → 0
print(a | b)   # OR   bit a bit → 1
print(a ^ b)   # XOR  bit a bit → 1
print(~a)      # NOT  bit a bit → -2
print(a << 2)  # shift esquerda → 4
print(4 >> 1)  # shift direita  → 2

# --- Entrada do usuário ---
# nome = input("Seu nome: ")   # input() sempre retorna string
# idade = int(input("Idade: ")) # converta quando necessário


# ─────────────────────────────────────────────────────────────
# MÓDULO 3 — ESTRUTURAS CONDICIONAIS E LOOPS
# ─────────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("  MÓDULO 3 — ESTRUTURAS CONDICIONAIS E LOOPS")
print("=" * 60)

# --- if / elif / else ---
nota = 75
if nota >= 90:
    print("A")
elif nota >= 70:
    print("B")   # ← cai aqui
elif nota >= 50:
    print("C")
else:
    print("Reprovado")

# --- Operador ternário ---
resultado = "par" if nota % 2 == 0 else "ímpar"
print(f"Nota é {resultado}")

# --- while ---
contador = 0
while contador < 5:
    print(f"  while → {contador}")
    contador += 1
else:
    # bloco else executa quando a condição se torna False (sem break)
    print("  Loop while encerrado normalmente.")

# --- for com range() ---
for i in range(1, 11):        # 1 até 10
    if i % 2 == 0:
        continue               # pula pares
    print(f"  ímpar: {i}", end=" ")
print()

# --- break e else em for ---
emails = ["user@cisco.com", "admin@python.org"]
alvo = "@cisco.com"
for email in emails:
    if alvo in email:
        print(f"  Encontrado: {email}")
        break
else:
    print("  Nenhum e-mail encontrado.")

# --- Loop prático: verificar pares e ímpares (baseado em script.py) ---
numeros = [10, 7, 4, 13, 6, 3]
pares = sum(1 for n in numeros if n % 2 == 0)
impares = len(numeros) - pares
print(f"  Pares: {pares} | Ímpares: {impares}")


# ─────────────────────────────────────────────────────────────
# MÓDULO 4 — LISTAS, TUPLAS, DICIONÁRIOS E CONJUNTOS
# ─────────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("  MÓDULO 4 — COLEÇÕES DE DADOS")
print("=" * 60)

# ── LISTAS ──────────────────────────────────────────────────
frutas = ["maçã", "banana", "laranja", "uva"]
print(frutas[0])          # indexação positiva → 'maçã'
print(frutas[-1])         # indexação negativa → 'uva'
print(frutas[1:3])        # slice → ['banana', 'laranja']

frutas.append("manga")    # adiciona no final
frutas.insert(1, "pera")  # insere em posição específica
frutas.remove("uva")      # remove por valor
popped = frutas.pop()     # remove e retorna o último
frutas.sort()             # ordena in-place
frutas.reverse()          # inverte in-place

print("Lista de frutas:", frutas)
print("Comprimento:", len(frutas))

# Maior elemento sem max()
numeros_lista = [17, 3, 11, 5, 1, 9, 7, 15, 13]
maior = numeros_lista[0]
for n in numeros_lista:
    if n > maior:
        maior = n
print("Maior valor:", maior)

# Remover duplicatas preservando ordem
com_dup = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
sem_dup = []
for item in com_dup:
    if item not in sem_dup:
        sem_dup.append(item)
print("Sem duplicatas:", sem_dup)

# List comprehension
quadrados = [x ** 2 for x in range(6)]       # [0, 1, 4, 9, 16, 25]
pares_comp = [x for x in range(20) if x % 2 == 0]
print("Quadrados:", quadrados)
print("Pares 0–18:", pares_comp)

# Lista 2D (matriz)
matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print("Elemento [1][2]:", matriz[1][2])   # → 6

# Copiar lista (atenção: vals = lista cria referência!)
original = [1, 2, 3]
copia    = original[:]    # cópia real por slicing
copia2   = list(original) # outra forma
del copia[0]
print("Original intacto:", original)  # [1, 2, 3]

# ── TUPLAS ──────────────────────────────────────────────────
coordenadas = (10.5, -23.4)    # imutável
print("Latitude:", coordenadas[0])

tupla = (1, 2, 4, 8)
print(tupla[1:-1])   # slice → (2, 4)
print(tupla[-2:-1])  # → (4,)

# ── DICIONÁRIOS ─────────────────────────────────────────────
aluno = {
    "nome"    : "Ana",
    "idade"   : 22,
    "curso"   : "Python Essentials",
    "aprovado": True,
}
print(aluno["nome"])                       # acesso por chave
aluno["nota"] = 9.5                        # adicionar / atualizar
del aluno["aprovado"]                      # remover chave

for chave, valor in aluno.items():
    print(f"  {chave}: {valor}")

print("Chaves:", list(aluno.keys()))
print("Valores:", list(aluno.values()))

# Percorrer valores de dicionário encadeado
chain = {'one': 'two', 'three': 'one', 'two': 'three'}
v = chain['one']
for _ in range(len(chain)):
    v = chain[v]
print("Dicionário encadeado:", v)   # → 'two'

# ── CONJUNTOS (sets) ─────────────────────────────────────────
conjunto_a = {1, 2, 3, 4}
conjunto_b = {3, 4, 5, 6}
print("União:", conjunto_a | conjunto_b)
print("Intersecção:", conjunto_a & conjunto_b)
print("Diferença:", conjunto_a - conjunto_b)


# ─────────────────────────────────────────────────────────────
# MÓDULO 5 — FUNÇÕES
# ─────────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("  MÓDULO 5 — FUNÇÕES")
print("=" * 60)

# --- Definição básica ---
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("Mundo")

# --- Parâmetros padrão ---
def apresentacao(primeiro, ultimo="Silva"):
    print(f"Meu nome é {primeiro} {ultimo}")

apresentacao("Carlos", "Souza")
apresentacao("Maria")   # usa padrão "Silva"

# --- Retorno de valor ---
def calcular_imc(peso, altura):
    """Calcula o Índice de Massa Corporal."""
    if altura < 1.0 or altura > 2.5 or peso < 20 or peso > 300:
        return None
    return peso / altura ** 2

imc = calcular_imc(70, 1.75)
if imc is not None:
    print(f"IMC: {imc:.2f}")
else:
    print("Valores fora do intervalo válido.")

# --- Múltiplos retornos (via tupla) ---
def minmax(lst):
    return min(lst), max(lst)

minimo, maximo = minmax([4, 2, 9, 1, 7])
print(f"Min: {minimo}, Max: {maximo}")

# --- Argumentos por palavra-chave ---
def info(nome, idade, cidade="BH"):
    print(f"{nome}, {idade} anos, mora em {cidade}")

info(idade=25, nome="Lucas")           # ordem não importa com kwargs
info("Fernanda", 30, cidade="SP")

# --- Escopo: local vs global ---
variavel_global = 100

def modificar_global():
    global variavel_global   # declara intenção de alterar a global
    variavel_global += 50

modificar_global()
print("Global após função:", variavel_global)   # → 150

def apenas_leitura():
    print("Leitura da global:", variavel_global)  # lê sem 'global'

apenas_leitura()

# --- Recursão ---
def fatorial(n):
    """Calcula n! de forma recursiva."""
    if n == 0:
        return 1
    return n * fatorial(n - 1)

print("5! =", fatorial(5))   # → 120

def fibonacci(n):
    """Retorna o n-ésimo número de Fibonacci."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci(8):", fibonacci(8))   # → 21

def soma_recursiva(n):
    """Soma de 0 até n."""
    if n == 0:
        return 0
    return n + soma_recursiva(n - 1)

print("Soma(10):", soma_recursiva(10))  # → 55

# --- None como retorno implícito ---
def funcao_sem_return(x):
    if x % 2 == 0:
        return 1
    # sem else → retorna None implicitamente

resultado = funcao_sem_return(funcao_sem_return(2))
print("None + 1:", resultado + 1)   # fun(2)=1 → fun(1)=None → None+1=1


# ─────────────────────────────────────────────────────────────
# MÓDULO 6 — EXCEÇÕES E TRATAMENTO DE ERROS
# ─────────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("  MÓDULO 6 — EXCEÇÕES")
print("=" * 60)

# --- try / except / else / finally ---
def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("  Erro: divisão por zero!")
        return None
    except TypeError:
        print("  Erro: tipos incompatíveis!")
        return None
    else:
        # executa SOMENTE se não houve exceção
        print(f"  {a} / {b} = {resultado:.4f}")
        return resultado
    finally:
        # executa SEMPRE, com ou sem exceção
        print("  [bloco finally executado]")

dividir(10, 3)
dividir(10, 0)

# --- Captura genérica e múltiplas exceções ---
def converter_para_int(valor):
    try:
        return int(valor)
    except (ValueError, TypeError) as e:
        print(f"  Conversão falhou: {e}")
        return None

print(converter_para_int("42"))
print(converter_para_int("abc"))
print(converter_para_int(None))

# --- Exceções comuns do Python ---
erros_exemplos = [
    ("int('abc')",            lambda: int("abc")),
    ("10 / 0",                lambda: 10 / 0),
    ("[1,2,3][10]",           lambda: [1, 2, 3][10]),
    ("{'a':1}['b']",          lambda: {"a": 1}["b"]),
    ("None + 1",              lambda: None + 1),
]

for descricao, fn in erros_exemplos:
    try:
        fn()
    except Exception as e:
        print(f"  {descricao} → {type(e).__name__}: {e}")


# ─────────────────────────────────────────────────────────────
# BÔNUS — EXERCÍCIOS PRÁTICOS INTEGRADOS
# ─────────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("  BÔNUS — EXERCÍCIOS PRÁTICOS")
print("=" * 60)

# 1. Verificar se número é primo
def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

primos = [n for n in range(2, 50) if eh_primo(n)]
print("Primos até 50:", primos)

# 2. Inverter lista sem reverse()
def inverter(lst):
    return lst[::-1]

print("Invertida:", inverter([1, 2, 3, 4, 5]))

# 3. Contar ocorrências em lista
def contar_ocorrencias(lst, elemento):
    return sum(1 for x in lst if x == elemento)

print("Ocorrências de 4:", contar_ocorrencias([1, 4, 2, 4, 3, 4], 4))

# 4. Temperatura: Celsius ↔ Fahrenheit
def celsius_para_fahrenheit(c):
    return c * 9 / 5 + 32

def fahrenheit_para_celsius(f):
    return (f - 32) * 5 / 9

print(f"100°C = {celsius_para_fahrenheit(100):.1f}°F")
print(f"212°F = {fahrenheit_para_celsius(212):.1f}°C")

# 5. Bubble sort simples
def bubble_sort(lst):
    lst = lst[:]  # não modifica o original
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

desordenada = [64, 25, 12, 22, 11]
print("Ordenada:", bubble_sort(desordenada))

# 6. Palíndromo
def eh_palindromo(texto):
    t = texto.lower().replace(" ", "")
    return t == t[::-1]

palavras = ["arara", "python", "ana", "radar", "cisco"]
for p in palavras:
    print(f"  '{p}' é palíndromo? {eh_palindromo(p)}")


# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("  FIM DO SCRIPT — Python Essentials 1 concluído! 🐍")
print("=" * 60)
