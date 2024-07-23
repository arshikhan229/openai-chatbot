# Voice Assistant

Voice Assistant is an AI-powered assistant that leverages speech recognition, text generation, and text-to-speech functionalities to interact with users. It uses OpenAI's GPT-3.5-turbo model for generating responses and Eleven Labs' tools for voice cloning and audio generation.

## Features

- **Speech-to-Text**: Converts spoken words into text using the Whisper model from OpenAI.
- **Text Generation**: Utilizes OpenAI's GPT-3.5-turbo model to generate responses.
- **Text-to-Speech**: Converts text responses into speech using Eleven Labs' voice cloning and generation tools.
- **Interactive Sessions**: Provides an AI assistant experience for interactive voice-based communication.

## Installation

1. **Clone the Repository**:
   ```sh
   git clone <repository_url>
   cd <repository_name>
   ```

2. **Set Up Virtual Environment**:
   - Install `virtualenv` if you haven't already:
     ```sh
     pip install virtualenv
     ```
   - Create a virtual environment:
     ```sh
     python -m venv env
     ```
   - Activate the virtual environment:
     ```sh
     .\env\Scripts\activate
     ```

3. **Install Dependencies**:
   ```sh
   pip install --upgrade pip
   pip install openai whisper torchaudio playsound elevenlabs
   ```

## Configuration

1. **API Keys**:
   - Set your OpenAI API key and Eleven Labs API key in the script:
     ```python
     openai.api_key = "your_openai_api_key"
     set_api_key("your_elevenlabs_api_key")
     ```

## Usage

1. **Activate the Virtual Environment**:
   ```sh
   .\env\Scripts\activate
   ```

2. **Run the Script**:
   ```sh
   python voice_assistant.py
   ```

3. **Input Audio File**:
   - Replace `audio` in the script with the path to your audio file.
   - Example:
     ```python
     audio = "path/to/your/audio/file.mp3"
     ```

4. **Script Workflow**:
   - The script will convert the audio file to text.
   - Generate a response based on the input text.
   - Convert the generated response back to speech and save it as an MP3 file.

## Example

To see an example in action, you can run the script with a provided audio file. The script will:
- Convert the audio input to text.
- Generate a response based on the input text.
- Convert the response to speech and save it as `output_voice.mp3`.

## Dependencies

- Python 3.6+
- [OpenAI](https://pypi.org/project/openai/)
- [Whisper](https://github.com/openai/whisper)
- [Torchaudio](https://pypi.org/project/torchaudio/)
- [Eleven Labs](https://elevenlabs.io/)
- [playsound](https://pypi.org/project/playsound/)

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.

## Acknowledgments

- OpenAI for providing the GPT-3.5-turbo and Whisper models.
- Eleven Labs for their voice cloning and text-to-speech tools.

---

You can create a file named `README.md` in your project directory and copy the above content into it. Additionally, rename the `answer123.py` script to `voice_assistant.py` to better reflect its purpose.

