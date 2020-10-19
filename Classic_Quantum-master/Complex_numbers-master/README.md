# Numeros Complejos
Numeros complejos es un proyecto en el cual se encuentra la librería complex_numbers, librería la cual tiene como funcion realizar 
operaciones basicas de los números complejos, de igual manera contiene funciones con operaciones entre vectores, matrices y escalares complejos. Cabe aclarar que se entiende un número complejo como un número con una parte real, y
una parte imaginaria. En el programa el número complejo se __muestra__ como `real + imaginario*i__`, sin embargo al momento de crearlo se presenta como una __tupla(real,img)__, el vector se __representa__ como una lista __[a,b,c,], donde a,b,c pertenecen a los complejos__, una matriz se representa como una lista de listas `A [[a,b,c],[d,e,f],[g,h,i]]` ,donde a,b,c,d,e,f,g,h,i y `A[0][0] = a` pertenecen a los complejos__
Para facilitar la experiencia del usuario, en el siguiente documento se le explica, como se debe usar la libreria, de igual manera, 
la libreria contiene comentarios en cada una de sus funciones en donde se explica que hace cada funcion.  

## Funciones complejos
- __Para facilitar la experiencia del usuario todos los números en este programa son redondeados a dos cifras.__
- Suma de números complejos.
    + Retorna un número complejo en forma cartesiana.
    + Sean dos númeroscomplejos _C1(a1,b1)_ y _C2(a2,b2)_, el resulatdo de la suma de estos dos es un número complejo en forma cartesiana _C3(a1+a2, b1+b2)_.
- Resta de número complejos.
    + Retorna un número complejo en forma cartesiana.
    + Sean dos númeroscomplejos _C1(a1,b1)_ y _C2(a2,b2)_, el resulatdo de la resta de estos dos es un número complejo en forma cartesiana _C3(a1-a2, b1-b2)_.
- Producto entre números complejos.  
    + Retorna un número complejo en forma cartesiana.
    + Sean dos número complejos _C1(a1,b1)_ y _C2(a2,b2)_, se realiza el producto entre números complejos, dando asi como resultado un número complejo _C3(a1*a2 - b1*b2, a1*b2 + a2*b1)_
- Division entre números complejos.  
    + Retorna un número complejo en forma cartesiana.
    + Sean dos números complejos _C1(a1,b)_ y _C2(a2,b2)_, se realiza el cocientre dando como resultado un número complejo _C3((a1*a2 + b1*b2)/b1^2, (b1*a2 - a1*b2)/b2^2))_
- Módulo o norma de un número complejo.  
    + Retorna el un número con el valor del módulo del número complejo.
    + Sea un número complejo _C(a,b)_, su módulo se da por _mod = sqrt(a^2+b^2)_.
- Conjugado de un número complejo.  
    + Retorna un número complejo en forma cartesiana.
    + Sea un número complejo _C1(a1,b1)_, su conjugado sería _C2(a1,-b1)_.
- Coordenadas de un número complejo de cartesianas a polares. 
    + Retorna un número complejo en forma polar.
    + Sea unnúmero complejo _C1(a,b)_, su forma polar es _C1(modulo, fase)_.
- Fase de un número complejo.
    + Reetorna un número con el valor de la fase o ángulo de un número complejo.
    + Sea _C(a,b)_ un número complejo, su fase esta dada por _arctan(b/a)_.
- Coordenadas de un número complejo de polar a cartesianas.  
    + Retorna un número complejo en forma cartesiana.
    + Sea un número complejo en forma polar _C(r,tetha)_, su forma cartesiana esta dada por _C(rcos(tetha),rsen(tetha))_.
    
## Funciones vectores/matricez complejas
- En este programa siempre se refiere a vector, matrices y escalares como complejos.
- Suma de vectores(complejos).
    + sum_vect(A,B)
    + Retorna el vector resultante de la suma de dos vectores, teniendo en cuenta que deben ser de la misma dimensión.
    + Sean dos vectores complejos _A [a,b,c,...,n],B [x,y,x,...,m]_ el vector resultante de la suma de A+B es _C [a+x,b+y,c+z,...,n+m]_.
- Inverso aditivo de vectores.
    + inv_adi(A)
    + Retorna el vector _inverso aditivo_ de un vector
    + Sea A un vector __C__ de dimension _n_, el vector _B_ inverso aditivo de A es definido como A+B = 0
- Producto entre un escalar y un vector.
    + mul_esc_vect(A,B)
    + Retorna el vector resultante de el producto entre un escalar y un vector.
    + Sea A un vector de dimension n y z un escalar complejo, z*A = C de dimension n, C[i] = z*A[i]
- Suma matrices complejas.
    + sum_mat_com(A,B)
    + Rerorna la matriz resultante de la suma entre dos matrices.
    + Sea A y B matrices de dimension _m*n_, la matriz resultante de la suma de A y B esta definida como: C[i][j] = A[i][j] + B[i][j].
- Inverso aditivo de un matriz.
    + inv_adit_mat(A)
    + Retorna la matriz _inversa aditiva_ de una matriz.
    + Sea A una matriz de dimensiones _m*n_, su matriz B _inversa aditiva_ de dimension _m*n_ es definida como A+B = 0
- Producto escalar matriz.
    + mult_esc_mat(A,B)
    + Retorna la matriz resultante de el producto entre un escalar y una matriz
    + Sea A una matriz de dimensiones _m*n_ y x un escalar, la matriz resultante C del producto x*A esta definida como C[i][j] = z*A[i][j].
- Transpuesta de una matriz, vector.
    + transpuesta(A)
    + Retorna la matriz/vector  traspuesta/o de una matriz/vector.
    + Sea A una matriz de dimensiones _m*n_ y B un vector de dimension _l_, la matriz transpuesta de A,C, y el vector transpuesto de B,D, estan definidos como. C[i][j] = A[j][i] donde C es de dimensiones _n*m_, D[i] = [[A[i]]], donde D es de dimension _l_.
- Conjugado de una matriz/vector.
    + conjugado(A)
    + Retorna la matriz/vector conjugada/o de una matriz/vector.
    + Sea A una matriz de dimensiones _m*n_ y B un vector de dimension _l_, la matriz conjugada de A,C, y el vector conjugado de B,D, estan definidos como. C[i][j] = conjugado(A[i][j]) donde C es de dimensiones _m*n_, D[i] = conjugado(B[i][j]), donde D es de dimension _l_.
- Adjunta de una matriz/vector.
    + adjunta(A)
    + Retorna la matriz/vector adjunta/o de una matriz/vector.
    + Sea A una matriz de dimensiones _m*n_ y B un vector de dimension _l_, la matriz adjunta de A,C, y el vector adjunto de B,D, estan definidos como. C = transpuesta(conjugado(A)) donde C es de dimensiones _n*m_, D = conjugado(transpuesta(B)), donde D es de dimension _l_.
- Producto entre matrices
    + mult_mat(A,B)
    + Retorna la matriz resultante del producto entre dos matrices.
    + Sea A una matriz de dimensiones _m*n_ y B una matriz de dimensiones _n*l_, la matriz resultante del produto entre A y B, es la matriz C, definida como C[i][j] = (+k|0 <= k <n: A[i][k]*B[k][j]), de dimensiones _m*l_.
- Accion de un mariz sobre un vector.
    + accion(A,B)
    + Retorna el vector resultantes del resultado de la accion de una matriz sobre un vecor.
    + Sea A una matriz de dimensiones _m*n_ y B un vector de dimension _n_, C es el vector resultantes de la accion de A sobre B, definida como C[i] = (+j| 0<=j < n: A[i][j]*B[j]).
- Producto interno entre vectores.
    + product_in(A,B)
    + Retorna el valor resultantes de el producto interno entre vectores.
    + Sea A un vector de dimension _n_ y B un vector de dimension _n_, el producto interno entre A y B denotado como <A,B>, es definido como. <A,B> = (+i| 0<= i< n: A[i][0]*B[i]).
- Norma de un vector.
    + norma_vect(A)
    + Retorna el valor resultante de la norma de un vector.+
    + Sea A un vector de dimension _n_, la norma del vector A denotado como |A|, es definido por |A| = <adjunta(A),A>.
- Distancia entre vectores.
    + dist(A,B)
    + Retorna el valor de la distancia entre dos vectores.
    + Sea A un vector de dimension _n_ y B un vector de dimension _n_, la distancia entre A y B, denotado como d(A,B) es definido como d(A,B)= |A-B|
- Unitario.
    + unitary(A)
    + Retorna si una matriz es unitaria o no.
    + Sea una matriz A de dimension n*n, se dice que A es unitaria si y solo si A = adjunta(A).
- Hermitiana.
    + hermitian(A)
    + Retorna si una matriz es hermitiana o no.
    + Sea una matriz A de dimension _n*n_, se dice que A es hermitiana si y solo si A = adjunta(A) = I_n, donde I_n es la matriz identidad de dimension _n*n_.
- Producto tensor.
    + product_tensor(A,B)
    + Retorna la matriz/vector de el producto tensor entre dos matrices/vectores.
    + Sea A una matriz _n*m_ y B una matriz _k*l_, C la matriz resultante de el producto tensor de A y B , donde C[i][j] = A[i//k][j//l]*B[i%k][j%l], de dimensiones _(nk)*(ml)_.
    + Sea A un vector de dimension _n_ y B un vector de dimension _m_, C el vector resultante de el producto tensor de A y B, donde C[i] = A[i//m]*B[j%m], de dimension _mn_.
    

    
 
 ## Ejecución  
 
 Para ejecutar de manera eficiente y correcta la libreria complex_numbers siga estos pasos...
 + Descargue el archivo __complex_numbers.py__ del repositorio,desde la opcion open(parte superior), en el menu deplegable seleccione Dowloand Zip.
 + Una vez descargado el archivo.py, abra la aplicacion IDLE(Python...), una vez dentro abra el archivo descargado anteriormente y oprima __F5__.Si usted no tiene la aplicacion anteriormente nombrada puede descargarla desde [Python](https://www.python.org/downloads/). 
 + Para crear un número complejo, asigne a una variable con el nombre que desee `complex_cart(real,img)`, entre el parentesis debe ingresar el valor de la 
   parte real del número complejo, seguido el valor de la parte imaginaria del número.    
   
   ![Imgur](https://i.imgur.com/TNsnpXW.png)
 + Para ejecutar una operacion entre números complejos(+,-,*,/), asigne a dos variables un número complejo, siguiendo el paso anterior, posterior a esto  operelas
   como lo haría normalmente.   
   
   ![Imgur](https://i.imgur.com/zMsCrNB.png)
 + Para ejecutar las fucniones de __modulo,fase,polar,conjugado__, debe llamar cada una de las funciones de la siguiente mánera.    
 
   ![Imgur](https://i.imgur.com/1PPoFGf.png)
 + Para ejecutar la función __cartesiana__, debe crear un número complejo en forma polar de la misma mánera que se creó un número complejo en forma cartesiana. Sin embargo en este caso se le asigna a la variable `complex_polar(norma,ángulo)` , asi ya puede hacer uso de la función __cartesiana__. De la siguiente mánera.   
 
   ![Imgur](https://i.imgur.com/0iWoVE5.png)
 + Para ejecutar la librería Test_complex siguiendo el primer paso, descargue la libreria y abra el archivo en el __IDLE__. 
     + Para ejecutar la librería simplemente oprima __F5__ en su teclado, el archivo se ejecutara. En la consola, se le mostrará el número de pruebas que se 
     realizaron en el programa, en este caso son 9, una por cada funcion de el programa _complex_numbers_. 
     
     ![Imgur](https://i.imgur.com/3nmPvyb.png)
 + Para modificar los valores de prueba, abra el archivo de Test_complex. En el encontrara la def `setUp`, en esta se inicializa cada uno de los números complejos. Si es de su agrado puede cambiar los valores o el nombre de las variables establecidos en el archivo, simplemente mantenga antes de cada nombre el __self.___, asi si desea cambiar la variable `self.complex_a` por `comp1`, este pasaría a ser `self.comp1`. Los valores se cambian en la linea `complex_cart(/,/)` ó `complex_polar(/,/)` dependiendo de la forma del número copmlejo, simplemente cambie los valores que se encuentran en los espacios del parentesis. De la siguiente mánera. 
 ![Imgur](https://i.imgur.com/xMbjswT.png)  
     + Para modificar las pruebas de cada función, simplemente cambie el contenido del `str()`, las pruebas estan formadas por dos partes la prueba, y el resultado esperado.
     `self.assertEqual(str(prueba),str(resultado))`. Debe tener en cuenta que retorna cada función (entero, tupla, decimal) además que recibe cada función(complex_cart(),complex_polar())
     ![Imgur](https://i.imgur.com/fb07UKm.png)
     
 + Para ejecutar el archivo mat_op.py, siga el paso 2 y ejecutelo.
 
 + Para crear un vector real de n dimension, en la consola digite `[a,b,c,...,n]`, y asignelo si es de su preferencia a una variable.    
 
 + para crear un vector complejo de n dimension, en la consola digite `[complex_cart(a,a'),complex_cart(b,b'),...,complex_cart(n,n')]`, y asignelo si es de su preferencia a una variable.    
 
    ![Imgur](https://i.imgur.com/eTkTkfQ.png)    
    
 + Para crear una matriz real de dimensiones _n*m_, en la consola digite `[[a,b,c,...,n],...,[a_m,b_m,c_m,...,n_m]]`, y asignelo si es de su preferencia  una variable.    
 
 + Para crear una matriz compleja de dimensiones _n*m_, en la consola digite `[[complex_cart(a,a'),complex_cart(b,b'),...,complex_cart(n,n')],...,[complex_cart(a_m,a'),complex_cart(b_m,b'),...,complex_cart(n_m,n')]]`, y asignelo si es de su preferencia  una variable.    
 
    ![Imgur](https://i.imgur.com/7MvXgXL.png)    
    
 + Para elegir cualquiera de los componentes de la matriz o vector tenga en cuenta sus dimensiones, para llamar un componente de un vector de dimension n simplemenmte digite `vector[i]`, donde 0<= i < n.    
 
 + Para llamar una componente de una matriz de dimensiones _n*m_, digite matriz[i][j], donde 0<= i< m, 0<=j<n. Para llamar una fila de la matriz digite matriz[i], donde 0<=i<m.
    ![Imgur](https://i.imgur.com/WBmRjo5.png)    
    
 + Para ejecutar cada una de las funciones tenga en cuenta como se llama a cada una, en la seccion funciones vectores/matrices complejas encuentra esta informacion.    
 
 + Acontinuacion encontrara ejemplos de como usar el archivo mat_op.py.    
 
    ![Imgur](https://i.imgur.com/hUpMaDF.png)    
    
    ![Imgur](https://i.imgur.com/Cvz4jOQ.png)    
    
    ![Imgur](https://i.imgur.com/MbjG27a.png)
    
```
1. creee unoanaosanlksjad
2. askjdañslkjdñlsa
```
 
     
 
 ## Autor
   ___Cristian Andres Castellanos Fino___
