# Jarvis: Rule-Based Python Desktop Assistant

A fully conversational, rule-based desktop assistant built using Python. This project features a continuous multi-turn active listening loop, safe dictionary-based media parsing, and native Windows speech generation.

## 🚀 Features
- **Continuous Conversation Mode:** Once activated with the wake word "Jarvis", the assistant stays awake to take multiple commands until explicitly told to sleep.
- **Smart Voice Switching:** Dynamically switches between male (David) and female (Zira) voices using native Windows system profiles.
- **Safe Media Playback:** Parses multi-word song titles cleanly and integrates with a standalone music library module to open YouTube links without crashing on missing keys.
- **Robust Driver Handling:** Tailored to bypass standard `pyttsx3` event-loop lockups and microphone warmup lags by forcing asynchronous COM streams.

## 🛠️ Tech Stack & Libraries
- **Language:** Python 3.12+
- **Speech Recognition:** `speech_recognition` (Google Web Speech API integration)
- **Audio Engine:** `pyaudio` (Hardware stream interfacing)
- **Text-to-Speech:** `win32com.client` (Native Windows SAPI.SpVoice automation)

## 🧠 Challenges Overcome (Engineering Logs)
1. **The Audio Lockup Bug:** Initially, standard cross-platform libraries caused silent failures. Solved this by hooking directly into the Windows native COM interface with asynchronous execution flags to prevent script freezes.
2. **The Sentence Splitting Defect:** Upgraded string array index slicing to a robust substring replacement pipeline (`command.replace("play", "")`), enabling the parsing of multi-word song titles safely.

## Status
🚧 under Development

## 🔮 Future Roadmap (AI/ML Upgrades)
- [ ] Replace strict `if/elif` rule-based blocks with an LLM pipeline (Gemini API Integration) for intent classification.
- [ ] Transition from cloud-dependent Google Speech API to a local, open-source Speech-to-Text model (OpenAI Whisper).
- [ ] Build an interactive visual dashboard interface using Web Development technologies (HTML/CSS/JavaScript).