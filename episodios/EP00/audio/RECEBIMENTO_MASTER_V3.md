# EP00 — Recebimento e análise técnica do master V3

Arquivo recebido do usuário: EP00_MASTER_VOZ_v3.wav. O arquivo com sufixo “(1)” é idêntico byte a byte.
SHA-256: 8e3c8eb42a503d13d2381db2f2215598b297407cdd9fd9bee862a7e16652056e.

- Duração medida: 40,862708333 segundos.
- 1.961.410 amostras; PCM, 48 kHz, 24-bit, mono.
- Pico amostral: aproximadamente 0 dBFS (−0,000001 dBFS); três amostras atingem o máximo positivo de 24-bit. Isso diverge do pico −1,5 dB informado na documentação anterior. Não equivale à medição de true peak nem confirma distorção audível.
- RMS global: −16,8643 dBFS; esta medida não é LUFS.
- Master preservado integralmente, sem alteração de ganho, EQ, velocidade ou cortes.
- A 30 fps, usar pelo menos 1.226 quadros (40,866667 s) para cobrir integralmente a duração do áudio.

## Pausas candidatas para revisão
Análise RMS por janelas de 10 ms, limiar −38 dBFS, duração mínima 150 ms.
Pausas próximas de transições previstas: 14,39–14,82; 15,88–16,20; 23,72–24,06; 32,31–32,76; 35,14–35,49; 36,66–36,95; 38,90–39,24; 39,72–39,91 s.
Trecho final de baixa energia: 40,57–40,862708 s. Preservar todo o trecho, que pode conter cauda acústica.
Esses intervalos não são transcrição ou cortes aprovados. Não atribuir palavras a eles sem ouvir a gravação. Os tempos internos das oito cenas continuam provisórios.

## Pacote e importação
ZIP contém WAV V3, preview M4A, comparação do final V2/V3 e LEIA-ME_V3.txt. O texto do pacote descreve a recuperação de “vamos conferir” e sua cauda; não contém uma EDL ou transcrição alinhada.
Cópia local de trabalho e ANALISE_MASTER_V3.json criadas na pasta de áudio do projeto.
Importação do WAV no Canva pelo conector falhou: import_failed / Failed To Convert File Format. Nenhum asset de áudio foi criado nessa tentativa e nenhum áudio foi inserido no design.
O binário permanece local. O GitHub recebe somente este registro.
Próxima etapa: conferência auditiva e transcrição alinhada, importação do áudio no editor de vídeo e ajuste das cenas ao master, preservando a locução humana.
