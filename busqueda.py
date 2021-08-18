#Cruz Matias Yuridia Elizabeth 
#Universidad Nacional Autonoma de Mexico
#Facultad de Ingenieria
#Inteligencia Artificial 
#Busqueda Ciega Amplitud
import time
import os
visitados = []
cola = []
estaciones = {   
            'A': [('B',2), ('C',3)],
            'B': [('C',3), ('E',5)],
			'C': [('G',7)],
			'D': [('H', 8)],
			'E': [('G',7), ('D',4), ('I',9)],
			'F': [],
			'G': [],
			'H': [('F',6)],
			'I': [],
		}

nombre = {   
            'A': 'Facultad de Ciencias Biológicas “A”',
            'B': "Aulas de Ciencias Químicas",
			'C': "Facultad de Ciencias Químicas",
			'D': "Facultad de FÍsico Matemáticos",
			'E': "Posgrado FÍsico Matemáticos",
			'F': "Laboratorio Fime",
			'G': "Faculta de IngenierÍa Civil",
			'H': "Facultad de IngenierÍa Mecánicas y Eléctrica",
			'I': "Librería Universitaria",
		}

def tiempoE():
    time.sleep(0.5)
    print()

def BusquedaAmplitud(origen,destino):
    cola.append(origen)
    i=1
    while i==1:
        if cola:
            actual = cola.pop(0)
            if (destino == actual and actual not in visitados):
                tiempoE()
                print("Hemos llegado a nuestro destino", nombre[actual])
                print("\n\tVuelva pronto...\n\n")
                while cola:
                    actual = cola.pop(0)
                    i=0
            else:
                if (actual not in visitados):
                    tiempoE()
                    print("Usted ha llegado a", nombre[actual])
                    visitados.append(actual)
                for k, l in estaciones[actual]:
                    if k not in visitados:
                        cola.append(k)
        else:
            print("Lo sentimos no encontramos tu destino")
            i=0

def main():	
    i=1	
    print("\n\t\t**BIENVENIDOS**")
    print("\tIngrese la letra")
    print("\t\tLas estaciones son:")
    
    while (i==1):
        print()
        print('\tA. Facultad de Ciencias Biológicas “A”')
        print('\tB. Aulas de Ciencias Químicas')
        print('\tC. Facultad de Ciencias Químicas')
        print('\tD. Facultad de Fisicco Matemáticos')
        print('\tE. Posgrado Físico Matemáticos')
        print('\tF. Laboratorio Fime')
        print('\tG. Faculta de Ingenieria Civil')
        print('\tH. Facultad de Ingenieria Mecánicas y Eléctrica ')
        print('\tI. Librería Universitaria')

        origen = input("\n\tOrigen: ")
        destino = input("\n\tDestino: ")
        if(origen == destino):
            os.system ("clear")
            print("Usted ya esta en su destino")
            print("\n\tInserte Otra opcion")
        else:
            if(origen=="A" or origen=="B" or origen=="C" or origen=="D" or origen=="E" or origen=="F" or origen=="G" or origen=="H" or origen=="I"):
                if(destino=="A" or destino=="B" or destino=="C" or destino=="D" or destino=="E" or destino=="F" or destino=="G" or destino=="H" or destino=="I"):
                    BusquedaAmplitud(origen,destino)
                    i=0
                else:
                    os.system ("clear")
                    print("\nDestino u origen incorrecto, ingrese correctamente la letra\n")
            else:
                os.system ("clear")
                print("\nDestino u origen incorrecto, ingrese correctamente la letra\n")
                
    print()
main()