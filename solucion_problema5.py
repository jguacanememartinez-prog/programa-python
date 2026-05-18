# ============================================================
# PROBLEMA 5 - Control de Horas Trabajadas
# Curso: Fundamentos de Programacion - UNAD - Codigo 213022
# Fase 5 - Evaluacion Final POA
# ============================================================

# ------ FUNCION: calcula total de horas y clasifica jornada ------
def calcular_jornada(horas_semana):
    total = sum(horas_semana)          # Suma las horas de lunes a viernes
    if total > 40:                      # Condicion: mas de 40 horas
        clasificacion = 'Sobretiempo'
    else:                               # 40 horas o menos
        clasificacion = 'Horario Estandar'
    return total, clasificacion         # Retorna dos valores

# ------ DATOS: Matriz con 4 empleados ------
# Formato: [Nombre, Lunes, Martes, Miercoles, Jueves, Viernes]
equipo = [
    ['Carlos Lopez',   8,  9, 10,  8,  9],
    ['Maria Gomez',    7,  8,  8,  7,  8],
    ['Pedro Ramirez',  9,  9,  9,  9,  9],
    ['Ana Martinez',   6,  7,  8,  6,  7]
]

# ------ INFORME: Recorre la matriz y muestra resultados ------
print('=' * 56)
print('    INFORME DE HORAS TRABAJADAS - SEMANA')
print('=' * 56)
print(f"{'Nombre':<20} {'Total Horas':>12} {'Clasificacion':>20}")
print('-' * 56)

for recurso in equipo:                 # Ciclo for: recorre cada empleado
    nombre = recurso[0]                # Columna 0: nombre
    horas  = recurso[1:]               # Columnas 1-5: horas por dia
    total, clasificacion = calcular_jornada(horas)  # Llama la funcion
    print(f"{nombre:<20} {total:>12} {clasificacion:>20}")

print('=' * 56)
