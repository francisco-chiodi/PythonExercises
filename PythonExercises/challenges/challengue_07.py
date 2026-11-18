import random
import dgraph


def generar_grafo():
    random.seed(2733)

    n = 20
    vertices = "ABCDEFGHIJKLMNOPQRST"

    g = dgraph.DirectedGraph(n)

    g.add_nodes(vertices)

    for i in range(60):
        n1 = random.choice(vertices)
        if random.random() < 0.90:
            n2 = n1
        else:
            n2 = random.choice(vertices)
        g.add_arc(n1, n2)

        if random.random() < 0.90:
            g.add_arc(n2, n1)

    # retornar el grafo creado.
    return g


def main():

    g = generar_grafo()

    # mostrar los resultados...
    print("Resultados:")
    print("¿El grafo es reflexivo?:", g.is_reflexive())
    print("¿El grafo es simétrico?:", g.is_symmetrical())
    print("¿El grafo es transitivo?:", g.is_transitive())
    print("¿Es relación de equivalencia?:", g.is_equivalence_relation())


if __name__ == "__main__":
    main()