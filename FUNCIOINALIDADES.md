# Gerenciador LL — Documentação de Funcionalidades

## Sobre o Produto
Gerenciador de arquivos inteligente para Windows com organização automática,
limpeza, segurança e assistente IA integrado.

**Desenvolvido por:** Luis Leal
**GitHub:** github.com/luiisocl/GERENCIADOR-LL  
**Versão:** 1.0.0

---

## Planos

| Plano | Preço | Descrição |
|---|---|---|
| **Gerenciador LL** | R$ 20,00 (único) | Todas as funcionalidades base |
| **Premium Mensal** | R$ 19,90/mês | Tudo + Assistente IA |
| **Premium Vitalício** | R$ 97,00 (único) | Tudo + Assistente IA para sempre |

---

## Funcionalidades

### 📊 Dashboard
- Painel principal com estatísticas em tempo real
- Total de arquivos, duplicatas, esquecidos e espaço livre
- Lista de arquivos recentes com nome, tipo, tamanho e data
- Visual moderno com tema escuro

### 📁 Organização Automática
- Seleciona qualquer pasta do computador
- Analisa e lista todos os arquivos com nome, tipo e tamanho
- Organiza automaticamente em subpastas por tipo:
  Imagens, Documentos, Vídeos, Músicas, Programas, Compactados, Outros
- Confirmação obrigatória antes de mover qualquer arquivo

### 🔍 Buscador Inteligente
- Busca arquivos em qualquer pasta e subpastas
- Busca por nome ou extensão (ex: .pdf, foto)
- Exibe nome, caminho completo e tamanho
- Resultados em tempo real com contador

### 👥 Detector de Duplicatas
- Analisa pasta e subpastas em busca de arquivos idênticos
- Usa algoritmo MD5 para comparação por conteúdo
- Otimizado: compara tamanho antes do hash para maior velocidade
- Mostra arquivo duplicado e arquivo original
- Calcula espaço total ocupado pelas duplicatas
- Exclusão com confirmação obrigatória
- Processamento em segundo plano sem travar a interface

### 💤 Arquivos Esquecidos
- Encontra arquivos sem uso há 180, 365, 730 ou 1825 dias
- Filtro de período ajustável com atualização automática da lista
- Ordena pelos mais esquecidos primeiro
- Mostra quantidade de dias sem acesso
- Aviso automático para pastas maiores que 20GB
- Ignora pastas do sistema automaticamente
- Exclusão com confirmação obrigatória

### 🧹 Limpeza Rápida
- Analisa pastas temporárias do Windows automaticamente
- Exibe arquivos temporários com nome, caminho e tamanho
- Mostra total de arquivos e espaço ocupado
- Limpeza com confirmação obrigatória
- Exibe espaço liberado após limpeza

### 🔐 Cofre de Arquivos
- Proteção de arquivos sensíveis com senha
- Criptografia real com algoritmo Fernet (AES 128-bit)
- Senha transformada em chave criptográfica com PBKDF2HMAC
- Arquivos ficam ilegíveis sem a senha correta
- Restauração do arquivo para o local original
- Arquivos originais removidos após entrada no cofre

### 🕒 Histórico de Ações
- Em desenvolvimento

### 🤖 Assistente IA (Premium)
- Chat em linguagem natural para gerenciar arquivos
- Em desenvolvimento

### 🎨 Interface
- Tema escuro moderno
- Menu lateral organizado por categorias
- Barra de progresso animada nas operações pesadas
- Processamento em segundo plano com threading
- Adaptável a qualquer tamanho de monitor
- Tamanho mínimo garantido de 900x600px

### 🔒 Segurança
- Nenhuma ação executada sem confirmação do usuário
- Criptografia real no cofre de arquivos
- Senhas nunca salvas em texto puro

---

## Tecnologias Utilizadas
- **Python 3.14**
- **CustomTkinter** — Interface gráfica moderna
- **cryptography** — Criptografia do cofre
- **hashlib** — Hash MD5 para duplicatas e SHA256 para senhas
- **threading** — Processamento em segundo plano
- **os / shutil** — Manipulação de arquivos

---

## Plataformas de Venda
- Hotmart
- Gumroad