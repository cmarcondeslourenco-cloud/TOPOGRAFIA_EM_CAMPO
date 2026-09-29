# EP00 V3 — Storyboard técnico vertical
Data: 28/09/2026. Direção: documental realista, moderna, técnica.
Status: storyboard de pré-produção; não é vídeo renderizado nem sincronização final.

## Referência editorial e sonora
Base Git: audio/ep00-selecao, commit 374bbb061eecef923ac244e09e7a67f914cfd6c0.
Fontes lidas: roteiros/EP00_a_topografia_esta_mudando.md; roteiros/EP00_locucao_42s.md; episodios/EP00/audio/MONTAGEM_VOZ_V1.md e MONTAGEM_VOZ_V3.md; planejamento/EP00_plano_producao_fontes.md.
A voz humana EP00_MASTER_VOZ_v3.wav é a referência principal. Duração DOCUMENTADA ~40,86 s; 48 kHz mono, WAV 24-bit. O arquivo binário não foi acessado nesta sessão. Não afirmar duração medida, transcrição integral ou sincronismo verificado.
Os roteiros escritos antecedem o encerramento gravado. Manter o encerramento documentado: “O levantamento… já não termina mais no desenho. Topografia em campo. Tecnologia na medida certa. Vem comigo. Vamos conferir.”
Não inserir a fala antiga “Aqui vamos mostrar...” ou nova voz. Legendas só após ouvir/transcrever o WAV.
A V1 documenta aproximadamente 15,87 s da primeira fonte e 16,19 s da segunda; usamos esses comprimentos apenas para orientar os blocos de 15,90 e 32,10 s. Emendas e pausas podem deslocá-los.

## Formato e identidade
1080 × 1920, 9:16. Proposta: 30 fps, conferir cadência dos materiais antes da montagem.
Paleta proposta: grafite #17232B, branco #F5F7F8 e ciano #26B9D1; cores naturais do campo preservadas. Não é um kit de marca já aprovado.
Tipografia sem serifa legível, títulos curtos; sem interfaces futuristas, hologramas ou anime.
Área de trabalho conservadora para textos: x=90–900 e y=180–1550 em 1080×1920; ajustar às interfaces da plataforma de publicação.
Textos, setas, rótulos e identidade em camadas editáveis no Canva. Imagens geradas não devem produzir números, coordenadas ou logotipos.
Prioridade de material: filmagem própria disponível → material oficial autorizado → ilustração gerada identificada como tal.
Não apresentar uma ilustração de IA como demonstração comprovada de equipamento.

## Storyboard técnico — tempos PROVISÓRIOS
| ID | Janela estimada | Duração | Referência de voz/conteúdo | Plano e tratamento | Texto |
|---|---|---:|---|---|---|
| S01 | 00,00–04,50 | 4,50 s | Gancho do roteiro: estação total, GPS, haste; “olha isso” a conferir no WAV | Campo → close rover → estação total; corte seco para terreno digital no gatilho da fala | A TOPOGRAFIA ESTÁ MUDANDO |
| S02 | 04,50–12,00 | 7,50 s | Bloco GNSS/IMU/laser; texto exato a conferir | Operador afastado da borda; plano médio + detalhe do alvo. Linha vetorial explicativa adicionada em pós, sem simular feixe visível real | GNSS + IMU + LASER |
| S03 | 12,00–15,90 | 3,90 s | Câmeras e pontos difíceis; texto exato a conferir | Sobre ombro no controlador; inserir associação foto/ponto com interface real autorizada ou esquema claramente identificado | IMAGEM + POSICIONAMENTO |
| S04 | 15,90–24,00 | 8,10 s | Track 10: LiDAR/SLAM; texto exato a conferir | Operador caminha; corte correspondente para nuvem de pontos da mesma geometria, real ou rotulada como ilustração | LiDAR • SLAM • 3D |
| S05 | 24,00–32,10 | 8,10 s | Track 10: terraplanagem, RTK e modelo digital | Plano lateral da motoniveladora; corte para superfície de projeto. CORTE/ATERRO sem valores fictícios | RTK + MODELO DIGITAL |
| S06 | 32,10–35,20 | 3,10 s | “O levantamento… já não termina mais no desenho.” | Três estados gráficos da mesma área: pontos, TIN, obra. Transições internas discretas | CAMPO → MODELO → OBRA |
| S07 | 35,20–38,20 | 3,00 s | “Topografia em campo. Tecnologia na medida certa.” | Assinatura sobre campo desfocado, composição estável | TOPOGRAFIA EM CAMPO / Tecnologia na medida certa |
| S08 | 38,20–40,86 | 2,66 s | “Vem comigo. Vamos conferir.” | Sustentar cartela até a cauda acústica final; não encurtar a última palavra | VAMOS CONFERIR |

Soma das janelas: 40,86 s. Isso verifica apenas a soma do planejamento.
A 30 fps, 40,86 s não corresponde a um número inteiro de quadros. Se o WAV confirmar esse fim, usar pelo menos 1226 quadros (~40,867 s), sem cortar o áudio para arredondar.
Ajustar cortes visuais às palavras e pausas reais; a voz não é acelerada nem remontada para caber nestas janelas.

## Movimento, transições e som
| ID | Movimento proposto | Saída | Material/fonte desejada | SFX opcionais |
|---|---|---|---|---|
| S01 | aproximação curta e estável; montagem de inserts | corte seco na ênfase vocal | campo próprio e equipamentos reais | clique discreto no corte |
| S02 | câmera fixa ou avanço mínimo; operador estável | corte por correspondência do alvo | demonstração autorizada GNSS/IMU/laser; candidato já registrado: ComNav Mercury | sinal suave de ponto, fora da sílaba |
| S03 | detalhe fixo; marcador vetorial entra uma vez | corte seco | vídeo próprio ou interface oficial com compatibilidade confirmada | toque curto opcional |
| S04 | acompanhamento lento; uma ação por plano | corte para modelo | scanner móvel real e nuvem correspondente; candidato registrado: NavVis VLX | ambiência baixa, sem som de “laser” inventado |
| S05 | tomada lateral lenta, máquina fisicamente coerente | correspondência terreno/modelo | controle de máquina real autorizado; candidatos: Leica iCON iGG3 / Topcon 3D-MC | máquina muito baixa sob voz |
| S06 | animação gráfica determinística, três estados | corte limpo para assinatura | gráfico próprio | transição discreta opcional |
| S07 | fundo quase estático | manter mesma composição | identidade tipográfica própria | nenhum destaque sonoro sobre marca |
| S08 | sustentar imagem | último quadro cobre cauda vocal | cartela própria | sem fade que corte “conferir” |

Os fabricantes acima são candidatos do plano existente, não materiais baixados ou licenças confirmadas. Confirmar produto/recurso e autorização antes de usar; registrar URL, titular, permissão e trecho. Para imagem/medição, revisar especialmente a combinação produto/software citada no plano antes de atribuir a um modelo.
Música é opcional; começar pela montagem com voz seca. Se adicionada, reduzir sob a voz e preservar inteligibilidade. Não normalizar ou equalizar novamente o master por padrão. Descartar qualquer fala ou música nativa dos clipes gerados na montagem final.

## Prompts de imagem e movimento — Screel/PixVerse
Parâmetros de geração e duração são configurados fora do prompt. São propostas, nenhuma mídia foi gerada.
Cada plano usa sua própria referência aprovada. Um produto identificável exige referência do equipamento; não inventar aparência nem marca.
Para animar, pedir uma tomada contínua com movimento contido, geometria estável, sem fala, sem música, sem texto. Silenciar a trilha do clipe no editor mesmo se o modelo devolver áudio.
### S01
Imagem:
Vertical 9:16, realistic contemporary documentary photograph of a survey site in Brazil, a total station on a stable tripod in foreground, natural earth textures, soft daylight, restrained graphite and cyan palette, no text, no logos, physically accurate equipment. Space in upper third for title. No anime.

Movimento: Slow subtle push-in toward the surveying setup. Stable tripod and equipment. One continuous shot, no morphing, no speaking, no music, no text.

### S02
Imagem:
Vertical 9:16 realistic documentary still, survey professional wearing hard hat and high visibility vest standing safely on firm ground away from an excavation edge, using a surveying pole and controller, excavation visible beyond, natural daylight, accurate human anatomy and plausible equipment, no visible laser beam, no text or logos, no futuristic holograms.

Movimento: Minimal camera drift. Professional remains safely on firm ground, hands and equipment stable. No visible beam. No speaking, music or text.

### S03
Imagem:
Vertical 9:16 realistic over shoulder close view of a survey professional holding a rugged field controller, terrain and an inaccessible target in background, controller screen blank and dark for compositing, natural light, no generated interface, no text, no logos, stable natural hands.

Movimento: Nearly static over-shoulder shot, controller and hands remain stable. No changing interface. No speaking, music or text.

### S04
Imagem:
Vertical 9:16 photorealistic industrial surveying environment, professional seen from behind walking slowly along a warehouse aisle with a mobile mapping scanner, realistic scale and soft industrial light, consistent geometry, no text, no logos, no glowing laser beams. Use an approved equipment reference for any named product.

Movimento: Slow tracking movement behind the walking operator. Preserve scanner shape and warehouse geometry. No speaking, music or text.

### S05
Imagem:
Vertical 9:16 realistic wide documentary view of a motor grader slowly leveling soil at a Brazilian construction site, plausible blade contact with the ground, soft daylight, grounded heavy machinery proportions, dust subtle, no operators near moving machine, no text or logos, room for a simple overlay.

Movimento: Slow lateral camera movement with the grader moving steadily, blade in plausible ground contact. No morphing, speaking, music or text.

### S06
Imagem:
Vertical 9:16 clean realistic terrain plate viewed obliquely from above, graded earth with a gentle embankment and road alignment, natural soil material, simple readable geometry, soft daylight, no text or graphic overlays, composition suitable for matching a digital terrain mesh in postproduction.

Movimento: Static plate; animate points and terrain mesh as editable graphics in postproduction.

### S07
Imagem:
Vertical 9:16 realistic survey landscape at soft daylight, subtle out of focus tripod silhouette near one edge, uncluttered graphite toned lower area, open central space for title added in postproduction, no text, no logos.

Movimento: Very subtle background drift; title added in Canva. No speaking, music or generated text.

### S08
Imagem:
Vertical 9:16 photorealistic close detail of a survey receiver against softly blurred terrain, modern restrained documentary look, soft daylight, stable equipment geometry, no text, no logos, no dramatic light effects. Reserve center for postproduction invitation.

Movimento: Hold a stable equipment detail and leave the ending still. No speaking, music or text.


## Fluxo e responsabilidades
1. GitHub: roteiro, storyboard, prompts, manifesto de fontes e registro das versões. Branch storyboard/ep00-v3-vertical criada a partir da V3. Toda revisão nesta branch; integração posterior por PR. Nenhuma escrita direta na main.
2. Screel: storyboard de oito cenas, durações provisórias, descrições e prompts. Projeto: https://screel.ai/editor/01a0eaec-1dc3-791b-a4c7-fcd501d4e56e. Geração de voz e legendas automáticas desativadas em todas as cenas.
3. PixVerse: produzir somente os complementos visuais selecionados após definir referências. Não regenerar todas as cenas se houver filmagem real. Planos longos podem usar dois clipes; S08 pode ser sustentação de cartela. Preservar sobras visuais para ajuste ao WAV.
4. Canva: montagem 1080×1920, importar WAV V3 integral na posição zero e bloquear a faixa; montar visuais e camadas gráficas ao redor da voz. Storyboard de revisão separado do vídeo final. Confirmar ajustes finos e trilhas no editor, pois criar design pelo conector não cria uma timeline de vídeo.
5. Creative Production: futura revisão de quadros de estilo quando houver referências e geração de imagens. Não há board de imagens nem geração neste pacote.
6. Studio Ghibli Anime Creator: disponível para uma eventual peça ilustrada separada; sem mudança da estética realista do EP00 por simples menção ao aplicativo.

## Handoff Canva
Criar projeto de vídeo vertical para montagem final quando o WAV estiver acessível. Camadas propostas:
- A1: EP00_MASTER_VOZ_v3.wav integral, início zero, velocidade 1×.
- A2: trilha opcional; A3: ambiência/SFX opcionais.
- V1: campo/material oficial/ilustração; V2: gráficos explicativos.
- V3: títulos; V4: legendas exatas da voz; V5: fonte ou “Ilustração” quando aplicável.
As legendas ficam em até duas linhas e seguem as palavras reais. Títulos não repetem toda a legenda.
Primeiro ajuste: marcar no WAV inícios de GNSS, imagem, LiDAR, terraplanagem, “O levantamento”, assinatura e “Vem comigo”.
Mover os cortes para esses marcadores. Nunca substituir a voz humana por TTS.
Saída proposta: MP4 H.264, 1080×1920; manter um pacote com WAV original, mídias e arquivos de referência.

## Organização dos próximos arquivos
- episodios/EP00/video/STORYBOARD_TECNICO_V3.md — este documento.
- EP00_S01_take01_v01.mp4 … EP00_S08_take01_v01.mp4 — visuais externos, nomeados por cena.
- EP00_V3_legendas.srt — somente após transcrição sincronizada real.
- EP00_V3_montagem_v01.mp4 — somente após importação do WAV e edição.
- manifesto de mídias: ID de cena, origem/URL, autor, licença, ID da geração, prompt, nome de arquivo, duração real, versão aceita e observações.
Não incluir binários pesados no Git por padrão; registrar local/URL e hash quando os arquivos existirem.

## Pendências reais para montagem final
WAV V3 ou ZIP V3 não está no repositório nem no espelho local desta sessão. Solicitar o arquivo ao usuário para ouvir, confirmar as palavras e cravar os cortes. O link sandbox da conversa antiga não equivale a um arquivo acessível aqui.
Mídias oficiais ainda não foram selecionadas/baixadas. Referências visuais de equipamentos ainda não foram vinculadas.
Esta entrega conclui o planejamento técnico e a organização de cenas; a edição final depende desses materiais.
