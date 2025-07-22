# Projeto de Automação de Testes API - Lojinha

Automação de testes para APIs do sistema **Lojinha**, utilizando Python, Requests, Pytest e o padrão **API Model** para organização e reuso de código. Este projeto garante validação de endpoints de autenticação, operações CRUD e consistência nas respostas.

## Sobre o Projeto
Este repositório implementa automação de testes para os endpoints da API **Lojinha**.  
Apliquei o design pattern **API Model**, que separa as chamadas de API em classes organizadas, facilitando:  
✅ Reutilização de código  
✅ Manutenção dos testes  
✅ Leitura e entendimento da estrutura do projeto

## Ferramentas e Tecnologias Utilizadas
- [Python 3.x](https://www.python.org/)
- [Requests](https://pypi.org/project/requests/)
- [Pytest](https://docs.pytest.org/)
- [Logging](https://docs.python.org/3/library/logging.html)
- **API Model (Design Pattern)**

##  Passo a passo para rodar o projeto: 
1. **Clone o repositório**
2. **Crie e ative um ambiente virtual e ative:**
python -m venv venv
venv\Scripts\Activate.ps1
3. **Instale as Dependências:**
pip install -r requirements.txt
