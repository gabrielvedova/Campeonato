#!/usr/bin/python3

cv, ce, cs, fv, fe, fs = input().split(" ")

# Dados do Cormengo
C = {
    'vitorias': int(cv),
    'empates': int(ce),
    'saldo': int(cs),
    'pontuação': [],
}

# Dados do Flaminthians
F = {
    'vitorias': int(fv),
    'empates': int(fe),
    'saldo': int(fs),
    'pontuação': [],
}

C['pontuação'] = C['vitorias']*3 + C['empates']
F['pontuação'] = F['vitorias']*3 + F['empates']

if C['pontuação'] > F['pontuação']:
    print('C')
if C['pontuação'] < F['pontuação']:
    print('F')
if C['pontuação'] == F['pontuação']:
    if C['saldo'] > F['saldo']:
        print('C')
    if C['saldo'] < F['saldo']:
        print('F')
    if C['saldo'] == F['saldo']:
        print('=')
