def tipo_entrada (num_usuario):
    
    if type(num_usuario) != int:
        return None

    elif (num_usuario % 2) == 0:
       return True

    elif (num_usuario % 2) == 1:
        return False
       

print(tipo_entrada (6))
    

def imprime_resultado():
    
    if tipo_entrada() == True:
       return 'Tu número es par'
       
    elif tipo_entrada() == False:
        return 'Tu número es impar'
       



if __name__ == "__main__":
   imprime_resultado(tipo_entrada(6))