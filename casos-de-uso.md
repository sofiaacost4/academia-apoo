# Caso de Uso 009: Fazer inscrição

## Autor: Maria Helena C. de Medeiros

## 1. Resumo

Este caso de uso permite que um aluno realize sua inscrição em uma aula oferecida pela instituição. O gestor também pode efetuar inscrições em nome do aluno, por exemplo, em casos administrativos ou de suporte.

---

## 2. Atores

- Aluno  
- Gestor

---

## 3. Pré-condições

- O aluno deve estar matriculado no sistema;  
- O gestor deve estar autenticado com permissões administrativas;  
- A aula deve estar disponível para inscrição (com vagas abertas).

---

## 4. Pós-condições

- O aluno estará inscrito na aula selecionada;  
- A quantidade de vagas disponíveis na aula será atualizada.

---

## 5. Fluxos de Evento

### 5.1 Fluxo Básico (Aluno)

1. O aluno acessa o sistema e se autentica;  
2. O aluno navega até a seção de aulas disponíveis;  
3. O sistema exibe a lista de aulas com vagas abertas;  
4. O aluno seleciona a aula desejada;  
5. O sistema verifica a disponibilidade de vaga;  
6. O sistema realiza a inscrição do aluno;  
7. O sistema confirma a inscrição com uma mensagem ao aluno.

### 5.2 Fluxo Alternativo (Gestor)

1. O gestor autentica-se no sistema;  
2. O gestor acessa a área administrativa de inscrições;  
3. O gestor busca o aluno pelo nome ou pela matrícula;  
4. O gestor seleciona o aluno e a aula desejada;  
5. O sistema verifica a disponibilidade de vagas;  
6. O sistema efetua a inscrição em nome do aluno;  
7. O sistema confirma a inscrição ao gestor.

### 5.3 Fluxo de Exceção

1. **Aula não possui mais vagas disponíveis:**  
   - O sistema informa que não é possível realizar a inscrição.

2. **Aula inexistente ou removida:**  
   - O sistema exibe mensagem de erro.

3. **O aluno não é habilitado para a aula (pré-requisitos não atendidos):**  
   - O sistema bloqueia a inscrição e exibe justificativa.

# Caso de Uso 0010: Ver Inscrição

## 1. Resumo

Permite que o aluno visualize as informações de sua inscrição em uma aula específica, 
incluindo detalhes como data, horário, disciplina, professor e local.

---

## 2. Atores

- Aluno 

---

## 3. Pré-condições

- O aluno deve estar matriculado no sistema; 
- O aluno deve possuir ao menos uma inscrição em aula registrada no sistema (exceto se 
o sistema for projetado para mostrar uma lista vazia com a opção de buscar novas 
aulas). 

---

## 4. Pós-condições

-  As informações da inscrição são exibidas corretamente na tela; 
-  Nenhum dado é alterado. 

---

## 5. Fluxos de Evento

### 5.1 Fluxo Básico (Aluno)

1. O aluno acessa o sistema e escolhe a opção “Minhas Inscrições” ou semelhante no menu;  
2. O sistema exibe a lista de aulas em que o aluno está inscrito;  
3. O aluno seleciona uma das aulas para visualizar os detalhes;  
4. O sistema exibe as informações completas da inscrição, como:  
   a. Nome da modalidade;  
   b. Código da modalidade;  
   c. Professor responsável;  
   d. Data e horário;  
   e. Local de aula;  
   f. Situação da inscrição: ativa, cancelada etc. 

### 5.2 Fluxo Alternativo (Gestor)

1. O sistema informa que o aluno não possui nenhuma inscrição ativa no momento;

### 5.3 Fluxo de Exceção

1. **Falha na conexão com o sistema:**  
   - O sistema não consegue se conectar ao banco de dados, exibindo uma mensagem de erro.

2. **Sessão expirada:**  
   - O sistema redireciona o aluno para a tela de login.

3. **Falha na autorização (usuário sem permissão):**  
   - Um usuário tenta acessar o recurso sem o perfil de aluno; o sistema bloqueia o acesso.

# Caso de Uso 0012: Remover Inscrição

## 1. Resumo

Permite que o aluno remova sua prória inscrição em uma aula ou que um gestor remova a inscrição de um aluno, quando necessário.

---

## 2. Atores

- Aluno 
- Gestor

---

## 3. Pré-condições

- O usuário, aluno ou gestor, deve estar autenticado no sistema;
- Deve haver, pelo menos, uma inscrição ativa registrada para ser removida;
- O período de cancelamento (se existir) deve ser aberto, ou o gestor deve ter permissão especial para forçar a remoção. 

---

## 4. Pós-condições

-  A inscrição é removida com sucesso do sistema (ou marcada como cancelada, dependendo da lógica de negócio);
- O aluno não está mais vinculado à aula. 

---

## 5. Fluxos de Evento

### 5.1 Fluxo Básico (Aluno ou gestor)

1. O usuário acessa a tela de inscrições; 
2. O sistema exibe a lista de inscrições ativas; 
3. O usuário seleciona uma inscrição a ser removida; 
4. O sistema solicita uma confirmação da ação; 
5. O usuário confirma a remoção; 
6. O sistema remove a inscrição (ou marca como cancelada);  
7. O sistema exibe mensagem de sucesso. 

### 5.2 Fluxo Alternativo (Gestor, em nome do aluno)

1. O gestor acessa a área administrativa de inscrições; 
2. Ele localiza o aluno e seleciona a inscrição a ser removida; 
3. O fluxo segue a partir do passo 4 do fluxo principal. 

### 5.3 Fluxo de Exceção

1. Inscrição não encontrada; 
a. O usuário tenta remover uma inscrição que já foi cancelada ou não existe mais. 
2. Prazo de cancelamento expirado (para aluno); 
a. O aluno tenta remover uma inscrição fora do prazo permitido.. 
3. Falha na conexão ou erro técnico; 
a. O sistema falha ao tentar remover a inscrição (problema no banco de dados ou 
falha interna). 
