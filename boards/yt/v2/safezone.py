"""Facecam safe zones (Mauro 2026-10-09 v6): both bottom corners of every recorded frame stay empty.

A zone is 22% of the viewport width x 28% of its height, bottom-left and bottom-right. SCAN_JS returns
every visible thing that enters a zone: text (per line box), images, videos (their controls), canvas,
buttons, svg marks (text, image, shapes) and small filled HTML leaves (chart bars, chips). Backgrounds
bigger than a quarter of the screen do not count. Recording UI (#ytbar, correction tools, facecam box)
is skipped. A part clipped away by an ancestor (overflow hidden) does not count. Copied byte for byte between mauro-os/boards/yt/v2/safezone.py (test_controls.py) and growthub-os/boards/safezone.py (test-boards.py).
"""
SCAN_JS = r"""
() => {
 const W=innerWidth,H=innerHeight,cw=W*0.22,ch=H*0.28,big=W*H*0.25;
 const Z=[[0,H-ch,cw,H],[W-cw,H-ch,W,H]];
 const out=[];
 const vis=el=>{for(let e=el;e&&e.nodeType===1;e=e.parentElement){const s=getComputedStyle(e);
   if(s.display==='none'||s.visibility==='hidden'||parseFloat(s.opacity)===0)return false;}return true;};
 const clipCache=new Map();
 const clipOf=el=>{  // the visible box left after every ancestor that clips (overflow not visible)
   let c=[-1e9,-1e9,1e9,1e9];
   for(let a=el.parentElement;a&&a!==document.documentElement;a=a.parentElement){
     if(a instanceof SVGElement&&a.tagName!=='svg')continue;
     let r=clipCache.get(a);
     if(r===undefined){const s=getComputedStyle(a);
       r=(s.overflowX!=='visible'||s.overflowY!=='visible')&&a!==document.body?(b=>[b.left,b.top,b.right,b.bottom])(a.getBoundingClientRect()):null;
       clipCache.set(a,r);}
     if(r)c=[Math.max(c[0],r[0]),Math.max(c[1],r[1]),Math.min(c[2],r[2]),Math.min(c[3],r[3])];
   }
   return c;};
 const cut=(b,c)=>{const l=Math.max(b.left,c[0]),t=Math.max(b.top,c[1]),r=Math.min(b.right,c[2]),bo=Math.min(b.bottom,c[3]);
   return {left:l,top:t,right:r,bottom:bo,width:r-l,height:bo-t};};
 const hit=b=>b.width>=1&&b.height>=1&&b.width*b.height<big&&Z.some(([x0,y0,x1,y1])=>b.right>x0+1&&b.left<x1-1&&b.bottom>y0+1&&b.top<y1-1);
 const SVGM=/^(text|tspan|image|rect|path|line|circle|ellipse|polyline|polygon|use|foreignObject)$/;
 for(const el of document.body.querySelectorAll('*')){
  if(el.closest('#ytbar,#ytlist,.bc-ui,#bc-draft,#bc-face,script,style,noscript,title'))continue;
  const tag=el.tagName, isSvg=el instanceof SVGElement;
  let rects=[];
  if(isSvg){
    if(!SVGM.test(tag))continue;
    if(tag!=='text'&&tag!=='tspan'&&tag!=='image'&&tag!=='foreignObject'){const s=getComputedStyle(el);
      if((s.fill==='none'||s.fillOpacity==='0')&&(s.stroke==='none'||s.strokeOpacity==='0'))continue;}
    rects=[el.getBoundingClientRect()];
  } else if(/^(IMG|VIDEO|CANVAS|BUTTON|INPUT|TEXTAREA|SELECT|IFRAME)$/.test(tag)){rects=[el.getBoundingClientRect()];}
  else{
    const r=document.createRange();
    for(const n of el.childNodes){if(n.nodeType===3&&n.textContent.trim()){r.selectNodeContents(n);rects.push(...r.getClientRects());}}
    if(!el.children.length){const s=getComputedStyle(el);
      const filled=(s.backgroundColor!=='rgba(0, 0, 0, 0)'&&s.backgroundColor!=='transparent')||s.backgroundImage!=='none'||
        (parseFloat(s.borderTopWidth)+parseFloat(s.borderBottomWidth)+parseFloat(s.borderLeftWidth)+parseFloat(s.borderRightWidth)>0);
      if(filled)rects.push(el.getBoundingClientRect());}
  }
  if(!rects.length)continue;
  const c=clipOf(el);
  for(const b0 of rects){const b=cut(b0,c);if(hit(b)){if(!vis(el))break;
    const cls=typeof el.className==='string'?el.className:(el.className&&el.className.baseVal)||'';
    out.push(tag+(cls?'.'+cls.split(/\s+/).join('.'):'')+' "'+(el.textContent||'').trim().replace(/\s+/g,' ').slice(0,36)+'" ['+[b.left,b.top,b.right,b.bottom].map(Math.round)+']');break;}}
 }
 return out;
}
"""
