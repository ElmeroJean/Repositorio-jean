#Palindromo, solicitar al usuario una palabara invertida
palabra=input('Ingresa una Palabra')

#Se verifica lo que es con un condicional 
if palabra==palabra[::-1]:
    print('¡Es un palindrome!')
    
else:
    print('No es un palindrome')
    
    
    