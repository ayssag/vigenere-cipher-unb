# vigenere-cipher-unb
Repositório contendo os códigos e o relatório referentes ao Trabalho de Implementação 1 da disciplina Seguranca Computacional ofertada em 2023/1.

Como especificado na descrição, esse trabalho é separado em duas partes: I e II.

## Parte I
O cifrador recebe uma senha e uma mensagem que é cifrada segundo a cifra de Vigenère, gerando um criptograma, enquanto o decifrador recebe uma senha e um criptograma que é decifrado segundo a cifra de Vigenère, recuperando uma mensagem.

## Parte II
Serão fornecidas duas mensagens cifradas (uma em português e outra em inglês) com senhas diferentes. Cada uma das mensagens deve ser utilizada para recuperar a senha geradora do keystream usado na cifração e então decifradas. 

Os textos devem estar contidos em arquivos .txt dentro da pasta src/texts para o funcionamento correto do programa.

## Execução
Instale as bibliotecas necessárias utilizando pip.
```
pip install -r requirements.txt
```
Para iniciar o programa, vá para a pasta /src via linha de comando em um terminal linux.
```
cd src
```
Execute o comando:
```
python main.py
```