def campo_electrico(q, distancias, k=9e+9):
    campos =[k*q/(r**2) for r in distancias]
    campo_y_distancia = []
    for E,r in zip(campos, distancias):
        campo_y_distancia.append(f"E = {E:.2} N/C, r = {r} m")
    return campo_y_distancia

