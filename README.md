# API Flask - Legendary Octo Robot

Uma API Flask simples e funcional para ser deployada no Render.

## Instalação Local

### 1. Clonar o repositório
```bash
git clone https://github.com/LAION1986/legendary-octo-robot.git
cd legendary-octo-robot
```

### 2. Criar ambiente virtual
```bash
python -m venv venv
```

### 3. Ativar ambiente virtual

**No Windows:**
```bash
venv\Scripts\activate
```

**No macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Instalar dependências
```bash
pip install -r requirements.txt
```

### 5. Executar a API localmente
```bash
python app.py
```

A API estará disponível em: `http://localhost:5000`

## Endpoints da API

### 1. GET / - Página Inicial
```bash
curl http://localhost:5000/
```

### 2. GET /health - Verificar Saúde da API
```bash
curl http://localhost:5000/health
```

### 3. GET /api/data - Obter Dados de Exemplo
```bash
curl http://localhost:5000/api/data
```

### 4. POST /api/echo - Ecoar Dados
```bash
curl -X POST http://localhost:5000/api/echo \
  -H "Content-Type: application/json" \
  -d '{"mensagem": "Olá API!"}'
```

## Deploy no Render

### Passos:

1. **Fazer push das alterações para o GitHub:**
   ```bash
   git add .
   git commit -m "Adicionar API Flask"
   git push origin main
   ```

2. **Criar um novo Web Service no Render:**
   - Acesse https://dashboard.render.com/
   - Clique em "New +" → "Web Service"
   - Conecte seu repositório GitHub
   - Configure:
     - **Name:** legendary-octo-robot
     - **Environment:** Python 3
     - **Build Command:** `pip install -r requirements.txt`
     - **Start Command:** `python app.py`
     - **PORT:** 5000

3. **Deploy e Pronto!** 🎉

Sua API estará disponível em uma URL como: `https://legendary-octo-robot.onrender.com`

## Estrutura do Projeto

```
legendary-octo-robot/
├── app.py              # Código principal da API
├── requirements.txt    # Dependências do projeto
├── venv/              # Ambiente virtual (não fazer commit)
├── .gitignore         # Arquivos ignorados pelo Git
└── README.md          # Este arquivo
```

## Testando a API no VS Code

### Extensão recomendada: REST Client

1. Instale a extensão "REST Client" no VS Code
2. Crie um arquivo `test.http`:

```http
### Teste Health Check
GET http://localhost:5000/health

### Teste Data
GET http://localhost:5000/api/data

### Teste Echo
POST http://localhost:5000/api/echo
Content-Type: application/json

{
  "mensagem": "Olá do VS Code!"
}
```

3. Clique em "Send Request" para testar cada endpoint

## Próximos Passos

- Adicionar mais rotas conforme necessário
- Implementar autenticação (JWT)
- Conectar a um banco de dados
- Adicionar testes automatizados
- Implementar CORS se necessário

---

**Desenvolvido com ❤️ por LAION1986**
