tabela = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético-MG', 'Atlético-PR', 'Cruzeiro', 'Botafogo',
          'Santos', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará', 'Vasco', 'Sport', 'América-MG', 'Vitória', 'Paraná')
print(f'Os cinco primeiro colocados do campeonato foram {tabela[:5]}')
print(f'Os úlmos quatro colocados foram {tabela[-4:]}')
print(f'Times em ordem alfabética: {sorted(tabela)}')
print(f"O Chapecoense está na posição {tabela.index('Chapecoense')+1}")
