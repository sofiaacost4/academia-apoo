# Descrição das classes

## Autora: Sofia Costa Kunzler

## Pessoa
Classe genérica que representa os dados comuns aos usuários do sistema (alunos, instrutores e gestores).

- **Atributos**:
  - `nome`: nome completo da pessoa;
  - `email`: endereço eletrônico de contato;
  - `telefone`: número de telefone para contato;
  - `cpf`: Cadastro de Pessoa Física (identificador único).

---

## Aluno
Representa os alunos cadastrados no sistema.  
Eles podem realizar inscrições em aulas e visualizar seus pagamentos efetuados.

---

## Instrutor
Representa os instrutores responsáveis por ministrar as aulas da academia.  
Cada instrutor pode estar associado a uma ou mais especialidades.

---

## Gestor
Responsável pela administração geral do sistema.  
O gestor tem permissões para:

- Realizar cadastros de alunos, horários, especialidades e perfis;
- Alocar instrutores nas aulas;
- Gerenciar pagamentos;
- Inscrever alunos em aulas;
- Listar e consultar horários e inscrições.

---

## Perfil
Representa os dados de acesso ao sistema para qualquer tipo de usuário (aluno, instrutor ou gestor).

- Cada aluno, instrutor ou gestor possui um único perfil.
- O gestor é o responsável por criar e gerenciar os perfis.

---

## Especialidade
Define a área de atuação específica de um instrutor, como:  
*Musculação, Yoga, Pilates, Crossfit*, entre outras.

---

## Horário
Define o horário em que uma determinada aula ocorre.  
Cada aula possui exatamente um horário associado.

- **Atributos**:
  - `dia_semana`: dia da semana em que a aula acontece;
  - `dt_inicio`: data e hora de início da aula;
  - `dt_fim`: data e hora de término da aula.

---

## Aula
Representa uma sessão de atividade física oferecida no sistema.  
Cada aula está associada a:

- Um instrutor;
- Um horário;
- Diversos alunos inscritos.

---

## Inscrição
Representa o ato de um aluno se inscrever em uma aula.  
Essa inscrição pode ser feita pelo próprio aluno ou por um gestor.

- **Atributos**:
  - `aula`: referência à aula escolhida;
  - `aluno`: referência ao aluno inscrito.

---

## Pagamento
Representa o pagamento associado a uma inscrição realizada por um aluno ou por um gestor.

- **Atributos**:
  - `status`: indica a situação do pagamento (ex: pago, em andamento, cancelado);
  - `valor`: valor da inscrição.