# EP00 — Montagem de voz v1

**Data:** 28/09/2026  
**Duração final:** 40,557 s  
**Objetivo:** master de voz seco, sem trilha e sem efeitos, pronto para sincronização com o storyboard.

## Sequência escolhida

### 1. Abertura / gancho + GNSS/IMU/laser + imagem/medição
- Fonte: `Nova Gravação 16.m4a`
- Corte aproximado: **00:00.740 → 00:16.610**
- Motivo: melhor encaixe temporal para os três primeiros blocos sem acelerar artificialmente a fala.

### 2. LiDAR/SLAM + terraplanagem 3D
- Fonte: `Track 10.m4a`
- Corte aproximado: **00:01.060 → 00:17.250**
- Motivo: melhor tomada técnica para o bloco; dicção clara e linguagem coerente com o vídeo.

### 3. Novo fluxo + assinatura + CTA
- Fonte: `Track 21.m4a`
- Montagem frase a frase.
- Ordem:
  1. “O levantamento…”
  2. “já não termina mais no desenho.”
  3. “Topografia em campo.”
  4. “Tecnologia na medida certa.”
  5. “Vem comigo.”
  6. “Vamos conferir.”
- As pausas longas da gravação foram encurtadas, mantendo o ritmo natural da voz.

## Tratamento do master
- 48 kHz
- mono
- WAV 24-bit para master
- AAC 192 kb/s para preview
- loudness de produção próximo de **-16 LUFS**
- true peak máximo **-1,5 dBFS**
- sem compressão agressiva
- sem trilha / SFX nesta versão

## Arquivos de saída
- `EP00_MASTER_VOZ_v1.wav`
- `EP00_PREVIEW_VOZ_v1.m4a`

Os binários são mantidos no pacote de produção enquanto a edição é validada. Esta documentação registra a montagem na branch `audio/ep00-selecao`.

## Observação editorial
A `Nova Gravação 17 cópia.m4a` continua preservada como referência de interpretação. Para esta montagem, a `Nova Gravação 16.m4a` foi escolhida na abertura por permitir atingir a duração de 40–42 s com mais naturalidade.
