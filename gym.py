from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Clientes del Gym"

ws.append(["ID", "Nombre", "Edad", "Correo", "Membresía"])

clientes_data = [
    (1, "Juan Pérez", 28, "juan@ejemplo.com", "Mensual"),
    (2, "Ana Gómez", 34, "ana@ejemplo.com", "Anual"),
    (3, "Carlos López", 22, "carlos@ejemplo.com", "Mensual"),
    (4, "Sofia Martínez", 40, "sofia@ejemplo.com", "Anual"),
]

for cliente in clientes_data:
    ws.append(cliente)

wb.save("clientes_gym.xlsx")

print("Datos guardados en 'clientes_gym.xlsx'")

