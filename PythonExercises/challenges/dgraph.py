class DirectedGraph:
    def __init__(self, n=10):
        """Crea un grafo dirigido vacío para un máximo de n nodos. El grafo dirigido se crea con capacidad
        para hasta un máximo de n nodos (aunque podría efectivamente tener menos que n nodos hasta que estos sean
        agregados al grafo).

        :param n: el número máximo de nodos que serán representados en este grafo.
        """

        # el vector de nodos, inicialmente con n casillas en None.
        self.nodes = n * [None]

        # la matriz de adyacencias, inicialmente toda en False.
        self.ady = [n * [False] for f in range(n)]

    def __str__(self):
        """Retorna una cadena con el contenido del grafo dirigido.
        Retorna una cadena con el contenido del grafo dirigido, en forma matricial, lista para ser visualizada.

        :return: Una cadena con el contenido del grafo.
        """
        r = "    "
        for nd in self.nodes:
            r += " " + str(nd) + "   "
        r += "\n"

        n = len(self.nodes)
        for i in range(n):
            r += str(self.nodes[i]) + "  "
            for j in range(n):
                c = ""
                if self.ady[i][j] is True:
                    c = "1"
                else:
                    c = "0"
                r += "  " + c + "  "
            r += "\n"

        return r

    def size(self):
        """Retorna la cantidad de nodos (o vértices) que tiene el grafo dirigido.

        :return: el número de nodos que tiene el grafo dirigido.
        """
        return len(self.nodes)

    def add_arc(self, n1, n2):
        """Une los nodos n1 y n2 con un arco en el grafo dirigido.
        Une dos nodos n1 y n2 con un arco. El arco partirá del nodo cuyo valor es n1 y llegará al nodo cuyo
        valor es n2, en caso de poder crear el arco. Si alguno de los nodos n1 o n2 no existe en el grafo, la
        operación no se llevará a cabo y retornará False.

        :param n1: el valor del nodo de partida del arco.
        :param n2: el valor del nodo de llegada del arco.
        :return: True si el arco pudo ser creado.
        """
        out = False
        i1 = self.search(n1)
        i2 = self.search(n2)
        if i1 != -1 and i2 != -1:
            self.ady[i1][i2] = True
            out = True
        return out

    def remove_arc(self, n1, n2):
        """Elimina el arco entre los nodos n1 y n2.
        Elimina el arco entre los nodos n1 y n2. Se supone que el arco parte del nodo cuyo valor es n1 y llega al
        nodo cuyo valor es n2. Si alguno de los nodos n1 o n2 no existe en el grafo, la operación no se llevará a
        cabo y retornará False.

        :param n1: el valor del nodo de partida del arco.
        :param n2: el valor del nodo de llegada del arco.
        :return: True si el arco pudo ser eliminado.
        """
        out = False
        i1 = self.search(n1)
        i2 = self.search(n2)
        if i1 != -1 and i2 != -1 and self.ady[i1][i2] is True:
            self.ady[i1][i2] = False
            out = True
        return out

    def is_there_arc(self, n1, n2):
        """Verifica si existe el arco entre los nodos n1 y n2.
        Comprueba si existe el arco entre los nodos n1 y n2. Se supone que el arco parte del nodo cuyo valor
        es n1 y llega al nodo cuyo valor es n2. Si alguno de los nodos n1 o n2 no existe en el grafo, la operación
        retorna False.

        :param n1: el valor del nodo de partida del arco.
        :param n2: el valor del nodo de llegada del arco.
        :return: True si el arco existe.
        """
        out = False
        i1 = self.search(n1)
        i2 = self.search(n2)
        if i1 != -1 and i2 != -1:
            out = self.ady[i1][i2]
        return out

    def search(self, x):
        """Busca un nodo en el grafo dirigido, y retorna su posición en el vector de nodos.
        :param x: el valor del nodo a buscar.
        :return: el índice del nodo si el mismo es encontrado, o -1 si no está en el grafo.
        """
        n = len(self.nodes)
        for i in range(n):
            if self.nodes[i] == x:
                return i
        return -1

    def add_nodes(self, ln):
        """Agrega nodos al grafo. Este método es la única forma recomendable de hacerlo en este modelo.
        Agrega cada uno de los valores de la lista ln al vector de nodos del grafo dirigido. Se recomienda que
        la lista ln contenga cadenas simples (y solo cadenas) que representen cada una a los valores a almacenar
        como nodos del grafo. El método no comprueba si los valores de ln son efectivamente cadenas pero sí comprueba
        si la cantidad de nodos a agregar coincide con el tamaño del vector de nodos tal como fue creado por el
        método constructor __init__(): si esos tamaños no coindicen, el método aborta y finaliza retornando False.
        Si el vector de nodos ya estaba creado, el método finaliza sin hacer nada y retorna tambien False.

        :param ln: Una lista con los valores a agregar como nodos del grafo dirigido.
        :return: True si los nodos pudieron efectivamente agregarse al grafo dirigido.
        """
        cn, n = len(ln), len(self.nodes)
        if self.nodes[0] is not None or cn != n:
            return False

        for i in range(n):
            self.nodes[i] = ln[i]
        return True

    def output_grade(self, x):
        """Calcula el "fuera de grado" del nodo x.
        Calcula y retorna el "fuera de grado" del nodo x. Si x no existe en el grafo dirigido, el método retorna -1.

        :param x: El valor del nodo al que se calculará el fuera de grado.
        :return: El fuera de grado de x (o -1 si x no existe en el grafo).
        """
        fx = self.search(x)
        if fx == -1:
            return -1

        n = len(self.nodes)
        og = 0
        for c in range(n):
            if self.ady[fx][c] is True:
                og += 1
        return og

    def input_grade(self, x):
        """Calcula el "entre grado" del nodo x.
        Calcula y retorna el "entre grado" del nodo x. Si x no existe en el grafo dirigido, el método retorna -1.

        :param x: El valor del nodo al que se calculará el entre grado.
        :return: El entre grado de x (o -1 si x no existe en el grafo).
        """
        cx = self.search(x)
        if cx == -1:
            return -1

        n = len(self.nodes)
        ig = 0
        for f in range(n):
            if self.ady[f][cx] is True:
                ig += 1
        return ig

    def grade(self, x):
        """Calcula el "grado" del nodo x.
        Calcula y retorna el "grado" del nodo x. Si x no existe en el grafo dirigido, el método retorna -1.

        :param x: El valor del nodo al que se calculará el grado.
        :return: El grado de x (o -1 si x no existe en el grafo).
        """
        cx = self.search(x)
        if cx == -1:
            return -1

        g = self.output_grade(x) + self.input_grade(x)
        return g

    def is_reflexive(self):
        n = len(self.ady)
        for i in range(n):
            if not self.ady[i][i]:
                return False
        return True

    def is_symmetrical(self):
        n = len(self.ady)
        for f in range(n - 1):
            for c in range(f + 1, n):
                if self.ady[f][c] != self.ady[c][f]:
                    return False
        return True

    def is_transitive(self):
        n = len(self.ady)
        for i in range(n):
            for j in range(n):
                if self.ady[i][j]:
                    for k in range(n):
                        if self.ady[j][k] and not self.ady[i][k]:
                            return False
        return True

    def is_equivalence_relation(self):
        return self.is_reflexive() and self.is_symmetrical() and self.is_transitive()