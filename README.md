# Study Reminder

Um pequeno projeto Python para praticar funções, entrada de dados, validação e uso de bibliotecas externas. Recebe um título e uma mensagem pelo terminal e solicita uma notificação ao Windows usando a biblioteca winotify.

## Executar

Requer Python 3, Windows e PowerShell disponível. Na pasta do projeto:

```bash
python -m pip install -r requirements.txt
python lembrete.py
```

Exemplo de título: Hora de estudar Python!
Exemplo de mensagem: Revisar funções e resolver três exercícios.

A notificação é solicitada imediatamente. Este projeto não agenda lembretes nem permanece executando em segundo plano. A exibição depende das configurações de notificações do Windows e do modo Não perturbe.

## Como funciona

1. Confere se o sistema é Windows e importa Notification.
2. Recebe título e mensagem com input().
3. Usa strip() e uma condicional para rejeitar campos vazios.
4. Cria um objeto Notification e guarda sua referência em notificacao.
5. Chama o método show() para solicitar a exibição da notificação.

O bloco if __name__ == "__main__" inicia o programa quando o arquivo é executado diretamente. Importar o arquivo em outro módulo não inicia as perguntas.

## Biblioteca e API

O projeto usa a interface de programação (API) da biblioteca winotify: a classe Notification e seu método show(). Não faz requisições a uma API web e não precisa de chave de API.

## Call stack

O código principal chama criar_lembrete(), que cria um quadro de execução com suas variáveis locais. As chamadas a input(), strip() e show() retornam o controle à função após terminarem. Ao chegar ao final ou executar return, criar_lembrete() sai da pilha e o programa termina. Não há recursão.

## Validação

Inclui mensagens para sistema incompatível, biblioteca ausente e campos vazios. Trata cancelamento da entrada. A exibição real da notificação ainda precisa ser verificada no Windows com Python instalado.

Referência: https://github.com/versa-syahptr/winotify
