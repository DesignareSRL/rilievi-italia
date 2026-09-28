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
 ('  EMAILJS_PUBLIC_KEY: "",      // EmailJS > Account > Public Key','  EMAILJS_PUBLIC_KEY: "bfua708T53l0bJGqy",'),
 ('  EMAILJS_SERVICE_ID: "",      // EmailJS > Email Services > Service ID','  EMAILJS_SERVICE_ID: "service_8ihczin",'),
 ('  EMAILJS_TEMPLATE_ID: "",     // EmailJS > Email Templates > Template ID','  EMAILJS_TEMPLATE_ID: "template_21zxz9g",'),
 ('    d.page=location.href;\n    btn.disabled=true;',"    d.page=location.href;\n    var e={name:d.from_name,email:d.reply_to,reply_to:d.reply_to,title:d.comune,comune:d.comune,\n      message:'Telefono: '+d.phone+'\\nEmail: '+d.reply_to+'\\nComune: '+d.comune+'\\nTipo immobile: '+d.tipo+'\\nSuperficie: '+(d.superficie||'-')+' m2\\nElaborati: '+d.elaborati+'\\n\\nNote:\\n'+(d.message||'-')+'\\n\\nInviato da: '+d.page};\n    btn.disabled=true;"),
 ('emailjs.send(C.EMAILJS_SERVICE_ID,C.EMAILJS_TEMPLATE_ID,d)','emailjs.send(C.EMAILJS_SERVICE_ID,C.EMAILJS_TEMPLATE_ID,e)'),
 ("      location.href='mailto:info@designare.pro?subject='+encodeURIComponent('Richiesta preventivo rilievo – '+(d.comune||''))+'&body='+encodeURIComponent(body);\n      riConv(C.CONV_FORM);\n",''),
 ('show(\'ok\',"Si è aperto il tuo programma di posta con la richiesta già compilata: premi Invia per completarla. In alternativa scrivici a info@designare.pro.");','show(\'err\',"Invio non riuscito. Riprova tra qualche minuto oppure scrivici a info@designare.pro.");'),
 ('<p class="lead">Rileviamo il tuo edificio con il Leica BLK2GO e ti consegniamo nuvola di punti, piante, prospetti e sezioni in DWG. Poche ore sul posto invece di giorni con metro e distanziometro.</p>','<p class="lead">Per studi tecnici, imprese e aziende: rileviamo edifici e impianti con il Leica BLK2GO e consegniamo nuvola di punti, piante, prospetti e sezioni in DWG. Poche ore sul posto invece di giorni con metro e distanziometro.</p>'),
 ('<article><h3>Condomini e proprietari</h3><p>Rilievo di facciate e parti comuni per manutenzioni, ponteggi e interventi di efficientamento, senza accessi ripetuti agli appartamenti.</p></article>','<article><h3>Amministratori di condominio</h3><p>Rilievo di facciate e parti comuni per progetti di manutenzione, ponteggi e interventi di efficientamento, senza accessi ripetuti agli appartamenti.</p></article>'),
 ('        <div><label for="f-comune">Comune dell\'immobile *</label>','        <div><label for="f-chi">Chi sei *</label>\n          <select id="f-chi" name="chi" required>\n            <option value="">Seleziona…</option><option>Studio tecnico (architetto, ingegnere, geometra)</option><option>Impresa edile / general contractor</option><option>Amministratore di condominio</option><option>Azienda / industria</option><option>Ente pubblico</option><option>Altro</option>\n          </select></div>\n        <div><label for="f-az">Studio / Azienda *</label><input id="f-az" name="azienda" autocomplete="organization" required></div>\n        <div><label for="f-comune">Comune dell\'immobile *</label>'),
 ('<option>Appartamento</option><option>Edificio / villa</option><option>Condominio / facciate</option>','<option>Edificio / villa</option><option>Condominio / facciate</option><option>Appartamento</option>'),
 ("message:'Telefono: '+d.phone","message:'Profilo: '+(d.chi||'-')+'\\nStudio/Azienda: '+(d.azienda||'-')+'\\nTelefono: '+d.phone"),
 ('var e={name:d.from_name,',"var e={name:d.from_name+(d.azienda?' – '+d.azienda:''),"),
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
