import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Discord Bot
    DISCORD_TOKEN = os.getenv('DISCORD_TOKEN', '')
    GUILD_ID = int(os.getenv('DISCORD_GUILD_ID', '0'))
    CLIENT_ID = os.getenv('CLIENT_ID', '')
    CLIENT_SECRET = os.getenv('CLIENT_SECRET', '')
    REDIRECT_URI = os.getenv('REDIRECT_URI', 'http://localhost:5000/callback')
    
    # Webhooks
    WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL', '')
    LOGS_WEBHOOK = os.getenv('DISCORD_LOGS_WEBHOOK', '')
    
    # MongoDB
    MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/')
    DATABASE_NAME = os.getenv('DATABASE_NAME', 'discord_verification')
    
    # Flask Website
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-me')
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    PORT = int(os.getenv('PORT', '5000'))  # Fixed: Convert string to int
    
    # Admin Credentials
    ADMIN_USERNAME = os.getenv('ADMIN_USERNAME', 'admin')
    ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'admin123')
    
    # Verification Role
    VERIFIED_ROLE_NAME = "Verified"
    VERIFIED_ROLE_ID = os.getenv('VERIFIED_ROLE_ID', '')
    VERIFIED_ROLE_COLOR = 0x00ff00
    
    # API Services
    IPINFO_TOKEN = os.getenv('IPINFO_TOKEN', '')
    VPN_API_KEY = os.getenv('VPN_API_KEY', '')
    
    # Security Settings
    MAX_LOGIN_ATTEMPTS = 3
    SESSION_TIMEOUT = 3600
    
    # Website URLs
    WEBSITE_URL = os.getenv('WEBSITE_URL', 'http://localhost:5000')
    VERIFY_URL = f"{WEBSITE_URL}/verify"
    
    @classmethod
    def validate_config(cls):
        """Validate configuration and print warnings"""
        warnings = []
        
        if not cls.DISCORD_TOKEN or cls.DISCORD_TOKEN == 'your_token_here':
            warnings.append("❌ DISCORD_TOKEN is not set or is default")
        
        if not cls.MONGODB_URI or 'mongodb+srv://' not in cls.MONGODB_URI:
            warnings.append("⚠️  MONGODB_URI might not be properly configured")
        
        if not cls.VERIFIED_ROLE_ID:
            warnings.append("⚠️  VERIFIED_ROLE_ID is not set - force_verify command won't work")
        
        if not cls.WEBHOOK_URL:
            warnings.append("⚠️  DISCORD_WEBHOOK_URL is not set")
        
        if not cls.IPINFO_TOKEN:
            warnings.append("ℹ️  IPINFO_TOKEN is not set - VPN detection will be basic")
        
        return warnings