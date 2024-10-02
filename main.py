import sys
import copy
#tuky tuky
class jarron():
    maxCap = None
    capAct = None
    def __init__(self, maxCap, capAct = 0):
        self.maxCap = maxCap
        self.capAct = capAct
    
    def llenar(self):
        self.capAct = self.maxCap 
        return self
    
    def llenarX(self, cantPasada):
        self.capAct = min((self.maxCap - self.capAct), cantPasada)
        return self.capAct 
    
    def vaciarPiso(self):
        self.capAct = 0
        return self
    
    def vaciarOtroJarron(self, otroJarron):
        cantVaciada = otroJarron.llenarX(self.capAct)
        self.capAct = self.capAct - cantVaciada
        return [self, otroJarron]
    
    def copia(self):
        copia = copy.deepcopy(self)
        return copia

class main():
    
    def __init__(self, jarron1, jarron2, jarron3, objetivo = 1, pasos = ""):
        self.jarron1 = jarron1
        self.jarron2 = jarron2
        self.jarron3 = jarron3
        self.objetivo = objetivo
        self.pasos =  pasos + "" + str(self.jarron1.capAct) + " " + str(self.jarron2.capAct) + " " + str(self.jarron3.capAct) + "\n"

    def encontramosEm(self):
        if(self.jarron1.capAct == self.objetivo):
            print("Logrado")
            print(self.pasos + "LLegamos al estado final")
            sys.exit(0)
        elif (self.jarron2.capAct == self.objetivo):
            print("Logrado")
            print(self.pasos + "LLegamos al estado final")
            sys.exit(0)
        elif (self.jarron3.capAct == self.objetivo):
            print("Logrado")
            print(self.pasos + "LLegamos al estado final")
            sys.exit(0)
        return False
    
    def primeroEnProfundidad(self):
        print("Dado 3 jarrones de capacidad " + str(self.jarron1.maxCap) + ", " + str(self.jarron2.maxCap) + ", "  + str(self.jarron3.maxCap) + " galones, se quiere conseguir que en algun jarron tenga exactamente " + str(self.objetivo) + " galon.")
        self.encontramosEm()
        pila = []
        pila.extend(self.generarHijos())
        while(True):
            for elemento in pila:
                elemento.encontramosEm()
            tamPila = len(pila)
            for i in range (tamPila):
                actual = pila.pop(i)
                aux = actual.generarHijos()
                pila.extend(aux)
    
    def generarHijos(self):
        pila = []
        if(self.jarron1.capAct != self.jarron1.maxCap):
            pasos1 = self.pasos + "Llenamos el primer jarron. \n"
            nuevoCaso1 = pila.append(main(self.jarron1.copia().llenar(), self.jarron2.copia(), self.jarron3.copia(),pasos = pasos1))
        if (self.jarron1.capAct != 0):
            pasos2 = self.pasos + "Vaciamos al piso todo el contenido del primer jarron. \n"
            nuevoCaso2 = pila.append(main(self.jarron1.copia().vaciarPiso(), self.jarron2.copia(), self.jarron3.copia(),pasos = pasos2))
        if (self.jarron1.capAct != 0 and self.jarron2.capAct != self.jarron2.maxCap):
            pasos3 = self.pasos + "Vaciamos el contenido del primer jarron al segundo jarron. \n"
            accion = self.jarron1.copia().vaciarOtroJarron(self.jarron2.copia())
            nuevoCaso3 = pila.append(main(accion[0], accion[1], self.jarron3.copia(),pasos = pasos3))
        if (self.jarron1.capAct != 0 and self.jarron3.capAct != self.jarron3.maxCap):
            pasos4 = self.pasos + "Vaciamos el contenido del primer jarron al tercer jarron. \n"
            accion = self.jarron1.copia().vaciarOtroJarron(self.jarron3.copia())
            nuevoCaso4 = pila.append(main(accion[0], self.jarron2.copia(), accion[1],pasos = pasos4))
        if (self.jarron2.capAct != self.jarron2.maxCap):
            pasos5 = self.pasos + "Llenamos el segundo jarron. \n"
            nuevoCaso5 = pila.append(main(self.jarron1.copia(), self.jarron2.copia().llenar(), self.jarron3.copia(),pasos = pasos5))
        if (self.jarron2.capAct != 0):
            pasos6 = self.pasos + "Vaciamos el contenido del segundo jarron. \n"
            nuevoCaso6 = pila.append(main(self.jarron1.copia(), self.jarron2.copia().vaciarPiso(), self.jarron3.copia(),pasos = pasos6))
        if (self.jarron2.capAct != 0 and self.jarron1.capAct != self.jarron1.maxCap):
            pasos7 = self.pasos + "Vaciamos el contenido del segundo jarron al primer jarron. \n"
            accion = self.jarron2.copia().vaciarOtroJarron(self.jarron1.copia())
            nuevoCaso7 = pila.append(main(accion[1], accion [0], self.jarron3.copia(),pasos = pasos7))
        if (self.jarron2.capAct != 0 and self.jarron3.capAct != self.jarron3.maxCap):
            pasos8 = self.pasos + "Vaciamos el contenido del segundo jarron al tercer jarron. \n"
            accion = self.jarron2.copia().vaciarOtroJarron(self.jarron3.copia())
            nuevoCaso8 = pila.append(main(self.jarron1.copia(), accion[0], accion[1],pasos = pasos8))
        if (self.jarron3.capAct != self.jarron3.maxCap):
            pasos9 = self.pasos + "Llenamos el tercer jarron. \n"
            nuevoCaso9 = pila.append(main(self.jarron1.copia(), self.jarron2.copia(), self.jarron3.copia().llenar(),pasos = pasos9))
        if (self.jarron3.capAct != 0):
            pasos10 = self.pasos + "Vaciamos el contenido del tercer jarron. \n"
            nuevoCaso10 = pila.append(main(self.jarron1.copia(), self.jarron2.copia(), self.jarron3.copia().vaciarPiso(),pasos = pasos10))
        if (self.jarron3.capAct != 0 and self.jarron1.capAct != self.jarron1.maxCap):
            pasos11 = self.pasos + "Vaciamos el contenido del tercer jarron al primer jarron. \n"
            accion = self.jarron3.copia().vaciarOtroJarron(self.jarron1.copia())
            nuevoCaso11 = pila.append(main(accion[1], self.jarron2.copia(), accion[0],pasos = pasos11))
        if (self.jarron3.capAct != 0 and self.jarron2.capAct != self.jarron2.maxCap):
            pasos12 = self.pasos + "Vaciamos el contenido del tercer jarron al segundo jarron. \n"
            accion = self.jarron3.copia().vaciarOtroJarron(self.jarron2.copia())
            nuevoCaso12 = pila.append(main(self.jarron1.copia(), accion[1], accion[0],pasos = pasos12))
        return pila

print("Inicio")
prueba = main(jarron(12), jarron(8), jarron(3), 1)
prueba.primeroEnProfundidad()
