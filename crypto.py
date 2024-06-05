"""
RESUMO: 
            - A Ideia incial é construir um programa que realize verificações da bolsa
                para identificar qual a melhor escolha de cryptomoedas para investimento
                sendo assim em primeiro desenvolvimento, realizar a construção de um programa
                que faça raspagem de dados do site https://cryptobubbles.net/ com o filtro
                da corretora BINANCE, na lista do site cryptobubbles contém 997 moedas registradas, 
                posso também pegar e e entrar no site da BINANCE https://www.binance.com/pt-BR
                e coletar as informações para fazer testes e verificações de qual a melhor
                crypto para investimento, os dados mais reais de fato são da BINANCE,
                de inicio vou começar com o site do crytobubbles.

ETAPAS:
    1- Entrar no site da CRYPTOBUBBLES
    2- clicar em escolher filtro de bolsas
    3- escolher BINANCE
    4- Percorrer lista de crypto e colertar as seguintes informações
            - Valor
            - Capacidade de Mercado
            - Volume em 24h
    5- Após percorrer e captar as informações pegar as seguintes informações
            - Hora
            - Dia
            - Semana
            - Mês
            - Ano
    6- Com base nessas informações construir um aprendizado de maquina que 
        identifique qual a escolha mais provavel para investimento, levando
        em consideração o valor minimo de investimento que é $5,00
        o valor que deseja ser investido e o valor que almeja alcançar no final
        
OBS:
    Após a realização desses 6 passos, tentar construir um sistema que analise o grafico
    de crypto para saber o melhor momento de fazer um investimento e o melhor momento de sair
    baseando-se em obter o maior lucro possivel, sendo assim essa analise devera ser feita com
    base nas informações de especialista no assunto.
"""

from binance.client import Client


client = Client(api_key, api_secret)
