<h1 align="center">🤖 Chatbot Terminal Gemini</h1>
<p align="center">Interaja com uma Inteligência Artificial no terminal com voz, cores e armazenamento inteligente 🧠💬</p>

---

## ✨ Visão Geral

O <strong>Chatbot Terminal Gemini</strong> é um assistente virtual desenvolvido para rodar diretamente no terminal, proporcionando uma experiência conversacional natural em português com respostas objetivas, personalizadas e com síntese de voz integrada. 

Utiliza a avançada <strong>API Gemini da Google</strong> para oferecer respostas rápidas e inteligentes, combinando eficiência, personalização visual e auditiva. Agora com melhorias na velocidade de resposta e falas mais naturais.

---

## 🚀 Funcionalidades

- Interação com IA diretamente pelo terminal  
- Respostas concisas, claras e sempre em português  
- **Fala automática das respostas com voz natural via `pyttsx3`**  
- Interface colorida com destaque nas mensagens (`colorama`)  
- Histórico de conversas salvo automaticamente em `chat.txt`  
- Registro de data, hora e tempo total de sessão

---

## 🔧 Bibliotecas Utilizadas

- [`google-generativeai`](https://pypi.org/project/google-generativeai/): integração com a API Gemini da Google  
- [`pyttsx3`](https://pypi.org/project/pyttsx3/): geração de voz offline  
- [`colorama`](https://pypi.org/project/colorama/): colorização dos textos no terminal  
- [`datetime`](https://docs.python.org/3/library/datetime.html): controle de data e hora  
- [`time`](https://docs.python.org/3/library/time.html): controle de tempo e pausas  
- [`sys`](https://docs.python.org/3/library/sys.html): manipulação do sistema e execução de comandos

---

## ⚙️ Requisitos Técnicos

- Python 3.7 ou superior  
- Conexão ativa com a internet para uso da API  
- Chave de API Gemini configurada corretamente  
- Sistema operacional compatível com `pyttsx3` (Windows, Linux, macOS)

---

## 📝 Histórico
Todas as conversas são registradas em tempo real no arquivo chat.txt, com marcação de data, hora e tempo total.

---

<p align="center"><em>Projeto desenvolvido para oferecer uma solução prática, leve e eficiente para interação com IA via terminal.</em></p>
