def tipo_entrada (num_usuario):
    
    if type(num_usuario) != int:
        return None

    elif (num_usuario % 2) == 0:
       return True

    elif (num_usuario % 2) == 1:
        return False
       




# if __name__ == "__main__":
#    tipo_entrada()

# else:
#     print(tipo_entrada ())