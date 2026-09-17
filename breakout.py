import yfinance as yf
import pandas as pd
import datetime

# List of Nifty 50 tickers on Yahoo Finance
NIFTY_50_TICKERS = [
    "ADANIENT.NS", "ADANIPORTS.NS", "APOLLOHOSP.NS", "ASIANPAINT.NS", "AXISBANK.NS",
    "BAJAJ-AUTO.NS", "BAJFINANCE.NS", "BAJAJFINSV.NS", "BEL.NS", "BPCL.NS",
    "BHARTIARTL.NS", "BRITANNIA.NS", "CIPLA.NS", "COALINDIA.NS", "DIVISLAB.NS",
    "DRREDDY.NS", "EICHERMOT.NS", "GRASIM.NS", "HCLTECH.NS", "HDFCBANK.NS",
    "HDFCLIFE.NS", "HEROMOTOCO.NS", "HINDALCO.NS", "HUNVR.NS", "ICICIBANK.NS",
    "ITC.NS", "INDUSINDBK.NS", "INFY.NS", "JSWSTEEL.NS", "KOTAKBANK.NS",
    "LT.NS", "LTIM.NS", "M&M.NS", "MARUTI.NS", "NTPC.NS", "NESTLEIND.NS",
    "ONGC.NS", "POWERGRID.NS", "RELIANCE.NS", "SBILIFE.NS", "SHRIRAMFIN.NS",
    "SBIN.NS", "SUNPHARMA.NS", "TCS.NS", "TATACONSUM.NS", "TATAMOTORS.NS",
    "TATASTEEL.NS", "TECHM.NS", "TITAN.NS", "TRENT.NS", "ULTRACEMCO.NS", "WIPRO.NS"
]

def scan_nifty50_breakouts():
    print("Scanning Nifty 50 for Breakout Candidates...\n")
    breakout_candidates = []

    for ticker in NIFTY_50_TICKERS:
        try:
            # Download recent daily data (60 days)
            df = yf.download(ticker, period="60d", interval="1d", progress=False)
            
            if len(df) < 30:
                continue

            # Flatten MultiIndex columns if present
            if isinstance(df.columns, pd.MultiIndex):
                df.columns = df.columns.get_level_values(0)

            # Technical Parameters
            latest = df.iloc[-1]
            prev_days = df.iloc[-21:-1] # Last 20 trading days excluding today
            
            close_price = latest['Close']
            high_20d = prev_days['High'].max()
            avg_volume_20d = prev_days['Volume'].mean()
            today_volume = latest['Volume']
            
            # 1. Proximity Condition: Price is within 2% of or above 20-day High
            distance_from_high = ((close_price - high_20d) / high_20d) * 100
            
            # 2. Volume Spike Condition: Today's volume > 1.5x of 20-day Average
            volume_ratio = today_volume / avg_volume_20d
            
            # 3. Consolidation Check: Range over last 5 days was narrow (< 3% spread)
            recent_5d_range = ((df.iloc[-6:-1]['High'].max() - df.iloc[-6:-1]['Low'].min()) / df.iloc[-6:-1]['Low'].min()) * 100

            # Filter Criteria
            is_breakout = (close_price >= high_20d) and (volume_ratio >= 1.3)
            is_near_breakout = (distance_from_high >= -1.5) and (distance_from_high < 0) and (volume_ratio >= 1.2) and (recent_5d_range < 4.0)

            if is_breakout:
                breakout_candidates.append({
                    "Ticker": ticker.replace(".NS", ""),
                    "Status": "🔥 ACTIVE BREAKOUT",
                    "Close": round(close_price, 2),
                    "20D High": round(high_20d, 2),
                    "Volume Ratio": f"{round(volume_ratio, 2)}x",
                    "Distance %": f"+{round(distance_from_high, 2)}%"
                })
            elif is_near_breakout:
                breakout_candidates.append({
                    "Ticker": ticker.replace(".NS", ""),
                    "Status": "⏳ COILING (Imminent Breakout)",
                    "Close": round(close_price, 2),
                    "20D High": round(high_20d, 2),
                    "Volume Ratio": f"{round(volume_ratio, 2)}x",
                    "Distance %": f"{round(distance_from_high, 2)}%"
                })

        except Exception as e:
            continue

    # Display Results
    results_df = pd.DataFrame(breakout_candidates)
    if not results_df.empty:
        print(results_df.to_string(index=False))
    else:
        print("No Nifty 50 stocks currently meet the strict breakout criteria.")

if __name__ == "__main__":
    scan_nifty50_breakouts()