# === Forex Trading Bot using tvdatafeed, MACD + Stochastic ===
from tvDatafeed import TvDatafeed, Interval
import pandas_ta as ta
import pandas as pd
import time
import requests

# === CONFIG ===
TELEGRAM_TOKEN = '8359746656:AAECBpdn6J3oIJiSHfZoKiUDoRGM3Xo8ZhE'
TELEGRAM_CHAT_ID = '6961366384'
USERNAME = 'jurameshko9@gmail.com'
PASSWORD = 'Jura4592.'

SYMBOLS = [
    "BTC-USD", "ETH-USD", "BNB-USD", "SOL-USD",           # крипта
    "EURUSD=X", "USDJPY=X", "GBPUSD=X", "AUDUSD=X",       # Forex
    "AAPL", "GOOG", "TSLA", "AMZN", "MSFT"                # Акції
]
EXCHANGE = "FX"

# === Init TV session ===
tv = TvDatafeed(usernamejurameshko9@gmail.com password=Jura4592.)

# === Send Telegram Message ===
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"[Telegram Error] {e}")

# === Analyze Market ===
def analyze_market(symbol, exchange):
    try:
        df = tv.get_hist(symbol=symbol, exchange=exchange, interval=Interval.in_5_minute, n_bars=200)
        df.dropna(inplace=True)

        df['macd'], df['macd_signal'], _ = ta.macd(df['close'])
        df['stoch_k'], df['stoch_d'] = ta.stoch(df['high'], df['low'], df['close'])

        last = df.iloc[-1]
        prev = df.iloc[-2]

        support = df['close'].min()
        resistance = df['close'].max()

        # CALL condition
        if (
            last['close'] <= support + 0.0003 and
            last['macd'] > last['macd_signal'] and
            prev['stoch_k'] < 20 and last['stoch_k'] > last['stoch_d']
        ):
            return "CALL"

        # PUT condition
        elif (
            last['close'] >= resistance - 0.0003 and
            last['macd'] < last['macd_signal'] and
            prev['stoch_k'] > 80 and last['stoch_k'] < last['stoch_d']
        ):
            return "PUT"

        else:
            return "WAIT"

    except Exception as e:
        print(f"[ERROR] {symbol} -> {e}")
        return "WAIT"

# === Main Loop ===
print("📡 Forex Signal Bot запущено. Кожні 60 сек перевірка сигналів...")
while True:
    for symbol in SYMBOLS:
        signal = analyze_market(symbol, EXCHANGE)
        msg = f"\ud83d\udcc8 {symbol}: {signal}"
        print(msg)
        send_telegram_message(msg)
    time.sleep(60)
