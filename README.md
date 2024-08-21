# AI Tech Support Voice Assistant with RAG and Mistral

This project implements an AI-powered voice assistant for technical support, using speech recognition, natural language processing, and text-to-speech technologies.

## Prerequisites

For the setup for this project, you will need the following prerequisites:

### Software Prerequisites:

1. Python 3.8 or higher
2. pip (Python package manager)
3. Git (for version control)
4. A C++ compiler (for building some dependencies)
5. Ollama (for running the language model)
6. Qdrant (for vector database)
7. FFmpeg (for audio processing)

### Hardware Prerequisites:

1. Microphone
2. Speakers or headphones

## System Requirements

- Operating System: Windows 10+, macOS 10.14+, or Linux (Ubuntu 18.04+)
- RAM: Minimum 8GB, Recommended 16GB+
- Storage: At least 5GB of free space
- CPU: Multi-core processor (Intel i5 or equivalent)
- GPU: Optional, but recommended for faster processing

## Installation

1. Install Python 3.8 or higher from [python.org](https://www.python.org/downloads/)

2. Install Git from [git-scm.com](https://git-scm.com/downloads)

3. Install a C++ compiler:
   - Windows: Install [Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
   - macOS: Install Xcode Command Line Tools by running `xcode-select --install` in the terminal
   - Linux: Install GCC by running `sudo apt-get install build-essential`

4. Install FFmpeg:
   - Windows: Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH
   - macOS: Install using Homebrew with `brew install ffmpeg`
   - Linux: Install using `sudo apt-get install ffmpeg`

5. Install Ollama:
   Follow the instructions at [Ollama's official website](https://ollama.ai/download) to install Ollama on your system.

6. Install Qdrant:
   Follow the instructions at [Qdrant's official documentation](https://qdrant.tech/documentation/quick_start/) to install and run Qdrant.

7. Clone the repository:
```
git clone https://github.com/gaganjotshan/AI-Voice-Assistant-LLM.git
cd AI-Voice-Assistant-LLM
```

8. [Create a virtual environment](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/):
For Mac OS X:
```
 python3.10.14 -m venv llm_env
 ```

9. Activate the virtual environment:
- On Windows:
  ```
  lm_env\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source lm_env/bin/activate
  ```

10. Install the required Python packages:
 ```
 pip install -r requirements.txt
 ```

## Project Structure
```
ai_tech_support/
├── src/
│ └── ai_tech_support/
│ ├── init.py
│ ├── audio/
│ │ ├── init.py
│ │ ├── recorder.py
│ │ └── transcriber.py
│ ├── llm_model/
│ │ ├── init.py
│ │ ├── tech_assistant.py
│ │ └── knowledge_base.py
│ ├── speech/
│ │ ├── init.py
│ │ └── synthesizer.py
│ └── utils/
│ ├── init.py
│ ├── config.py
│ ├── logger.py
│ └── exception.py
├── tests/
│ ├── init.py
│ ├── test_audio.py
│ ├── test_support.py
│ └── test_speech.py
├── config/
│ └── config.yaml
├── data/
│ └── product_manual.txt
├── requirements.txt
├── setup.py
├── app.py
├── main.py
└── README.md
```


## Configuration

1. Update the knowledge base:
   Edit the `data/product_manual.txt` file with relevant technical support information for your product or service.

2. Adjust the AI assistant's behavior:
   Modify the system prompt in `src/ai_tech_support/support/tech_assistant.py` to fit your specific use case.


## Usage

1. Ensure Qdrant is running on your system, open a seprate terminal and run:
```
qdrant
```

2. We are using Mistral, make sure Ollama is running on your system and pull mistral:
```
ollama pull mistral  
```


3. Start the AI Tech Support Assistant:
```
python app.py
```


4. When you see the "_" prompt, speak your query clearly into your microphone.

5. The assistant will process your query and respond verbally and in text.

6. To exit the program, use Ctrl+C.

## Key Components

### AIVoiceAssistant.py

This file contains the main `AIVoiceAssistant` class, which initializes the Qdrant client, Ollama language model, and creates the knowledge base and chat engine. It handles the interaction with the language model and provides responses to user queries.

### app.py

The main application script that handles audio recording, transcription, and interaction with the AI assistant. It uses the Whisper model for speech recognition and manages the main loop of the application.

### voice_service.py

This file contains the `play_text_to_speech` function, which converts text to speech using gTTS and plays it back using Pygame.

## Troubleshooting

- If you encounter audio-related errors, ensure your microphone is properly connected and selected as the default input device.
- For performance issues, consider using a smaller language model or enabling GPU acceleration if available.
- If the assistant's responses are too long or repetitive, adjust the system prompt in `src/ai_tech_support/support/tech_assistant.py`.

## Contributing

Contributions to improve the AI Tech Support Assistant are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.