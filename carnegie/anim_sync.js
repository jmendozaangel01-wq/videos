window.__timelines = window.__timelines || {};
const S=__S__, D=__D__;
const tl = gsap.timeline({ paused: true });
const E="power3.out";
const slideIn=(id,t,x=80)=>tl.fromTo(id,{x:x,opacity:0},{x:0,opacity:1,duration:.3,ease:E},t);
const popUp=(id,t,y=40)=>tl.fromTo(id,{y:y,opacity:0},{y:0,opacity:1,duration:.3,ease:E},t);
const cardIn=(id,t)=>tl.fromTo(id,{opacity:0,y:50},{opacity:1,y:0,duration:.3,ease:E},t);
const fade=(id,t)=>tl.fromTo(id,{opacity:0},{opacity:1,duration:.3},t);
// s1 hook (video con texto)
tl.fromTo("#s1-t",{scale:1.14},{scale:1,duration:.22,ease:"back.out(2)"},0);
tl.fromTo("#hook-v",{scale:1},{scale:1.08,duration:3.2,ease:"none"},0);
// s2 (revolución industrial 1840)
cardIn("#s2-c",S.s2); tl.fromTo("#s2-i",{scale:1},{scale:1.25,duration:D.s2,ease:"none"},S.s2);
fade("#s2-k",S.s2+.2); slideIn("#s2-t",S.s2+.4);
// s3 (familia Carnegie / mapa)
cardIn("#s3-c",S.s3); tl.fromTo("#s3-i",{scale:1},{scale:1.12,duration:D.s3,ease:"none"},S.s3); popUp("#s3-t",S.s3+.3,30);
// p1/p2/p3 fotos (cambio con clic de cámara + destello)
tl.set("#flash",{opacity:0},0);
[S.p1,S.p2,S.p3].forEach(t=>{ tl.to("#flash",{opacity:.75,duration:.04,ease:"none"},t); tl.to("#flash",{opacity:0,duration:.18,ease:"power2.out"},t+.04); });
tl.fromTo("#p1-i",{scale:1},{scale:1.12,duration:D.p1,ease:"none"},S.p1);
slideIn("#p1-t",S.p1+.1);
cardIn("#p2-c",S.p2); tl.fromTo("#p2-i",{scale:1},{scale:1.12,duration:D.p2,ease:"none"},S.p2);
popUp("#p2-t",S.p2+.15,30);
cardIn("#p3-c",S.p3); tl.fromTo("#p3-i",{scale:1},{scale:1.1,duration:D.p3,ease:"none"},S.p3);
popUp("#p3-t",S.p3+.15,30);
// s4 el pequeño Andrew
cardIn("#s4-c",S.s4); tl.fromTo("#s4-i",{scale:1},{scale:1.25,duration:D.s4,ease:"none"},S.s4);
popUp("#s4-t",S.s4+.1,30);
// s5 eligió otro camino
["#s5-w1","#s5-w2","#s5-w3"].forEach((id,i)=>tl.fromTo(id,{opacity:0,y:40},{opacity:1,y:0,duration:.25,ease:E},S.s5+.1+i*.45));
// s6 barco
tl.fromTo("#s6-i",{scale:1},{scale:1.12,duration:D.s6,ease:"none"},S.s6);
fade("#s6-r",S.s6+.2);
tl.fromTo("#s6-line",{scaleX:0},{scaleX:1,duration:2,ease:"none"},S.s6+.4);
const a={v:0}; const an=document.getElementById("s6-num");
tl.fromTo(a,{v:0},{v:12,duration:2,ease:"none",onUpdate(){an.textContent=Math.round(a.v)}},S.s6+.4);
popUp("#s6-age",S.s6+.4,30);
// s7 fábrica / s8 mensajero
tl.fromTo("#s7-i",{x:0},{x:-420,duration:D.s7,ease:"none"},S.s7); slideIn("#s7-t",S.s7+.2);
tl.fromTo("#s8-i",{x:0},{x:-120,duration:D.s8,ease:"none"},S.s8); slideIn("#s8-t",S.s8+.2);
// s9 bibliotecas
tl.fromTo("#s9-i",{scale:1},{scale:1.1,duration:D.s9,ease:"none"},S.s9);
fade("#s9-k",S.s9+.2);
const lab=[["#s9-0",S.s9+.2,27.6],["#s9-a",27.6,29.9],["#s9-b",29.9,31.3],["#s9-c",31.3,S.s9+D.s9]];
lab.forEach(([id,t,e])=>{
  tl.set(id,{opacity:0},0);
  tl.fromTo(id,{x:60,opacity:0},{x:0,opacity:1,duration:.3,ease:E},t);
  tl.to(id,{opacity:0,duration:.15},e-.15);
});
// s10 Scott / s11 telégrafo
cardIn("#s10-c",S.s10); tl.fromTo("#s10-i",{scale:1},{scale:1.1,duration:D.s10,ease:"none"},S.s10);
tl.fromTo("#s10-bar",{x:-1080},{x:0,duration:.35,ease:"power3.out"},S.s10+1.0);
fade("#s10-sub",S.s10+1.5);
cardIn("#s11-c",S.s11); tl.fromTo("#s11-i",{scale:1},{scale:1.1,duration:D.s11,ease:"none"},S.s11);
tl.fromTo("#s11-t",{opacity:0,scale:.9},{opacity:1,scale:1,duration:.25,ease:"back.out(2)"},S.s11+.3);
// s12 mentor / s13 trenes
tl.fromTo("#s12-i",{scale:1},{scale:1.12,duration:D.s12,ease:"none"},S.s12);
slideIn("#s12-t",S.s12+.3);
tl.fromTo("#s13-i",{x:-30},{x:-560,duration:D.s13,ease:"power1.inOut"},S.s13); popUp("#s13-t",S.s13+.1);
// s14 puente en llamas
tl.fromTo("#s14-i",{scale:1},{scale:1.15,duration:D.s14,ease:"none"},S.s14);
tl.set("#s14-t",{opacity:0},0);
fade("#s14-k",S.s14+.1); tl.to("#s14-k",{opacity:0,duration:.15},47.3);
tl.fromTo("#s14-t",{opacity:0,x:-14},{opacity:1,x:0,duration:.4,ease:"elastic.out(1,.3)"},47.5);
// s15 riel
tl.fromTo("#s15-i",{scale:1},{scale:1.2,duration:D.s15,ease:"none"},S.s15);
slideIn("#s15-t",S.s15+.1); tl.fromTo("#s15-u",{opacity:0},{opacity:1,duration:.4},51.5);
// s16 acero
tl.fromTo("#s16-i",{x:0},{x:-260,duration:D.s16,ease:"power1.inOut"},S.s16);
tl.set("#s16-t",{opacity:0},0);
fade("#s16-k",S.s16+.1); tl.to("#s16-k",{opacity:0,duration:.1},55.6);
tl.set("#s16-heat",{opacity:0},0);
tl.to("#s16-heat",{opacity:.6,duration:.06,ease:"none"},55.7);
tl.to("#s16-heat",{opacity:0,duration:.5,ease:"power2.out"},55.76);
tl.fromTo("#s16-t",{scale:1.5,opacity:0},{scale:1,opacity:1,duration:.2,ease:"power4.out"},55.7);
// s17 lo tradicional cambia
tl.fromTo("#s17-after",{clipPath:"inset(100% 0 0 0)"},{clipPath:"inset(0% 0 0 0)",duration:1.7,ease:"power2.inOut"},S.s17+.3);
tl.fromTo("#s17-line",{y:0},{y:-1917,duration:1.7,ease:"power2.inOut"},S.s17+.3);
popUp("#s17-t",S.s17+.1,30);
// s18 puentes / s19 ferrocarril / s20 rascacielos
tl.fromTo("#s18-i",{x:0},{x:-500,duration:D.s18,ease:"none"},S.s18); slideIn("#s18-t",S.s18+.3);
tl.fromTo("#s19-i",{x:-560},{x:-30,duration:D.s19,ease:"power1.inOut"},S.s19); popUp("#s19-t",S.s19+.2,30);
tl.fromTo("#s20-c",{clipPath:"inset(100% 0 0 0)"},{clipPath:"inset(0% 0 0 0)",duration:.45,ease:"power3.out"},S.s20);
tl.fromTo("#s20-i",{scale:1},{scale:1.15,duration:D.s20,ease:"none"},S.s20); popUp("#s20-t",S.s20+.3);
// s21 fortuna
cardIn("#s21-c",S.s21); tl.fromTo("#s21-i",{scale:1},{scale:1.1,duration:D.s21,ease:"none"},S.s21);
tl.fromTo("#s21-bar",{x:-1080},{x:0,duration:.3,ease:"power3.out"},S.s21+.2);
tl.fromTo("#s21-t",{opacity:0,y:30},{opacity:1,y:0,duration:.25,ease:E},S.s21+.5);
// s22 el secreto
tl.fromTo("#s22-a",{opacity:0,scale:.9},{opacity:1,scale:1,duration:.3,ease:"back.out(2)"},S.s22+.1);
tl.fromTo("#s22-strike",{scaleX:0},{scaleX:1,duration:.35,ease:"power3.out"},74.9);
tl.fromTo("#s22-a",{y:200},{y:0,duration:.4,ease:"power2.inOut"},75.4);
tl.fromTo("#s22-b",{opacity:0,scale:.8},{opacity:1,scale:1,duration:.3,ease:"power4.out"},75.6);
// s23 robot
tl.fromTo("#s23-v",{scale:1.0},{scale:1.1,duration:D.s23,ease:"none"},S.s23);
slideIn("#s23-t1",S.s23+.1); slideIn("#s23-t2",80.7);
// s24 CTA
tl.fromTo("#s24-b",{opacity:0,scale:.8},{opacity:1,scale:1,duration:.3,ease:"back.out(2)"},S.s24+.2);
tl.to("#s24-b",{scale:1.06,duration:.45,yoyo:true,repeat:3,ease:"sine.inOut"},S.s24+.7);
fade("#s24-s",S.s24+.5);
window.__timelines["main"] = tl;
