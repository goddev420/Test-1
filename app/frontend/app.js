const connectWallet = async () => {
    try {
        if (window.solana && window.solana.isPhantom) {
            const response = await window.solana.connect();
            console.log("Connected to Phantom Wallet:", response.publicKey.toString());
            return response.publicKey.toString();
        } else {
            alert("Phantom Wallet not found! Install it to continue.");
        }
    } catch (error) {
        console.error("Error connecting to Phantom Wallet:", error);
    }
};