RAG-Based AI Teaching Assistant 
=====================================================

This project implements a **Retrieval-Augmented Generation (RAG)**–based **AI Teaching Assistant** for any youtube video course.It automatically converts lecture videos into structured knowledge and answers student questions **strictly grounded in the lecture content**.

The system is designed for **academic use**, **learning support**, and **project demonstrations**, with a strong focus on **accuracy, explainability, and hallucination control**.

Key Features
------------

*   Automatic YouTube playlist video download
    
*   Video → Audio conversion using FFmpeg
    
*   Speech-to-text transcription using **OpenAI Whisper (large-v2)**
    
*   Timestamped chunking of lecture content
    
*   Semantic embeddings using **BAAI/bge-m3**
    
*   Cosine similarity–based semantic retrieval
    
*   RAG-based answering using **Google Gemini**
    
*   Hallucination-safe answers (lecture-only knowledge)
    

Important Execution Notes (Must Read)
-------------------------------------

### Local vs Google Colab

This project is **computationally heavy** due to:

*   Whisper **large-v2** model
    
*   High-dimensional embedding generation
    
*   Large audio/video processing
    

**Running locally on CPU is extremely slow and NOT recommended.**

**Recommended Environment: Google Colab with GPU**

To enable GPU in Colab:

`   Runtime → Change runtime type → GPU   `

Using Colab with GPU significantly improves:

*   Transcription speed
    
*   Embedding generation time
    
*   Overall pipeline performance
    

Notebook Usage Options
----------------------

### Option 1: All-in-One Execution (Best for Demo)

If you want to see the **entire pipeline in a single place**, use:

`   All_in_one.ipynb   `

This notebook includes:

*   Environment setup
    
*   Video download
    
*   Audio extraction
    
*   Transcription & chunking
    
*   Embedding creation
    
*   Retrieval
    
*   Gemini-based RAG answering
    

**Running only this file is enough to see the full project working end-to-end.**

### Option 2: Modular Execution (Best for Learning & Debugging)

For better understanding and modular design, the project is also split into **separate notebooks**:

```  
01_setup.ipynb
02a_auto_video_download.ipynb
02_video_to_audio.ipynb
03_audio_to_json.ipynb
04_embeddings.ipynb
05_retrieval.ipynb
06_rag_gemini.ipynb

  ```

**Each notebook focuses on one clear stage** **Easy to debug, modify, or extend**

**Ideal for academic evaluation and presentations**

System Architecture
-------------------


YouTube Playlist  
↓  
Video Download  
↓  
Video → Audio  
↓  
Whisper Transcription  
↓  
Embeddings  
↓  
Top-K Retrieval  
↓  
Gemini RAG Answer  

Project Directory Structure
---------------------------

  ```
RAG_BAS_PROJECT/
├── All_in_one.ipynb
├── 01_setup.ipynb
├── 02_video_to_audio.ipynb
├── 03_audio_to_json.ipynb
├── 04_embeddings.ipynb
├── 05_retrieval.ipynb
├── 06_rag_gemini.ipynb
├── VIDEOS/
├── AUDIOS/
├── jsons/
├── embeddings.csv
├── top_k.json
├── user_question.json
└── response.txt
```


Notebook Descriptions
---------------------

### **01\_setup.ipynb**

*   Mounts Google Drive
    
*   Installs required libraries
    
*   Creates project directory structure
    

### **02\_video\_to\_audio.ipynb**

*   Downloads lecture videos from a YouTube playlist using yt-dlp
    
*   Converts videos to audio (.mp3) using ffmpeg
    

### **03\_audio\_to\_json.ipynb**

*   Uses **OpenAI Whisper (large-v2)** for transcription
    
*   Splits audio into **timestamped chunks**
    
*   Stores output as structured JSON files
    

**Chunk Format:**

```
   {
       "Number": "01",  
        "Title": "Introduction to Signals",  
        "Start": 12.4,
        "End": 21.8,   
        "Text": "A signal is a function that conveys    information..." 

      }   
```

### **04\_embeddings.ipynb**

*   Converts text chunks into embeddings using **BAAI/bge-m3**
    
*   Stores embeddings + metadata in a **CSV file**
    
*   Embeddings are normalized for cosine similarity
    

### **05\_retrieval.ipynb**

*   Takes **user question input (only once)**
    
*   Encodes the query using the same embedding model
    
*   Computes cosine similarity against all chunks
    
*   Selects **Top-K most relevant chunks**
    
*   Saves:
    
    *   top\_k.json (retrieved chunks)
        
    *   user\_question.json (user query)
        

### **06\_rag\_gemini.ipynb**

*   Loads retrieved chunks and saved user question
    
*   Builds a **strict RAG prompt**
    
*   Uses **Google Gemini** only for reasoning
    
*   Generates:
    
    *   Simple, student-friendly answer
        
    *   Exact lecture references (title, number, timestamps)
        
*   Saves final answer to response.txt
    

 User Interaction Flow
------------------------

1.  User runs 05\_retrieval.ipynb
    
2.  User enters a question **once**
    
3.  Relevant lecture chunks are retrieved and saved
    
4.  User runs 06\_rag\_gemini.ipynb
    
5.  AI generates a grounded answer automatically
    

No repeated inputs Works across separate Colab notebooks

Hallucination Control Strategy
------------------------------

*   The AI **never uses external knowledge**
    
*   Answers are generated **only from retrieved lecture chunks**
    
*   If the topic is not covered, the system responds:
    

> _"This question is not covered in the provided lectures."_

This ensures **academic reliability and trustworthiness**.

Example
-------

**User Question:**

> What is a continuous-time signal?

**AI Answer Includes:**

*   Simple explanation
    
*   Lecture title and number
    
*   Exact start & end timestamps
    

Technologies Used
-----------------

*   Python
    
*   Google Colab
    
*   OpenAI Whisper
    
*   Sentence Transformers (BAAI/bge-m3)
    
*   Scikit-learn
    
*   Google Gemini API
    
*   yt-dlp
    
*   FFmpeg
    

Features
--------

*   Timestamp-level retrieval
    
*   Lecture-aware answers
    
*   Student-friendly explanations
    
*   Lightweight CSV-based vector store
    
*   Fully modular pipeline
    

Dataset Source
--------------

Neso Academy – Signals & Systems (YouTube Playlist) Used strictly for educational purposes

Future Scope & Enhancements
---------------------------

This RAG-based AI Teaching Assistant has strong potential for scalability, real-world deployment, and academic impact. The following enhancements can significantly extend its capabilities:

### 1\. Scalability Improvements

*   Replace CSV-based embedding storage with vector databases such as **FAISS, ChromaDB, or Pinecone**
    
*   Support thousands of lectures and multi-course datasets
    
*   Enable faster and more accurate semantic retrieval
    

### 2\. Advanced Retrieval Techniques

*   Hybrid search (semantic + keyword-based retrieval)
    
*   Cross-encoder or reranker models for improved relevance
    
*   Overlapping and topic-aware chunking strategies
    

### 3\. Expanded Subject Coverage

*   Extend beyond Signals & Systems to other domains such as:
    
    *   Machine Learning
        
    *   Physics
        
    *   Mathematics
        
    *   Medical and Law education
        
*   Create a multi-course AI tutor system
    

### 4\. Multilingual & Accessibility Support

*   Automatic translation of lecture transcripts
    
*   Support for queries in regional and international languages
    
*   Improved accessibility for diverse learners
    

### 5\. Deployment & Productization

*   Develop a **web-based interface** using Streamlit or React
    
*   Backend API using FastAPI
    
*   Cloud deployment using Docker and Kubernetes
    
*   Mobile application for on-the-go learning
    

### 6\. AI Model Enhancements

*   Use faster transcription models like WhisperX or Faster-Whisper
    
*   Fine-tune embeddings and LLM prompts for educational accuracy
    
*   Add hallucination control and answer verification mechanisms
    

### 7\. Educational & Research Applications

*   Intelligent tutoring systems with personalized learning paths
    
*   Learning analytics based on student queries
    
*   Research in AI-assisted education and video-based learning
    

### 8\. Commercial & Industry Applications

*   AI-powered tutor for online learning platforms
    
*   Smart video search engine for long educational videos
    
*   Licensing solutions for universities and coaching institutes
    

This project can evolve into a **scalable, timestamp-aware AI educational assistant** that transforms how students interact with video-based learning content.