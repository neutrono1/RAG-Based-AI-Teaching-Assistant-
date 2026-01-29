# RAG-Based AI Teaching Assistant 

This project is a **Retrieval-Augmented Generation (RAG) based AI Teaching Assistant** built using **Signals & Systems lectures from Neso Academy (YouTube)**.

The system allows a student to ask a question and automatically:
- Finds **which lecture** the concept appears in
- Identifies the **exact timestamp (start–end)**
- Retrieves the **relevant transcript text**
- Generates a **simple student-friendly explanation**
- Mentions **Lecture Title, Lecture Number, and Duration**

---

##  Project Workflow

1. **Download YouTube lecture videos automatically**
2. **Convert videos to audio (.mp3)**
3. **Transcribe audio using OpenAI Whisper**
4. **Split transcript into timestamped chunks**
5. **Generate embeddings using Sentence Transformers**
6. **Store embeddings in CSV**
7. **Use cosine similarity to retrieve relevant chunks**
8. **Use Gemini API to generate final RAG-based answer**
9. **Save the AI response to a text file**

---

## Project Structure

```text
RAG_BAS_PROJECT/
├── download_videos_YT.py        # Download first 15 YouTube lectures
├── video_to_mp3.py              # Convert videos to MP3 audio
├── collab_file.ipynb            # Transcription, embeddings,
|                                  RAG pipeline
├── embeddings.csv               # Stored vector embeddings
├── response.txt                 # Final AI-generated answer
├── VIDEOS/                      # (Empty) Place downloaded videos here
├── AUDIOS/                      # (Empty) Place extracted MP3 files here
├── jsons/                         # all the json file which store the chunks and text 
└── README.md
```

>  `VIDEOS` and `AUDIOS` folders are intentionally empty in GitHub.  
> They will be populated automatically when scripts are executed.

---

##  Requirements

### Local Machine
- Python 3.9+
- ffmpeg (must be installed and added to PATH)
- Node.js (required by `yt-dlp`)

### Python Libraries
yt-dlp,
openai-whisper,
sentence-transformers,
torch,
pandas,
numpy,
scikit-learn,
google-generativeai,


---

##  Step 1: Download YouTube Lectures

Downloads the **first 15 videos** from Neso Academy Signals & Systems playlist.


python download_videos_YT.py
Videos will be saved inside:

VIDEOS/
##  Step 2: Convert Videos to Audio
Convert .mp4 lecture videos into .mp3 audio files.

python video_to_mp3.py
Output:
```
AUDIOS/
├── 1_LectureName.mp3
├── 2_LectureName.mp3
```
...
 ## Step 3: Transcription & RAG Pipeline (Google Colab)
* Open collab_file.ipynb in Google Colab.

### What this notebook does:
* Installs Whisper

* Transcribes each MP3 into timestamped text chunks

* Saves transcripts as JSON

* Generates embeddings using BAAI/bge-m3

* Stores embeddings in embeddings.csv

* Takes user question input

* Retrieves top relevant chunks using cosine similarity

* Generates final answer using Gemini API

* Saves output to response.txt

###  Gemini API Setup (Required)
In Google Colab:

Go to Runtime → Manage Secrets

Add:
```
GOOGLE_API_KEY = your_api_key_here
```

### Example Query
```
Ask Any Question:
What is convolution in continuous-time signals?
Output (response.txt)
Simple explanation

Lecture Title

Lecture Number

Start & End Time
```
## Features
* Timestamp-level retrieval

* Lecture-aware answers

* Student-friendly explanations

* Lightweight CSV-based vector store

* Fully modular pipeline

##  Dataset Source
Neso Academy – Signals & Systems (YouTube Playlist)
Used strictly for educational purposes

##  Future Improvements
* Replace CSV with FAISS / ChromaDB
* Add Streamlit or Web UI
* Support more subjects
* Add multi-language support,
* Deploy as an API
