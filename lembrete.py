import sys


def criar_lembrete():
    if sys.platform != "win32":
        print("Este programa precisa do Windows para exibir notificacoes.")
        return

    try:
        from winotify import Notification
    except ModuleNotFoundError as erro:
        if erro.name != "winotify":
            raise
        print("Instale a biblioteca: python -m pip install -r requirements.txt")
        return

    print("Lembrete de estudos")
    titulo = input("Digite o titulo: ").strip()
    mensagem = input("O que voce quer estudar? ").strip()

    if not titulo or not mensagem:
        print("Preencha o titulo e a mensagem do lembrete.")
        return

    notificacao = Notification(
        app_id="Lembrete de Estudos",
        title=titulo,
        msg=mensagem,
    )
    notificacao.show()
    print("Notificacao solicitada. Confira as notificacoes do Windows.")


if __name__ == "__main__":
    try:
        criar_lembrete()
    except (KeyboardInterrupt, EOFError):
        print("\nEntrada cancelada.")
