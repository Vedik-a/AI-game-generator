from dotenv import load_dotenv
import os

load_dotenv()

NVIDIA_API_KEY = os.getenv("NVIDIA_NIM_API_KEY")

MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "meta/llama3-8b-instruct"
)

NVIDIA_BASE_URL = "https://integrate.api.nvidia.com/v1"