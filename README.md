# MyGPT
RAG (Retrieval-Augmented Generation) Project with LangChain and Ollama

## Description

MyGPT is a full-stack RAG system that combines document retrieval with AI-powered text generation. Built with LangChain and Ollama, it provides a chat interface with contextual responses based on your document corpus.

### Key Features

- RAG-based conversational AI using LangChain
- Local LLM inference with Ollama
- Vector database with ChromaDB
- React-based web interface
- Discord & Slack bot integration
- Admin panel for data management
- Conversation history management

## Tech Stack

### Backend
- **FastAPI** - Modern web framework
- **LangChain** - LLM orchestration
- **Ollama** - Local LLM inference
- **ChromaDB** - Vector database
- **Unstructured** - Document processing

### Frontend
- **React 18** - UI framework
- **React Router** - Navigation
- **Modern JavaScript** (ES6+)

### Integration
- Discord Bot
- Slack Bot

## Project Structure

```
MyGPT/
├── backend/
│   ├── app/
│   │   ├── config.py              # Configuration
│   │   ├── main.py                # FastAPI app
│   │   ├── models/                # Data models
│   │   ├── routers/               # API routes
│   │   ├── services/              # Business logic
│   │   └── utils/                 # Utilities
│   ├── bot/
│   │   ├── discord_bot.py         # Discord integration
│   │   └── slack_bot.py           # Slack integration
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/            # React components
│   │   ├── routes/                # Route configuration
│   │   └── App.js                 # Main app
│   └── package.json
├── scripts/                       # Utility scripts
├── test/                          # Test files
└── docker-compose.yml
```

## Setup

### Requirements
- Docker & Docker Compose
- Python 3.9+
- Node.js 16+ (for local development)
- Ollama installed locally

### Installation

1. Clone the repository
```bash
git clone https://github.com/herbpot/MyGPT.git
cd MyGPT
```

2. Create environment file
```bash
cp .env.example .env
# Edit .env with your configuration
```

3. Start with Docker Compose
```bash
docker-compose up --build
```

The application will be available at:
- Backend API: `http://localhost:8000`
- Frontend UI: Check docker-compose.yml for port configuration

### Local Development

#### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

#### Frontend
```bash
cd frontend
npm install
npm start
```

## API Endpoints

- `POST /query` - Submit queries to the RAG system
- `GET /admin` - Access admin panel
- Additional endpoints in routers directory

## Configuration

Edit `.env` file to configure:
- Ollama model settings
- ChromaDB connection
- API keys for Discord/Slack bots
- Other application settings

## Usage

1. Upload documents through the admin panel
2. Documents are processed and stored in ChromaDB
3. Ask questions in the chat interface
4. Receive contextual answers based on your documents

## Bot Integration

### Discord Bot
Configure Discord bot token in `.env` and run:
```bash
python backend/bot/discord_bot.py
```

### Slack Bot
Configure Slack credentials in `.env` and run:
```bash
python backend/bot/slack_bot.py
```

## Testing

```bash
cd frontend
npm test
