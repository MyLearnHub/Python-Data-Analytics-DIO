# Descrição
# No reino mágico onde cada feiticeiro possui uma afinidade elemental única, seu desafio é criar um
# modelo de machine learning para prever essa afinidade. Os feiticeiros podem pertencer a um dos quatro
# elementos mágicos: Fogo, Água, Terra ou Ar. A predição será baseada em cinco atributos mágicos: 
# intensidade do feitiço, presença de componente raro, fase lunar, idade do feiticeiro e afinidade com
# animais mágicos.

# Aqui estão os critérios mágicos para cada elemento:

# Elemento Fogo:
# Intensidade do feitiço maior ou igual a 5.
# Fase lunar durante o feitiço é crescente.
# Idade do feiticeiro é superior a 100 anos.

# Elemento Água:
# Intensidade do feitiço maior ou igual a 7.
# Presença de componente raro.
# Fase lunar durante o feitiço é cheia.
# Idade do feiticeiro é igual ou inferior a 100 anos.
# Afinidade com animais mágicos.

# Elemento Terra:
# Intensidade do feitiço maior ou igual a 7.
# Presença de componente raro.
# Fase lunar durante o feitiço é cheia.
# Idade do feiticeiro é igual ou inferior a 100 anos.
# Afinidade com animais mágicos.

# Elemento Ar:
# Caso não se encaixe nos critérios anteriores.

# Entrada
# Seu código deve receber as seguintes entradas do usuário:

# Intensidade do feitiço (de 1 a 10): um número inteiro representando a força do feitiço.
# Componente raro (sim ou não): uma string indicando se o feitiço contém um componente raro.
# Fase lunar (cheia, crescente ou minguante): uma string indicando a fase lunar durante o lançamento do 
# feitiço.
# Idade do feiticeiro (em anos): um número inteiro representando a idade do feiticeiro.
# Afinidade com animais mágicos (sim ou não): uma string indicando se o feiticeiro tem afinidade com 
# animais mágicos.

# Saída
# O código deve produzir uma saída indicando a afinidade elemental prevista do feiticeiro com base nos
# atributos fornecidos.

# Exemplos
# A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas.
# Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

# Entrada     Saída
# 6           A afinidade elemental do feiticeiro é com o elemento Fogo!
# sim
# crescente
# 110
# sim	

# 8           A afinidade elemental do feiticeiro é com o elemento Água!
# sim
# cheia
# 80
# não	

# 9           A afinidade elemental do feiticeiro é com o elemento Terra!
# sim
# cheia
# 80
# sim	

def prever_afinidade_elemental(intensidade, componente_raro, fase_lunar, idade_feiticeiro, afinidade_animais):
  componente_raro = componente_raro.lower() == "sim"
  afinidade_animais = afinidade_animais.lower() == "sim"

  if intensidade >= 5 and fase_lunar == "crescente" and idade_feiticeiro > 100:
    return "A afinidade elemental do feiticeiro é com o elemento Fogo!"
  elif intensidade >= 8 and componente_raro and fase_lunar == "cheia" and idade_feiticeiro <= 100 and not afinidade_animais:
    return "A afinidade elemental do feiticeiro é com o elemento Água!"
  elif intensidade >= 7 and componente_raro and fase_lunar == "cheia" and idade_feiticeiro <= 100 and afinidade_animais:
    return "A afinidade elemental do feiticeiro é com o elemento Terra!"
  else:
    return "A afinidade elemental do feiticeiro é com o elemento Ar!"
   
intensidade_feitico = int(input())
componente_raro_feitico = input()
fase_lunar_feitico = input()
idade_feiticeiro = int(input ())
afinidade_animais_feiticeiro = input()

resultado = prever_afinidade_elemental(intensidade_feitico, componente_raro_feitico, fase_lunar_feitico, idade_feiticeiro, afinidade_animais_feiticeiro)

print(resultado)