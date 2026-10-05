#!/usr/bin/env python3
"""Build an unreviewed translation batch for the v1.9 core workflow.

The generated JSON is a review artifact only. It is not loaded by the prototype
and must not be described as complete localization or production copy.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

SOURCE_BLOB = "b2ebcaf4cfd59d0825fb105ed0d320808776b902"
TARGET_STAGES = {"shell", "evidence-check", "site-model", "dispatchComparison"}
EXPECTED_COUNTS = {"shell": 65, "evidence-check": 43, "site-model": 35, "dispatchComparison": 99}
TRANSLATIONS: dict[str, dict[str, str]] = {
    "組合概覽": {"en": "Portfolio overview", "pt": "Visão geral do portefólio"},
    "主導覽": {"en": "Main navigation", "pt": "Navegação principal"},
    "當前調度階段；展開以切換階段": {"en": "Current dispatch stage; expand to change stage", "pt": "Fase atual do despacho; expanda para mudar de fase"},
    "使用者": {"en": "User", "pt": "Utilizador"},
    "選擇時間粒度": {"en": "Select time resolution", "pt": "Selecionar resolução temporal"},
    "目前規劃條件": {"en": "Current planning conditions", "pt": "Condições atuais de planeamento"},
    "選擇規劃日期": {"en": "Select planning date", "pt": "Selecionar data de planeamento"},
    "調度工作流程": {"en": "Dispatch workflow", "pt": "Fluxo de trabalho do despacho"},
    "關閉": {"en": "Close", "pt": "Fechar"},
    "能源模型": {"en": "Energy model", "pt": "Modelo energético"},
    "來源調度": {"en": "Source dispatch", "pt": "Despacho de fontes"},
    "證據": {"en": "Evidence", "pt": "Evidências"},
    "查看此方案的假設": {"en": "Review this schedule's assumptions", "pt": "Consultar os pressupostos deste plano"},
    "比較同一時段": {"en": "Compare the same interval", "pt": "Comparar o mesmo intervalo"},
    "站點能源模型": {"en": "Site energy model", "pt": "Modelo energético do local"},
    "所有數值均為合成演示。沒有顯示上網、跨樓宇抵扣、節省金額或已執行控制。請以現場點位、合同與安全約束替換後再評估。": {
        "en": "All values are synthetic demonstrations. No grid export, cross-building credits, savings, or executed control are shown. Replace them with site telemetry points, contract terms, and safety constraints before evaluating.",
        "pt": "Todos os valores são demonstrações sintéticas. Não são apresentados injeção na rede, compensação entre edifícios, poupanças ou controlo executado. Substitua-os por pontos de telemetria do local, termos contratuais e restrições de segurança antes de avaliar.",
    },
    "查看輸入依據": {"en": "View input evidence", "pt": "Ver evidências dos dados de entrada"},
    "查看流程⌄": {"en": "View workflow⌄", "pt": "Ver fluxo de trabalho⌄"},
    "空調可調範圍、建築舒適約束與移峰後反彈；": {"en": "HVAC flexibility, building comfort constraints, and rebound after load shifting;", "pt": "Flexibilidade do AVAC, limites de conforto do edifício e recuperação da carga após o deslocamento;"},
    "12:00–18:00 · 澳門時間示例": {"en": "12:00–18:00 · Macau time example", "pt": "12:00–18:00 · exemplo na hora de Macau"},
    "合成資料 · 版本 DEMO-04": {"en": "Synthetic data · version DEMO-04", "pt": "Dados sintéticos · versão DEMO-04"},
    "未核實 · 暫不提供帳單級金額": {"en": "Unverified · bill-level amounts unavailable", "pt": "Não verificado · valores ao nível da fatura indisponíveis"},
    "放回每個時段。": {"en": "Show each interval again.", "pt": "Mostrar novamente cada intervalo."},
    "原型邊界：": {"en": "Prototype boundary:", "pt": "Limites do protótipo:"},
    "監測與回放": {"en": "Monitoring and replay", "pt": "Monitorização e reprodução"},
    "解讀限制和證據": {"en": "Interpret constraints and evidence", "pt": "Interpretar restrições e evidências"},
    "規劃條件 · 12:00–18:00 · Shadow": {"en": "Planning conditions · 12:00–18:00 · SHADOW", "pt": "Condições de planeamento · 12:00–18:00 · SHADOW"},
    "建議狀態": {"en": "Recommendation status", "pt": "Estado da recomendação"},
    "示例日期 · 合成情境": {"en": "Example date · synthetic scenario", "pt": "Data de exemplo · cenário sintético"},
    "把能源安排，": {"en": "Plan energy use,", "pt": "Planear o uso de energia,"},
    "儲能容量、SOC、效率、保留電量與運行界限；": {"en": "storage capacity, SOC, efficiency, reserved energy, and operating limits;", "pt": "capacidade de armazenamento, SOC, eficiência, energia de reserva e limites operacionais;"},
    "方案可解讀，仍不可執行": {"en": "Schedules are explainable, but not executable", "pt": "Os planos são explicáveis, mas não executáveis"},
    "時序與方案": {"en": "Timeline and schedules", "pt": "Cronologia e planos"},
    "進線／分項電表對應、時鐘與資料品質；": {"en": "Main/submeter mapping, clock alignment, and data quality;", "pt": "Correspondência entre contador geral e subcontadores, sincronização dos relógios e qualidade dos dados;"},
    "分清物理與結算": {"en": "Separate physical flows from settlement", "pt": "Separar fluxos físicos do acerto da fatura"},
    "等待實測證據": {"en": "Awaiting measured evidence", "pt": "A aguardar evidências medidas"},
    "跳至主要內容": {"en": "Skip to main content", "pt": "Saltar para o conteúdo principal"},
    "光伏逆變器與並網點能力，以及適用的上網／限發狀態；": {"en": "PV inverter and grid-connection capacity, plus applicable export or curtailment status;", "pt": "Capacidade do inversor fotovoltaico e do ponto de ligação à rede, incluindo o estado aplicável de injeção ou limitação;"},
    "建議不會下發": {"en": "Recommendations are not sent to equipment", "pt": "As recomendações não são enviadas aos equipamentos"},
    "明白": {"en": "Understood", "pt": "Compreendi"},
    "合成情境 · 非現場資料": {"en": "Synthetic scenario · not site data", "pt": "Cenário sintético · não são dados do local"},
    "Macau Commercial Energy OS · 調度流程研究 v1.9": {"en": "Macau Commercial Energy OS · dispatch workflow study v1.9", "pt": "Macau Commercial Energy OS · estudo do fluxo de despacho v1.9"},
    "繁體中文介面實驗 · 尚不代表完整多語支援或已核准視覺方向": {"en": "Traditional Chinese interface experiment · not complete multilingual support or an approved visual direction", "pt": "Estudo da interface em chinês tradicional · não representa suporte multilingue completo nem uma direção visual aprovada"},
    "證據與假設": {"en": "Evidence and assumptions", "pt": "Evidências e pressupostos"},
    "Shadow 審查": {"en": "SHADOW review", "pt": "Revisão SHADOW"},
    "概覽": {"en": "Overview", "pt": "Visão geral"},
    "適用電價、需量計算與合同有效期。": {"en": "Applicable tariff, demand calculation, and contract effective period.", "pt": "Tarifa aplicável, cálculo da procura e período de vigência do contrato."},
    "成本與約束": {"en": "Costs and constraints", "pt": "Custos e restrições"},
    "輸入快照": {"en": "Input snapshot", "pt": "Instantâneo dos dados de entrada"},
    "計費規則": {"en": "Billing rules", "pt": "Regras de faturação"},
    "模型": {"en": "Model", "pt": "Modelo"},
    "規劃時段": {"en": "Planning horizon", "pt": "Horizonte de planeamento"},
    "來源與負荷 · 調度工作區": {"en": "Sources and loads · dispatch workspace", "pt": "Fontes e cargas · área de trabalho do despacho"},
    "情境比較 · Shadow": {"en": "Scenario comparison · SHADOW", "pt": "Comparação de cenários · SHADOW"},
    "資料與合約": {"en": "Data and contracts", "pt": "Dados e contratos"},
    "澳門情境": {"en": "Macau scenario", "pt": "Cenário de Macau"},
    "能源營運 / 調度": {"en": "Energy operations / dispatch", "pt": "Operações energéticas / despacho"},
    "目前畫面用一個合成平衡示例測試調度任務的資訊層次。實際排程至少需要以下現場與合同證據：": {
        "en": "This view uses a synthetic balance example to examine the information hierarchy for dispatch work. A real schedule requires, at minimum, the following site and contract evidence:",
        "pt": "Esta vista usa um exemplo sintético de balanço para avaliar a hierarquia da informação numa tarefa de despacho. Um plano real exige, no mínimo, as seguintes evidências do local e do contrato:",
    },
    "核驗輸入依據": {"en": "Verify input evidence", "pt": "Verificar evidências dos dados de entrada"},
    "缺少結算依據時，只呈現物理功率情境；缺少控制和安全授權時，只能審查建議，不提供下發操作。": {
        "en": "Without settlement evidence, show physical-power scenarios only. Without control and safety authorization, recommendations may be reviewed, but no dispatch command is available.",
        "pt": "Sem evidências de faturação, apresentar apenas cenários de potência física. Sem autorização de controlo e segurança, as recomendações podem ser revistas, mas não é possível enviar comandos aos equipamentos.",
    },
    "比較同一時段的供能與負荷安排，先核實現場證據，再看成本與約束。": {
        "en": "Compare supply and load schedules for the same interval. Verify site evidence before reviewing costs and constraints.",
        "pt": "Compare os planos de fornecimento e carga para o mesmo intervalo. Verifique as evidências do local antes de analisar custos e restrições.",
    },
    "調度": {"en": "Dispatch", "pt": "Despacho"},
    "1 小時示例粒度": {"en": "Example resolution: 1 hour", "pt": "Resolução de exemplo: 1 hora"},
    "示範商業站點": {"en": "Demonstration commercial site", "pt": "Local comercial de demonstração"},
    "合成來源清單；水平捲動查看所有欄位": {"en": "Synthetic source inventory; scroll horizontally to view all fields", "pt": "Inventário sintético de fontes; desloque horizontalmente para ver todos os campos"},
    "本原型沒有代表任何客戶帳戶。正式工作區只列出目前角色可查看的範圍；站點授權不自動授予帳戶權限。": {
        "en": "This prototype does not represent a customer account. A production workspace shows only the scope visible to the current role; site authorization does not automatically grant account access.",
        "pt": "Este protótipo não representa uma conta de cliente. A área de trabalho de produção apresenta apenas o âmbito visível para o perfil atual; a autorização do local não concede automaticamente acesso à conta.",
    },
    "下一步：檢視站點能源模型 ↓": {"en": "Next: review the site energy model ↓", "pt": "Seguinte: consultar o modelo energético do local ↓"},
    "結算範圍示意 · 合成狀態": {"en": "Settlement-scope illustration · synthetic status", "pt": "Ilustração do âmbito de faturação · estado sintético"},
    "逆變器、接線點、可用性與輸出邊界": {"en": "Inverters, connection points, availability, and export limits", "pt": "Inversores, pontos de ligação, disponibilidade e limites de injeção"},
    "物理模型": {"en": "Physical model", "pt": "Modelo físico"},
    "阻擋經濟結果": {"en": "Economic results blocked", "pt": "Resultados económicos bloqueados"},
    "電價與合同": {"en": "Tariffs and contracts", "pt": "Tarifas e contratos"},
    "現場光伏": {"en": "On-site PV", "pt": "Fotovoltaico no local"},
    "輸入為示例；站點接線和設備能力未確認。": {"en": "Inputs are illustrative; site wiring and equipment capabilities are unverified.", "pt": "Os dados de entrada são ilustrativos; a cablagem do local e as capacidades dos equipamentos não foram verificadas."},
    "部分情境": {"en": "Partial scenario", "pt": "Cenário parcial"},
    "儲能": {"en": "Energy storage", "pt": "Armazenamento de energia"},
    "阻擋 · 未有已核實帳戶/合同": {"en": "Blocked · no verified account or contract", "pt": "Bloqueado · sem conta ou contrato verificado"},
    "表計映射、時鐘、資料品質及帳戶關係": {"en": "Meter mapping, clock alignment, data quality, and account relationships", "pt": "Correspondência dos contadores, sincronização dos relógios, qualidade dos dados e relações entre contas"},
    "本例未提供": {"en": "Not provided in this example", "pt": "Não fornecido neste exemplo"},
    "資料充足度不等於調度權限。所有設備狀態和合同映射都需有來源、時間和審核紀錄。": {
        "en": "Data sufficiency does not grant dispatch authority. Every equipment status and contract mapping needs a source, timestamp, and review record.",
        "pt": "A suficiência dos dados não concede autorização de despacho. Cada estado de equipamento e correspondência contratual precisa de fonte, data/hora e registo de revisão.",
    },
    "若一個站點有多個獨立供電/結算帳戶，需逐個範圍核驗並分開計算，不按站點名稱推定合併。": {
        "en": "If a site has multiple independent supply or settlement accounts, verify and calculate each scope separately. Do not infer that accounts are combined from the site name.",
        "pt": "Se um local tiver várias contas independentes de fornecimento ou faturação, verifique e calcule cada âmbito separadamente. Não presuma que as contas estão agregadas com base no nome do local.",
    },
    "原型示例": {"en": "Prototype example", "pt": "Exemplo do protótipo"},
    "電網進線": {"en": "Grid import point", "pt": "Ponto de entrada da rede"},
    "經濟模型：BLOCKED": {"en": "Economic model: BLOCKED", "pt": "Modelo económico: BLOQUEADO"},
    "HVAC 負荷": {"en": "HVAC load", "pt": "Carga do AVAC"},
    "進入現場模型前需核實": {"en": "Verify before adding to the site model", "pt": "Verificar antes de incluir no modelo do local"},
    "點位、舒適/服務界限、授權和響應證據": {"en": "Telemetry points, comfort/service limits, authorization, and response evidence", "pt": "Pontos de telemetria, limites de conforto/serviço, autorização e evidências de resposta"},
    "合成示例 · 未連接現場": {"en": "Synthetic example · no site connection", "pt": "Exemplo sintético · sem ligação ao local"},
    "示意發電曲線": {"en": "Illustrative generation profile", "pt": "Perfil de produção ilustrativo"},
    "未連接結算帳戶 · 0 個已核實範圍": {"en": "No settlement account connected · 0 verified scopes", "pt": "Nenhuma conta de faturação ligada · 0 âmbitos verificados"},
    "合成": {"en": "Synthetic", "pt": "Sintético"},
    "先看輸入是否可用，再看能否作經濟判斷。": {"en": "Check whether the inputs are usable before making an economic assessment.", "pt": "Verifique se os dados de entrada são utilizáveis antes de fazer uma avaliação económica."},
    "合成來源清單 · 尚未核實的項目不帶入帳單級結果": {"en": "Synthetic source inventory · unverified items are excluded from bill-level results", "pt": "Inventário sintético de fontes · itens não verificados são excluídos dos resultados ao nível da fatura"},
    "經濟模型": {"en": "Economic model", "pt": "Modelo económico"},
    "未提供適用合同、電價及需求計算規則。": {"en": "Applicable contract, tariff, and demand calculation rules have not been provided.", "pt": "Não foram fornecidos o contrato aplicável, a tarifa nem as regras de cálculo da procura."},
    "適用客戶/表計、有效期、Pu 規則及合同條文": {"en": "Applicable customer and meter, validity period, Pu rules, and contract terms", "pt": "Cliente e contador aplicáveis, período de validade, regras Pu e cláusulas contratuais"},
    "兩種就緒度，分開判斷": {"en": "Two readiness states, assessed separately", "pt": "Dois estados de prontidão, avaliados separadamente"},
    "物理模型：僅可作合成情境": {"en": "Physical model: synthetic scenarios only", "pt": "Modelo físico: apenas cenários sintéticos"},
    "輸入類別": {"en": "Input category", "pt": "Categoria de dados de entrada"},
    "功率/容量、SOC、效率、保留值及安全界限": {"en": "Power/capacity, SOC, efficiency, reserve, and safety limits", "pt": "Potência/capacidade, SOC, eficiência, reserva e limites de segurança"},
    "01 · 資料與合約核驗": {"en": "01 · Data and contract review", "pt": "01 · Verificação de dados e contratos"},
    "可用狀態": {"en": "Availability status", "pt": "Estado de disponibilidade"},
    "情境放電及充電；SOC 軌跡為合成示例": {"en": "Scenario discharge and charging; SOC trajectory is synthetic", "pt": "Descarga e carregamento do cenário; trajetória do SOC sintética"},
    "以下只展示合成欄位。本站點、表計、合約及設備點位均未連接；狀態不能當成澳門現場資料。": {
        "en": "Only synthetic fields are shown below. This site, its meters, contracts, and equipment points are not connected; these statuses are not Macau site data.",
        "pt": "Abaixo são apresentados apenas campos sintéticos. Este local, os seus contadores, contratos e pontos dos equipamentos não estão ligados; estes estados não são dados de um local em Macau.",
    },
    "未驗證": {"en": "Unverified", "pt": "Não verificado"},
    "示意移峰與回彈": {"en": "Illustrative load shifting and rebound", "pt": "Deslocamento de carga e recuperação ilustrativos"},
    "示意電表／小時平均 kW": {"en": "Illustrative meter / hourly average kW", "pt": "Contador ilustrativo / média horária em kW"},
    "物理流 · 合成平衡示意": {"en": "Physical flows · synthetic balance illustration", "pt": "Fluxos físicos · balanço sintético ilustrativo"},
    "把實際能源路徑和電費規則放在不同層。": {"en": "Keep physical energy paths separate from billing rules.", "pt": "Separe os fluxos físicos de energia das regras da fatura."},
    "EV 充電 · 物理負荷候選": {"en": "EV charging · candidate physical load", "pt": "Carregamento de VE · carga física candidata"},
    "演示移峰和回彈，不代表已核實點位、舒適/服務界限、控制權或現場響應。": {"en": "Illustrates load shifting and rebound; it does not establish verified points, comfort or service limits, control authority, or site response.", "pt": "Ilustra o deslocamento e a recuperação da carga; não comprova pontos verificados, limites de conforto ou serviço, autoridade de controlo nem resposta no local."},
    "未納入 · 證據不足": {"en": "Excluded · insufficient evidence", "pt": "Excluído · evidências insuficientes"},
    "電網輸入 · 現場 PV · 可選 ESS 放電": {"en": "Grid import · on-site PV · optional ESS discharge", "pt": "Importação da rede · fotovoltaico no local · descarga opcional do ESS"},
    "儲能 ESS": {"en": "Energy storage (ESS)", "pt": "Armazenamento de energia (ESS)"},
    "本次情境用了哪些資源？": {"en": "Which resources are used in this scenario?", "pt": "Que recursos são utilizados neste cenário?"},
    "「納入示例」不代表現場可調度；只有站點映射、設備能力、營運限制和授權都核實後，資源才可進入實際評估。": {"en": "“Included in example” does not mean dispatchable at the site. A resource may enter a real assessment only after site mapping, equipment capability, operating limits, and authorization are verified.", "pt": "“Incluído no exemplo” não significa que o recurso possa ser despachado no local. Só pode integrar uma avaliação real após verificar o mapeamento do local, a capacidade dos equipamentos, os limites operacionais e a autorização."},
    "EV 可在證據齊全後作為物理柔性負荷建模；本合成候選未建模或調度 EV。仍需核實充電樁、服務表計、可用時窗、離場電量、授權及響應。充電費用歸屬須另行匹配實際表計、帳戶、合同與電價，不假設沿用樓宇電價。": {"en": "EV charging can be modelled as a physical flexible load when evidence is complete; this synthetic candidate does not model or dispatch EVs. Verify the chargers, service meter, availability window, required departure charge, authorization, and response. Attribute charging costs only after matching the actual meter, account, contract, and tariff; do not assume the building tariff applies.", "pt": "O carregamento de VE pode ser modelado como carga física flexível quando existirem evidências completas; este cenário sintético não modela nem despacha VE. Verifique os carregadores, o contador de serviço, a janela de disponibilidade, a carga necessária à partida, a autorização e a resposta. Atribua os custos de carregamento apenas após associar o contador, a conta, o contrato e a tarifa reais; não presuma que se aplica a tarifa do edifício."},
    "只有已核實的電表與設備關係才可形成物理事實。此處的連線是合成示意，不表示反送、跨樓宇共享或抵扣權利。": {"en": "Only verified meter-to-equipment relationships establish physical facts. The connections shown here are synthetic and do not imply export, cross-building sharing, or credit rights.", "pt": "Só relações verificadas entre contadores e equipamentos estabelecem factos físicos. As ligações aqui apresentadas são sintéticas e não implicam injeção na rede, partilha entre edifícios ou direitos de compensação."},
    "顯示合成進口曲線；未核實實際表計、帳戶、供電容量或適用需求規則。": {"en": "Shows a synthetic import profile; actual meters, accounts, supply capacity, and applicable demand rules are unverified.", "pt": "Apresenta um perfil sintético de importação; os contadores, as contas, a capacidade de fornecimento e as regras de procura aplicáveis não foram verificados."},
    "合成候選：15:00–16:00 電網 430 + PV 110 + ESS 放電 20 = 負荷 560 kW；16:00–17:00 電網 509.691 + PV 85 = 負荷 570 + ESS 充電 24.691 kW。SOC 由 40 降至 17.778 kWh，再於充電後回到 40 kWh。分別按 90% 充、放電效率積分；全部設備參數均非現場證據。": {"en": "Synthetic candidate: 15:00–16:00 grid 430 + PV 110 + ESS discharge 20 = load 560 kW; 16:00–17:00 grid 509.691 + PV 85 = load 570 + ESS charge 24.691 kW. SOC falls from 40 to 17.778 kWh, then returns to 40 kWh after charging. Integrated with 90% charge and discharge efficiency; no equipment parameter is site evidence.", "pt": "Cenário sintético: 15:00–16:00 rede 430 + fotovoltaico 110 + descarga do ESS 20 = carga 560 kW; 16:00–17:00 rede 509,691 + fotovoltaico 85 = carga 570 + carregamento do ESS 24,691 kW. O SOC desce de 40 para 17,778 kWh e regressa a 40 kWh após o carregamento. Cálculo com eficiência sintética de 90% na carga e descarga; nenhum parâmetro dos equipamentos constitui evidência do local."},
    "光伏輸出 → 自用/反送/抵扣：": {"en": "PV output → self-consumption / export / credits:", "pt": "Produção fotovoltaica → autoconsumo / injeção / compensação:"},
    "資源資格 · 按證據納入": {"en": "Resource eligibility · include only when supported by evidence", "pt": "Elegibilidade dos recursos · incluir apenas com evidências"},
    "02 · 站點能源模型": {"en": "02 · Site energy model", "pt": "02 · Modelo energético do local"},
    "只作合成發電與自用平衡示意；未核實逆變器、併網、輸出表計、收購或結算權利。": {"en": "Synthetic generation and self-consumption balance only; inverter, grid connection, export meter, purchase terms, and settlement rights are unverified.", "pt": "Apenas balanço sintético de produção e autoconsumo; inversor, ligação à rede, contador de injeção, condições de compra e direitos de faturação não foram verificados."},
    "結算映射 · 另外核驗": {"en": "Settlement mapping · verify separately", "pt": "Mapeamento de faturação · verificar separadamente"},
    "熱水負荷": {"en": "Hot-water load", "pt": "Carga de água quente"},
    "納入示例 · 合成": {"en": "Included in example · synthetic", "pt": "Incluído no exemplo · sintético"},
    "不納入此排程 · 證據不足": {"en": "Excluded from this schedule · insufficient evidence", "pt": "Excluído deste plano · evidências insuficientes"},
    "用能端": {"en": "Consumption side", "pt": "Lado do consumo"},
    "電網電量 → 適用電價/合同：": {"en": "Grid energy → applicable tariff/contract:", "pt": "Energia da rede → tarifa/contrato aplicável:"},
    "尚無設備/熱水箱映射、溫度與服務界限、需求時窗、控制權及響應證據。": {"en": "Equipment or hot-water tank mapping, temperature and service limits, demand windows, control authority, and response evidence are missing.", "pt": "Faltam o mapeamento dos equipamentos ou depósitos de água quente, os limites de temperatura e serviço, as janelas de procura, a autoridade de controlo e evidências de resposta."},
    "HVAC / 冷水機": {"en": "HVAC / chiller", "pt": "AVAC / chiller"},
    "未提供證據，經濟輸出阻擋。": {"en": "Evidence not provided; economic outputs are blocked.", "pt": "Evidências não fornecidas; resultados económicos bloqueados."},
    "供能端": {"en": "Supply side", "pt": "Lado do fornecimento"},
    "跨樓宇能源關係：": {"en": "Cross-building energy relationship:", "pt": "Relação energética entre edifícios:"},
    "只顯示合成發電與自用情境，不推斷上網或帳戶權利。": {"en": "Shows only synthetic generation and self-consumption scenarios; no export or account rights are inferred.", "pt": "Apresenta apenas cenários sintéticos de produção e autoconsumo; não presume direitos de injeção na rede ou direitos associados às contas."},
    "未建模、未主張。": {"en": "Not modelled or claimed.", "pt": "Não modelado nem declarado."},
    "只演示充放電與 SOC 積分；實際功率、容量、效率、保留值和安全限制未知。": {"en": "Illustrates charging, discharging, and SOC integration only; actual power, capacity, efficiency, reserve, and safety limits are unknown.", "pt": "Ilustra apenas carga, descarga e integração do SOC; a potência, capacidade, eficiência, reserva e limites de segurança reais são desconhecidos."},
    "電網進口": {"en": "Grid import", "pt": "Importação da rede"},
    "下一步：比較同一規劃時段 ↓": {"en": "Next: compare schedules for the same planning horizon ↓", "pt": "Seguinte: comparar planos para o mesmo horizonte de planeamento ↓"},
    "基礎負荷 · HVAC · 其他已核實可調負荷": {"en": "Base load · HVAC · other verified flexible loads", "pt": "Carga base · AVAC · outras cargas flexíveis verificadas"},
    "圖例": {"en": "Legend", "pt": "Legenda"},
    "六小時逐時供能與負荷安排摘要": {"en": "Six-hour, interval-by-interval supply and load schedule summary", "pt": "Resumo horário do fornecimento e das cargas ao longo de seis horas"},
    "逐時段平均功率表格，可水平捲動查看完整欄位": {"en": "Interval average-power table; scroll horizontally to view all columns", "pt": "Tabela de potência média por intervalo; desloque horizontalmente para ver todas as colunas"},
    "圖表突顯方案": {"en": "Chart schedule highlight", "pt": "Destaque do plano no gráfico"},
    "SHADOW 原型審閱動作": {"en": "SHADOW prototype review actions", "pt": "Ações de revisão do protótipo SHADOW"},
    "CEM 本計費期 Pu 狀態未知": {"en": "CEM Pu status for this billing period is unknown", "pt": "O estado do Pu do CEM neste período de faturação é desconhecido"},
    "六小時供能與負荷曲線，可左右捲動": {"en": "Six-hour supply and load curves; scroll horizontally", "pt": "Curvas de fornecimento e carga de seis horas; desloque horizontalmente"},
    "本 MVP 原型不提供設備控制": {"en": "This MVP prototype does not control equipment", "pt": "Este protótipo de MVP não controla equipamentos"},
    "電網輸入": {"en": "Grid import", "pt": "Importação da rede"},
    "來源與電表映射": {"en": "Source and meter mapping", "pt": "Mapeamento de fontes e contadores"},
    "設備控制未啟用": {"en": "Equipment control is disabled", "pt": "O controlo dos equipamentos está desativado"},
    "基線 485 → 候選 510 kW（回彈時段 +25 kW）。本計費期 Pu 未知，不計算費用。": {"en": "Baseline 485 → candidate 510 kW (rebound interval +25 kW). Pu for this billing period is unknown; cost is not calculated.", "pt": "Base 485 → cenário proposto 510 kW (mais 25 kW no intervalo de recuperação). O Pu deste período de faturação é desconhecido; o custo não é calculado."},
    "候選功率平衡（AC 端）": {"en": "Candidate power balance (AC side)", "pt": "Balanço de potência proposto (lado CA)"},
    "ESS 充電 24.691 kW · SOC 17.778 → 40 kWh · HVAC —": {"en": "ESS charge 24.691 kW · SOC 17.778 → 40 kWh · HVAC —", "pt": "Carregamento do ESS 24,691 kW · SOC 17,778 → 40 kWh · AVAC —"},
    "儲能放電": {"en": "ESS discharge", "pt": "Descarga do ESS"},
    "18:00 · 結束": {"en": "18:00 · end", "pt": "18:00 · fim"},
    "候選情境 · 含 20 kW ESS 放電": {"en": "Candidate scenario · includes 20 kW ESS discharge", "pt": "Cenário proposto · inclui descarga do ESS de 20 kW"},
    "供能與負荷時間線": {"en": "Supply and load timeline", "pt": "Cronologia do fornecimento e das cargas"},
    "負荷 580 → 580 kW · PV 125 kW": {"en": "Load 580 → 580 kW · PV 125 kW", "pt": "Carga 580 → 580 kW · fotovoltaico 125 kW"},
    "先看方案依據是否完整": {"en": "First check whether the schedule evidence is complete", "pt": "Verifique primeiro se as evidências do plano estão completas"},
    "時段能源平衡": {"en": "Interval energy balance", "pt": "Balanço energético do intervalo"},
    "未核實 · 不計算帳單金額": {"en": "Unverified · bill amount not calculated", "pt": "Não verificado · valor da fatura não calculado"},
    "候選 · HVAC 負荷移峰": {"en": "Candidate · HVAC load shifting", "pt": "Proposto · deslocamento da carga AVAC"},
    "展示窗口峰值：": {"en": "Displayed-window peak:", "pt": "Pico da janela apresentada:"},
    "+30 · 回彈": {"en": "+30 · rebound", "pt": "+30 · recuperação"},
    "電網輸入 候選": {"en": "Grid import · candidate", "pt": "Importação da rede · proposto"},
    "要求補證據": {"en": "Request more evidence", "pt": "Solicitar evidências adicionais"},
    "現場光伏": {"en": "On-site PV", "pt": "Fotovoltaico no local"},
    "ESS 充電 候選": {"en": "ESS charging · candidate", "pt": "Carregamento do ESS · proposto"},
    "電網輸入 基線": {"en": "Grid import · baseline", "pt": "Importação da rede · base"},
    "電網": {"en": "Grid", "pt": "Rede elétrica"},
    "以下候選是合成情境，只用於檢查時段能源平衡、儲能軌跡與 HVAC 回彈；不代表預測、最佳化結果或現場可行性。": {"en": "The candidate below is synthetic and is used only to inspect interval energy balance, storage trajectory, and HVAC rebound. It is not a forecast, optimization result, or indication of site feasibility.", "pt": "O cenário proposto abaixo é sintético e serve apenas para analisar o balanço energético por intervalo, a trajetória do armazenamento e a recuperação do AVAC. Não é uma previsão, um resultado de otimização nem uma indicação de viabilidade no local."},
    "HVAC 移峰／回彈": {"en": "HVAC load shifting / rebound", "pt": "Deslocamento / recuperação da carga AVAC"},
    "時段": {"en": "Interval", "pt": "Intervalo"},
    "示意將 30 kW 空調需求移出 15:00，儲能情境於15:00放電20 kW、16:00以24.691 kW充電恢復SOC；未驗證現場可調能力。": {"en": "Illustrates shifting 30 kW of air-conditioning demand away from 15:00. In the storage scenario, the ESS discharges 20 kW at 15:00 and charges at 24.691 kW at 16:00 to restore SOC; site flexibility is unverified.", "pt": "Ilustra o deslocamento de 30 kW de procura de ar condicionado para fora das 15:00. No cenário de armazenamento, o ESS descarrega 20 kW às 15:00 e carrega a 24,691 kW às 16:00 para repor o SOC; a flexibilidade no local não foi verificada."},
    "15:00–16:00 電網輸入": {"en": "15:00–16:00 grid import", "pt": "Importação da rede das 15:00 às 16:00"},
    "為甚麼仍是情境比較？ ↗": {"en": "Why is this still a scenario comparison? ↗", "pt": "Porque continua a ser uma comparação de cenários? ↗"},
    "HVAC 調整": {"en": "HVAC adjustment", "pt": "Ajuste do AVAC"},
    "動作只更新本頁示意，不寫入審計、不授權、不下發；重新載入後重設。": {"en": "Actions update this page-only illustration; they do not create an audit record, grant authorization, or send commands. Reloading resets the state.", "pt": "As ações atualizam apenas esta ilustração na página; não criam um registo de auditoria, não concedem autorização nem enviam comandos. O estado é reposto ao recarregar."},
    "未知": {"en": "Unknown", "pt": "Desconhecido"},
    "kW 為合成區間平均功率；SOC 以小時區間積分為 kWh。此例並非計費週期或現場結果。此版按合成效率逐時積分 ESS 充放電與 SOC；容量、功率、效率、HVAC 舒適度均非現場驗證，亦未計退化、預測不確定性或電費。": {"en": "kW values are synthetic interval-average power; SOC is integrated over hourly intervals in kWh. This example is neither a billing-period nor a site result. ESS charge/discharge and SOC use synthetic efficiencies; capacity, power, efficiency, and HVAC comfort are unverified. Degradation, forecast uncertainty, and electricity charges are not modelled.", "pt": "Os valores em kW são potências médias sintéticas por intervalo; o SOC é integrado em intervalos horários e expresso em kWh. Este exemplo não representa um período de faturação nem resultados do local. A carga/descarga do ESS e o SOC usam eficiências sintéticas; capacidade, potência, eficiência e conforto do AVAC não foram verificados. A degradação, a incerteza das previsões e os custos de eletricidade não são modelados."},
    "未審查 · 示意": {"en": "Unreviewed · illustration", "pt": "Não revisto · ilustração"},
    "示例基礎負荷、空調與現場光伏曲線；不是需求預測。": {"en": "Example base-load, air-conditioning, and on-site PV profiles; not a demand forecast.", "pt": "Perfis de exemplo da carga base, do ar condicionado e do fotovoltaico local; não são uma previsão da procura."},
    "尚未計入電費或收益": {"en": "Electricity charges or revenue not calculated", "pt": "Custos de eletricidade ou receitas não calculados"},
    "目前突顯：基線；基線與候選均同時顯示。": {"en": "Currently highlighted: baseline; both baseline and candidate remain visible.", "pt": "Em destaque: cenário base; base e cenário proposto permanecem visíveis."},
    "基線 · 合成參照": {"en": "Baseline · synthetic reference", "pt": "Base · referência sintética"},
    "合成情境": {"en": "Synthetic scenario", "pt": "Cenário sintético"},
    "審查狀態": {"en": "Review status", "pt": "Estado da revisão"},
    "17:00–18:00 · 展示窗口峰值 510 kW": {"en": "17:00–18:00 · displayed-window peak 510 kW", "pt": "17:00–18:00 · pico da janela apresentada: 510 kW"},
    "查看經濟與方案假設": {"en": "Review economic and schedule assumptions", "pt": "Consultar pressupostos económicos e do plano"},
    "光伏": {"en": "PV", "pt": "Fotovoltaico"},
    "參照": {"en": "Reference", "pt": "Referência"},
    "基線電網輸入": {"en": "Baseline grid import", "pt": "Importação da rede no cenário base"},
    "本展示窗口峰值 · 基線 → 候選": {"en": "Peak in this displayed window · baseline → candidate", "pt": "Pico desta janela apresentada · base → cenário proposto"},
    "ESS 放電 20 kW · SOC 40 → 17.778 kWh · HVAC −30 kW": {"en": "ESS discharge 20 kW · SOC 40 → 17.778 kWh · HVAC −30 kW", "pt": "Descarga do ESS 20 kW · SOC 40 → 17,778 kWh · AVAC −30 kW"},
    "03 · 同一能源平衡 · 不同安排": {"en": "03 · Same energy balance · different schedules", "pt": "03 · Mesmo balanço energético · planos diferentes"},
    "負荷 540 → 570 kW · PV 60 kW": {"en": "Load 540 → 570 kW · PV 60 kW", "pt": "Carga 540 → 570 kW · fotovoltaico 60 kW"},
    "合成情境：逐時段平均功率（kW）；18:00 為結束邊界": {"en": "Synthetic scenario: interval-average power (kW); 18:00 is the end boundary", "pt": "Cenário sintético: potência média por intervalo (kW); 18:00 é o limite final"},
    "電價與合約規則": {"en": "Tariff and contract rules", "pt": "Regras tarifárias e contratuais"},
    "負荷 570 → 570 kW · PV 85 kW": {"en": "Load 570 → 570 kW · PV 85 kW", "pt": "Carga 570 → 570 kW · fotovoltaico 85 kW"},
    "基線總負荷": {"en": "Baseline total load", "pt": "Carga total no cenário base"},
    "17:00 HVAC 回彈": {"en": "17:00 HVAC rebound", "pt": "Recuperação do AVAC às 17:00"},
    "基線 → 候選": {"en": "Baseline → candidate", "pt": "Base → cenário proposto"},
    "合成情境下的供能及負荷安排": {"en": "Supply and load schedules in a synthetic scenario", "pt": "Planos de fornecimento e carga num cenário sintético"},
    "總負荷 候選": {"en": "Total load · candidate", "pt": "Carga total · proposto"},
    "候選總負荷": {"en": "Candidate total load", "pt": "Carga total proposta"},
    "12時至18時，共六個一小時區間。曲線按區間平均功率繪成階梯，18時為時段結束邊界。候選總負荷在 15 至 16 時較基線少 30 kW，17 至 18 時因 HVAC 回彈增加 30 kW；候選17至18時的本展示窗口最高電網輸入為510 kW，基線最高為485 kW；該值不是計費周期 Pu；候選15至16時放電20 kW，16至17時充電24.691 kW，SOC由40降至17.778再回到40 kWh；效率為合成假設。全部為合成示例，並非設備控制、帳單結論或實際節省。": {"en": "12:00–18:00 comprises six one-hour intervals. Curves show interval-average power as steps, with 18:00 as the end boundary. Candidate total load is 30 kW below baseline from 15:00–16:00 and 30 kW higher from 17:00–18:00 due to HVAC rebound. Candidate grid import peaks at 510 kW during 17:00–18:00 in this displayed window, versus 485 kW for baseline; this is not billing-period Pu. The candidate discharges 20 kW at 15:00–16:00 and charges 24.691 kW at 16:00–17:00; SOC falls from 40 to 17.778 and returns to 40 kWh. Efficiency is synthetic. All values are illustrative, not equipment control, a bill conclusion, or actual savings.", "pt": "O período das 12:00 às 18:00 contém seis intervalos de uma hora. As curvas representam a potência média por intervalo em degraus, sendo 18:00 o limite final. A carga total proposta é 30 kW inferior à base das 15:00 às 16:00 e 30 kW superior das 17:00 às 18:00 devido à recuperação do AVAC. Nesta janela apresentada, a importação proposta atinge um máximo de 510 kW entre as 17:00 e as 18:00, face a 485 kW no cenário base; este valor não é o Pu do período de faturação. O cenário proposto descarrega 20 kW das 15:00 às 16:00 e carrega 24,691 kW das 16:00 às 17:00; o SOC desce de 40 para 17,778 e regressa a 40 kWh. A eficiência é sintética. Todos os valores são ilustrativos e não representam controlo de equipamentos, conclusão de fatura ou poupança real."},
    "小時平均功率 kW · 計費週期未核實 · 合成情境": {"en": "Hourly average power in kW · billing period unverified · synthetic scenario", "pt": "Potência média horária em kW · período de faturação não verificado · cenário sintético"},
    "回彈時段 +25 kW": {"en": "Rebound interval +25 kW", "pt": "Intervalo de recuperação +25 kW"},
    "窄屏可左右滑動曲線；完整逐時數值可開啟數據表。": {"en": "Scroll the curves horizontally on narrow screens; open the data table for complete interval values.", "pt": "Em ecrãs estreitos, desloque as curvas horizontalmente; abra a tabela para consultar todos os valores por intervalo."},
    "負荷 590 → 560 kW · PV 110 kW": {"en": "Load 590 → 560 kW · PV 110 kW", "pt": "Carga 590 → 560 kW · fotovoltaico 110 kW"},
    "ESS — · SOC 40 → 40 kWh · HVAC +30 kW 回彈": {"en": "ESS — · SOC 40 → 40 kWh · HVAC +30 kW rebound", "pt": "ESS — · SOC 40 → 40 kWh · recuperação do AVAC +30 kW"},
    "駁回建議": {"en": "Reject recommendation", "pt": "Rejeitar recomendação"},
    "可用性檢查": {"en": "Availability check", "pt": "Verificação de disponibilidade"},
    "相同資料快照": {"en": "Same input snapshot", "pt": "Mesmo instantâneo de dados"},
    "展示窗口峰值由485升至510 kW（+25 kW），出現在17:00–18:00回彈時段。這不是計費周期 Pu。計量窗口、當期已觀測 Pu、適用合同及完整賬期資料未提供，故本例不能推斷需求費或賬單影響；只呈現合成功率安排。HVAC時移不代表降低總用電；ESS充電令16:00–17:00電網輸入增至509.691 kW。": {"en": "The displayed-window peak rises from 485 to 510 kW (+25 kW) during the 17:00–18:00 rebound interval. This is not billing-period Pu. The measurement window, observed Pu for the current period, applicable contract, and complete billing-period data were not provided, so demand charges or bill impact cannot be inferred; only a synthetic power schedule is shown. HVAC shifting does not mean lower total energy use. ESS charging raises grid import to 509.691 kW from 16:00–17:00.", "pt": "O pico da janela apresentada sobe de 485 para 510 kW (+25 kW) no intervalo de recuperação das 17:00–18:00. Este valor não é o Pu do período de faturação. Não foram fornecidos a janela de medição, o Pu observado no período atual, o contrato aplicável nem os dados completos do período de faturação; por isso, não é possível inferir encargos de procura ou impacto na fatura. Apresenta-se apenas um plano de potência sintético. O deslocamento do AVAC não significa menor consumo total de energia. O carregamento do ESS eleva a importação da rede para 509,691 kW entre as 16:00 e as 17:00."},
    "總負荷 基線": {"en": "Total load · baseline", "pt": "Carga total · base"},
    "ESS 放電 候選": {"en": "ESS discharge · candidate", "pt": "Descarga do ESS · proposto"},
    "15:00–16:00 · ESS 放電 20 kW；SOC 40 → 17.778 kWh": {"en": "15:00–16:00 · ESS discharge 20 kW; SOC 40 → 17.778 kWh", "pt": "15:00–16:00 · descarga do ESS 20 kW; SOC 40 → 17,778 kWh"},
    "15–16時移出；17–18時回彈": {"en": "Shifted out of 15:00–16:00; rebounds at 17:00–18:00", "pt": "Deslocado das 15:00–16:00; recupera entre as 17:00–18:00"},
    "示意映射 · 未連接現場": {"en": "Illustrative mapping · no site connection", "pt": "Mapeamento ilustrativo · sem ligação ao local"},
    "查看資料就緒度 →": {"en": "View data readiness →", "pt": "Ver prontidão dos dados →"},
    "未提供現場負荷／光伏預測 · 不可生成正式最佳排程": {"en": "No site load/PV forecasts provided · a formal optimized schedule cannot be generated", "pt": "Sem previsões locais de carga/fotovoltaico · não é possível gerar um plano otimizado formal"},
    "儲能與負荷約束": {"en": "Storage and load constraints", "pt": "Restrições do armazenamento e das cargas"},
    "手機版逐時摘要 · 合成情境。完整欄位可開啟數據表；此處不代表預測或現場可行性。": {"en": "Mobile interval summary · synthetic scenario. Open the data table for all fields; this view is not a forecast or proof of site feasibility.", "pt": "Resumo móvel por intervalo · cenário sintético. Abra a tabela para ver todos os campos; esta vista não é uma previsão nem comprova a viabilidade no local."},
    "檢視數據表": {"en": "View data table", "pt": "Ver tabela de dados"},
    "方案比較": {"en": "Schedule comparison", "pt": "Comparação de planos"},
    "CEM 本計費期 Pu": {"en": "CEM Pu for this billing period", "pt": "Pu do CEM neste período de faturação"},
    "負荷 520 → 520 kW · PV 170 kW": {"en": "Load 520 → 520 kW · PV 170 kW", "pt": "Carga 520 → 520 kW · fotovoltaico 170 kW"},
    "ESS 容量/功率/SOC、效率與 HVAC 功率界限均為合成假設；舒適模型未建立": {"en": "ESS capacity/power/SOC, efficiency, and HVAC power limits are synthetic assumptions; no comfort model is defined", "pt": "Capacidade/potência/SOC e eficiência do ESS, bem como limites de potência do AVAC, são pressupostos sintéticos; não existe modelo de conforto"},
    "標記已閱": {"en": "Mark as reviewed", "pt": "Marcar como consultado"},
    "計量窗口與賬期峰值未提供": {"en": "Measurement window and billing-period peak not provided", "pt": "Janela de medição e pico do período de faturação não fornecidos"},
    "16:00–17:00 · ESS 充電 24.691 kW；SOC 17.778 → 40 kWh": {"en": "16:00–17:00 · ESS charge 24.691 kW; SOC 17.778 → 40 kWh", "pt": "16:00–17:00 · carregamento do ESS 24,691 kW; SOC 17,778 → 40 kWh"},
    "SOC 候選 kWh": {"en": "SOC · candidate · kWh", "pt": "SOC · proposto · kWh"},
    "HVAC 時移與回彈": {"en": "HVAC shifting and rebound", "pt": "Deslocamento e recuperação do AVAC"},
    "可左右滑動；聚焦表格後可用左右方向鍵查看完整欄位。": {"en": "Scroll horizontally; focus the table and use the left/right arrow keys to view all columns.", "pt": "Desloque horizontalmente; foque a tabela e use as setas esquerda/direita para ver todas as colunas."},
    "示意數據可核對；非現場驗證": {"en": "Illustrative data can be checked; not validated on site", "pt": "Os dados ilustrativos podem ser conferidos; não foram validados no local"},
    "負荷 550 → 550 kW · PV 145 kW": {"en": "Load 550 → 550 kW · PV 145 kW", "pt": "Carga 550 → 550 kW · fotovoltaico 145 kW"},
    "候選電網輸入": {"en": "Candidate grid import", "pt": "Importação da rede proposta"},
}


def git_blob_sha(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("catalog", type=Path)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    raw = args.source.read_bytes()
    actual = git_blob_sha(raw)
    if actual != SOURCE_BLOB:
        raise SystemExit(f"Source blob mismatch: expected {SOURCE_BLOB}, got {actual}")
    catalog: dict[str, Any] = json.loads(args.catalog.read_text(encoding="utf-8"))
    if catalog.get("source", {}).get("blob") != SOURCE_BLOB:
        raise SystemExit("Catalog does not reference the pinned v1.9 source blob.")

    counts = {stage: 0 for stage in TARGET_STAGES}
    missing: list[str] = []
    for message in catalog.get("messages", []):
        if message.get("stage") not in TARGET_STAGES:
            continue
        counts[message["stage"]] += 1
        translation = TRANSLATIONS.get(message["sourceText"])
        if translation is None:
            missing.append(message["key"])
            continue
        message["translations"].update(translation)
        message["translationReviewState"] = "DRAFT_NEEDS_MACAU_ENERGY_DOMAIN_REVIEW"

    if counts != EXPECTED_COUNTS:
        raise SystemExit(f"Unexpected source-unit counts for target stages: {counts}")
    if missing:
        raise SystemExit("Missing translation map entries for:\n" + "\n".join(missing))

    catalog["catalogVersion"] = "0.2.0-draft-batch"
    catalog["status"] = "PARTIAL_TRANSLATION_DRAFT_NOT_RUNTIME"
    catalog["defaultReviewState"] = "MISSING_OR_DRAFT_REQUIRES_HUMAN_REVIEW"
    catalog["translationBatch"] = {
        "sourceBlob": SOURCE_BLOB,
        "stages": ["shell", "evidence-check", "site-model", "dispatchComparison"],
        "unitCount": sum(counts.values()),
        "state": "AI_ASSISTED_DRAFT_NOT_REVIEWED_BY_MACAU_DOMAIN_SPECIALIST",
        "portugueseVariant": "UNRESOLVED",
        "runtimeWiring": "NONE",
        "remainingLocaleApproval": "UNRESOLVED",
    }
    catalog["extraction"]["limitations"].append(
        "This draft batch covers shell, evidence-check, site-model, and dispatchComparison units only. Constraint-analysis, shadow-review, outcome-replay, and dynamic interaction messages remain untranslated; do not use this catalog as runtime localization."
    )
    args.output.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote review-only draft: {sum(counts.values())} units; {counts}; source {actual}")


if __name__ == "__main__":
    main()

