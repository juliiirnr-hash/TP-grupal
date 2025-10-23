from actividad4_Computadora import Computadora
from actividad4_ComponenteCPU import ComponenteCPU

class CostoComputadora:
    def __init__(self):
        pass

    def definir_computadora(self):
        while True:
            try:
                print()
                marca = input("Marca: ")
                if marca[0:1] == " " or marca == "":
                    print("No se admiten espacios al principio ni caracteres vacíos.")
                    print()
                else:
                    break
            except ValueError:
                print("Tipo de valor inválido.")
            except Exception:
                print("Ocurrió un error imprevisto.")

        while True:
            try:
                print()
                modelo = input("Modelo: ")
                if modelo[0:1] == " " or modelo == "":
                    print("No se admiten espacios al principio ni caracteres vacíos.")
                else:
                    break
            except ValueError:
                print("Tipo de valor inválido.")
            except Exception:
                print("Ocurrió un error imprevisto.")
        return marca, modelo

    def definir_componentes(self):
        Computadora.componentes_de_cpu = []
        while True:
            print()
            if input("Ingrese una «S» si quiere añadir un componente. ") != "s":
                break

            while True:
                try:
                    print()
                    componente = input("Componente: ")
                    if componente[0:1] == " " or componente == "":
                        print("No se admiten espacios al principio ni caracteres vacíos.")
                    else:
                        break
                except ValueError:
                    print("Tipo de valor inválido.")
                except Exception:
                    print("Ocurrió un error imprevisto.")

            while True:
                try:
                    print()
                    marca = input("Marca: ")
                    if marca[0:1] == " " or marca == "":
                        print("No se admiten espacios al principio ni caracteres vacíos.")
                        print()
                    else:
                        break
                except ValueError:
                    print("Tipo de valor inválido.")
                except Exception:
                    print("Ocurrió un error imprevisto.")

            while True:
                try:
                    print()
                    cantidad = int(input("Cantidad de unidades: "))
                    if cantidad > 0:
                        break
                    print("No tiene sentido tener cero o menos unidades del componente. ")

                except ValueError:
                    print("Tipo de valor inválido.")
                except Exception:
                    print("Ocurrió un error imprevisto.")

            while True:
                try:
                    print()
                    precio = float(input("Precio individual: "))
                    if precio > 0:
                        break
                    print("No se puede tener valores núlos o negativos. ")

                except ValueError:
                    print("Tipo de valor inválido.")
                except Exception:
                    print("Ocurrió un error imprevisto.")

            componente = ComponenteCPU(componente, marca, cantidad, precio)
            Computadora.componentes_de_cpu.append(componente)

    def main(self):
        while True:
            if input("Ingrese «S» si quiere valuar una computadora. ").lower() != "s":
                print("Saliendo del programa...")
                break

            marca, modelo = self.definir_computadora()

            self.definir_componentes()
            print()

            self.mostrar_resultados(marca, modelo)

    def mostrar_resultados(self, marca, modelo):
        print("-"*5, "Computadora", "-"*5)
        print("—", marca, "—")
        print("—", modelo, "—")
        print()

        if not Computadora.componentes_de_cpu:
            print("No hay componentes. Terminando programa...")
            return

        precio_componentes = 0.0
        print("Componente; Marca; Unidades; Precio")
        for i in range(len(Computadora.componentes_de_cpu)):
            print("-"*5, "Componente", i+1, "-"*5)
            print(f"Componente: {Computadora.componentes_de_cpu[i].componente};")
            print(f"Marca: {Computadora.componentes_de_cpu[i].marca};")
            print(f"Unidades: {Computadora.componentes_de_cpu[i].cantidad};")
            print(f"Precio: {Computadora.componentes_de_cpu[i].precio} pesos Arg.")
            precio_componentes += (Computadora.componentes_de_cpu[i].precio * Computadora.componentes_de_cpu[i].cantidad)
            print()

        print(f"Precio por componentes: {precio_componentes} pesos Arg.")
        precio_venta = 0
        if precio_componentes < 50000:
            precio_venta += (precio_componentes * 1.40)
            print(f"El precio de venta es: {precio_venta} pesos Arg.")
        else:
            precio_venta += (precio_componentes * 1.30)
            print(f"Precio de venta: {precio_venta} pesos Arg.")

        print(f"Precio combinado: {precio_componentes+precio_venta} pesos Arg.")
        print()

costo_computadora = CostoComputadora()
costo_computadora.main()
print()
