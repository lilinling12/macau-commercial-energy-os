"""Complete the remaining v1.9 locale draft units for human review.

This creates a separate review artifact; it does not modify the source HTML,
wire translations at runtime, or establish an approved locale policy.
"""
from __future__ import annotations

import copy
import json
from pathlib import Path

ROOT = Path(__file__).parent
DATA = ROOT.parent if ROOT.name == "tools" else ROOT
SOURCE_CATALOG = DATA / "locale-catalog-draft-core-v0.2.json"
OUTPUT = DATA / "locale-catalog-draft-full-workflow-v0.3.json"

# key suffix -> (English draft, neutral Portuguese draft)
TRANSLATIONS = {
    "0943908e8c": ("Item", "Item"),
    "0c9bd6277c": ("Required evidence", "Evidência necessária"),
    "0e3c2968bc": ("Next: review the SHADOW recommendation ↓", "Seguinte: rever a recomendação SHADOW ↓"),
    "0f38b68739": ("4 of 6 intervals have precise, verified tariffs", "4 de 6 intervalos têm tarifas precisas e verificadas"),
    "1e247ae803": ("EV charging cost allocation", "Imputação do custo de carregamento de VE"),
    "217c9174a4": ("Not covered", "Não abrangido"),
    "22d49a1ced": ("Charger service meter, account, effective contract/tariff, and matching bill", "Contador do serviço de carregamento, conta, contrato/tarifa em vigor e fatura correspondente"),
    "23066572fc": ("Synthetic score · unverified", "Pontuação sintética · não verificada"),
    "23cc36863e": ("Applicable meter configuration, contract, and matched bill", "Configuração do contador aplicável, contrato e fatura correspondente"),
    "246409376b": ("Observed maximum to date, complete billing-period boundary, and subsequent-period data", "Máximo observado até à data, limites do período de faturação completo e dados do período seguinte"),
    "25860c501c": ("Do not assume the building's applicable tariff or cost-allocation rules", "Não presumir a tarifa aplicável ao edifício nem as regras de imputação de custos"),
    "286fbe0bc6": ("Pu averaging interval", "Intervalo de média de Pu"),
    "2d4a3f86d8": ("Display-window power must not be treated as Pu", "A potência na janela apresentada não deve ser tratada como Pu"),
    "33cc05f28d": ("This prototype has not solved an optimal plan or verified HVAC comfort or ESS feasibility.", "Este protótipo não calculou um plano ótimo nem verificou o conforto do AVAC ou a viabilidade do ESS."),
    "35175fbf84": ("Covered", "Abrangido"),
    "359de44d2d": ("Equipment ratings, SOC trajectory, and safety reserve", "Potências nominais dos equipamentos, trajetória do SOC e reserva de segurança"),
    "40b0244b67": ("Tariff / effective period / account association", "Tarifa / período de vigência / associação à conta"),
    "469adf8de6": ("Parameter consistency can be checked; this does not establish an operable site schedule", "É possível verificar a consistência dos parâmetros; isso não comprova que o horário seja executável no local"),
    "46f275b08e": ("Customer contract, tariff, and meter-to-account mapping", "Contrato do cliente, tarifa e associação do contador à conta"),
    "4d8c1c5b42": ("Unknown", "Desconhecido"),
    "50d2bb615a": ("Complete billing rules, Pu interval, and evidence for the billing period", "Regras completas de faturação, intervalo de Pu e evidência do período de faturação"),
    "5a1ab1da22": ("Approved operating limits and site data", "Limites operacionais aprovados e dados do local"),
    "5a4ddc887e": ("Bill-level cost BLOCKED", "Custo ao nível da fatura BLOQUEADO"),
    "65c83dfb47": ("Illustrative", "Ilustrativo"),
    "6a71a42e6e": ("; 2 other intervals are excluded because no valid tariff is available. This example contains no energy, tariff, or monetary amount, so no total is shown.", "; 2 outros intervalos são excluídos por não existir uma tarifa válida. Este exemplo não contém energia, tarifa ou montante monetário, pelo que não apresenta um total."),
    "6cf9d4b3e7": ("HVAC comfort / service limits", "Limites de conforto / serviço do AVAC"),
    "756762e293": ("Not provided", "Não fornecido"),
    "7d379fe28e": ("Physical scenario increases by 25 kW; this is not Pu", "O cenário físico aumenta 25 kW; isto não corresponde a Pu"),
    "803cf6fa19": ("Candidate feasibility unverified", "Viabilidade da alternativa não verificada"),
    "872f4852ac": ("Cannot determine whether the candidate changes this period's demand charge", "Não é possível determinar se a alternativa altera a componente de potência deste período"),
    "94f6fe9111": ("ESS SOC / efficiency / losses", "SOC / eficiência / perdas do ESS"),
    "95b51ad6fa": ("An unknown limit must not be treated as zero, unlimited, or permissive. Candidate results must identify blockers, applicable intervals, source, version, and review status.", "Um limite desconhecido não deve ser tratado como zero, ilimitado ou permissivo. Os resultados da alternativa devem identificar impedimentos, intervalos aplicáveis, fonte, versão e estado de revisão."),
    "9613751d3e": ("04 · Cost, constraints, and evidence", "04 · Custos, restrições e evidências"),
    "98c3614dd5": ("Only precisely matched intervals may be priced", "Só podem ser valorizados os intervalos correspondentes com precisão"),
    "a02c315c7c": ("State the reason; do not replace unknown with zero", "Indicar o motivo; não substituir desconhecido por zero"),
    "a273293ba6": ("Current status", "Estado atual"),
    "b1de15a21a": ("Unverified", "Não verificado"),
    "bfb1bccce7": ("Without economic evidence, allow only a named physical/scenario comparison; show no bill amount, cost saving, or investment return.", "Sem evidência económica, permitir apenas uma comparação física/de cenários identificada; não apresentar valor de fatura, poupança de custos ou retorno do investimento."),
    "c2c00bc245": ("Display-window maximum import", "Importação máxima na janela apresentada"),
    "c64978fd09": ("Observed Pu for this billing period", "Pu observado neste período de faturação"),
    "d4c768415b": ("Status examples · synthetic UI states, not the schedule above", "Exemplos de estado · estados sintéticos da interface, não correspondem ao horário acima"),
    "d5201a5cfe": ("An interval improvement is not a billing-period or economic improvement.", "Uma melhoria num intervalo não equivale a uma melhoria no período de faturação nem a um benefício económico."),
    "d65b981e05": ("Cost and constraint status · synthetic scenario", "Estado dos custos e das restrições · cenário sintético"),
    "d9bc928777": ("Do not claim optimization when constraint evidence is missing", "Não afirmar que houve otimização quando faltam evidências sobre as restrições"),
    "ec104d139a": ("Demand charge/Pu, full bill, export revenue, and savings each require their own metering, contract, and settlement evidence.", "A componente de potência/Pu, a fatura completa, a receita de injeção e as poupanças exigem, cada uma, evidência própria de medição, contrato e liquidação."),
    "f319aa5cd4": ("Imported-energy charge component · PARTIAL", "Componente de custo da energia importada · PARCIAL"),
    "f5f03f9819": ("Impact", "Impacto"),
    "fd52237654": ("The candidate reduces grid import in the 15:00–16:00 interval, but rebound raises the maximum grid import in this display window by 25 kW; billing-period Pu is unknown. This change is not converted into a cost.", "A alternativa reduz a importação da rede no intervalo 15:00–16:00, mas o efeito de recuperação aumenta em 25 kW a importação máxima nesta janela apresentada; o Pu do período de faturação é desconhecido. Esta variação não é convertida em custo."),
    "067ee2fb89": ("The illustrative state on this page changed; no audit record, authorization, or equipment action was written. It resets on reload.", "O estado ilustrativo desta página foi alterado; não foi registado qualquer evento de auditoria, autorização ou ação sobre equipamentos. É reposto ao recarregar."),
    "127a9f6fef": ("Stage navigation", "Navegação por etapas"),
    "22e6ea36aa": ("The illustrative state on this page changed; no evidence task was created and nothing was written to the audit log. It resets on reload.", "O estado ilustrativo desta página foi alterado; não foi criada nenhuma tarefa de evidência nem escrito qualquer registo de auditoria. É reposto ao recarregar."),
    "3883693e6f": ("Collapse data table", "Recolher tabela de dados"),
    "3b8ea8693a": ("Illustrative evidence request; not submitted.", "Pedido ilustrativo de evidência; não submetido."),
    "3d1d1440f8": ("Request evidence · page-only example", "Solicitar evidência · exemplo apenas nesta página"),
    "55f480cfcb": ("Candidate schedule", "Horário alternativo"),
    "584ba1dbdb": ("; the other series remains visible for direct comparison.", "; a outra série continua visível para comparação direta."),
    "7ea7965a02": ("← Previous stage", "← Etapa anterior"),
    "85f825dc7a": ("Chart emphasis updated; this changes this page's display only and is not saved or executed.", "Destaque do gráfico atualizado; altera apenas a apresentação nesta página e não é guardado nem executado."),
    "8c267223ce": ("Currently highlighted:", "Em destaque:"),
    "9552fe3bd3": ("Stage ", "Etapa "),
    "9b93fa0713": ("The illustrative state on this page changed; nothing was saved, no recommendation was changed, and no equipment was controlled. It resets on reload.", "O estado ilustrativo desta página foi alterado; nada foi guardado, nenhuma recomendação foi alterada e nenhum equipamento foi controlado. É reposto ao recarregar."),
    "a49a4e75dd": ("Dismiss · page-only example", "Rejeitar · exemplo apenas nesta página"),
    "c8dfa2a7ee": ("Baseline", "Referência"),
    "ce072e6939": ("Reviewed · page-only example", "Revisto · exemplo apenas nesta página"),
    "d2e6398581": ("View data table", "Ver tabela de dados"),
    "ea8c4ca558": ("Illustrative dismissal; not submitted.", "Rejeição ilustrativa; não submetida."),
    "f1deeff5c7": ("Illustrative review; not submitted.", "Revisão ilustrativa; não submetida."),
    "f8060364c7": (" Stage<strong>", " Etapa<strong>"),
    "fea1a5d500": ("Next stage →", "Etapa seguinte →"),
    "04c38c1cea": ("Forecasts, external actions, and measured outcomes are recorded separately.", "As previsões, as ações externas e os resultados medidos são registados separadamente."),
    "22c66c1cc1": ("Not calculable · customer-approved baseline and measurement period missing", "Não calculável · falta uma linha de base aprovada pelo cliente e o período de medição"),
    "25ede92cbd": ("Snapshot identity:", "Identificador do instantâneo:"),
    "328eae461a": ("Not authorized or executed · this MVP boundary is SHADOW", "Não autorizado nem executado · o limite deste MVP é SHADOW"),
    "3a64a3ee71": ("Return to data qualification ↑", "Voltar à validação dos dados ↑"),
    "503e0f7fa9": ("Site outcome", "Resultado no local"),
    "717b7d2cec": ("Equipment action", "Ação sobre equipamento"),
    "9918258ad8": ("Savings / M&V", "Poupanças / M&V"),
    "9fd52c372f": ("06 · Outcome monitoring and replay", "06 · Monitorização de resultados e reprodução"),
    "bd0cd71bcc": ("Same site, time zone, and intervals; input-data snapshot and quality; contract/rule version (if applicable); model/forecast/optimizer versions; candidate and constraints; human review status; subsequent independent action receipt and measurement window.", "Mesmo local, fuso horário e intervalos; instantâneo e qualidade dos dados de entrada; versão do contrato/regra (se aplicável); versões do modelo/previsão/otimizador; alternativa e restrições; estado da revisão humana; comprovativo independente da ação posterior e janela de medição."),
    "cd841e97ed": ("Not implemented · this static prototype has no input snapshot ID, version lock, or durable replay. A production system should show “replay unavailable/incomplete” when the original snapshot is missing; it must not substitute the latest data.", "Não implementado · este protótipo estático não tem identificador do instantâneo de entrada, bloqueio de versões ou reprodução persistente. Um sistema de produção deve indicar “reprodução indisponível/incompleta” quando falta o instantâneo original; não deve substituí-lo pelos dados mais recentes."),
    "d76f379e87": ("Not yet measured · no customer-site data", "Ainda não medido · sem dados de um local do cliente"),
    "dd87272c6b": ("Immutable evidence required for replay", "Evidência imutável necessária para reprodução"),
    "e1ecec8d97": ("There is currently no site connection, execution record, or agreed M&V baseline; therefore this view shows blockers and future data needs rather than inventing monitoring results.", "Atualmente não existe ligação ao local, registo de execução nem linha de base de M&V acordada; por isso, esta vista mostra impedimentos e dados necessários no futuro, sem inventar resultados de monitorização."),
    "fc758b0b05": ("No site execution or measurement records; this screen replays synthetic example data only.", "Sem registos de execução ou medição no local; este ecrã reproduz apenas dados de exemplo sintéticos."),
    "ff04ab8c77": ("Current replay status:", "Estado atual da reprodução:"),
    "2678e06a65": ("05 · SHADOW recommendation review", "05 · Revisão da recomendação SHADOW"),
    "2f8c2f569f": ("Candidate summary", "Resumo da alternativa"),
    "3abc6fe48c": ("This prototype can switch among three illustrative page states: reviewed, evidence requested, and dismissed; a reload resets them. A production system must persist the audit record and bind it to an authenticated identity.", "Este protótipo permite alternar entre três estados ilustrativos da página: revisto, evidência solicitada e rejeitado; ao recarregar, os estados são repostos. Um sistema de produção deve persistir o registo de auditoria e associá-lo a uma identidade autenticada."),
    "3be5ee01a0": ("This prototype can change a review state on the page; reloading clears it. It does not save or send commands, and does not mean anyone approved the actual site plan.", "Este protótipo permite alterar o estado de revisão na página; ao recarregar, o estado é apagado. Não guarda dados nem envia comandos, e não significa que alguém tenha aprovado o plano real do local."),
    "767698ae39": ("Use the “Record illustrative review (page only)” button on the right; the state appears immediately and is not persisted.", "Use o botão “Registar revisão ilustrativa (apenas nesta página)” à direita; o estado aparece imediatamente e não é persistido."),
    "7e9dc38a73": ("Record illustrative review in the candidate panel", "Registar revisão ilustrativa no painel da alternativa"),
    "b28346dc84": ("Grid import in the 15:00–16:00 scenario interval falls by 50 kW; the candidate display-window maximum rises from 485 to 510 kW; billing-period Pu remains unknown. HVAC rebounds by +30 kW; contract cost, comfort, and equipment response are unverified; SOC/efficiency are integrated from synthetic parameters only, not field evidence.", "A importação da rede no intervalo de cenário das 15:00–16:00 diminui 50 kW; o máximo apresentado para a alternativa aumenta de 485 para 510 kW; o Pu do período de faturação continua desconhecido. O AVAC recupera +30 kW; o custo contratual, o conforto e a resposta dos equipamentos não foram verificados; o SOC/eficiência são calculados apenas a partir de parâmetros sintéticos, sem evidência de campo."),
    "d761ff771f": ("Available review actions:", "Ações de revisão disponíveis:"),
    "e6c1ac9865": ("Jump to review controls ↓", "Ir para os controlos de revisão ↓"),
    "ff2a75beaa": ("A review is traceable feedback, not control authorization.", "Uma revisão é um comentário rastreável, não uma autorização de controlo."),
}


def main() -> None:
    catalog = json.loads(SOURCE_CATALOG.read_text(encoding="utf-8"))
    draft = copy.deepcopy(catalog)
    missing = [m for m in draft["messages"] if not m["translations"].get("en") or not m["translations"].get("pt")]
    expected = {m["key"].rsplit(".", 1)[-1] for m in missing}
    if expected != set(TRANSLATIONS):
        raise SystemExit(f"Translation key mismatch: missing={sorted(expected-set(TRANSLATIONS))}; extra={sorted(set(TRANSLATIONS)-expected)}")
    for message in missing:
        en, pt = TRANSLATIONS[message["key"].rsplit(".", 1)[-1]]
        message["translations"]["en"] = en
        message["translations"]["pt"] = pt
        message["reviewState"] = "DRAFT_NEEDS_MACAU_ENERGY_DOMAIN_AND_LANGUAGE_REVIEW"
    draft["catalogVersion"] = "0.3.0-full-workflow-translation-draft"
    draft["status"] = "AI-assisted complete-coverage draft; human Macau Portuguese and energy-domain review required; not runtime localization or approved locale policy."
    draft["defaultReviewState"] = "DRAFT_NEEDS_MACAU_ENERGY_DOMAIN_AND_LANGUAGE_REVIEW"
    draft["translationBatch"] = {
        "scope": "All 337 extracted contextual units across shell, data qualification, site model, dispatch comparison, constraints/economics, SHADOW review, outcome replay, and dynamic interaction messages.",
        "newlyDraftedUnitsPerLocale": 95,
        "priorDraftSource": "locale-catalog-draft-core-v0.2.json (242/337 units per target locale)",
        "locales": {"en": "English draft", "pt": "Portuguese draft; Macau regional terminology and variant require specialist review"},
        "runtimeIntegrated": False,
        "ownerLocaleApproval": False,
    }
    OUTPUT.write_text(json.dumps(draft, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(OUTPUT)
    print(f"Added {len(missing)} contextual units x 2 target locales; total catalog units: {len(draft['messages'])}.")


if __name__ == "__main__":
    main()
