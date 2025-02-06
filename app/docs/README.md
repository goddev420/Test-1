# Solana Token Sniper Application

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   npm install
   ```
2. Configure `.env` file:
   ```
   TWITTER_API_KEY=<your_api_key>
   TWITTER_API_SECRET=<your_api_secret>
   SOLANA_RPC_URL=<your_rpc_url>
   ```
3. Run the backend:
   ```bash
   python backend/sniper.py
   ```
4. Open `frontend/index.html` to connect your Phantom Wallet.