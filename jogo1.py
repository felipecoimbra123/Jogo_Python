import tkinter as tk

def nomear():
   abertura.pack()
   continuarInicial.pack()
   comecar.destroy()

def continuacaoInicial():
   abertura.destroy()
   primeiroTexto.pack()
   continuarInicial.destroy()
   ataqueUm.pack(padx=10, pady=10)
   ataqueDois.pack(padx=10, pady=10)

def socoEsquerda():
   primeiroTexto.destroy()
   soco2Resultado.pack()
   ataqueUm.destroy()
   ataqueDois.destroy()
   continuarSecundario.pack()

def socoDireita():
   global vidaInimigo
   primeiroTexto.destroy()
   soco1Resultado.pack()
   vidaInimigo -= 3
   ataqueUm.destroy()
   ataqueDois.destroy()
   continuarSecundario.pack()

def continuacaoSecundaria():
   soco1Resultado.destroy()
   soco2Resultado.destroy()
   segundoTexto.pack()
   continuarSecundario.destroy()
   ataqueTres.pack(padx=10, pady=10)
   ataqueQuatro.pack(padx=10, pady=10)

def chuteEsquerda():
   global vidaInimigo
   segundoTexto.destroy()
   chute1Resultado.pack()
   vidaInimigo -= 5
   ataqueTres.destroy()
   ataqueQuatro.destroy()
   continuarTerciario.pack()

def chuteDireita():
   segundoTexto.destroy()
   chute2Resultado.pack()
   ataqueTres.destroy()
   ataqueQuatro.destroy()
   continuarTerciario.pack()

def continuacaoTerciaria():
   chute1Resultado.destroy()
   chute2Resultado.destroy()
   terceiroTexto.pack()
   continuarTerciario.destroy()
   ataqueCinco.pack(padx=10, pady=10)
   ataqueSeis.pack(padx=10, pady=10)

def cotovelada():
   global derrota
   terceiroTexto.destroy()
   cotoveladaResultado.pack()
   derrota = 1
   decisaoFinal.pack()
   ataqueCinco.destroy()
   ataqueSeis.destroy()
   decisaoFinal.config(command=lambda: ultimaDecisao(False))
   decisaoFinal.pack()

def joelhada():
   global vidaInimigo
   terceiroTexto.destroy()
   joelhadaResultado.pack()
   vidaInimigo -= 5
   ataqueCinco.destroy()
   ataqueSeis.destroy()
   continuarQuaternario.pack()

def continuacaoQuaternaria():
   joelhadaResultado.destroy()
   cotoveladaResultado.destroy()
   quartoTexto.pack()
   continuarQuaternario.destroy()
   ataqueSete.pack(padx=10, pady=10)
   ataqueOito.pack(padx=10, pady=10)

def jab():
   quartoTexto.destroy()
   jabResultado.pack()
   ataqueSete.destroy()
   ataqueOito.destroy()
   continuarQuinario.pack()

def cruzado():
   global vidaInimigo
   quartoTexto.destroy()
   cruzadoResultado.pack()
   vidaInimigo -= 4
   ataqueSete.destroy()
   ataqueOito.destroy()
   continuarQuinario.pack()

def continuacaoQuinaria():
   cruzadoResultado.destroy()
   jabResultado.destroy()
   quintoTexto.pack()
   continuarQuinario.destroy()
   ataqueNove.pack(padx=10, pady=10)
   ataqueDez.pack(padx=10, pady=10)

def cabecada():
   quintoTexto.destroy()
   cabecadaResultado.pack()
   ataqueNove.destroy()
   ataqueDez.destroy()
   decisaoFinal.config(command=lambda: ultimaDecisao(True))
   decisaoFinal.pack()

def soco2Direita():
   global vidaInimigo
   quintoTexto.destroy()
   soco2DResultado.pack()
   vidaInimigo -= 3
   ataqueNove.destroy()
   ataqueDez.destroy()
   decisaoFinal.config(command=lambda: ultimaDecisao(False))
   decisaoFinal.pack()

def ultimaDecisao(cabeceou):
   global derrota
   cabecadaResultado.destroy()
   soco2DResultado.destroy()
   if vidaInimigo <= 0 or cabeceou:
      ultimoTextoV.pack()
      decisaoFinal.destroy()
   elif vidaInimigo > 0 or derrota == 1:
      ultimoTextoD.pack()
      decisaoFinal.destroy()
      cotoveladaResultado.destroy()

janela = tk.Tk()
janela.config(bg="#222")
janela.title("Jogo Luta de boxe")
janela.resizable(width=False, height=False)
janela.geometry("700x250")

abertura = tk.Label(janela, text=f"Olá, você tem uma luta hoje contra um \ndos maiores lutadores de boxe da história, \no nome dele é Conor Mcgregor, \no seu objetivo é tentar vencê-lo. \nTenha uma Boa luta e Boa sorte!", font=("13"), background="#3a352f", fg="white")
primeiroTexto = tk.Label(janela, text="A sua luta começou, você está tentando \nacertar algum golpe nele, ele acabou de tentar \ndar um chute em você mas acabou errando, \n assim dando uma abertura para você dar um golpe, \nOque você faz?", font=("13"), background="#3a352f", fg="white")
soco1Resultado = tk.Label(janela, text="Você conseguiu dar dano no \ninimigo acertando o soco nele, o deixando um pouco \nmachucado, mas ainda não foi o \nsuficiente para ganhá-lo, \ncontinue dando o seu melhor!", font=("13"), background="#3a352f", fg="white")
soco2Resultado = tk.Label(janela, text="Ele bloqueou o seu soco, e te golpeu nas \npernas, assim fazendo você se machucar um pouco \nmas você ainda não caiu, então continue tentando.", font=("13"), background="#3a352f", fg="white")
segundoTexto = tk.Label(janela, text="Continuando a luta ele acabou de \ntentar te dar um soco de esquerda, mas ele acabou \nerrando o soco e abrindo \numa brecha para você dar outro golpe nele. \nOque você faz?", font=("13"), background="#3a352f", fg="white")
chute1Resultado = tk.Label(janela, text="Você conseguiu acertar bastante \ndano nele, acabou de terminar o primeiro round e \nvocê acabou o deixando com muita dor, com \nele tendo que chamar a ajuda de um médico, o \nsegundo round já vai começar, prepare-se!", font=("13"), background="#3a352f", fg="white")
chute2Resultado = tk.Label(janela, text="Você errou o chute, e ele te acertou \num soco, acabou de terminar o primeiro round mas tente dar \no seu melhor no próximo round, o segundo round ja vai começar, \nprepare-se!", font=("13"), background="#3a352f", fg="white")
terceiroTexto = tk.Label(janela, text="O segundo round começou, ele \nestá partindo pra cima com muita força, ele te \nacertou um chute muito forte no seu \nabdômen, você ainda ficou de pé mas perdeu um pouco \nda sua respiração, você terá que dar algum golpe! \nQual você escolhe?", font=("13"), background="#3a352f", fg="white")
cotoveladaResultado = tk.Label(janela, text="Você tentou dar um cotovelada\n mas ele conseguiu desviar.", font=("13"), background="#3a352f", fg="white")
joelhadaResultado = tk.Label(janela, text="Você conseguiu acertar a joelhada no seu \ninimigo e o golpeou com muita força, \nassim fazendo ele cair no chão.", font=("13"), background="#3a352f", fg="white")
quartoTexto = tk.Label(janela, text="Seguindo a luta, ele ainda continua de pé, então você \nainda terá que tentar acertar mais alguns golpes.", font=("13"), background="#3a352f", fg="white")
jabResultado = tk.Label(janela, text="Você acabou não conseguindo dar o dano e tomou \num soco no nariz, que acabou te deixando um pouco tonto, \nmas você ainda não pode cair!", font=("13"), background="#3a352f", fg="white")
cruzadoResultado = tk.Label(janela, text="Você conseguiu acertar o cruzado e conseguiu o deixar mais tonto \ndo que ele já estava, mas ainda falta mais alguns golpes para derrotá-lo.", font=("13"), background="#3a352f", fg="white")
quintoTexto = tk.Label(janela, text="Agora, na ultima rodada da luta você está muito motivado a \nganhar, mas para ganhar ainda terá que dar mais alguns golpes.", font=("13"), background="#3a352f", fg="white")
cabecadaResultado = tk.Label(janela, text="Você não conseguiu \nacertar ele, mas do nada ele \nacabou desistindo da luta, por achar que você merecia \nganhar a luta mais do que ele, por ele já ser bem conhecido pelas suas lutas.", font=("13"), background="#3a352f", fg="white")
soco2DResultado = tk.Label(janela, text="Você acertou ele e conseguiu dar \nmais dano nele, conseguindo acertar seu soco.", font=("13"), background="#3a352f", fg="white")
ultimoTextoD = tk.Label(janela, text="Você até que tentou, mas você não conseguiu \ndar dano o suficiente e\n ele te nocauteou logo após você tentar dar \noutro seu golpe no seu inimigo, você perdeu. \nGAME OVER", font=("13"), background="#3a352f", fg="white")
ultimoTextoV = tk.Label(janela, text="Parabéns por todo o esforço, você foi o grande VENCEDOR!!", font=("13"), background="#3a352f", fg="white")

comecar = tk.Button(janela, text="Começar", background="#5c493d", width=5, command=nomear, fg="white")
comecar.pack(expand = "YES")
comecar.config(width=6)
continuarInicial = tk.Button(janela, text="Continuar", background="#5c493d", command=continuacaoInicial, fg="white")
continuarSecundario = tk.Button(janela, text="Continuar", background="#5c493d", command=continuacaoSecundaria, fg="white")
continuarTerciario = tk.Button(janela, text="Continuar", background="#5c493d", command=continuacaoTerciaria, fg="white")
continuarQuaternario = tk.Button(janela, text="Continuar", background="#5c493d", command=continuacaoQuaternaria, fg="white")
continuarQuinario = tk.Button(janela, text="Continuar", background="#5c493d", command=continuacaoQuinaria, fg="white")
decisaoFinal = tk.Button(janela, text="Decisão", background="#5c493d", command=ultimaDecisao, fg="white")

vidaInimigo = 10

ataqueUm = tk.Button(janela, text="Soco de esquerda", background="#5c493d", command=socoEsquerda, fg="white")
ataqueDois = tk.Button(janela, text="Soco de direita", background="#5c493d", command=socoDireita, fg="white")
ataqueTres = tk.Button(janela, text="Chute de esquerda", background="#5c493d", command=chuteEsquerda, fg="white")
ataqueQuatro = tk.Button(janela, text="Chute de direita", background="#5c493d", command=chuteDireita, fg="white")
ataqueCinco = tk.Button(janela, text="Cotovelada", background="#5c493d", command=cotovelada, fg="white")
ataqueSeis = tk.Button(janela, text="Joelhada", background="#5c493d", command=joelhada, fg="white")
ataqueSete = tk.Button(janela, text="Jab", background="#5c493d", command=jab, fg="white")
ataqueOito = tk.Button(janela, text="Cotovelada", background="#5c493d", command=cruzado, fg="white")
ataqueNove = tk.Button(janela, text="Cabeçada", background="#5c493d", command=cabecada, fg="white")
ataqueDez = tk.Button(janela, text="Soco de direita", background="#5c493d", command=soco2Direita, fg="white")

janela.mainloop()