def diagrama_estados(palabra):
    estado = "q0"
    recorrido = [estado]
    
    print(f"\nProcesando palabra: '{palabra}'")
    print("-" * 40)
    print(f"Estado inicial: {estado}")
    
    for i, letra in enumerate(palabra):
        letra = letra.lower()
        
        if letra not in ['a', 'b']:
            print(f"\nError: La letra '{letra}' no es válida. Solo se permiten 'a' y 'b'.")
            return
        
        estado_anterior = estado
        
        if estado == "q0":
            if letra == "a":
                estado = "q1"
            elif letra == "b":
                estado = "q2"
        elif estado == "q1":
            estado = "q1"
        elif estado == "q2":
            if letra == "a":
                estado = "q0"
            elif letra == "b":
                estado = "q2"
        
        print(f"Letra {i+1}: '{letra}' | {estado_anterior} -> {estado}")
        recorrido.append(estado)
    
    print("-" * 40)
    if estado == "q0":
        print("<<<<< PALABRA NO ACEPTADA >>>>>")
        print(f"<<<<<  ESTADO FINAL: {estado}  >>>>>")
    else:
        print("<<<<< PALABRA ACEPTADA >>>>>")
        print(f"<<<<<  ESTADO FINAL: {estado}  >>>>>")
    print(f"\nRecorrido completo: {' → '.join(recorrido)}")

def main():
    print("=" * 40)
    print("DIAGRAMA DE ESTADOS SIMPLIFICADO")
    print("=" * 40)
    print("Reglas:")
    print("- Estado inicial: q0")
    print("- q0 con 'a' -> q1")
    print("- q0 con 'b' -> q2")
    print("- q1: 'a' y 'b' regresan a q1")
    print("- q2 con 'a' -> q0")
    print("- q2 con 'b' -> q2")
    print("=" * 40)
    
    palabra = input("\nIngresa una palabra compuesta solo por 'a' y 'b': ").strip()
    
    if not palabra:
        print("Error: Debes ingresar una palabra.")
        return
    
    diagrama_estados(palabra)
    
    while True:
        continuar = input("\n¿Quieres probar otra palabra? (s/n): ").strip().lower()
        if continuar == 's':
            palabra = input("\nIngresa una palabra compuesta solo por 'a' y 'b': ").strip()
            if palabra:
                diagrama_estados(palabra)
        elif continuar == 'n':
            print("\n¡Gracias por usar el programa!")
            break
        else:
            print("Por favor, ingresa 's' para sí o 'n' para no.")

if __name__ == "__main__":
    main()