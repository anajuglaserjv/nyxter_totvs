import streamlit as st 
import requests 
import pandas as pd 
import io

# Configuração da página
st.set_page_config(
    page_title="Nyxter - Solução de Segmentação Inteligente",
    layout="wide",
    initial_sidebar_state="expanded"
) 

# Estilos CSS
st.markdown("""
<style>
/* Fundo branco para a aplicação toda */
.stApp {
    background-color: white; 
}

/* Esconde as bolinhas do st.radio */
.st-emotion-cache-1f06x6f .st-emotion-cache-k7vsyb {
    display: none;
}

/* Estilo do menu de navegação lateral (o seu "índice") */
/* Fundo cinza claro ao passar o mouse */
.st-emotion-cache-1f06x6f:hover {
    background-color: #f0f2f6; /* Fundo cinza claro */
    border-radius: 8px; /* Cantos arredondados */
}

/* Estilo para o item de menu SELECIONADO (fundo azul e texto branco) */
.st-emotion-cache-1f06x6f:has(input[type="radio"]:checked) {
    background-color: #3b5998; /* Fundo azul escuro */
    color: white; /* Texto branco */
    border-radius: 8px;
}

/* Estilo para o logo no canto superior direito */
.totvs-logo {
    position: fixed;
    top: 20px;
    right: 20px;
    z-index: 999; /* Garante que a logo fique acima de outros elementos */
}
</style>
""", unsafe_allow_html=True)

# Adiciona o logo da TOTVS fixo no canto superior direito
st.markdown(
    '<div class="totvs-logo">'
    '<img src="https://logodownload.org/wp-content/uploads/2014/05/totvs-logo-0.png" width="100">'
    '</div>',
    unsafe_allow_html=True
)

# ---- Sidebar da Aplicação ---
st.sidebar.image("logonyxter.png", width=150)
st.sidebar.markdown("---") 
# Opções de menu na sidebar
opcoes = ["Página Inicial", "Visão Geral", "Jornada do Cliente", "Análise RFM", "Clustering", "NyxterIA"] 
escolha = st.sidebar.radio("**Escolha o tema:**", opcoes)

# ---- Conteúdo Principal ----
if escolha == "Página Inicial":
    st.markdown("<h1 style='font-size: 50px; color: #0f2b6d;'>NYXTER</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='font-size: 34px; color: #dda53d;'>Cada cliente, uma jornada única. Cada jornada, um sucesso.</h2>", unsafe_allow_html=True) 
    st.markdown("---")
    
    # --- Seção: O Problema a ser Resolvido ---
    st.markdown("<h2 style='color: #092e86;'>O Desafio da Jornada do Cliente TOTVS</h2>", unsafe_allow_html=True)
    st.markdown("""
        A TOTVS atende um grande número de clientes de diversos segmentos, cada um com necessidades específicas e diferentes níveis de maturidade tecnológica. Isso torna a jornada do cliente complexa e desafiadora, dificultando a personalização do atendimento e a eficiência na implementação das soluções. 
    """)

    st.subheader("⚠️ Consequências da Falta de Segmentação")
    st.markdown("""
        Sem um modelo estruturado de segmentação, a experiência do cliente pode ser inconsistente, resultando em desafios como:
        
        * **Dificuldade na personalização:** Clientes com perfis distintos recebem o mesmo tratamento, reduzindo a efetividade das soluções.
        * **Processos morosos e pouco eficientes:** A falta de categorização adequada leva a etapas desnecessárias ou inadequadas para determinados grupos.
        * **Suporte e atendimento pouco otimizado:** Sem uma compreensão clara dos padrões de comportamento, o suporte pode ser reativo em vez de proativo.
    """)
    st.markdown("---")

    # --- Seção: A Solução Nyxter (já existente) ---
    
    st.markdown("<h2 style='color: #092e86;'>A Solução: Segmentação Inteligente NYXTER</h2>", unsafe_allow_html=True)
    st.markdown("""
        **Bem-vindo ao Nyxter,** a plataforma que transforma dados em inteligência de negócios. 🚀
                
        Diante da diversidade de perfis e segmentos atendidos pela TOTVS, nossa solução é baseada em **segmentação inteligente**, com foco na **otimização da jornada do cliente** por meio da **análise de dados comportamentais e padrões de consumo.**
    """)
    st.subheader("Nosso Processo")
    st.markdown("""
        O processo começa com o tratamento da base de dados da TOTVS através de um ETL 
        (Extração, Limpeza, Padronização e Cruzamento dos Dados). Com os dados estruturados, 
        aplicamos dois modelos de clusterização para gerar insights valiosos:

        
        - **Modelo 1 - Perfil de Consumo:** Agrupa clientes de acordo com os produtos 
          e soluções utilizados, viabilizando jornadas personalizadas de onboarding e suporte utilizando o algoritmo GMM.
        - **Modelo 2 - RFM (Recência, Frequência e Valor Monetário):** Segmenta clientes 
          com base no comportamento de compra para permitir estratégias direcionadas de 
          marketing e retenção.
    """)
    st.markdown("---")
    st.markdown("Explore as opções na barra lateral para ver os resultados das análises!")


elif escolha == "Visão Geral":
    st.markdown("<h1 style='color: #092e86;'>Visão Geral dos Clientes TOTVS</h1>", unsafe_allow_html=True)
    st.markdown("""
        Veja as princípais métricas de todos os seus clientes. Entenda seu comportamento.
    """)
    # Adicione este código no final da sua seção de "Jornada do Cliente"
    st.markdown("---")
    st.subheader("Veja nossas análises!")
    st.info("Acesse nosso painel completo no Power BI.")

    # URL do seu dashboard no Power BI - LINK ATUALIZADO
    powerbi_url = "https://app.powerbi.com/view?r=eyJrIjoiNGY2ZTMzY2EtM2ZhMS00MWY0LWFlOWUtZTc4MjdlMjhjZDMxIiwidCI6IjExZGJiZmUyLTg5YjgtNDU0OS1iZTEwLWNlYzM2NGU1OTU1MSIsImMiOjR9" 

    if st.button("Acessar o Dashboard Nyxter"):
        st.markdown(f'<a href="{powerbi_url}" target="_blank">Clique aqui para abrir o Dashboard</a>', unsafe_allow_html=True)

elif escolha == "Jornada do Cliente":
    st.markdown("<h1 style='color: #092e86;'>Jornada do Cliente</h1>", unsafe_allow_html=True)
    st.subheader("Análise de Perfil de Consumo")
    st.markdown("""
        Esta seção detalha a jornada do cliente TOTVS e mostra como nossos clusters se
        distribuem por essas etapas. A partir desta análise, é possível
        criar **jornadas personalizadas** e estratégias de retenção mais eficazes para cada grupo.
    """)

    # Adicione este código no final da sua seção de "Jornada do Cliente"
    st.markdown("---")
    st.subheader("Explore nosso Dashboard Interativo!")
    st.info("Acesse nosso painel completo no Power BI para mergulhar nos dados de cada cluster e entender as análises em detalhes.")

    # URL do seu dashboard no Power BI - LINK ATUALIZADO
    powerbi_url = "https://app.powerbi.com/view?r=eyJrIjoiNGY2ZTMzY2EtM2ZhMS00MWY0LWFlOWUtZTc4MjdlMjhjZDMxIiwidCI6IjExZGJiZmUyLTg5YjgtNDU0OS1iZTEwLWNlYzM2NGU1OTU1MSIsImMiOjR9" 

    if st.button("Acessar o Dashboard Nyxter"):
        st.markdown(f'<a href="{powerbi_url}" target="_blank">Clique aqui para abrir o Dashboard</a>', unsafe_allow_html=True)

    # --- Visão Geral da Jornada TOTVS ---
    st.markdown("---")
    st.markdown("<h2 style='color: #092e86;'>Visão Geral da Jornada TOTVS</h2>", unsafe_allow_html=True)
    st.markdown("A jornada do cliente TOTVS pode ser dividida em **quatro fases** principais:")
    
    # Exibir a imagem da jornada completa
    st.image("imagem1.png", caption="Jornada do Cliente TOTVS")

    st.markdown("---")
    st.header("Descrição detalhada das fases da jornada")
    st.subheader("Fase 1: Aquisição e Prospecção")
    st.markdown("""
        O cliente está conhecendo a TOTVS. É um período de descoberta e negociação, que inclui as etapas de **Interesse**,
        **Apresentação**, **Proposta** e **Fechamento**.
    """)
    
    st.subheader("Fase 2: Onboarding e Implementação")
    st.markdown("""
        Fase de integração e entrada em produção. O cliente é introduzido à empresa e às soluções contratadas,
        com foco em garantir o sucesso da implantação. Inclui **Onboarding**, **Implementação** e **Operação Assistida**.
    """)

    st.subheader("Fase 3: Sustentação e Suporte Contínuo")
    st.markdown("""
        Nesta fase, o cliente já está com o sistema em operação e a relação se torna de suporte e manutenção,
        com o **Suporte Técnico e Administrativo** para resolver dúvidas e problemas.
    """)

    st.subheader("Fase 4: Expansão e Inovação")
    st.markdown("""
        O foco muda do suporte para a expansão e inovação. A TOTVS busca novas oportunidades de negócio,
        oferecendo **Atualizações** e **Novos Negócios** para gerar mais valor ao cliente.
    """)

    # --- Concentração dos Clusters na Jornada ---
    st.markdown("---")
    st.markdown("<h2 style='color: #092e86;'>Concentração dos Clusters na Jornada</h2>", unsafe_allow_html=True)
    st.markdown("Veja como **nossos clusters** de clientes se distribuem ao longo da jornada:")
    st.image("imagem2.png", caption="Concentração dos Clusters na Jornada do Cliente")
    st.markdown("Os pontos de maior concentração indicam as **fases mais relevantes** para cada grupo de clientes.")

    # --- Análise Detalhada de Cada Cluster ---
    st.markdown("---")
    st.markdown("<h2 style='color: #092e86;'>Análise Detalhada de Cada Cluster</h2>", unsafe_allow_html=True)
    st.markdown("**Explore** as características e a **jornada de cada grupo** para entender como atendê-los melhor.")

    # Cluster: Novos Clientes
    st.markdown("<h2 style='color: #dda53d;'>Novos Clientes</h2>", unsafe_allow_html=True)
    st.image("imagem3.png", caption="Jornada do Cliente: Novos Clientes")

    st.header("Características do Cluster")
    st.markdown("""
        * **Tempo de cliente:** São os clientes mais novos, com um tempo médio de 22 meses (quase 2 anos), indicando um cluster de entrada.
        * **Contratos:** Têm o menor número de contratos ativos (6) e contratos totais (9), como esperado para clientes em início de jornada.
        * **Marcas TOTVS:** O consumo de marcas é focado em Backoffice - Core (27.35%) e Distribuição & Varejo - Core (27.37%), o que é comum para empresas que estão iniciando a digitalização de seus processos.
        * **Segmento do Cliente:** Concentram-se em Serviços (12.45%), Construção e Projetos (6.18%), Manufatura (8.02%) e Varejo (12.7%).
        * **Hospedagem do Cliente:** A grande maioria não possui a informação sobre hospedagem (72.5%), o que pode indicar que são clientes que estão em fase de onboarding.
        """)
    st.header("Foco e Jornada")
    st.markdown("""
        Este grupo é composto por clientes recém-chegados, focados em integrar as soluções básicas da TOTVS. 
        Sua jornada é de **descoberta e adaptação**, com foco na implantação inicial e na estabilização do uso.
    """)
    st.subheader("Onde estão na jornada TOTVS?")
    st.markdown("""
        Eles estão majoritariamente nas etapas de **Onboarding (Corporativo, Suporte, Projeto)**, 
        **Projeto de Implementação** e **Operação Assistida**.
    """)
    st.subheader("Sugestões de Próximos Passos")
    st.markdown("""
        * **Acelerar o Onboarding:** Crie pacotes de onboarding mais rápidos.
        * **Educação Proativa:** Ofereça treinamentos e webinars sobre funcionalidades básicas.
        * **Suporte Dedicado:** Atribua um ponto focal de suporte nos primeiros meses.
    """)

    # Cluster: Clientes em Expansão
    st.markdown("<h2 style='color: #dda53d;'>Clientes em Expansão</h2>", unsafe_allow_html=True)
    st.image("imagem4.png", caption="Jornada do Cliente: Clientes em Expansão")
    st.header("Características do Cluster")
    st.markdown("""
    * **Tempo de cliente:** Possuem um tempo médio de 66 meses (pouco mais de 5 anos), indicando que são clientes estabelecidos, mas ainda não os mais antigos.
    * **Contratos:** Têm uma média de 12 contratos ativos e 22 contratos totais, mostrando que já expandiram suas contratações.
    * **Marcas TOTVS:** O consumo se concentra em marcas como Distribuição & Varejo - CORE (34.17%) e Cross - Intera (23.64%), o que sugere um foco no crescimento e na otimização de operações.
    * **Segmento do Cliente:** Destacam-se nos segmentos de Manufatura (10.66%), Serviços (13.71%) e Construção e Projetos (17.52%), o que indica uma diversidade de atuação.
    * **Hospedagem do Cliente:** Grande parte deles ainda está em ON PREMISES (38.08%) ou com informação nula (58.32%), o que pode indicar potencial para migração para a nuvem.
    """)
    st.subheader("Foco e Jornada")
    st.markdown("""
        Este grupo já está estabelecido e usa as soluções há algum tempo. Seu foco é **expandir o uso da tecnologia**
        para otimizar seus processos. A jornada é de otimização e crescimento, buscando novas soluções para agregar mais valor.
    """)
    st.subheader("Onde estão na jornada TOTVS?")
    st.markdown("""
        Estão nas etapas de **Suporte Técnico/Administrativo** e principalmente na fase de **Atualização / Ciclo de Vida do Produto**.
    """)
    st.subheader("Sugestões de Próximos Passos")
    st.markdown("""
        * **Programa de Expansão:** Ofereça diagnósticos de processos para identificar oportunidades.
        * **Promoção de Módulos:** Apresente módulos adicionais ou produtos complementares.
        * **Incentivo à Nuvem:** Crie uma campanha focada em migração para a nuvem.
    """)

    # Cluster: Clientes Fiéis
    st.markdown("<h2 style='color: #dda53d;'>Clientes Fiéis</h2>", unsafe_allow_html=True)
    st.image("imagem5.png", caption="Jornada do Cliente: Clientes Fiéis")
    st.header("Características do Cluster:")
    st.markdown("""
    * **Tempo de cliente:** Têm a maior média de tempo como clientes, com 100 meses (pouco mais de 8 anos), o que mostra um relacionamento de longa data e fidelidade.
    * **Contratos:** Possuem a maior média de contratos ativos (20) e contratos totais (42), o que indica que são clientes com uma forte integração com os produtos TOTVS.
    * **Marcas TOTVS:** O consumo é mais diversificado, com destaque para Cross - Intera (23.64%) e Backoffice - Core (7.66%), o que sugere um uso abrangente das soluções da empresa.
    * **Segmento do Cliente:** Representam um mix significativo de clientes dos segmentos de Serviços (28.33%), Varejo (11.67%) e Construção e Projetos (8.8%).
    * **Hospedagem do Cliente:** A maioria utiliza ON PREMISES (46.6%), reforçando o perfil de clientes tradicionais e estabelecidos.
    """)
    st.subheader("Foco e Jornada")
    st.markdown("""
        Este é o grupo mais leal, com uma alta quantidade de contratos. O foco é **manter a excelência operacional** e aprofundar a parceria. 
        Sua jornada é de maturidade e fidelização.
    """)
    st.subheader("Onde estão na jornada TOTVS?")
    st.markdown("""
        Eles estão majoritariamente nas etapas de **Suporte Técnico/Administrativo**, **Atualização / Ciclo de Vida do Produto** e **Novos Negócios**.
    """)
    st.subheader("Sugestões de Próximos Passos")
    st.markdown("""
        * **Programa de Parceria Premium:** Ofereça benefícios exclusivos, como suporte prioritário.
        * **Co-criação:** Convide-os a participar de projetos-piloto de novas soluções.
        * **Mentoria/Embaixadores:** Encoraje-os a compartilhar suas experiências de sucesso.
    """)
        
    # Cluster: Clientes Estratégicos
    st.markdown("<h2 style='color: #dda53d;'>Clientes Estratégicos</h2>", unsafe_allow_html=True)
    st.image("imagem6.png", caption="Jornada do Cliente: Clientes Estratégicos")
    st.header("Características do Cluster")
    st.markdown("""
    * **Tempo de cliente:** Têm o maior tempo médio como clientes, com 109 meses (pouco mais de 9 anos), indicando um relacionamento maduro e consolidado.
    * **Contratos:** Possuem um alto número de contratos ativos (18) e contratos totais (33), mostrando um portfólio de soluções já robusto.
    * **Marcas TOTVS:** O consumo é bastante diversificado, com foco em Backoffice - Core (17.01%), Varejo - Core (13.7%) e Distribuição & Varejo - Core (8.1%).
    * **Segmento do Cliente:** Destacam-se nos segmentos de Varejo (12.2%), Serviços (11.56%) e Logística (7.1%), o que mostra uma forte presença em setores-chave.
    * **Hospedagem do Cliente:** Grande parte ainda utiliza ON PREMISES (40.67%) ou não tem a informação disponível (53.6%), o que representa uma grande oportunidade para a migração para a nuvem.
    """)
    st.subheader("Foco e Jornada")
    st.markdown("""
        Este grupo é vital para a TOTVS, com o maior tempo de relacionamento e portfólio robusto. O foco é **maximizar o valor da parceria**
        e inovar usando a tecnologia. A jornada é de liderança e estratégia.
    """)
    st.subheader("Onde estão na jornada TOTVS?")
    st.markdown("""
        Estão no topo da jornada, nas fases de **Novos Negócios** e **Atualização**.
    """)
    st.subheader("Sugestões de Próximos Passos")
    st.markdown("""
        * **Comitê de Relacionamento Executivo:** Crie um comitê para discutir metas estratégicas.
        * **Apresentação de Inovações:** Ofereça apresentações personalizadas de novas tecnologias.
        * **Projetos Conjuntos de Inovação:** Explore a possibilidade de projetos de inovação conjuntos.
    """)

elif escolha == "Análise RFM":
    st.markdown("<h1 style='color: #092e86;'>Análise RFM (Recência, Frequência e Valor Monetário)</h1>", unsafe_allow_html=True)
    st.markdown("""
        Aqui você verá a segmentação dos clientes da TOTVS com base em seu comportamento de compra.
        Esta página será usada para visualizar clusters como "Cliente Campeão", "Leal", "Em Ascensão" e "Em Atenção".
    """)


    st.markdown("---")
    st.subheader("Explore nosso Dashboard Interativo!")
    st.info("Acesse nosso painel completo no Power BI para entender nossa análise RFM.")

    # URL do seu dashboard no Power BI - LINK ATUALIZADO
    powerbi_url = "https://app.powerbi.com/view?r=eyJrIjoiNGY2ZTMzY2EtM2ZhMS00MWY0LWFlOWUtZTc4MjdlMjhjZDMxIiwidCI6IjExZGJiZmUyLTg5YjgtNDU0OS1iZTEwLWNlYzM2NGU1OTU1MSIsImMiOjR9" 

    if st.button("Acessar o Dashboard Nyxter"):
        st.markdown(f'<a href="{powerbi_url}" target="_blank">Clique aqui para abrir o Dashboard</a>', unsafe_allow_html=True)


    st.markdown("---")
    
    # Informação sobre o Método RFM
    st.markdown("<h2 style='color: #dda53d;'>O que é o Método RFM? 🎯</h2>", unsafe_allow_html=True)
    st.subheader("""
        **O RFM é uma poderosa técnica de marketing usada para analisar o comportamento do cliente com base em três fatores:**""")
        
    st.markdown("""
        * **Recência (R):** Há quanto tempo o cliente fez a última compra? Clientes mais recentes são mais propensos a responder a promoções.
        * **Frequência (F):** Com que frequência o cliente compra? Clientes que compram com frequência são mais leais e engajados.
        * **Valor Monetário (M):** Quanto o cliente gastou no total? Clientes que gastam mais são mais valiosos para a empresa.
        
        Ao combinar essas três métricas, conseguimos segmentar a base de clientes em grupos estratégicos.
    """)
    
    st.markdown("---")

    # Benefícios e Aplicações
    st.markdown("<h2 style='color: #dda53d;'>O que é possível obter com a Análise RFM? 📈</h2>", unsafe_allow_html=True)
    st.subheader("""
        **A aplicação do método RFM permite:**""") 
    st.markdown("""
        * **Identificar Clientes de Alto Valor:** Reconhecer os "Clientes Campeões" que geram a maior receita e devem ser prioridade.
        * **Detectar Clientes em Risco:** Encontrar clientes que não compram há um tempo e estão prestes a sair da base.
        * **Personalizar Campanhas:** Criar ofertas e comunicações direcionadas para cada grupo (por exemplo, promoções para "Novos Clientes" ou programas de fidelidade para "Clientes Leais").
    """)
    
    st.markdown("---")

    # Como a Análise RFM Ajuda o Negócio
    st.markdown("<h2 style='color: #dda53d;'>Como isso nos ajuda? 💡</h2>", unsafe_allow_html=True)
    st.subheader("""
        **A análise RFM transforma dados brutos em inteligência de negócios. Ela nos permite:**""")
    st.markdown("""     
        * **Otimizar o ROI (Retorno sobre o Investimento):** Direcionar esforços de marketing para os clientes que trarão o maior retorno.
        * **Aumentar a Retenção de Clientes:** Implementar estratégias proativas para reengajar clientes em risco antes que eles se percam.
        * **Melhorar a Eficiência Operacional:** Reduzir o tempo e os recursos gastos em clientes que não são lucrativos, focando naqueles com maior potencial.
    """)
    

elif escolha == "Clustering":
    st.markdown("<h1 style='color: #092e86;'>Entenda Como Nossa Clusterização Funciona!</h1>", unsafe_allow_html=True)
    st.markdown("""Nesta seção, mostramos os bastidores da nossa análise: as escolhas de modelo, o tratamento dos dados e a lógica por trás da segmentação. O objetivo é garantir que cada cluster seja significativo e útil para a estratégia de negócio.
    """)

    st.markdown("---")

    # Explicação do Processo de Machine Learning
    st.header("Jornada do Cliente - Nosso Modelo de Machine Learning 🤖")
    st.markdown("""
        Para segmentar os clientes, utilizamos um modelo de **clusterização**, que agrupa automaticamente clientes com características semelhantes. Testamos duas abordagens principais:
        
        * **K-Means:** Um dos algoritmos mais populares para clusterização. No entanto, ele assume que os clusters têm um formato esférico e tamanhos similares. No nosso caso, as features dos clientes não seguiam esse padrão, o que resultou em uma separação artificial dos grupos.
        
        * **Gaussian Mixture Model (GMM):** O GMM, por sua vez, foi a nossa escolha ideal. Ele assume que os dados são compostos por distribuições gaussianas (em forma de sino) e consegue se adaptar melhor a clusters de diferentes tamanhos e formas. Isso nos permitiu criar agrupamentos mais precisos, refletindo a complexa diversidade da base de clientes da TOTVS.
    """)

    st.markdown("---")


    # Características dos Clusters
    st.header("Quais Features Diferenciam os Clusters? 📊")
    st.markdown("""
    
    Nossa clusterização foi baseada em 5 features principais, cada uma revelando um aspecto da jornada do cliente, sendo elas:
        
    Tempo de cliente: Contagem do tempo em meses;
    Contratos: Quantidade de contratos no total e ativos;
    Marcas TOTVS: Marca TOTVS que o cliente consome;
    Segmento do Cliente: O segmento que o cliente pertence;
    Hospedagem do Cliente: Hospedagem que o cliente utiliza.

    A combinação dessas features nos permitiu entender não só o comportamento de compra, mas também o nível de engajamento de cada cliente.
    """)

    st.markdown("---")


    # Como o RFM foi Calculado
    st.header("Clusterização RFM ")
    st.markdown("""
        A análise RFM foi feita sobre uma amostra de **4.053 clientes**, de um total de 10.615. O motivo para o uso da amostra foi um desafio comum em bases de dados reais: a presença de dados incompletos. A data de assinatura do contrato, essencial para a análise de Recência, não estava completa para todos os clientes, o que fez com que a data mínima fosse de julho de 2024.
        
        Ainda assim, essa amostra se mostrou robusta para nos dar um panorama valioso sobre o comportamento de compra dos clientes, permitindo a segmentação em clusters estratégicos.
    """)
    st.markdown("---")


    # Certifique-se de que o arquivo "dados_cluster.xlsx" está no mesmo diretório do seu script
    try:
        df_rfm = pd.read_excel("Dados_Clusters_RFM.xlsx")
        df_jornada = pd.read_excel("Dados_Cluster_Jornada_do_Cliente (1).xlsx")
    except FileNotFoundError:
        st.error("Erro: Arquivos Excel não encontrados! Certifique-se de que 'Dados_Clusters_RFM.xlsx' e 'Dados_Cluster_Jornada_do_Cliente (1).xlsx' estão no mesmo diretório do script.")
        st.stop()


    st.header("Faça o download dos dados")
    st.markdown("""
        Você pode fazer o download dos dados dos clientes após a clusterização.
    """)

    # Funções para converter DataFrames em bytes
    @st.cache_data
    def convert_df_to_excel_bytes(df):
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name='Sheet1')
        processed_data = output.getvalue()
        return processed_data

    excel_bytes_rfm = convert_df_to_excel_bytes(df_rfm)
    excel_bytes_jornada = convert_df_to_excel_bytes(df_jornada)


    # Botões de download
    col1, col2 = st.columns(2)

    with col1:
        st.download_button(
            label="Download Dados RFM",
            data=excel_bytes_rfm,
            file_name="Dados_Clusters_RFM.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            help="Baixe os dados completos da clusterização RFM."
        )

    with col2:
        st.download_button(
            label="Download Dados Jornada do Cliente",
            data=excel_bytes_jornada,
            file_name="Dados_Cluster_Jornada_do_Cliente (1).xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            help="Baixe os dados numéricos da clusterização por jornada."
        )

elif escolha == "NyxterIA":
    st.title("Análise RFM (Recência, Frequência e Valor Monetário)")
    st.markdown("""
        Aqui você verá a segmentação dos clientes da TOTVS com base em seu comportamento de compra.
        Esta página será usada para visualizar clusters como "Cliente Campeão", "Leal" e "Em Risco".
    """)

