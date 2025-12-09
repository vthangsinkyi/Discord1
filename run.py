import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import threading
import time
from website.app import create_app
from bot.bot import run_discord_bot
from config import Config

def run_website():
    """Run Flask website"""
    app = create_app()
    print(f"🌐 Website starting on http://localhost:{Config.PORT}")
    print(f"   • Verification: http://localhost:{Config.PORT}/verify")
    print(f"   • Admin: http://localhost:{Config.PORT}/admin/login")
    app.run(debug=True, host='0.0.0.0', port=Config.PORT, use_reloader=False)

def main():
    print("=" * 60)
    print("🚀 DISCORD VERIFICATION SYSTEM - STARTING")
    print("=" * 60)
    
    # Check essential credentials
    if not Config.DISCORD_TOKEN or Config.DISCORD_TOKEN == 'your_token_here':
        print("❌ ERROR: No Discord token found in .env file!")
        print("Please add your Discord bot token to .env")
        return
    
    if not Config.MONGODB_URI or 'mongodb+srv://' not in Config.MONGODB_URI:
        print("⚠️ WARNING: MongoDB URI not configured properly")
        print("Using local database (JSON files)")
    
    # Start Discord bot in separate thread
    print("🤖 Starting Discord bot...")
    bot_thread = threading.Thread(target=run_discord_bot, daemon=True)
    bot_thread.start()
    
    # Give bot time to start
    time.sleep(3)
    
    # Start Flask website
    print("🌐 Starting website...")
    print("=" * 60)
    run_website()

if __name__ == '__main__':
    main()