def secuenciador_adn(N,secuencia, mutaciones_requeridas):
    mutaciones = set()

    def generar_combinaciones(secuencia_actual, mutaciones_restantes, index):
        if mutaciones_restantes == 0:
            mutaciones.add(secuencia_actual)
            return

        for i in range(index, N):
            for letra in ['A','C','G','T']:
                nueva_secuencia = secuencia_actual[:i] + letra + secuencia_actual[i+1:]
                generar_combinaciones(nueva_secuencia, mutaciones_restantes - 1, i + 1)
    generar_combinaciones(secuencia,mutaciones_requeridas, 0)
    return sorted(mutaciones)

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    secuencia = input().strip()

    mutaciones = secuenciador_adn(N, secuencia, K)
    print(len(mutaciones))
    for mutacion in mutaciones:
        print(mutacion)