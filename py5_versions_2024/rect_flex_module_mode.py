"""
To draw SVG for lasercut box parts - 
Depends on py5 (https://py5coding.org)

This draws "half" a box, cut twice to build a complete box
"""

import py5   

fator_escala = 3.78 * 50 / 189

NOME = "caixa_flex-v1"  # Precisa ser cortado 2x! só desenha "meia caixa"
W, H, P = 200, 120, 50  # dimensões
R = 30                  # raio
XO, YO = 50, 50         # offset do desenho na página

def setup():
    py5.size(400, 400) # tamanho do desenho
    # PREPARO DA GRAVAÇÂO DO SVG
    saida = py5.create_graphics(
        int(py5.width * fator_escala),
        int(py5.height * fator_escala),
        py5.SVG, f'{NOME}.svg')
    py5.begin_record(saida)
    saida.scale(fator_escala)
    py5.no_fill()
    py5.stroke(0)
    
    # Desenho dos elementos
    # SEGMENTO LATERAL
    HSR1 = W / 2 - R
    py5.line(XO, YO, XO + P, YO)
    seg_rect(XO, YO, P, HSR1)
    HSF1 = py5.PI * R / 2
    flexivel(XO, YO + HSR1, P, HSF1)
    HSR2 = H - 2 * R
    seg_rect(XO, YO + HSR1 + HSF1, P, HSR2)
    flexivel(XO, YO + HSR1 + HSF1 + HSR2, P, HSF1)
    seg_rect(XO, YO + HSR1 + 2 * HSF1 + HSR2, P, HSR1)
    py5.line(XO, YO + HSR1 + HSF1 + HSR2 + HSF1 + HSR1,
         XO + P, YO + HSR1 + HSF1 + HSR2 + HSF1 + HSR1)
    
    # FUNDO / TAMPA
    XOT, YOT = XO + 2*P, YO
    # canto superior direito
    py5.arc(XOT + W - R, YOT + R, R * 2, R * 2, py5.PI + py5.HALF_PI,  py5.TWO_PI)
    # canto superior esq 
    py5.arc(XOT + R, YOT + R, R * 2, R * 2, py5.PI, py5.PI + py5.HALF_PI)
    #canto inf direito
    py5.arc(XOT + W - R, YOT + H - R, R * 2, R * 2, 0, py5.HALF_PI)
    # ccanto inf 
    py5.arc(XOT + R, YOT + H - R, R * 2, R * 2, py5.HALF_PI, py5.PI)
    seg_rect(XOT, YOT + R, W, H - 2 * R, dd=-3)
    py5.translate(XOT + W / 2, YOT + H / 2)
    py5.rotate(py5.HALF_PI)
    seg_rect2(-H / 2, -W / 2 + R, H, W - 2 * R, dd=-3)
    
    # FIM DA GRAVAÇÂO DO SVG
    py5.end_record()

def seg_rect2(x, y, w, h, hd=10, dd=3):
    lado(x, y, h / 2, hd, dd)
    lado(x + w, y, h / 2, hd, -dd)
    lado(x, y + h / 2, h / 2, hd, dd)
    lado(x + w, y + h / 2, h / 2, hd, -dd)
                                                                                           
def seg_rect(x, y, w, h, hd=10, dd=3):
    lado(x, y, h, hd, dd)
    lado(x + w, y, h, hd, -dd)
    
def lado(x, y, h, hd, dd):  
    nd = (h - (2 * hd)) / 3
    py5.begin_shape()
    py5.vertex(x, y)
    py5.vertex(x, y + nd)
    py5.vertex(x + dd, y + nd)
    py5.vertex(x + dd, y + nd + hd)
    py5.vertex(x, y + nd + hd)
    py5.vertex(x, y + 2 * nd +hd)
    py5.vertex(x + dd, y + 2 * nd +hd)
    py5.vertex(x + dd, y + 2 * nd + 2 * hd)
    py5.vertex(x, y + 2 * nd + 2 * hd)
    py5.vertex(x, y + 3 * nd + 2 * hd)
    py5.end_shape()
     
def flexivel(x, y, w, h_total, n=6):
    h = h_total / n
    segmento(x, y, w, h, start=None)
    for i in range(1, n - 1):
        segmento(x, y + h * i, w, h)
    #translate(5, 5)
    segmento(x, y + h * (n - 1), w, h, end=None)    
    
def segmento(x, y, w, h, start=None, end=None):
    with py5.push_matrix():
        py5.translate(x, y)
        pd = 0
        lateral(0, pd, h)
        lateral(w, -pd, h)
        tg =  h / 4.0
        mh = h / 2.0
        hs4 = h / 4.0
        if start is None:
            py5.line(pd, 0, (w - tg) / 2.0, 0)
            py5.line((w + tg) / 2.0, 0, w - pd, 0)
        else:
            py5.line(0, -hs4 * start, w, -hs4 * start)            
        py5.line(pd, mh, (w - tg) / 2.0, mh)
        py5.line((w + tg) / 2.0, mh, w - pd, mh)
        py5.line(pd + tg, hs4, w - pd - tg, hs4) 
        py5.line(pd + tg, hs4 * 3, w - pd - tg, hs4 * 3) 
        if end is not None: # acabamento inferior
            py5.line(0, h + hs4 * end, w, h + hs4 * end)
                            
def lateral(x, e, h):
    hs4 = h / 4.0
    py5.begin_shape()
    py5.vertex(x, 0)
    py5.vertex(x, hs4)
    py5.vertex(x + e, hs4)
    py5.vertex(x + e, 3 * hs4)
    py5.vertex(x, 3 * hs4)
    py5.vertex(x, h)
    py5.end_shape()
    
py5.run_sketch()
