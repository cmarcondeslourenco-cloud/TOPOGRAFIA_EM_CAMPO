# EP00 — Montagem de voz V2

Data: 28/09/2026

## Motivo da revisão
Após ouvir o master V1, o primeiro trecho apresentou timbre excessivamente grave em relação aos blocos seguintes.

## Diagnóstico
A diferença não era apenas de volume. O primeiro trecho tinha menos presença na faixa aproximada de 1–2 kHz e mais sensação de baixo-médio, destacando a troca de gravação na passagem para o Track 10.

## Correção aplicada somente no primeiro trecho
- filtro passa-altas suave em ~78 Hz;
- redução em ~170 Hz e ~350 Hz;
- recuperação gradual de presença em ~750 Hz;
- reforço controlado em ~1,3 kHz e ~2,2 kHz;
- leve recuperação de definição em ~3,6 kHz;
- limiter conservador, com teto de -1,5 dBFS;
- sem alteração de velocidade da fala;
- demais trechos preservados.

## Sequência mantida
1. Nova Gravação 16 — abertura + GNSS/IMU/laser + imagem/medição
2. Track 10 — LiDAR/SLAM + terraplanagem
3. Track 21 — novo fluxo + assinatura + CTA

## Resultado
- duração: ~40,56 s;
- 48 kHz mono;
- master WAV 24-bit;
- preview AAC;
- loudness medido da V2: aproximadamente -17,3 LUFS;
- pico máximo: -1,5 dBFS.

A V2 deve ser validada por audição antes de qualquer trilha ou efeito.