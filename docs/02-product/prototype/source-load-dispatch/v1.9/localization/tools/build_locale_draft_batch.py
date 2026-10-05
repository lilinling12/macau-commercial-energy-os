#!/usr/bin/env python3
"""Build an unreviewed translation batch for v1.9 shell + evidence review.

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
TARGET_STAGES = {"shell", "evidence-check"}
EXPECTED_COUNTS = {"shell": 65, "evidence-check": 43}
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

    catalog["catalogVersion"] = "0.1.0-draft-batch"
    catalog["status"] = "PARTIAL_TRANSLATION_DRAFT_NOT_RUNTIME"
    catalog["defaultReviewState"] = "MISSING_OR_DRAFT_REQUIRES_HUMAN_REVIEW"
    catalog["translationBatch"] = {
        "sourceBlob": SOURCE_BLOB,
        "stages": ["shell", "evidence-check"],
        "unitCount": sum(counts.values()),
        "state": "AI_ASSISTED_DRAFT_NOT_REVIEWED_BY_MACAU_DOMAIN_SPECIALIST",
        "portugueseVariant": "UNRESOLVED",
        "runtimeWiring": "NONE",
        "remainingLocaleApproval": "UNRESOLVED",
    }
    catalog["extraction"]["limitations"].append(
        "This draft batch translates only shell and evidence-check units. Other workflow stages remain untranslated; do not use this catalog as runtime localization."
    )
    args.output.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote review-only draft: {sum(counts.values())} units; {counts}; source {actual}")


if __name__ == "__main__":
    main()

