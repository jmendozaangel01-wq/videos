import json,sys
proj="/home/user/videos/carnegie/proj"
V='<div style="position:absolute;left:0;right:0;top:1000px;height:920px;background:linear-gradient(180deg,rgba(27,26,23,0),rgba(27,26,23,.86))"></div>'
# (id,start,end)
T=[("s1",0,3.2),("s2",3.2,6.0),("s3",6.0,9.0),("p1",9.0,10.5),("p2",10.5,12.4),("p3",12.4,14.0),("s4",14.0,15.4),("s5",15.4,16.8),("s6",16.8,19.6),("s7",19.6,21.9),("s8",21.9,24.8),
("s9",24.8,32.6),("s10",32.6,37.1),("s11",37.1,39.6),("s12",39.6,43.3),("s13",43.3,45.8),("s14",45.8,49.4),("s15",49.4,54.5),
("s16",54.5,59.6),("s17",59.6,62.8),("s18",62.8,66.0),("s19",66.0,68.9),("s20",68.9,71.4),("s21",71.4,73.7),("s22",73.7,77.9),
("s23",77.9,82.2),("s24",82.2,86.0)]
S={i:a for i,a,b in T}; D={i:round(b-a,2) for i,a,b in T}
TOTAL=86.0
def full(i,src,style,cls=""):
    return f'<div class="card {cls}" style="left:0;top:0;width:1080px;height:1920px;border:0"><img id="{i}" src="assets/{src}" style="{style}" /></div>'
B={}
B["s1"]=("background:transparent",'''
  <div style="position:absolute;left:0;right:0;top:900px;height:1020px;background:linear-gradient(180deg,rgba(27,26,23,0),rgba(27,26,23,.88))"></div>
  <div id="s1-t" class="tx" style="top:1010px;font-size:108px;color:var(--cream)">¿TE <span class="or">REEMPLAZAN</span><br>O TE ADAPTAS?</div>''')
B["s2"]=('','''
  <div id="s2-c" class="card" style="left:40px;top:345px;width:1000px;height:800px"><img id="s2-i" src="assets/a2_telar_mecanico.jpg" style="left:-122px;top:0;width:1245px;height:800px;transform-origin:45% 55%" /></div>
  <div id="s2-k" class="tx" style="top:1180px;font-size:40px;letter-spacing:.16em;color:var(--muted);font-weight:700">REVOLUCIÓN INDUSTRIAL</div>
  <div id="s2-t" class="tx" style="top:1250px;font-size:130px">DÉCADA<br>DE <span class="or">1840</span></div>''')
B["s3"]=('','''
  <div id="s3-c" class="card" style="left:140px;top:310px;width:800px;height:949px"><img id="s3-i" src="assets/c1_familia_carnegie.jpg" style="left:0;top:0;width:800px;height:949px" /></div>
  <div id="s3-t" class="tx" style="top:1300px;font-size:120px;text-align:center">FAMILIA<br><span class="or">CARNEGIE</span></div>''')
B["p1"]=("background:#000",'''
  <div class="card" style="left:0;top:0;width:1080px;height:1920px;border:0"><img id="p1-i" src="assets/b2_fabrica_pintura.jpg" style="left:-123px;top:0;width:1327px;height:1920px" /></div>
  '''+V+'''
  <div id="p1-t" class="tx" style="top:1150px;font-size:100px;color:var(--cream)">MILES DE<br><span class="or">TEJEDORES</span></div>''')
B["p2"]=('','''
  <div id="p2-c" class="card" style="left:40px;top:400px;width:1000px;height:750px"><img id="p2-i" src="assets/b1_protesta.jpg" style="left:0;top:0;width:1000px;height:750px" /></div>
  <div id="p2-t" class="tx" style="top:1210px;font-size:120px;text-align:center">POBREZA<br><span class="or">EXTREMA</span></div>''')
B["p3"]=('','''
  <div id="p3-c" class="card" style="left:210px;top:337px;width:660px;height:977px"><img id="p3-i" src="assets/b3_maquina.jpg" style="left:0;top:0;width:660px;height:977px" /></div>
  <div id="p3-t" class="tx" style="top:1364px;font-size:74px;text-align:center">MÁQUINAS TOMARON<br><span class="or">SUS EMPLEOS</span></div>''')
B["s4"]=('','''
  <div id="s4-c" class="card" style="left:40px;top:420px;width:1000px;height:700px"><img id="s4-i" src="assets/d1_andrew_joven.jpg" style="left:-200px;top:0;width:1243px;height:700px;transform-origin:58% 40%" /></div>
  <div id="s4-t" class="tx" style="top:1190px;font-size:120px;text-align:center">EL PEQUEÑO<br><span class="or">ANDREW</span></div>''')
B["s5"]=('','''
  <div class="tx" style="top:700px;font-size:150px;text-align:center;line-height:1.08">
    <span id="s5-w1" style="display:inline-block">ELIGIÓ</span><br>
    <span id="s5-w2" style="display:inline-block">OTRO</span>
    <span id="s5-w3" class="or" style="display:inline-block">CAMINO</span>
  </div>''')
B["s6"]=("background:#000",'''
  <img id="s6-i" src="assets/a7_travesia.jpg" style="position:absolute;left:0;top:0;width:1080px;height:1913px;transform-origin:60% 60%" />
  <div style="position:absolute;left:0;right:0;top:880px;height:1040px;background:linear-gradient(180deg,rgba(27,26,23,0),rgba(27,26,23,.82))"></div>
  <div id="s6-r" class="tx" style="top:1020px;font-size:44px;letter-spacing:.14em;color:var(--cream);font-weight:700;display:flex;justify-content:space-between"><span>ESCOCIA</span><span>EE. UU.</span></div>
  <div id="s6-line" style="position:absolute;left:80px;top:1100px;height:6px;width:870px;background:var(--orange);transform-origin:0 50%"></div>
  <div id="s6-age" class="tx" style="top:1150px;font-size:150px;color:var(--cream)"><span id="s6-num">0</span> <span class="or">AÑOS</span></div>''')
B["s7"]=("background:#000",'''
  <div class="card" style="left:0;top:0;width:1080px;height:1920px;border:0"><img id="s7-i" src="assets/a8_fabrica.jpg" style="left:-700px;top:0;width:2698px;height:1920px" /></div>
  '''+V+'''
  <div id="s7-t" class="tx" style="top:1180px;font-size:92px;color:var(--cream)">FÁBRICA<br><span class="or">DE ALGODÓN</span></div>''')
B["s8"]=("background:#000",'''
  <div class="card" style="left:0;top:0;width:1080px;height:1920px;border:0"><img id="s8-i" src="assets/a10_mensajero.jpg" style="left:-780px;top:0;width:2878px;height:1920px" /></div>
  '''+V+'''
  <div id="s8-t" class="tx" style="top:1190px;font-size:76px;color:var(--cream)">MENSAJERO DE <span class="or">TELÉGRAFOS</span></div>''')
B["s9"]=("background:#000",'''
  <div class="card nt" style="left:0;top:0;width:1080px;height:1920px;border:0"><img id="s9-i" src="assets/a9_lectura.jpg" style="left:0;top:0;width:1084px;height:1920px" /></div>
  '''+V+'''
  <div id="s9-k" class="tx" style="top:1090px;font-size:36px;letter-spacing:.16em;color:var(--cream);font-weight:700">EN SUS RATOS LIBRES</div>
  <div id="s9-0" class="tx" style="top:1170px;font-size:100px;color:var(--cream)">ESTUDIABA EN <span class="or">BIBLIOTECAS</span></div>
  <div id="s9-a" class="tx" style="top:1170px;font-size:100px;color:var(--cream)">PENSAMIENTO <span class="or">CRÍTICO</span></div>
  <div id="s9-b" class="tx" style="top:1170px;font-size:100px;color:var(--cream)"><span class="or">ELOCUENCIA</span></div>
  <div id="s9-c" class="tx" style="top:1170px;font-size:100px;color:var(--cream)">NATURALEZA <span class="or">HUMANA</span></div>''')
B["s10"]=('','''
  <div id="s10-c" class="card" style="left:160px;top:330px;width:760px;height:962px"><img id="s10-i" src="assets/a11_scott.jpg" style="left:0;top:0;width:760px;height:962px" /></div>
  <div id="s10-bar" class="bar" style="top:1272px;font-size:38px"><i></i>THOMAS SCOTT</div>
  <div id="s10-sub" class="tx" style="top:1392px;font-size:48px;letter-spacing:.1em;color:var(--muted);font-weight:700">EMPRESARIO FERROVIARIO</div>''')
B["s11"]=('','''
  <div id="s11-c" class="card" style="left:40px;top:460px;width:1000px;height:700px"><img id="s11-i" src="assets/a12_telegrafo.jpg" style="left:-266px;top:0;width:1532px;height:700px" /></div>
  <div id="s11-t" class="tx" style="top:1220px;font-size:84px;text-align:center">SECRETARIO<br><span class="or">+ TELEGRAFISTA</span></div>''')
B["s12"]=('','''
  <div id="s12-c" class="card" style="left:160px;top:357px;width:760px;height:962px"><img id="s12-i" src="assets/a11_scott.jpg" style="left:0;top:0;width:760px;height:962px" /></div>
  <div id="s12-t" class="tx" style="top:1369px;font-size:130px;text-align:center">SU <span class="or">MENTOR</span></div>''')
B["s13"]=('','''
  <div class="card" style="left:0;top:300px;width:1080px;height:1000px;border-left:0;border-right:0"><img id="s13-i" src="assets/a13_locomotora.jpg" style="left:0;top:0;width:1645px;height:1000px" /></div>
  <div id="s13-t" class="tx" style="top:1360px;font-size:96px;text-align:center">TRENES<br><span class="or">INVERSIONES</span></div>''')
B["s14"]=("background:#000",'''
  <div class="card nt" style="left:0;top:0;width:1080px;height:1920px;border:0"><img id="s14-i" src="assets/a14_puente_fuego.jpg" style="left:0;top:0;width:1084px;height:1920px;transform-origin:45% 45%" /></div>
  <div style="position:absolute;left:0;right:0;top:960px;height:960px;background:linear-gradient(180deg,rgba(27,26,23,0),rgba(27,26,23,.88))"></div>
  <div id="s14-k" class="tx" style="top:1080px;font-size:40px;letter-spacing:.16em;color:var(--cream);font-weight:700">PERO NOTÓ ALGO</div>
  <div id="s14-t" class="tx" style="top:1130px;font-size:100px;color:var(--cream)">PUENTES DE<br><span class="or">MADERA</span></div>''')
B["s15"]=("background:#000",'''
  <div class="card nt" style="left:0;top:0;width:1080px;height:1920px;border:0"><img id="s15-i" src="assets/a15_riel.jpg" style="left:0;top:0;width:1084px;height:1920px;transform-origin:55% 60%" /></div>
  '''+V+'''
  <div id="s15-t" class="tx" style="top:1130px;font-size:92px;color:var(--cream)">RIELES DE <span class="or">HIERRO</span></div>
  <div id="s15-u" class="tx" style="top:1260px;font-size:56px;color:var(--cream);letter-spacing:.06em">MATERIALES VULNERABLES</div>''')
B["s16"]=("background:#000",'''
  <div class="card" style="left:0;top:0;width:1080px;height:1920px;border:0"><img id="s16-i" src="assets/a16_acero.jpg" style="left:-300px;top:0;width:2376px;height:1920px" /></div>
  <div id="s16-heat" style="position:absolute;inset:0;background:var(--orange);opacity:0"></div>
  '''+V+'''
  <div id="s16-k" class="tx" style="top:1110px;font-size:44px;letter-spacing:.16em;color:var(--cream);font-weight:700">SU VISIÓN FUE EL</div>
  <div id="s16-t" class="tx" style="top:1150px;font-size:200px;color:var(--cream);letter-spacing:-.03em">ACERO</div>''')
B["s17"]=("background:#000",'''
  <div class="card" style="left:0;top:0;width:1080px;height:1920px;border:0"><img src="assets/a2_telar_mecanico.jpg" style="left:-790px;top:0;width:2989px;height:1920px" /></div>
  <div id="s17-after" class="card" style="left:0;top:0;width:1080px;height:1920px;border:0;clip-path:inset(100% 0 0 0)"><img src="assets/a16_acero.jpg" style="left:-560px;top:0;width:2376px;height:1920px" /></div>
  <div id="s17-line" style="position:absolute;left:0;top:1917px;width:1080px;height:6px;background:var(--orange)"></div>
  <div style="position:absolute;left:0;right:0;top:0;height:760px;background:linear-gradient(180deg,rgba(27,26,23,.85),rgba(27,26,23,0))"></div>
  <div id="s17-t" class="tx" style="top:300px;font-size:92px;color:var(--cream)">LO TRADICIONAL<br><span class="or">CAMBIA</span></div>''')
B["s18"]=("background:#000",'''
  <div class="card hv" style="left:0;top:0;width:1080px;height:1920px;border:0"><img id="s18-i" src="assets/a17_eads.jpg" style="left:-800px;top:0;width:2898px;height:1920px" /></div>
  '''+V+'''
  <div id="s18-t" class="tx" style="top:1190px;font-size:96px;color:var(--cream)">PUENTES</div>''')
B["s19"]=('','''
  <div class="card" style="left:0;top:300px;width:1080px;height:1000px;border-left:0;border-right:0"><img id="s19-i" src="assets/a13_locomotora.jpg" style="left:0;top:0;width:1645px;height:1000px" /></div>
  <div id="s19-t" class="tx" style="top:1360px;font-size:92px;text-align:center">REDES DE<br><span class="or">FERROCARRIL</span></div>''')
B["s20"]=("background:#000",'''
  <div id="s20-c" class="card" style="left:0;top:0;width:1080px;height:1920px;border:0"><img id="s20-i" src="assets/a18_rascacielos.jpg" style="left:-120px;top:0;width:1566px;height:1920px;transform-origin:50% 100%" /></div>
  '''+V+'''
  <div id="s20-t" class="tx" style="top:1190px;font-size:92px;color:var(--cream)">LOS PRIMEROS<br><span class="or">RASCACIELOS</span></div>''')
B["s21"]=('','''
  <div id="s21-c" class="card" style="left:160px;top:280px;width:760px;height:890px"><img id="s21-i" src="assets/a3_carnegie.jpg" style="left:0;top:0;width:760px;height:890px" /></div>
  <div id="s21-bar" class="bar" style="top:1150px"><i></i>ANDREW CARNEGIE</div>
  <div id="s21-t" class="tx" style="top:1280px;font-size:100px;text-align:center">FORTUNA<br><span class="or">MILLONARIA</span></div>''')
B["s22"]=('','''
  <div id="s22-a" class="tx" style="top:560px;font-size:130px;text-align:center;line-height:1.02">NO FUE EL<br><span style="position:relative;display:inline-block">ACERO<span id="s22-strike" style="position:absolute;left:-2%;top:50%;width:104%;height:16px;margin-top:-8px;background:var(--orange);transform-origin:0 50%"></span></span></div>
  <div id="s22-b" class="tx or" style="top:1020px;font-size:150px;text-align:center;line-height:1.02"><span style="color:var(--ink);font-size:80px;display:block;line-height:1.1">FUE</span>ADAPTARSE</div>''')
B["s24"]=('','''
  <div id="s24-b" style="position:absolute;left:160px;top:830px;width:760px;height:150px;background:var(--orange);color:var(--cream);font-weight:900;font-size:66px;letter-spacing:.08em;display:flex;align-items:center;justify-content:center">SÍGUEME</div>
  <div id="s24-s" class="tx" style="top:1030px;font-size:44px;text-align:center;letter-spacing:.14em;color:var(--muted);font-weight:700">PARA MÁS HISTORIAS ASÍ</div>''')
html='''
<video id="hook-v" class="clip" src="assets/hook_video_src.mp4" muted playsinline data-start="0" data-duration="3.1" data-media-start="16.1" data-track-index="2" style="position:absolute;left:-54px;top:0;width:1188px;height:2112px;object-fit:cover;z-index:0"></video>
'''
k=0
for i,a,b in T:
    if i=="s23": continue
    k+=1
    bg,body=B[i]
    html+=f'\n<div id="{i}" class="scene clip" data-start="{a}" data-duration="{D[i]}" data-track-index="1" style="z-index:{k};{bg}">{body}\n</div>\n'
r0=S["s23"]; rd=D["s23"]; t2=80.6
html+=f'''
<video id="s23-v" class="clip" src="assets/robot_ia.mp4" muted playsinline data-start="{r0}" data-duration="{rd}" data-media-start="5.5" data-track-index="2" style="position:absolute;left:0;top:0;width:1080px;height:1920px;object-fit:cover;object-position:50% 40%;z-index:30"></video>
<div id="s23-veil" class="clip" data-start="{r0}" data-duration="{rd}" data-track-index="3" style="position:absolute;left:0;right:0;top:1000px;height:920px;background:linear-gradient(180deg,rgba(27,26,23,0),rgba(27,26,23,.88));z-index:31"></div>
<div id="s23-t1" class="tx clip" data-start="{r0}" data-duration="{round(t2-r0,2)}" data-track-index="4" style="top:1160px;font-size:92px;color:var(--cream);z-index:32">LA PRÓXIMA<br><span class="or">MÁQUINA</span> YA LLEGÓ</div>
<div id="s23-t2" class="tx clip" data-start="{t2}" data-duration="{round(r0+rd-t2,2)}" data-track-index="4" style="top:1160px;font-size:104px;color:var(--cream);z-index:32">¿QUÉ VAS A<br><span class="or">HACER TÚ?</span></div>
<audio id="cam1" src="assets/camara.wav" data-start="9.0" data-duration="0.19" data-track-index="7" data-volume="0.8"></audio>
<audio id="cam2" src="assets/camara.wav" data-start="10.5" data-duration="0.19" data-track-index="7" data-volume="0.8"></audio>
<audio id="cam3" src="assets/camara.wav" data-start="12.4" data-duration="0.19" data-track-index="7" data-volume="0.8"></audio>
<audio id="voz" src="assets/voz.mp3" data-start="0" data-duration="84.25" data-track-index="6" data-volume="1"></audio>
'''
head=open(proj+"/../index_v1_guion_original.html").read()
a=head.index('<!-- 0:00-0:03 HOOK -->'); b=head.index('<div id="flash"')
out=head[:a]+html+'\n'+head[b:]
out=out.replace('data-duration="90" data-width','data-duration="%s" data-width'%TOTAL)
out=out.replace('<div id="flash" class="clip" data-start="0" data-duration="90"','<div id="flash" class="clip" data-start="0" data-duration="%s"'%TOTAL)
js=open("/home/user/videos/carnegie/anim_sync.js").read()
js=js.replace("__S__",json.dumps(S)).replace("__D__",json.dumps(D))
sa=out.index('<script>',out.index('<div id="flash"')); sb=out.index('</script>',sa)
out=out[:sa]+'<script>'+js+out[sb:]
open(proj+"/index.html","w").write(out)
print("ok")
