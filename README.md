<h1>Postpartum Depression Dataset</h1>
<p>Este repositório utiliza a base de dados "Postpartum Depression", disponível no Kaggle, para explorar e analisar fatores que podem estar associados à depressão pós-parto.</p>
<a href="https://www.kaggle.com/datasets/parvezalmuqtadir2348/postpartum-depression/data">Link para a base</a>
<h1>Atributos</h1>
<p>Os atributos contidos na base de dados incluem uma série de respostas a perguntas que avaliam o estado emocional, social e de saúde da mãe:</p>
<ul>
    <li><strong><code>Timestamp</code></strong>: Data e hora em que as respostas foram coletadas.</li>
    <li><strong><code>Age</code></strong>: Idade.</li>
    <li><strong><code>Feeling Sad or Tearful</code></strong>: Sentindo-se triste ou chorosa.</li>
    <li><strong><code>Irritable towards baby and partner</code></strong>: Irritabilidade com o bebê e o parceiro.</li>
    <li><strong><code>Trouble sleeping at night</code></strong>: Problemas para dormir à noite.</li>
    <li><strong><code>Problems concentrating or making decisions</code></strong>: Problemas para se concentrar ou tomar decisões.</li>
    <li><strong><code>Overeating or loss of appetite</code></strong>: Excesso ou perda de apetite.</li>
    <li><strong><code>Feeling anxious</code></strong>: Sentindo-se ansiosa.</li>
    <li><strong><code>Feeling of guilt</code></strong>: Sentimento de culpa.</li>
    <li><strong><code>Problems of bonding with baby</code></strong>: Problemas de criação de laços com o bebê.</li>
</ul>
<h2>Variável Alvo (<code>Feeling Anxious</code>)</h2>
<p>A variável alvo, denominada "feeling anxious", é a variável definida como preditora da depressão pós-parto.</p>
<ul>
        <li><strong><code>0</code></strong>: Indica a ausência de ansiedade.</li>
        <li><strong><code>1</code></strong>: Indica a presença de ansiedade.</li>
    </ul>
<h2>Justificativa do Trabalho: Diagnóstico da Depressão Pós-Parto com Machine Learning</h2>
<p>Este projeto propõe uma abordagem inovadora e complementar, utilizando algoritmos de Machine Learning para apoiar a equipe de saúde no diagnóstico. É importante frisar que esta ferramente é deve ser encarada como instrumento de apoio no diagnóstico e não devendo ser utilizada como ferramenta decisória autônoma. </p>
<h2>COMPARATIVO DOS MODELOS</h2>
<img width="1184" height="784" alt="Image" src="https://github.com/user-attachments/assets/4ef806b5-ae7d-4d4f-b5da-f2d710097ed4" />
<h2>Testando a API com Postman</h2>
<p>A imagem abaixo demonstra o uso do Postman para interagir com o endpoint de previsão da nossa API.</p>
<img width="1442" height="732" alt="Image" src="https://github.com/user-attachments/assets/760f5e07-e467-4fe7-a507-8a6287e863a8" />
<h2>Persistência dos dados no MongoDb</h2>
<p>Após a requisição à API, os dados do paciente e o resultado da previsão são persistidos em nosso banco de dados MongoDB. A imagem abaixo mostra o MongoDB Compass, uma ferramenta gráfica para interagir com o MongoDB, exibindo o registro recém-criado</p>
<img width="1920" height="587" alt="Image" src="https://github.com/user-attachments/assets/85baa433-ac19-418e-8db7-1ebb0a87d71a" />

