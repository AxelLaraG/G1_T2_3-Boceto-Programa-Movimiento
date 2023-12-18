import math as Math

matOriginal = [
    [3, 16, 1],
    [3, 18, 1],
    [1, 16, 1],
    [3, 18, 1],
    [3, 14, 1],
    [5, 13, 1],
    [5, 16, 1],
    [3, 14, 1],
    [2, 12, 1],
    [4, 11, 1],
    [5, 13, 1],
    [2, 12, 1],
    [2, 7, 1],
    [4, 11, 1],
    [4.5, 12, 1],
    [4.5, 2.7, 1],
    [2, 7, 1],
    [4.5, 12, 1],
    [4.5, 2.7, 1],
    [13, 2.7, 1],
    [4.5, 12, 1],
    [14.9, 12, 1],
    [10.9, 5, 1],
]

matTraslado = [[1, 0, 0], [0, 1, 0], [-3, -4, 1]]


matEscAumento = [[3, 0, 0], [0, 2, 0], [0, 0, 1]]


matEscDisminucion = [[1, 0, 0], [0, 0.5, 0], [0, 0, 1]]


matEscPunFijAumento = [[3, 0, 0], [0, 2, 0], [(2 * (1 - 3)), (7 * (1 - 2)), 1]]


matEscPunFijDismin = [[1, 0, 0], [0, 0.5, 0], [(2 * (1 - 1)), (7 * (1 - 0.5)), 1]]


matRefR = [[0, 1, 0], [1, 0, 0], [0, 0, 1]]


marRefO = [[-1, 0, 0], [0, -1, 0], [0, 0, 1]]


matRefX = [[1, 0, 0], [0, -1, 0], [0, 0, 1]]


matRedY = [[-1, 0, 0], [0, 1, 0], [0, 0, 1]]


matCorH = [[1, 0, 0], [2, 1, 0], [0, 0, 1]]


matCorV = [[1, 1, 0], [0, 1, 0], [0, 0, 1]]

matRotPunFijIzq = [
    [(Math.cos(120)), (Math.sin(120)), 0],
    [-(Math.sin(120)), Math.cos(120), 0],
    [
        (2 * (1 - (Math.cos(120))) + 1 * (Math.sin(120))),
        (1 * (1 - (Math.sin(120))) - 2 * (Math.cos(120))),
        1,
    ],
]

matRotPunFijDer = [
    [(Math.cos(30)), (Math.sin(30)), 0],
    [-(Math.sin(30)), Math.cos(30), 0],
    [
        (2 * (1 - (Math.cos(30))) + 1 * (Math.sin(30))),
        (1 * (1 - (Math.sin(30))) - 2 * (Math.cos(30))),
        1,
    ],
]

matRotIzq = [
    [(Math.cos(30)), -(Math.sin(30)), 0],
    [(Math.sin(30)), ((Math.cos(30))), 0],
    [0, 0, 1],
]

matRotDer = [
    [(Math.cos(120)), -(Math.sin(120)), 0],
    [(Math.sin(120)), ((Math.cos(120))), 0],
    [0, 0, 1],
]


def multiplicacion(mat2):
    res = [[0.0] * 3 for _ in range(23)]
    global matOriginal
    # Realiza la multiplicación de matrices
    for i in range(23):
        for j in range(3):
            for k in range(3):
                res[i][j] += matOriginal[i][k] * mat2[k][j]

    return res
