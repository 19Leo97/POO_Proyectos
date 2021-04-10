
#Advertencia: todo número no declarado como lo contrario, se toma como entero
#Multiplicaremos por 1.0 para cuando queremos que un numero sea float

#Variables de las dimensiones del canvax y lado de cuadros, ajustables
canvasx=1360
canvasy=700
lado=5

#Definimos variables de pausa y velocidad
Pausa=True
lentitud=10

#Definimos variables relacionadas a la ubicacion de la grilla en el canvas
columna=canvasx/lado
extrax=((1.0*canvasx/lado)-columna)*0.5*lado
fila=canvasy/lado
extray=((1.0*canvasy/lado)-fila)*0.5*lado
        
#Definimos una matriz de estados en 0
estado=[]
for x in range(columna):
    estado_y=[]
    for y in range(fila):
        estado_y.append(0)
    estado.append(estado_y)

#Estructura ejemplo de partida        
#estado[3][1]=1
#estado[3][2]=1
#estado[3][3]=1
#estado[2][3]=1
#estado[1][2]=1

#Hacemos una copia de la matriz de estados
estado_N=[]
for x in range(columna):
    estado_y=[]
    for y in range(fila):
        estado_y.append(estado[x][y])
    estado_N.append(estado_y)




def setup():
    global canvasx,canvasy
    size(canvasx,canvasy)
    frameRate(60)
    

def draw():
    global canvasx,canvasy,lado,estado,estado_N,Pausa,lentitud
    background(50)
    
    
    #Definimos de otra forma los frames por segundo, deacuerdo a la variable "lentitud"
    if lentitud<1: lentitud=1
    if (frameCount%lentitud==0): Accion=True
    else: Accion=False
    
    if (not Pausa) and Accion:
        print(frameCount)
        #Actualizamos los nuevos estados
        for x in range(columna):
            for y in range(fila):
                estado[x][y]=estado_N[x][y]
    
    
    #Imprimimos cuadrado por cuadrado
    for x in range(columna):
        for y in range(fila):
                        
            #miramos su estado para rellenarlo
            if estado[x][y]==0: noFill()
            else: fill(250)
            
            #Dibujamos el cuadrado
            posx=(x*lado)+extrax
            posy=(y*lado)+extray
            strokeWeight(0.4)
            stroke(250)
            square(posx,posy,lado)
            
            if (not Pausa) and Accion:
                #Hallamos la suma de los estados vecinos
                vecinos= estado[(x+1)%columna][(y+1)%fila]\
                            + estado[(x+1)%columna][(y)%fila]\
                            + estado[(x+1)%columna][(y-1)%fila]\
                            + estado[(x)%columna][(y+1)%fila]\
                            + estado[(x)%columna][(y-1)%fila]\
                            + estado[(x-1)%columna][(y+1)%fila]\
                            + estado[(x-1)%columna][(y)%fila]\
                            + estado[(x-1)%columna][(y-1)%fila] 
                
                #Definimos las leyes para asignar un nuevo estado
                #1° Ley: Si esta muerta y hay solo 3 vecinos vivos, revive:
                if estado[x][y]==0 and vecinos==3:
                    estado_N[x][y]=1
                #2° Ley: Si esta viva y no hay 2 o 3 vecinos vivos, muere:
                elif estado[x][y]==1 and (vecinos<2 or vecinos>3):
                    estado_N[x][y]=0
                #Si no, se deja el mismo estado
                else: estado_N[x][y]=estado[x][y]
            

def keyPressed():
    #Teclas para pausar y velocidad
    global Pausa,lentitud
    if int(keyCode)==32:
        Pausa=not Pausa
    if key==CODED:
        if keyCode==LEFT:
            lentitud+=1
        if keyCode==RIGHT:
            lentitud-=1
    
    #Teclas para patrones establecidos y aleatorios
    if key=='0': 
        for x in range(columna):
            for y in range(fila):
                estado[x][y]=estado_N[x][y]=0
    
    if key=='1': 
        for x in range(columna):
            for y in range(fila):
                estado[x][y]=estado_N[x][y]=int(random(2))%2

#Click para cambiar estado
def mousePressed():
    if mouseX>extrax and mouseX<(canvasx-extrax) and mouseY>extray and mouseY<(canvasy-extray):
        estado[int(mouseX-extrax)/lado][int(mouseY-extray)/lado]=not estado[int(mouseX-extrax)/lado][int(mouseY-extray)/lado]
        estado_N[int(mouseX-extrax)/lado][int(mouseY-extray)/lado]=not estado_N[int(mouseX-extrax)/lado][int(mouseY-extray)/lado]

    
