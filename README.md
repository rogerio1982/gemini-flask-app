# Gemini + Flask + Docker

## Rodar localmente
```bash
docker build -t gemini-flask .
docker run -d -p 5000:5000 --env-file .env gemini-flask
```

## Teste
POST http://localhost:5000/chat
```json
{
  "prompt": "Explique o que é Docker"
}
```
