O programa utiliza três critérios clássicos de semelhança de triângulos:

1. **LAL (Lado-Ângulo-Lado):**
   - Se dois lados de um triângulo são proporcionais aos dois lados correspondentes de outro triângulo, e o ângulo entre esses lados é congruente, os triângulos são semelhantes.

2. **AA (Ângulo-Ângulo):**
   - Se dois ângulos de um triângulo forem congruentes aos dois ângulos correspondentes de outro triângulo, os triângulos são semelhantes.

3. **LLL (Lado-Lado-Lado):**
   - Se os três lados de um triângulo são proporcionais aos três lados correspondentes de outro triângulo, os triângulos são semelhantes.

## Como o Programa Funciona

1. **Entrada de Dados:**
   - O programa solicita ao usuário que insira os três lados e dois ângulos de cada triângulo.
   - Todos os lados e ângulos são obrigatórios para permitir que o programa verifique a semelhança automaticamente.

2. **Verificação Automática:**
   - O programa verifica automaticamente os três critérios de semelhança (LLL, LAL e AA) com base nas entradas fornecidas.
   - Ele começa verificando o critério **LLL** (mais restritivo), seguido por **LAL**, e por último o critério **AA**.

3. **Resultado:**
   - Se os triângulos forem semelhantes por qualquer um dos critérios, o programa imprime uma mensagem indicando qual critério foi atendido.
   - Se nenhum critério for atendido, o programa informa que os triângulos não são semelhantes.

