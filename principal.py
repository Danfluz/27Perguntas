import PySimpleGUI as sg

pontuacao = 0
pontuacaotemp = 0

sg.theme('LightBlue6')
contador = 1
layout = [
    [sg.Text(''), sg.Text('Pergunta',size=(54,1),font=('Eras Bold ITC','12'),justification='right',visible=False,key='perguntanome'),sg.ProgressBar(27,size=(10,5),key='progresso',bar_color=('orange',None),visible=False),sg.Text(f'{contador}/27', font=('Eras Bold ITC','12'),key='n_pergunta',visible=False)],
    [sg.Text('Direita ou esquerda?', font=('Eras Bold ITC','20'), key='titulo')],
    [sg.Text('',size=(6,3))],
    [sg.Text('Responda 27 perguntas não relacionadas à política e tentarei acertar com qual dos lados você tende a concordar mais.', font=('Eras Bold ITC','15'),key='pergunta',visible=True,size=(60,5),justification='center')],
    [sg.Button('Iniciar',font=('Eras Bold ITC','17'),size=(10,2)), sg.Button('Reiniciar', font=('Eras Bold ITC','17'),size=(10,2),visible=False),sg.Button('Sair',size=(10,2), font=('Eras Bold ITC','17'))],
    [sg.Button('Discordo\nmuito', font=('Eras Bold ITC','12'),size=(13,6),visible=False,key='Discordo muito'), sg.Button('Discordo\num pouco', font=('Eras Bold ITC','12'),size=(13,6),visible=False,key='Discordo um pouco'), sg.Button('Neutro', font=('Eras Bold ITC','12'),size=(13,6),visible=False), sg.Button('Concordo\num pouco', font=('Eras Bold ITC','12'),size=(13,6),visible=False,key='Concordo um pouco'), sg.Button('Concordo\nmuito', font=('Eras Bold ITC','12'),size=(13,6),visible=False,key='Concordo muito')],
]

janela = sg.Window('Direita ou Esquerda', layout, finalize=True, size=(800,500),element_justification='center')

while True:
    event, value = janela.read()

    if event == sg.WIN_CLOSED or event == 'Sair':
        break
    if event == 'Iniciar':
        janela['Sair'].update(visible=False)
        janela['Iniciar'].update(visible=False)
        sg.popup_quick_message('Iniciando...',auto_close=True,auto_close_duration=1,no_titlebar=True, non_blocking=False,font=('Eras Bold ITC','12'))
        janela['perguntanome'].update(visible=True)
        janela['progresso'].update(visible=True)
        janela['n_pergunta'].update(visible=True)
        janela['titulo'].update('')
        janela['pergunta'].update('Dependendo das circunstâncias, talvez eu estivesse disposto(a) a tentar comer carne de macaco.')
        janela['Discordo muito'].update(visible=True)
        janela['Discordo um pouco'].update(visible=True)
        janela['Neutro'].update(visible=True)
        janela['Concordo um pouco'].update(visible=True)
        janela['Concordo muito'].update(visible=True)

    if event == 'Discordo muito':
        contador +=1
        janela['progresso'].update(current_count=contador)
        janela['n_pergunta'].update(f'{contador}/27')
        pontuacaotemp = 0
    if event == 'Discordo um pouco':
        contador += 1
        janela['progresso'].update(current_count=contador)
        janela['n_pergunta'].update(f'{contador}/27')
        pontuacaotemp = 1
    if event == 'Neutro':
        contador += 1
        janela['progresso'].update(current_count=contador)
        janela['n_pergunta'].update(f'{contador}/27')
        pontuacaotemp = 2
    if event == 'Concordo um pouco':
        contador += 1
        janela['progresso'].update(current_count=contador)
        janela['n_pergunta'].update(f'{contador}/27')
        pontuacaotemp = 3
    if event == 'Concordo muito':
        contador += 1
        janela['progresso'].update(current_count=contador)
        janela['n_pergunta'].update(f'{contador}/27')
        pontuacaotemp = 4


    if contador == 2 or contador == 7 or contador == 11:
        if pontuacaotemp == 4:
            pontuacaotemp = 0
        elif pontuacaotemp == 3:
            pontuacaotemp = 1
        elif pontuacaotemp == 1:
            pontuacaotemp = 3
        elif pontuacaotemp == 0:
            pontuacaotemp = 4

    if contador == 1:
        janela['pergunta'].update('Dependendo das circunstâncias, talvez eu estivesse disposto(a) a tentar comer carne de macaco.')
    if contador == 2:
        janela['pergunta'].update('Eu ficaria incomodado(a) se estivesse numa aula de ciências e visse uma mão humana preservada dentro de um frasco.')
    if contador == 3:
        janela['pergunta'].update('Me incomoda ouvir alguém limpar a garganta cheia de catarro.')
    if contador == 4:
        janela['pergunta'].update('Eu nunca deixo que qualquer parte do meu corpo toque no assento da privada em banheiros públicos.')
    if contador == 5:
        janela['pergunta'].update('Eu iria por um caminho mais longo para evitar ter que passar por dentro de um cemitério.')
    if contador == 6:
        janela['pergunta'].update('Ver uma barata na casa de outra pessoa não me incomoda.')
    if contador == 7:
        janela['pergunta'].update('Ficaria extremamente incomodado(a) se tocasse num cadáver humano.')
    if contador == 8:
        janela['pergunta'].update('Se vejo alguém vomitar, me dá logo uma indisposição no estômago também.')
    if contador == 9:
        janela['pergunta'].update('Eu provavelmente não iria no restaurante que eu gosto se descobrisse que o cozinheiro está trabalhando gripado hoje.')
    if contador == 10:
        janela['pergunta'].update('Não me perturbaria de modo algum ver uma pessoa com um olho de vidro tirar o olho da cavidade ocular.')
    if contador == 11:
        janela['pergunta'].update('Eu ficaria incomodado(a) se visse um rato correndo e cruzando o meu caminho quando estivesse andando num parque.')
    if contador == 12:
        janela['pergunta'].update('Eu preferia comer um pedaço de fruta do que comer um pedaço de papel.')
        pontuacaotemp = 0
    if contador == 13:
        janela['pergunta'].update('Mesmo que tivesse fome, eu recusaria um prato da minha sopa preferida se ela tivesse sido mexida com um mata-moscas usado, mas que foi lavado cuidadosamente.')
    if contador == 14:
        janela['pergunta'].update('Ficaria incomodado(a) de dormir num quarto de hotel se soubesse que um homem tinha morrido de ataque cardíaco nesse mesmo quarto na noite anterior.')
    if contador == 15:
        janela['pergunta'].update('Você vê larvas num pedaço de carne numa caixa de lixo na rua.')
        janela['Discordo muito'].update('Nada\nnojento')
        janela['Discordo um pouco'].update('Um pouquinho\nnojento')
        janela['Neutro'].update('Moderadamente\nnojento')
        janela['Concordo um pouco'].update('Bem\nnojento')
        janela['Concordo muito'].update('Muito\nnojento!')
    if contador == 16:
        janela['pergunta'].update('Você vê uma pessoa comendo uma maçã com garfo e faca.')
        pontuacaotemp = 0
    if contador == 17:
        janela['pergunta'].update('Enquanto caminha por um túnel por baixo de uma linha de trem sente o fedor de mijo.')
    if contador == 18:
        janela['pergunta'].update('Depois de tomar um gole de refrigerante, você percebe que bebeu num copo que uma pessoa conhecida já havia bebido.')
    if contador == 19:
        janela['pergunta'].update('O gato do seu amigo morre e você tem de pegar no corpo morto com as mãos.')
    if contador == 20:
        janela['pergunta'].update('Você vê alguém colocar ketchup num sorvete de baunilha e comer.')
    if contador == 21:
        janela['pergunta'].update('Você vê um homem com os intestinos expostos após um acidente.')
    if contador == 22:
        janela['pergunta'].update('Descobre que um amigo(a) seu/sua apenas muda de cueca ou calcinha uma vez por semana.')
    if contador == 23:
        janela['pergunta'].update('Um amigo(a) te oferece um pedaço de chocolate em forma de merda de cachorro.')
    if contador == 24:
        janela['pergunta'].update('Você acidentalmente toca nas cinzas de uma pessoa que foi cremada.')
    if contador == 25:
        janela['pergunta'].update('Você está quase bebendo um copo de leite quanto sente o cheiro de que ele está estragado.')
    if contador == 26:
        janela['pergunta'].update('Como parte de uma aula de educação sexual, pedem para você encher de ar com a boca um preservativo novo não lubrificado.')
    if contador == 27:
        janela['pergunta'].update('Você está caminhando descalço(a) num chão de concreto e pisa numa minhoca.')
    pontuacao += pontuacaotemp
    if contador == 28:
        print(pontuacao)

        if pontuacao >= 60:
            orientacao = 'a direita'
            if pontuacao > 98:
                orientacao = 'a extrema-direita'
        if pontuacao <= 40:
            orientacao = 'a esquerda'
            if pontuacao < 2:
                orientacao = 'a extrema-esquerda'
        if pontuacao <60 and pontuacao >52:
            orientacao = 'o centro, mas levemente apontados para direita'
        if pontuacao >40 and pontuacao <48:
            orientacao = 'o centro, mas levemente apontados para esquerda'
        if pontuacao >= 48 and pontuacao <=52:
            orientacao = 'o centro.'


        janela['n_pergunta'].update(f'27/27')
        janela['pergunta'].update(visible=False)
        janela['Discordo muito'].update(visible=False)
        janela['Discordo um pouco'].update(visible=False)
        janela['Neutro'].update(visible=False)
        janela['Concordo um pouco'].update(visible=False)
        janela['Concordo muito'].update(visible=False)
        sg.popup_quick_message('Avaliando respostas...', auto_close=True, auto_close_duration=1, no_titlebar=True, non_blocking=False, font=('Eras Bold ITC', '12'))
        janela['Reiniciar'].update(visible=True)
        janela['Sair'].update(visible=True)
        janela['titulo'].update('Resultado')
        janela['pergunta'].update(f'Baseado nas suas respostas, eu chuto que você tem muitos pensamentos alinhados com {orientacao}')
        janela['pergunta'].update(visible=True)
        contador = 0

    if event == 'Reiniciar':
        contador = 1
        pontuacaotemp = 0
        pontuacao = 0
        janela['titulo'].update('')
        janela['pergunta'].update('')
        janela['Reiniciar'].update(visible=False)
        janela['Sair'].update(visible=False)
        sg.popup_quick_message('Reiniciando...', auto_close=True, auto_close_duration=1, no_titlebar=True,non_blocking=False, font=('Eras Bold ITC', '12'))
        janela['perguntanome'].update(visible=True)
        janela['progresso'].update(current_count=contador,visible=True)
        janela['n_pergunta'].update(f'{contador}/27',visible=True)
        janela['pergunta'].update('Dependendo das circunstâncias, talvez eu estivesse disposto(a) a tentar comer carne de macaco.')
        janela['Discordo muito'].update(visible=True)
        janela['Discordo um pouco'].update(visible=True)
        janela['Neutro'].update(visible=True)
        janela['Concordo um pouco'].update(visible=True)
        janela['Concordo muito'].update(visible=True)



janela.close()
