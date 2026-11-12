MOTIVOS = (
    'Textos copiados de otra fuente conocida',
    'Texto con referencia pero muy largo',
    'Texto con fuente citada pero inválida',
    'Texto en otro idioma sin traducción ni justificación',
    'Abstract no coincidente con el desarrollo del paper',
    'Otro'
)

OBVIEDADES = (
    'Muy obvio', 'Obvio', 'Disimulable', 'Sutil', 'Muy sutil'
)


class Paper:

    def __init__(self, id_paper, titulo, autor, motivo, obviedad):
        self.id_paper = id_paper
        self.titulo = titulo
        self.autor = autor
        self.motivo = motivo
        self.obviedad = obviedad

    def __str__(self):
        return (f'ID: {self.id_paper:>6} |Título: {self.titulo:<30} |Autor: {self.autor:<30} '
                f' |Motivo: {MOTIVOS[self.motivo - 1]:<30} '
                f' |Obviedad: {OBVIEDADES[self.obviedad - 1]:<10}')

class Totalizador:
    def __init__(self, desc_motivo, nro_motivo, nro_obviedad, desc_obviedad, cantidad):
        self.desc_motivo = desc_motivo
        self.nro_motivo = nro_motivo
        self.nro_obviedad = nro_obviedad
        self.desc_obviedad = desc_obviedad
        self.cantidad = cantidad