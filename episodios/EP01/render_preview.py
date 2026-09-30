"""EP01: animação técnica original, sem fabricantes ou locução. Pillow + FFmpeg."""
from pathlib import Path
import math, subprocess, json
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
W, H, FPS, SECONDS = 720, 1280, 24, 42
BG, PANEL, WHITE, MUTED = '#081323', '#12253b', '#f2f6fc', '#a7b9cc'
CYAN, AMBER = '#40d8ed', '#ffb64f'
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def font(n, bold=False): return ImageFont.truetype(BOLD if bold else FONT, n)
CAPTIONS = [
 (0,2.5,'Como medir aquele ponto sem levar a haste até ele'),
 (2.5,5,'e sem colocar o operador em risco?'),
 (5,8.5,'Em alguns receptores RTK, o laser permite visar'),
 (8.5,13,'um alvo distante ou de acesso difícil.'),
 (13,16,'O GNSS posiciona o equipamento.'),
 (16,19,'A IMU registra sua orientação.'),
 (19,23,'O sistema combina essa direção com a distância medida para calcular o ponto.'),
 (23,27,'Na prática, o operador mira e confere a leitura.'),
 (27,31,'Depois registra a coordenada sem apoiar a haste no alvo.'),
 (31,34,'Mas alcance não é sinônimo de precisão.'),
 (34,37,'Distância, visada e condições de campo também importam.'),
 (37,42,'RTK com laser: mais uma ferramenta para escolher o método certo em campo.')
]
SCENES = [
 (0,5,'DO OUTRO LADO.','Como medir sem alcançar o alvo?'),
 (5,13,'RTK + LASER','Medição remota de pontos'),
 (13,23,'COMO FUNCIONA','Posição + orientação + distância'),
 (23,31,'ROTINA DE CAMPO','Mirar. Conferir. Registrar.'),
 (31,37,'ALCANCE ≠ PRECISÃO','Verifique as condições de campo'),
 (37,42,'MÉTODO CERTO','Tecnologia na prática')
]
def center(d,text,y,n=32,color=WHITE,bold=False):
 f=font(n,bold); width=d.textlength(text,font=f)
 d.text(((W-width)/2,y),text,font=f,fill=color)
def wrapped(d,text,y,n=29,width=604,color=WHITE):
 f=font(n); lines=[]; line=''
 for word in text.split():
  candidate=(line+' '+word).strip()
  if d.textlength(candidate,font=f)>width and line: lines.append(line); line=word
  else: line=candidate
 if line: lines.append(line)
 for i,line in enumerate(lines): center(d,line,y+i*(n+12),n,color)
def tag(d,text,x,y,color=CYAN):
 f=font(19,True); width=d.textlength(text,font=f)+26
 d.rounded_rectangle((x,y,x+width,y+38),radius=10,fill=PANEL,outline=color,width=1)
 d.text((x+13,y+7),text,font=f,fill=color)
def target(d,x,y,r=15):
 d.ellipse((x-r,y-r,x+r,y+r),outline=AMBER,width=3)
 d.line((x-25,y,x+25,y),fill=AMBER,width=2)
 d.line((x,y-25,x,y+25),fill=AMBER,width=2)
def receiver(d,x,y,tilt=0):
 # Símbolo geométrico, não representa a forma de um modelo comercial.
 end=(x+math.sin(tilt)*125,y+math.cos(tilt)*125)
 d.line((x,y,*end),fill=MUTED,width=6)
 d.rounded_rectangle((x-35,y-12,x+35,y+21),radius=9,fill='#6a7c90',outline=WHITE,width=2)
 d.ellipse((x-35,y-23,x+35,y+6),fill='#d6dee8',outline=WHITE,width=2)
 d.ellipse((x+23,y-2,x+30,y+5),fill=CYAN)
def arrow(d,a,b,color=CYAN,width=3):
 d.line((*a,*b),fill=color,width=width)
 angle=math.atan2(b[1]-a[1],b[0]-a[0]); r=13
 d.polygon([b,(b[0]-r*math.cos(angle-.45),b[1]-r*math.sin(angle-.45)),(b[0]-r*math.cos(angle+.45),b[1]-r*math.sin(angle+.45))],fill=color)
def check(d,x,y,color=CYAN):
 d.line((x,y,x+8,y+9,x+24,y-10),fill=color,width=4)
def make_frame(t):
 scene=next(i for i,s in enumerate(SCENES) if s[0]<=t<s[1]); start,end,title,sub=SCENES[scene]
 u=(t-start)/(end-start)
 im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im)
 for x in range(0,W,48): d.line((x,0,x,H),fill='#0c1c2e')
 for y in range(0,H,48): d.line((0,y,W,y),fill='#0c1c2e')
 d.text((46,55),'TOPOGRAFIA EM CAMPO',font=font(22,True),fill=WHITE)
 d.text((46,88),'EP01  /  RTK COM LASER',font=font(17),fill=MUTED)
 d.rounded_rectangle((568,55,674,95),radius=10,fill=PANEL)
 d.text((589,66),f'0{scene+1} / 06',font=font(17,True),fill=CYAN)
 center(d,title,179,40,CYAN,True); center(d,sub,243,24,MUTED)
 d.rounded_rectangle((42,319,678,895),radius=26,fill=PANEL,outline='#28405a',width=2)
 # A cena é sempre um esquema conceitual, sem escala ou dados medidos.
 if scene==0:
  d.polygon([(72,729),(265,729),(324,810),(437,810),(500,657),(645,657),(645,850),(72,850)],fill='#31465d')
  d.line((75,729,265,729,324,810,437,810,500,657,645,657),fill=MUTED,width=3)
  receiver(d,196,590); target(d,569,652)
  d.line((260,741,300,741),fill=AMBER,width=4)
  tag(d,'OBSTÁCULO',306,816,AMBER)
  center(d,'ALVO SEM ACESSO DIRETO',380,23,WHITE,True)
  if u>.35: arrow(d,(231,590),(545,652),CYAN,3)
 elif scene in (1,2,5):
  d.line((78,757,642,757),fill='#597189',width=3)
  receiver(d,185,604,.1); target(d,571,556)
  if scene!=2 or u>.54:
   frac=min(1,u*3) if scene==1 else 1
   p=(222+(548-222)*frac,603+(556-603)*frac)
   arrow(d,(222,603),p,AMBER,3)
   tag(d,'DISTÂNCIA',345,614,AMBER)
  if scene==2:
   if u>.05:
    d.ellipse((159,419,215,475),outline=CYAN,width=3)
    d.line((151,417,128,397),fill=CYAN,width=4); d.line((218,469,246,488),fill=CYAN,width=4)
    arrow(d,(187,483),(185,569),CYAN)
    tag(d,'POSIÇÃO GNSS',81,787)
   if u>.28:
    d.arc((145,555,265,675),-50,25,fill=CYAN,width=4)
    tag(d,'ORIENTAÇÃO IMU',350,787)
  elif scene==1:
   center(d,'MIRA NO ALVO',394,24,WHITE,True)
   tag(d,'RECEPTOR',92,787); tag(d,'PONTO REMOTO',423,787,AMBER)
  else:
   tag(d,'ESCOLHA DO MÉTODO',215,787)
   if u>.3: check(d,555,389)
   center(d,'CONHEÇA AS CONDIÇÕES',394,23,WHITE,True)
 elif scene==3:
  steps=[('01','MIRAR','Definir o ponto-alvo'),('02','CONFERIR','Verificar a leitura'),('03','REGISTRAR','Salvar o ponto')]
  for i,(num,head,detail) in enumerate(steps):
   y=390+i*147; active=u>(i/3)
   d.rounded_rectangle((85,y,633,y+115),radius=18,fill='#19324d',outline=CYAN if active else '#345068',width=2)
   d.text((111,y+30),num,font=font(30,True),fill=CYAN if active else MUTED)
   d.text((182,y+19),head,font=font(27,True),fill=WHITE)
   d.text((182,y+65),detail,font=font(20),fill=MUTED)
   if active: check(d,579,y+51)
 elif scene==4:
  center(d,'MAIS LONGE',409,31,AMBER,True)
  arrow(d,(140,495),(580,495),AMBER,4)
  center(d,'não garante',548,25,MUTED)
  center(d,'MAIS PRECISO',598,31,CYAN,True)
  cx,cy=360,737
  for radius in [65,38,12]: d.ellipse((cx-radius,cy-radius,cx+radius,cy+radius),outline=CYAN,width=2)
  for j in range(5):
   a=j*1.31; r=17+j*7; x=cx+math.cos(a)*r; y=cy+math.sin(a)*r
   d.ellipse((x-4,y-4,x+4,y+4),fill=AMBER)
  tag(d,'VISADA • DISTÂNCIA • CAMPO',166,827)
 center(d,'ILUSTRAÇÃO DO MÉTODO • SEM ESCALA',925,15,MUTED)
 d.rounded_rectangle((42,981,678,1189),radius=18,fill='#0c1b2e',outline='#28405a',width=1)
 caption=next(text for a,b,text in CAPTIONS if a<=t<b)
 wrapped(d,caption,1020,28)
 d.line((46,1221,674,1221),fill='#28405a',width=4)
 d.line((46,1221,46+628*t/SECONDS,1221),fill=CYAN,width=4)
 # Entrada/saída curta de cada cena.
 opacity=min(1,(t-start)/.22,(end-t)/.22)
 if opacity<1: im=Image.blend(Image.new('RGB',(W,H),BG),im,max(0,opacity))
 return im

def main():
 out=ROOT/'EP01_RTK_LASER_PREVIA_SEM_MARCAS.mp4'
 cmd=['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pixel_format','rgb24','-video_size',f'{W}x{H}','-framerate',str(FPS),'-i','pipe:0','-an','-c:v','libx264','-preset','fast','-crf','20','-pix_fmt','yuv420p','-movflags','+faststart',str(out)]
 proc=subprocess.Popen(cmd,stdin=subprocess.PIPE)
 for i in range(FPS*SECONDS):
  proc.stdin.write(make_frame(i/FPS).tobytes())
 proc.stdin.close()
 if proc.wait()!=0: raise RuntimeError('Falha ao codificar o vídeo')
 make_frame(16.5).save(ROOT/'EP01_PREVIA_FRAME.png')
 def stamp(x):
  ms=round(x*1000); return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
 (ROOT/'EP01_legendas.srt').write_text('\n\n'.join(f'{i+1}\n{stamp(a)} --> {stamp(b)}\n{text}' for i,(a,b,text) in enumerate(CAPTIONS))+'\n',encoding='utf-8')
 print(json.dumps({'file':str(out),'seconds':SECONDS,'size':out.stat().st_size,'audio':'none','brand_names':'none'},ensure_ascii=False))
if __name__=='__main__': main()
