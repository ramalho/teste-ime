#!/usr/bin/env python
# coding: utf-8

"""
Dado um arquivo onde se espera encontrar todas as palavras do
Alfabeto Fonético da OTAN, este programa indica palavras faltantes.
"""

import sys, re

PALAVRAS = '''Alfa Bravo Charlie Delta Echo Foxtrot Golf Hotel India Juliett
              Kilo Lima Mike November Oscar Papa Quebec Romeo Sierra Tango
              Uniform Victor Whiskey Xray Yankee Zulu'''.split()

QT_EXIBIR = 3

nao_palavra = re.compile(r'\W+')

if len(sys.argv) != 2:
    print 'modo de usar:'
    print '\t%s <arquivo-a-verificar>' % sys.argv[0]
    sys.exit(1)

if sys.argv[1] == '-l':
    for palavra in PALAVRAS:
        print palavra
    sys.exit(0)
elif sys.argv[1] == '-l2':
    for palavra in PALAVRAS[::2]:
        print palavra
    sys.exit(0)

with open(sys.argv[1]) as arq_entrada:
    entrada = set()
    for lin in arq_entrada:
        entrada.update(p for p in re.split(nao_palavra, lin) if p)

faltando = 0
for palavra in PALAVRAS:
    if palavra not in entrada:
        if faltando == 0:
            print 'Faltando:'
        faltando += 1
        if faltando <= QT_EXIBIR:
            print '\t'+palavra

if faltando > QT_EXIBIR:
    dif = faltando - QT_EXIBIR
    quantas = 'uma palavra' if dif == 1 else '%s palavras' % dif
    print '\t\t... e mais %s faltando' % quantas
