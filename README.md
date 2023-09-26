# Sistema de Gestão de Estabelecimento

_Dando início ao Side Project de um Sistema de Gestão de Estabelecimento, com foco no controle de estoque, visualização de vendas e desempenho geral (Dashboard) e controle de datas de validade. O foco é o Mercado FEFO, onde tenho experiência e onde a dinamicidade das vendas demanda agilidade e informações claras._

## FEFO

Sigla para _"First Expired First Out"_, ou seja, entre os produtos do estoque **o primeiro em ordem de validade é o primeiro a sair para a área de vendas**. É um mercado em ascensão nas áreas de comunidade, devido ao baixo valor que os produtos de data curta (FEFO) adquirem no grande mercado. Geralmente as grandes indústrias dão vazão a esses produtos dentro desses mercados comunitários, para não gerar perdas. Como a tendência da superprodução é o desperdício, esses pólos de mercantilização também servem a uma vez como espaços de acesso a alimentos e vias de recuperação do que seria facilmente descartado pela grande indústria alimentícia.

### Objetivo

Construir um ERP modular com interface amigável ao usuário, um sistema de gerenciamento de FEFO em módulos, de modo que possa atender o pequeno e o médio empreendedor, buscando também incentivar a formação de cooperativas de desenvolvimento de código em sinergia com cooperativas de comércio de alimentos.

<img height="400" style="border-radius:50px;" src="https://res.cloudinary.com/petraiosklytometis/image/upload/v1694380215/Beige_Minimalist_Financial_Plan_Dashboard_Graph_1_dzakk7.gif">

### 🏁 Features

- [x] Cadastro de Usuário
- [x] Cadastro de Produto
- [ ] Cadastro de Empresa
- [x] Cadastro de Vendedor
- [x] Listagem de Produtos
- [ ] Listagem de Empresa
- [ ] Listagem de Gerentes
- [ ] Data de Validade
- [ ] Controle de Vencimentos
- [ ] Deletar Produto
- [ ] Desativar Empresa
- [x] Deletar Vendedor
- [x] Login
- [ ] Reset de senha
- [ ] PDF com as informações das movimentações do mês
- [ ] Acessando Informações Filtradas

### 🧾 Detalhamento do Produto

- [x] Nome do produto (até 100 caracteres)
- [ ] Código do produto (para identificação)
- [x] Código de Barras (EAN)
- [x] Categoria de Classificação do Produto
- [x] Valor de Venda
- [ ] Custo Médio (habilitado apenas se o estoque for maior que 1)
- [x] Estoque Disponível
- [ ] Estoque Mínimo
- [ ] Estoque Máximo
- [ ] Configurar notificações por e-mail quando o estoque atingir o mínimo ou máximo.
- [x] Permitir entrada ou saída de produtos no estoque.
- [ ] Origem do Produto (código conforme a legislação)
- [ ] Tipo do Produto (para definir alíquotas de impostos)
- [ ] NCM (Nomenclatura Comum do Mercosul para nota fiscal)
- [ ] CEST (Código Especificador da Substituição Tributária)
- [ ] Unidade de Medida (na nota fiscal)
- [ ] Observações (detalhes adicionais do produto)
- [ ] Peso Líquido (sem embalagem)
- [ ] Peso Bruto (com embalagem)

### 🛠 Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

- ![DJANGO](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
- ![BOOTSTRAP](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
- ![SQLITE](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
