import os
from dotenv import load_dotenv

load_dotenv()

AGENT_NAME = "dev-assist"
DESCRIPTION = "A trainer/tutor agent for developers."
PROJECT = os.getenv("GOOGLE_CLOUD_PROJECT", "EMPTY")
LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION", "global")
TUTOR_MODEL = os.getenv("TUTOR_MODEL", "gemini-2.0-flash-thinking-exp-01-21")
BASE_MODEL = os.getenv("BASE_MODEL", "gemini-2.0-flash-thinking-exp-01-21")