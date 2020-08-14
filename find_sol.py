from copy import copy, deepcopy
meta=[2,2,-1,-1,-1,0,1,1,1,2,2]
#estado,movimientos
abiertos=[[[2,2,1,1,1,0,-1,-1,-1,2,2],[]]]
cerrados=[]

#Regresa la lista de posibles movimientos
def obtenerTransformaciones(nodo):
    print("Nodo: "+ str(nodo))
    estado=nodo[0]
    transformaciones=[]
    for i in range(2, len(estado)-2):
        actual=estado[i]
        if((estado[i+actual]==0 or (estado[i+actual*2]==0 and estado[i+actual]==-1*estado[i])) and estado[i]!=0):#slide o jump
            newNode=copy(estado)
            newNode[i]=0
            if(estado[i+actual]==0):#Slide
                newNode[i+actual]=actual
                movimiento=[i-2,i+actual-2]
            else:                   #Jump
                newNode[i+actual*2]=actual
                movimiento=[i-2,i+actual*2-2]
            transformaciones+=[[newNode,copy(nodo[1])+[movimiento]]]
    print("Abre:"+str(len(transformaciones)))
    for i in transformaciones:
        print(str(i[0])+"Movimiento hecho:"+ str(i[1][-1]))
    print("--------------------------------------------------------------/n")
    return transformaciones
                
#Vagancia
def copy(x):
    return deepcopy(x)

def imprimir(estados):
    for i in estados:
        print(str(i[0][2:len(i[0])-2])+' Movimientos:'+str(i[1]))
        
def cerrar(node):
    global abiertos
    global cerrados
    result=[]
    cerrados+=[abiertos[node]]
    for i in range(0,len(abiertos)):
        if(node == i):
            continue
        result+=[abiertos[i]]
    abiertos=result

def find_solution():
    global abiertos
    global cerrados
    global meta
    logrado=False
    while(len(abiertos)!=0):
        seleccionado=len(abiertos)-1
        abiertos+=obtenerTransformaciones(abiertos[seleccionado])
        if(abiertos[seleccionado][0]==meta):
            print('Solucionado')
            imprimir([abiertos[seleccionado]])
            solucion=abiertos[seleccionado]
            logrado = True
            #input("Listo")
            break
        cerrar(seleccionado)
        #print("Mejor nota:"+str(mejorNota))
        #input("Enter para seguir")
        #imprimir(cerrados)
           
    if(logrado):
        print("Solucionado en "+str(len(solucion[1])) +" movimientos")
        return solucion[1]
    else:
        print('No hay solucion, pero deberia haberla')
#find_solution()
    
    
