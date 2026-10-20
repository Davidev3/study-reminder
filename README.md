# Estudo da biblioteca winotify

Repositório de estudo em Python para testar uma nova biblioteca e aprender a exibir uma notificação no Windows.

## Código

```python
from winotify import Notification

notf = Notification (
    app_id= "Python",
    title="Aprende essa!",
    msg="!",
)

notf.show()
```

## Como funciona

- `from winotify import Notification` importa a classe usada para criar a notificação.
- `Notification(...)` cria um objeto com o identificador do aplicativo (`app_id`), o título (`title`) e a mensagem (`msg`).
- `notf` guarda a referência desse objeto.
- `notf.show()` chama o método que solicita a exibição da notificação.

## Executar

Com Python 3 e PowerShell disponíveis no Windows, execute na pasta do projeto:

```bash
python -m pip install -r requirements.txt
python lembrete.py
```

A exibição depende das configurações de notificações do Windows. Este exemplo ainda precisa ser testado nesse ambiente.

Biblioteca utilizada: [winotify](https://github.com/versa-syahptr/winotify).
