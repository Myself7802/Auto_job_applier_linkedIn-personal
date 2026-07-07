'''
Author:     Sai Vignesh Golla
LinkedIn:   https://www.linkedin.com/in/saivigneshgolla/

Copyright (C) 2024 Sai Vignesh Golla

License:    GNU Affero General Public License
            https://www.gnu.org/licenses/agpl-3.0.en.html

GitHub:     https://github.com/GodsScion/Auto_job_applier_linkedIn

Support me: https://github.com/sponsors/GodsScion

version:    24.12.3.10.30
'''

import os


def _load_dotenv() -> None:
    '''
    Loads simple KEY=VALUE pairs from the project root `.env` file.
    Existing environment variables are preserved.
    '''
    env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
    if not os.path.exists(env_path):
        return

    try:
        with open(env_path, 'r', encoding='utf-8') as env_file:
            for line in env_file:
                line = line.strip()
                if not line or line.startswith('#') or '=' not in line:
                    continue
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip().strip('"').strip("'")
                if key and key not in os.environ:
                    os.environ[key] = value
    except Exception:
        pass


_load_dotenv()

###################################################### CONFIGURE YOUR TOOLS HERE ######################################################


# Login Credentials for LinkedIn (Optional)
username = "username@example.com"       # Enter your username in the quotes
password = "example_password"           # Enter your password in the quotes


## Artificial Intelligence (Beta Not-Recommended)
# Use AI
use_AI = os.getenv("USE_AI", "False").lower() == "true"   # True or False, Note: True or False are case-sensitive
'''
Note: Set it as True only if you want to use AI, and If you either have a
1. Local LLM model running on your local machine, with it's APIs exposed. Example softwares to achieve it are:
    a. Ollama - https://ollama.com/
    b. llama.cpp - https://github.com/ggerganov/llama.cpp
    c. LM Studio - https://lmstudio.ai/ (Recommended)
    d. Jan - https://jan.ai/
2. OR you have a valid OpenAI API Key, and money to spare, and you don't mind spending it.
CHECK THE OPENAI API PIRCES AT THEIR WEBSITE (https://openai.com/api/pricing/).
'''

# Select AI Provider
ai_provider = "openai"               # "openai"
'''
Note: This project is now configured to use only OpenAI-compatible APIs for tailored Easy Apply answers.
Keep this value as "openai".
'''


# Your LLM url or other AI api url and port
llm_api_url = os.getenv("OPENAI_API_URL", "https://api.openai.com/v1/")       # Examples: "https://api.openai.com/v1/", "http://127.0.0.1:1234/v1/", "http://localhost:1234/v1/"
'''
Note: Don't forget to add / at the end of your url.
'''

# Your LLM API key or other AI API key
llm_api_key = os.getenv("OPENAI_API_KEY", "not-needed")              # Loaded from .env or environment variables.
'''
Note: Leave it empty as "" or "not-needed" if not needed. Else will result in error!
If you are using ollama, you MUST put "not-needed".
'''

# Your LLM model name or other AI model name
llm_model = os.getenv("OPENAI_MODEL", "gpt-5-mini")          # Examples: "gpt-4o", "gpt-4o-mini", "gpt-5-mini", "llama-3.2-3b-instruct", "qwen3:latest"

llm_spec = "openai"                # Examples: "openai", "openai-like", "openai-like-github", "openai-like-mistral"
'''
Note: OpenAI and OpenAI-compatible endpoints are supported.
Most local LLM gateways are OpenAI-compatible, so keeping this as "openai" or "openai-like" will work.
'''

# # Yor local embedding model name or other AI Embedding model name
# llm_embedding_model = "nomic-embed-text-v1.5"

# Do you want to stream AI output?
stream_output = False                    # Examples: True or False. (False is recommended for performance, True is recommended for user experience!)
'''
Set `stream_output = True` if you want to stream AI output or `stream_output = False` if not.
'''
##



############################################################################################################
'''
THANK YOU for using my tool 😊! Wishing you the best in your job hunt 🙌🏻!

Sharing is caring! If you found this tool helpful, please share it with your peers 🥺. Your support keeps this project alive.

Support my work on <PATREON_LINK>. Together, we can help more job seekers.

As an independent developer, I pour my heart and soul into creating tools like this, driven by the genuine desire to make a positive impact.

Your support, whether through donations big or small or simply spreading the word, means the world to me and helps keep this project alive and thriving.

Gratefully yours 🙏🏻,
Sai Vignesh Golla
'''
############################################################################################################
