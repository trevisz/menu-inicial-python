
print("|                                           |")
print("|        SEJA BEM VINDO (A) AO MENU CCR!    |")
print("|                                           |")
print("|                                           |")
print("| 1. Infos sobre a CCR                      |")
print("| 2. Servicos Prestados                     |")
print("| 3. Noticias Recentes                      |")
print("| 4. Site CCR                               |")
print("| 5. Fechar o Menu                          |")
print("|                                           |")

def infos_ccr():
    print("A CCR é uma das principais de transporte do Brasil, atuando em diversos setores como:")
    print("- Concessões rodoviárias")
    print("- Aeroportos")
    print("- Mobilidade urbana")
    print("Essa empresa se destaca por sempre buscar inovações e sustentabilidade em suas operações.\n")

def servicos_prestados():
    print("Os serviços prestados pela CCR são:")
    print("- Gestão de rodovias")
    print("- Administração de aeroportos")
    print("- Transporte urbano\n")


while True:
    try:
        opcao = int(input("Escolha uma opcao: "))

        if opcao == 1:
            infos_ccr() # Chama a função de informações sobre a CCR
        elif opcao == 2: 
            servicos_prestados() # Chama as infos sobre os serviços prestados 
        elif opcao == 3:
            print("Redirecionando você ao site de noticias...") 
            import webbrowser
            url = "https://www.grupoccr.com.br/noticias/" # Abre o navegador diretamente a parte de noticias da CCR
            webbrowser.open(url)
        elif opcao == 4:
            print("Redirecionando você a home do site CCR...")  
            import webbrowser
            url = "https://www.grupoccr.com.br" # Abre o navegador na pagina inicial da CCR
            webbrowser.open(url)
        elif opcao == 5: # Fecha o programa
            print("Fechando o programa...") 
            break
        else:
            print("Opção invalida, verifique as opções disponiveis!\n")

    except ValueError:
        print("Por favor, digite um número válido.")
        
