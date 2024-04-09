===============================================================================

                      Sistema de Gerenciamento de Ponto Eletrônico

===============================================================================

Criador: Brayan Vieira
Função:  Um sistema de gerenciamento de ponto eletrônico
Versão: 1.0
Data da Criação: 08/03/2024

===============================================================================

Este código implementa um sistema simples de gerenciamento de ponto eletrônico. 
Permite aos funcionários registrar seus horários de entrada e saída, além de 
verificar atrasos, armazenando essas informações em um arquivo.

===============================================================================

Principais Funcionalidades:

1. Bater Ponto de Horário: Permite aos funcionários registrar seus horários 
de entrada e saída.

2. Ver Pontos Batidos: Exibe os pontos batidos pelos funcionários.

3. Sair: Encerra o programa.

===============================================================================

Descrição das Funções:

1. verificar_cargo(cargo):
   Verifica se o cargo informado está na lista de cargos válidos.

2. mostrar_cargos():
   Mostra os cargos disponíveis.

3. limpador():
   Limpa a tela do terminal, compatível com diferentes sistemas operacionais.

4. verificar_existencia_do_arquivo():
   Verifica se o arquivo de registro de pontos existe. Se não existir, cria um 
   novo arquivo.

5. verificar_atraso():
   Verifica se o horário atual é maior ou igual ao horário definido, considerando
   atraso caso seja.

6. registrar_ponto():
   Registra o ponto do funcionário, solicitando nome e cargo, e armazena as 
   informações no arquivo.

7. ver_pontos():
   Exibe os pontos batidos registrados no arquivo.

===============================================================================

Uso do Programa:

1. Execute o programa.
2. Selecione a opção correspondente ao que deseja fazer:
   - B para bater ponto de horário.
   - V para ver pontos batidos.
   - E para sair do programa.

===============================================================================
