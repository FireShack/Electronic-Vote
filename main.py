print(' ')

print('Bienvenido al sistema de voto electronico')

print('''
    
    A. Votar
    B. Resultados
      
      ''')

N = input('Indique A o B: ')

if N == 'A':
    import voto
    
elif N == 'B':
    print(' ')
    import resultados