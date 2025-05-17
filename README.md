# 🤖 Cyber Bot — A Telegram Chatbot for Cybersecurity Topics

Cyber Bot is an AI-powered Telegram chatbot designed to explain (cybersecurity topics) in simple and understandable language. Built with **LangChain**, **Groq**, and the **Telegram Bot API**, this bot helps users learn about concepts like malware, phishing, firewalls, and much more — directly from Telegram.

---

## 🚀 Features

- 📚 Explains cybersecurity topics like ransomware, DDoS, VPNs, firewalls, and more.
- 🧠 Uses **LangChain** with **Groq LLM** for powerful natural language responses.
- 🤖 Responds to users via **Telegram** with easy-to-use mention syntax.
- 🌐 Deployed using **Railway** for quick and scalable hosting.

---

## 🛠️ Tech Stack

| Technology           | Role                                     |
|----------------------|---------------------------------- -------|
| **LangChain**        | Prompt management + LLM chaining         |
| **Groq**             | LLM provider for generating explanations |
| **Telegram Bot API** | Messaging interface with users           |
| **Python**           | Bot backend logic                        |
| **Railway**          | Deployment platform                      |
| **dotenv**           | Secure API key management                |

---

## 🧑‍💻 How It Works

1. Users tag the bot with a topic.
2. The bot receives the message and extracts the topic.
3. LangChain sends a structured prompt to the Groq LLM.
4. The LLM generates a detailed explanation of the topic.
5. If the response exceeds Telegram's message limit, the bot splits it into chunks and sends them sequentially.

---

## 🔐 Use Case
@ go to --->>  htts://t.me/CyberTech_bot  <<---
Ask about a the topic before calling @CyberTech_bot..

Example:
@CyberTech_bot malware  [Prefered to use one word questions].




