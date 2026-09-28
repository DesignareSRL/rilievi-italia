import sys
# Correzioni applicate al sito dopo l'estrazione dello zip (rimozione numero di telefono)
R={
"index.html":[
 ('  "telephone": "+39 389 197 2308",\n',''),
 ('<a class="tel" href="tel:+393891972308" data-conv="tel">389 197 2308</a>','<a class="tel" href="#preventivo">Richiedi preventivo</a>'),
 ('<a class="btn btn-ghost" href="tel:+393891972308" data-conv="tel">Chiama 389 197 2308</a>','<a class="btn btn-ghost" href="mailto:info@designare.pro">Scrivici una email</a>'),
 ('Se preferisci, chiamaci.','Se preferisci, scrivici a info@designare.pro.'),
 ('        <a href="tel:+393891972308" data-conv="tel">389 197 2308</a>\n',''),
 ('<a href="tel:+393891972308" data-conv="tel">Chiama</a>','<a href="mailto:info@designare.pro">Email</a>'),
 ('In alternativa chiamaci al 389 197 2308.','In alternativa scrivici a info@designare.pro.'),
 ('<a href="mailto:info@designare.pro" style="font-size:1.05rem">','<a href="mailto:info@designare.pro">'),
],
"privacy.html":[(' · Tel. 389 197 2308.','.')],
}
d=sys.argv[1] if len(sys.argv)>1 else '.'
for f,pairs in R.items():
    p=d+'/'+f
    s=open(p,encoding='utf-8').read()
    for a,b in pairs:
        s=s.replace(a,b)
    open(p,'w',encoding='utf-8').write(s)
