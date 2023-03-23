import tkinter as tk
from tkinter import filedialog
from nodos import DLE
from objetos import orgas, muestra
import xml.dom.minidom
MDLE = DLE()

ventana = tk.Tk()
ventana.geometry("350x250")
ventana.title("Ejemplo de ventana con botones y etiquetas")

etiqueta1 = tk.Label(ventana, text="Juan Pablo Samayoa Ruiz", font=("Arial", 16), fg="blue")
etiqueta1.pack(pady=10)

etiqueta2 = tk.Label(ventana, text="202109705", font=("Arial", 16), fg="green")
etiqueta2.pack(pady=10)

def simulacion():
    print("Se está realizando la simulación :D")

def carga():
    ventanaCarga = tk.Toplevel(ventana)
    ventanaCarga.geometry("400x180")

    etiqueta1 = tk.Label(ventanaCarga, text="Menu Carga de Archivos", font=("Arial", 16), fg="blue")
    etiqueta1.pack(padx=10, pady=10)

    def archivoXML():
        ruta = filedialog.askopenfilename(filetypes=[("XML Files", "*.xml")])
        f = open(ruta,'r', encoding='utf-8')

        try:
            mashe = xml.dom.minidom.parse(f)
            rano = mashe.documentElement

            CDLE = DLE()
            ORGA = rano.getElementsByTagName("organismo")
            for contable in ORGA:
                CodiGO = contable.getElementsByTagName("codigo")[0].childNodes[0].nodeValue
                NomBre = contable.getElementsByTagName("nombre")[0].childNodes[0].nodeValue
                CDLE.insertar(orgas(CodiGO, NomBre))

            Mostra = rano.getElementsByTagName("muestra")
            for contable in Mostra:
                CodiGOMuestra = contable.getElementsByTagName("codigo")[0].childNodes[0].nodeValue
                NomBreMuestra = contable.getElementsByTagName("descripcion")[0].childNodes[0].nodeValue
                Filas = contable.getElementsByTagName("filas")[0].childNodes[0].nodeValue
                Columnas = contable.getElementsByTagName("columnas")[0].childNodes[0].nodeValue
                contableOrgaV = rano.getElementsByTagName("celdaViva")
                for contable2 in contableOrgaV:
                    OrgaCode = contable.getElementsByTagName("codigoOrganismo")[0].childNodes[0].nodeValue
                    Filas = contable.getElementsByTagName("filas")[0].childNodes[0].nodeValue
                    Columnas = contable.getElementsByTagName("columnas")[0].childNodes[0].nodeValue
                    pivott = CDLE.next
                    while pivott != None:
                        if pivott.data.codigo == OrgaCode:
                            break
                        if pivott == CDLE.primero:
                            pivott = None
                        pivott = pivott.posterior
                MDLE.insertar(muestra(Filas, Columnas, pivott))
            print(CDLE)
            print(CDLE)
            print("Regresar a la ventana anterior por favor")
        except Exception as e:
            print(e)

    boton1 = tk.Button(ventanaCarga, text="Buscar archivo", font=("Arial", 14), fg="blue", command=archivoXML)
    boton1.pack(padx=10, pady=10)

    boton2 = tk.Button(ventanaCarga, text="Regresar", font=("Arial", 14), fg="green", command=ventanaCarga.destroy)
    boton2.pack(padx=10, pady=10)

boton1 = tk.Button(ventana, text="Cargar archivo", font=("Arial", 14), fg="blue", command=carga)
boton1.pack(padx=10, pady=10)

boton2 = tk.Button(ventana, text="Iniciar simulacion", font=("Arial", 14), fg="green", command=simulacion)
boton2.pack(padx=10, pady=10)

boton3 = tk.Button(ventana, text="cerrar programa", font=("Arial", 14), fg="red", command=ventana.destroy)
boton3.pack(padx=10, pady=10)

ventana.geometry("400x400")
ventana.configure(bg="#F5F5F5")

ventana.mainloop()