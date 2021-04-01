#Advertencia: todo número no declarado como lo contrario, se toma como entero
#Multiplicaremos por 1.0 para cuando queremos que un numero sea float
canvasx=223
canvasy=119
lado=13

def setup():
    global canvasx,canvasy
    size(canvasx,canvasy)
    

def draw():
    global canvasx,canvasy,lado
    background(50)
    
    #Definimos variables relacionadas a la ubicacion de la grilla en el canvas
    columna=canvasx/lado
    extrax=((1.0*canvasx/lado)-columna)*0.5*lado
    fila=canvasy/lado
    extray=((1.0*canvasy/lado)-fila)*0.5*lado
        
    #Imprimimos cuadrado por cuadrado
    for x in range(columna):
        for y in range(fila):
            posx=(x*lado)+extrax
            posy=(y*lado)+extray
            strokeWeight(1)
            noFill()
            stroke(200)
            square(posx,posy,lado)
            
            
