# 🚀 API Geradora de Nomes

## 📌 Descrição
A **API Geradora de Nomes** é uma aplicação desenvolvida com **FastAPI** que permite gerar nomes aleatórios, nomes completos e nomes categorizados por gênero.  
Ela foi estruturada de forma modular para facilitar a manutenção e escalabilidade.

---

## 📂 Estrutura do Projeto
api_gera_nomes 
├── app/ │ 
├── init.py │ ├── main.py │ ├── routes/ │ │ ├── init.py │ │ ├── nomes.py │ ├── services/ │ │ ├── init.py │ │ ├── gerador_nomes.py │ ├── data/ │ │ ├── init.py │ │ ├── nomes_data.py ├── requirements.txt ├── README.md
- `routes/nomes.py` → Contém os endpoints da API.
- `services/gerador_nomes.py` → Lógica de geração de nomes.
- `data/nomes_data.py` → Lista fixa de nomes masculinos, femininos e sobrenomes.

---

## 🛠️ Configuração do Ambiente

### 1️⃣ Criar e Ativar o Ambiente Virtual
```bash
python -m venv venv

Windows:

venv\Scripts\activate

Linux/Mac:

source venv/bin/activate