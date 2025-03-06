# 🔐 Cifra de César - Criptografia e Descriptografia em Python

Este projeto implementa a **Cifra de César**, um método simples de criptografia por substituição, onde cada letra do texto é deslocada um número fixo de posições no alfabeto.

## 🛠 Funcionalidades

✔️ **Criptografar** um texto com um deslocamento definido pelo usuário.  
✔️ **Descriptografar** um texto criptografado usando a mesma chave.  
✔️ **Interface interativa** no terminal para escolha de opções.  
✔️ **Mantém caracteres especiais e espaços** inalterados.  

## 📜 Como funciona?

A Cifra de César desloca cada letra do alfabeto por um número fixo de posições.  
Por exemplo, com deslocamento de **3**:

- **A → D**
- **B → E**
- **C → F**
- **X → A**
- **Y → B**
- **Z → C**

Para descriptografar, basta inverter o deslocamento.

## 🚀 Como executar o projeto?

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/cifra-de-cesar.git
   cd cifra-de-cesar
   ```

2. **Execute o script principal:**
   ```bash
   python main.py
   ```

3. **Escolha uma opção no menu:**
   - 1️⃣ Criptografar um texto
   - 2️⃣ Descriptografar um texto
   - 3️⃣ Sair

## 📝 Exemplo de uso

### **Criptografando um texto**
```
Digite o texto para criptografar: hello world
Digite a chave (1 a 26): 3
Texto criptografado: khoor zruog
```

### **Descriptografando o texto**
```
Digite o texto para descriptografar: khoor zruog
Digite a chave (1 a 26): 3
Texto descriptografado: hello world
```

## 📌 Estrutura do projeto

```
cifra-de-cesar/
│── src/
│   ├── services/
│   │   ├── encrypt.py
│   │   ├── decrypt.py
│── main.py
│── README.md
```

- **`encrypt.py`**: Contém a função de criptografia.
- **`decrypt.py`**: Contém a função de descriptografia.
- **`main.py`**: Gerencia o menu e a interação com o usuário.
- **`README.md`**: Documentação do projeto.

## 📌 Tecnologias utilizadas
- **Python 3.x**
- Manipulação de strings
- Estruturas de controle (`if`, `while`)
- Listas e índices

## 🎯 Próximos passos (Melhorias futuras)
- ✅ Implementar suporte para letras maiúsculas.
- ✅ Adicionar testes automatizados.
- 🔜 Criar uma interface gráfica (GUI).
- 🔜 Adicionar suporte a múltiplas linguagens.

📌 **Sinta-se à vontade para contribuir!** Forks e PRs são bem-vindos. 🚀
