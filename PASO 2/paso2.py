def modificar_diccionario(archivo_entrada, archivo_salida):
    contador = 0 # Contador para las contraseñas modificadas

    # Abre el archivo de entrada y el archivo de salida
    with open(archivo_entrada, 'r', encoding='latin-1') as f_in, open(archivo_salida, 'w', encoding='latin-1') as f_out:
        for linea in f_in:
            password = linea.strip()
            if password and not password[0].isdigit(): # Verifica si la contraseña no está vacía y no empieza con un número.
                nueva_password = password.capitalize() + '0' # Modifica las contraseñas.
                f_out.write(nueva_password + '\n')  # Escribe la nueva contraseña en el archivo de salida
                contador += 1 

    return contador 

# Nombre del archivo original y el archivo del modificado.
archivo_entrada = 'rockyou.txt'
archivo_salida = 'rockyou_mod.txt'

num_contraseñas = modificar_diccionario(archivo_entrada, archivo_salida)
print(f"Cantidad de contraseñas en el diccionario modificado: {num_contraseñas}")

