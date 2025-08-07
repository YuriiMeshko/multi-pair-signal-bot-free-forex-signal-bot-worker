
# 🧠 Multi-Pair Signal Bot (Forex + Crypto + Stocks)

Цей бот:
- Під'єднується до TradingView (через `tvdatafeed`)
- Аналізує пари з використанням MACD + Stochastic
- Генерує сигнал (CALL / PUT)
- Відображає графік із сигналом та надсилає його у Telegram

---

## 🚀 Розгорнути на Render

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/YOUR_GITHUB_USERNAME/multi-pair-signal-bot)

---

## ⚙️ Налаштування

Заповни файл `config.py`:
```python
TELEGRAM_TOKEN = '...'
TELEGRAM_CHAT_ID = '...'
USERNAME = 'your_tradingview_username'
PASSWORD = 'your_tradingview_password'
```
