
#Advertencia: todo número no declarado como lo contrario, se toma como entero
#Multiplicaremos por 1.0 para cuando queremos que un numero sea float
canvasx=523
canvasy=419
lado=50

Pausa=False
lentitud=40

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
        
estado[0][0]=1
estado[0][1]=1
estado[0][2]=1

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
    global canvasx,canvasy,lado,estado,estado_N,Pausa
    background(50)
    
    
    #Definimos de otra forma los frames por segundo, deacuerdo a la variable "lentitud"
    if (frameCount%lentitud==0): Accion=True
    else: Accion=False
    
    if (not Pausa) and Accion:
        #Actualizamos los nuevos estados
        for x in range(columna):
            for y in range(fila):
                estado[x][y]=estado_N[x][y]
    
    
    #Imprimimos cuadrado por cuadrado
    for x in range(columna):
        for y in range(fila):
                        
            #miramos su estado para rellenarlo
            if estado[x][y]==0: noFill()
            else: fill(220)
            
            #Dibujamos el cuadrado
            posx=(x*lado)+extrax
            posy=(y*lado)+extray
            strokeWeight(1)
            stroke(220)
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
    global Pausa
    if int(keyCode)==32:
        Pausa=not Pausa
