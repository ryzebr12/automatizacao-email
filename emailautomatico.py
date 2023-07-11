import smtplib

def enviar_email(destinatario, assunto, corpo):
    remetente = "seu_email@gmail.com"
    senha = "sua_senha"

    mensagem = f"Subject: {assunto}\n\n{corpo}"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(remetente, senha)
        server.sendmail(remetente, destinatario, mensagem)
        server.close()
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao enviar o e-mail: {str(e)}")

def ler_emails_do_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo:
            emails = arquivo.readlines()
            emails = [email.strip() for email in emails if email.strip()]
            return emails
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
        return []
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {str(e)}")
        return []

def main():
    nome_arquivo = "emails.txt"  # Nome do arquivo de bloco de notas

    emails = ler_emails_do_arquivo(nome_arquivo)
    if not emails:
        print("Não foram encontrados endereços de e-mail válidos.")
        return

    assunto = "Assunto do e-mail"
    corpo = "Corpo do e-mail"

    for email in emails:
        enviar_email(email, assunto, corpo)

if __name__ == "__main__":
    main()
