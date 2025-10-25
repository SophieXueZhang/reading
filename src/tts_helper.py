"""
Text-to-Speech Helper using OpenAI TTS API
Provides high-quality, natural-sounding voice for reading stories
"""

import os
from pathlib import Path
import hashlib


class TTSHelper:
    """Helper class for text-to-speech functionality"""

    AUDIO_CACHE_DIR = Path(__file__).parent.parent / 'data' / 'audio_cache'

    @classmethod
    def get_audio_cache_path(cls, text, voice='alloy'):
        """Get cached audio path for given text"""
        # Create cache directory if it doesn't exist
        cls.AUDIO_CACHE_DIR.mkdir(parents=True, exist_ok=True)

        # Create hash of text for filename
        text_hash = hashlib.md5(text.encode()).hexdigest()
        return cls.AUDIO_CACHE_DIR / f"{voice}_{text_hash}.mp3"

    @classmethod
    def generate_speech(cls, text, voice='alloy'):
        """
        Generate speech audio using OpenAI TTS API

        Args:
            text: Text to convert to speech
            voice: Voice to use (alloy, echo, fable, onyx, nova, shimmer)

        Returns:
            Path to generated audio file
        """
        cache_path = cls.get_audio_cache_path(text, voice)

        # Return cached file if exists
        if cache_path.exists():
            return cache_path

        # Check if API key is available
        api_key = os.environ.get('OPENAI_API_KEY')
        if not api_key:
            from api_config import APIConfig
            api_key = APIConfig.get_api_key()

        if not api_key:
            raise ValueError("OpenAI API key not configured. Please set it in the Settings.")

        # Generate audio using OpenAI TTS
        try:
            from openai import OpenAI
            client = OpenAI(api_key=api_key)

            response = client.audio.speech.create(
                model="tts-1",  # Use tts-1-hd for higher quality
                voice=voice,
                input=text,
                speed=0.9  # Slightly slower for kids
            )

            # Save audio file
            response.stream_to_file(str(cache_path))

            return cache_path

        except Exception as e:
            raise Exception(f"Failed to generate speech: {str(e)}")

    @classmethod
    def clear_cache(cls):
        """Clear all cached audio files"""
        if cls.AUDIO_CACHE_DIR.exists():
            for file in cls.AUDIO_CACHE_DIR.glob("*.mp3"):
                file.unlink()
