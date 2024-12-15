Atualizei o nome no README para refletir o título **AutoMessenger**:  

```markdown
# AutoMessenger - Bot para Envio Automático de Mensagens no WhatsApp

AutoMessenger é um bot automatizado que utiliza o **Selenium** para enviar mensagens no WhatsApp Web. Ele é ideal para automatizar tarefas repetitivas, como envio de notificações, lembretes ou mensagens personalizadas para múltiplos contatos.

## Funcionalidades

- Login automatizado no WhatsApp Web.
- Envio de mensagens personalizadas para uma lista de contatos.
- Tratamento de mensagens (remoção de emojis e caracteres não alfanuméricos).
- Busca automatizada de contatos no WhatsApp Web.
- Encaminhamento de mensagens para múltiplos contatos.

## Pré-requisitos

Certifique-se de ter os seguintes itens instalados no seu sistema:

- **Python 3.8 ou superior**
- Gerenciador de pacotes `pip`
- Navegador Google Chrome
- Bibliotecas Python listadas em `requirements.txt`

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/automessenger.git
   cd automessenger
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure os contatos e a mensagem no código fonte.

## Como Usar

1. Certifique-se de que o Google Chrome está instalado no seu computador.
2. Execute o script:
   ```bash
   python automessenger.py
   ```
3. Escaneie o código QR com seu aplicativo WhatsApp para autenticar no WhatsApp Web.
4. O bot começará a enviar mensagens automaticamente para os contatos configurados.

## Estrutura do Código

- **`mensagem`**: Mensagem a ser enviada para os contatos.
- **`contatos`**: Lista de contatos que receberão a mensagem.
- **`Selenium`**: Automação do navegador para interagir com o WhatsApp Web.
- **`pyperclip`**: Utilizado para copiar a mensagem para a área de transferência.

## Observações

- Este projeto foi desenvolvido para fins educacionais e de automação pessoal.
- Certifique-se de respeitar as políticas de uso do WhatsApp.
- A automação pode falhar caso o layout do WhatsApp Web seja alterado.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Desenvolvido com ❤️ e Python. 🐍
```

Se precisar de algo mais, é só avisar! 😊
