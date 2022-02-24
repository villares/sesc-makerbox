"""
Desenha metade (meia lateral e o fundo ou topo) de uma caixa retangular com cantos arredondados.
Para executar use Processing 3.5.4 + Modo Python
"""

from __future__ import division

add_library('svg')

fator_escala = 3.78 * 50 / 189
 
def setup():
    size(600, 600) # tamanho do desenho
    nome = "caixa_flex-v1"
    saida = createGraphics(int(width * fator_escala),
                           int(height * fator_escala),
                           SVG, nome + '.svg')
    beginRecord(saida)
    saida.scale(fator_escala)
    noFill()
    stroke(0)
    XO, YO = 50, 50
    W, H, P = 200, 120, 50
    R = 30
    # SEGMENTO LATERAL
    HSR1 = W / 2 - R
    line(XO, YO, XO + P, YO)
    seg_rect(XO, YO, P, HSR1)
    HSF1 = PI * R / 2
    flexivel(XO, YO + HSR1, P, HSF1)
    HSR2 = H - 2 * R
    seg_rect(XO, YO + HSR1 + HSF1, P, HSR2)
    flexivel(XO, YO + HSR1 + HSF1 + HSR2, P, HSF1)
    seg_rect(XO, YO + HSR1 + 2 * HSF1 + HSR2, P, HSR1)
    line(XO, YO + HSR1 + HSF1 + HSR2 + HSF1 + HSR1,
         XO + P, YO + HSR1 + HSF1 + HSR2 + HSF1 + HSR1)
    # FUNDO / TAMPA
    XOT, YOT = XO + 2*P, YO
    #rect(XOT, YOT, W, H, R)
    stroke(255, 0, 0)
    # canto superior direito
    arc(XOT + W - R, YOT + R, R * 2, R * 2, PI+HALF_PI, TWO_PI)
    # canto superior esq 
    arc(XOT + R, YOT + R, R * 2, R * 2, PI, PI +HALF_PI)
    #canto inf direito
    arc(XOT + W - R, YOT + H - R, R * 2, R * 2, 0, HALF_PI)
    # ccanto inf 
    arc(XOT + R, YOT + H - R, R * 2, R * 2, HALF_PI, PI)
    seg_rect(XOT, YOT + R, W, H - 2 * R, dd=-3)
    translate(XOT + W / 2, YOT + H / 2)
    rotate(HALF_PI)
    #circle(0, 0, 5)
    #rect(-H / 2, -W / 2, H, W)
    seg_rect2(-H / 2, -W / 2 + R, H, W - 2 * R, dd=-3)
    endRecord()

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
    beginShape()
    vertex(x, y)
    vertex(x, y + nd)
    vertex(x + dd, y + nd)
    vertex(x + dd, y + nd + hd)
    vertex(x, y + nd + hd)
    vertex(x, y + 2 * nd +hd)
    vertex(x + dd, y + 2 * nd +hd)
    vertex(x + dd, y + 2 * nd + 2 * hd)
    vertex(x, y + 2 * nd + 2 * hd)
    vertex(x, y + 3 * nd + 2 * hd)
    endShape()
     
        
def flexivel(x, y, w, h_total, n=6):
    h = h_total / n
    segmento(x, y, w, h, start=None)
    for i in range(1, n - 1):
        segmento(x, y + h * i, w, h)
    #translate(5, 5)
    segmento(x, y + h * (n - 1), w, h, end=None)    
    
def segmento(x, y, w, h, start=None, end=None):
    with pushMatrix():
        translate(x, y)
        pd = 0
        lateral(0, pd, h)
        lateral(w, -pd, h)
        tg =  h / 4.0
        mh = h / 2.0
        hs4 = h / 4.0
        if start is None:
            line(pd, 0, (w - tg) / 2.0, 0)
            line((w + tg) / 2.0, 0, w - pd, 0)
        else:
            line(0, -hs4 * start, w, -hs4 * start)            
        line(pd, mh, (w - tg) / 2.0, mh)
        line((w + tg) / 2.0, mh, w - pd, mh)
        line(pd + tg, hs4, w - pd - tg, hs4) 
        line(pd + tg, hs4 * 3, w - pd - tg, hs4 * 3) 
        if end is not None: # acabamento inferior
            line(0, h + hs4 * end, w, h + hs4 * end)
                            
def lateral(x, e, h):
    hs4 = h / 4.0
    beginShape()
    vertex(x, 0)
    vertex(x, hs4)
    vertex(x + e, hs4)
    vertex(x + e, 3 * hs4)
    vertex(x, 3 * hs4)
    vertex(x, h)
    endShape()
