import socket
import threading


class ClienteThread(threading.Thread):
    def __init__(self, sock):
        super().__init__()
        self.sock = sock

    def run(self):
        try:
            reader = self.sock.makefile("r")  

            while True:
                resposta = reader.readline()
                if not resposta:
                    break
                print("Servidor:", resposta.strip())

        except Exception as e:
            print("Erro na thread:", e)


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("localhost", 6000))  # trocar pelo IP da rede wifi

    print("Conectado ao servidor!")
    print("1 - Hora")
    print("2 - Data")
    print("3 - Me fale algo legal")
    print("4 - Sair")

    
    thread = ClienteThread(sock)
    thread.start()

    try:
        while True:
            msg = input()
            sock.sendall((msg + "\n").encode())  

            if msg == "4":
                break
    except Exception as e:
        print("Erro:", e)

    sock.close()


if __name__ == "__main__":
    main()