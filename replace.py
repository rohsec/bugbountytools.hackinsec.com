from pyscript import document

def replacer(e):
    urls=document.getElementById('txt1')
    rep=document.getElementById('rep')
    rep1=document.getElementById('rep1')
    out=document.getElementById('out')
    warn=document.getElementById('warn')
    if(urls.value!="" and rep.value!="" and rep1.value!=""):
        warn.innerText=""
        xx=urls.value.replace(rep.value,rep1.value)
        print(xx)
        out.innerHTML=f"Output<br><textarea class='cus_txt' id='cc'></textarea>"
        cc=document.getElementById('cc')
        cc.value=xx
    else:
        warn.innerText="Please validate your inputs !!"

