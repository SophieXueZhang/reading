"""
API Configuration Manager
Handles OpenAI API key storage and validation
"""

import os
from pathlib import Path


class APIConfig:
    """Manages API key configuration"""

    ENV_FILE = Path(__file__).parent.parent / '.env'

    @classmethod
    def get_api_key(cls):
        """Get the current API key from .env file"""
        if not cls.ENV_FILE.exists():
            return None

        with open(cls.ENV_FILE, 'r') as f:
            for line in f:
                line = line.strip()
                if line.startswith('OPENAI_API_KEY='):
                    key = line.split('=', 1)[1].strip()
                    return key if key else None
        return None

    @classmethod
    def save_api_key(cls, api_key):
        """Save API key to .env file"""
        api_key = api_key.strip()

        # Read existing content
        other_lines = []
        if cls.ENV_FILE.exists():
            with open(cls.ENV_FILE, 'r') as f:
                for line in f:
                    if not line.strip().startswith('OPENAI_API_KEY='):
                        other_lines.append(line)

        # Write back with new API key
        with open(cls.ENV_FILE, 'w') as f:
            f.write(f'OPENAI_API_KEY={api_key}\n')
            for line in other_lines:
                f.write(line)

        # Update environment variable
        os.environ['OPENAI_API_KEY'] = api_key

        return True

    @classmethod
    def validate_api_key(cls, api_key):
        """Basic validation of API key format"""
        if not api_key:
            return False, "API key cannot be empty"

        api_key = api_key.strip()

        # Check if it starts with expected prefix
        if not api_key.startswith('sk-'):
            return False, "OpenAI API keys should start with 'sk-'"

        # Check minimum length
        if len(api_key) < 20:
            return False, "API key seems too short"

        return True, "API key format looks valid"

    @classmethod
    def mask_api_key(cls, api_key):
        """Mask API key for display (show first 7 and last 4 characters)"""
        if not api_key or len(api_key) < 15:
            return "***"

        return f"{api_key[:7]}...{api_key[-4:]}"

    @classmethod
    def is_configured(cls):
        """Check if API key is configured"""
        key = cls.get_api_key()
        return key is not None and len(key) > 0
