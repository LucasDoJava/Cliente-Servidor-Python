import socket
import threading

class LeituraThread(threading.Thread):
    def __init__(self, sock):
        super().__init__()
        self.sock = sock

    def run(self):
        try:
            reader = self.sock.makefile("r")

            while True:
                resposta = reader.readline()
                if not resposta:
                    print("Conexão encerrada pelo servidor.")
                    break

                print("Servidor:", resposta.strip())

        except Exception as e:
            print("Erro na leitura:", e)



class EscritaThread(threading.Thread):
    def __init__(self, sock):
        super().__init__()
        self.sock = sock

    def run(self):
        try:
            while True:
                msg = input()
                self.sock.sendall((msg + "\n").encode())

                if msg == "4":
                    break

        except Exception as e:
            print("Erro na escrita:", e)


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("localhost", 6000))  # trocar pelo IP do servidor

    sock.settimeout(2)

    try:
        reader = sock.makefile("r")
        resposta = reader.readline()

        if resposta and "Conexão não aceita" in resposta:
            print(resposta.strip())
            sock.close()
            return
    except:
        pass

    sock.settimeout(None)

    print("===========================================")
    print("Conectado ao servidor!")
    print("1 - Hora")
    print("2 - Data")
    print("3 - Me fale algo legal")
    print("4 - Sair")
    print("===========================================")

    LeituraThread(sock).start()
    EscritaThread(sock).start()


if __name__ == "__main__":
    main()