from scipy.optimize import linprog as linear_programming


def print_results():
    # Definimos los coeficientes de la función objetivo
    obj_function = [4, 6, 0]

    # Definimos los coeficientes de las restricciones como una matriz de numpy
    lhs_eq = [[2, 1, 1]]
    rhs_eq = [5]

    results = linear_programming(
        c=obj_function, A_eq=lhs_eq, b_eq=rhs_eq, method="simplex"
    )

    # Mostramos el resultado
    print(results)
