# Roast-gadget v2 — kandidat + skor (kriteria juri RULES.txt)

Kriteria (urutan juri): 1 gadget/app harian disebut jelas · 2 lucu bacaan pertama (sting of recognition) · 3 fresh · 4 rapi/ketat · 5 detail konkret perilaku benda. Skor 1–5 per kriteria. Tie-break platform: teks lebih pendek menang → kandidat 120–180 karakter.

v1 (AirPods case, 161 kar) R1: rank 154/3031, skor 649142. Kandidat v2 WAJIB angle/gadget berbeda dari v1.

## Kandidat A — printer
"My printer flawlessly prints test pages, alignment sheets and low-ink warnings, then stares at my one actual document like I just asked it to defuse a bomb."
- Skor: 1=5 (printer disebut, perilaku khasnya disebut) · 2=5 (test page selalu bisa, dokumen asli selalu gagal — recognition instan) · 3=4 (angle "yang latihan rajin, yang beneran mogok" jarang dipakai) · 4=4 (satu napas, punch di akhir) · 5=5 (test page + alignment sheet + low-ink warning = tiga perilaku nyata spesifik)
- Total 23/25.

## Kandidat B — Bluetooth speaker
"My Bluetooth speaker shouts 'CONNECTED!' at full volume to the whole house at 6 a.m., then plays my podcast at a whisper, like the music is classified."
- Skor: 1=5 · 2=5 (teriakan pairing jam 6 pagi sangat dikenal) · 3=4 · 4=4 · 5=5 (pengumuman pairing full-volume vs volume konten pelan)
- Total 23/25. Seri dengan A; A menang di kesegaran angle (speaker pairing sudah agak sering jadi bahan).

## Kandidat C — robot vacuum
"My robot vacuum mapped my entire apartment and dodges every chair leg, yet loses to the same rug fringe it has been eating for breakfast since March."
- Skor: 1=5 · 2=4 · 3=5 (rug fringe sangat spesifik, jarang) · 4=4 · 5=5
- Total 23/25. Seri juga; punch "eating for breakfast since March" bagus tapi setup mapping/chair leg lebih panjang.

## Kandidat D — smart TV
"My smart TV takes a minute to boot, demands an update, then forgets my Wi-Fi — my grandpa's TV just needed one good slap on the side to show the news."
- Skor: 1=5 · 2=4 · 3=3 (perbandingan TV kakek cukup umum) · 4=3 (dua klausa, kurang ketat) · 5=4
- Total 19/25.

## Kandidat E — washing machine
"My washing machine sings a 30-second jingle when the wash is done, then beeps like a reversing truck every three minutes until I come free the hostages."
- Skor: 1=5 · 2=4 · 3=4 · 4=4 · 5=4 (jingle selesai-cuci itu nyata; "hostages" agak lompat)
- Total 21/25.

## Pilihan v2: Kandidat A (printer)
Alasan: total tertinggi bersama, angle paling segar di antara yang seri, tiga detail perilaku konkret dalam satu baris, punch terakhir ("defuse a bomb") menaikkan tawa bacaan pertama. Panjang dihitung persis saat verifikasi main.py (target 120–180 kar, gate 1–200).

## R2 revision notes

v1, the AirPods-case line, finished R1 at rank 154 of 3,031. For the R2 revision, v2 switches to the printer roast (Candidate A above): it tied for the highest candidate score at 23/25, and among the tied candidates its angle — flawless on every practice sheet, helpless on the one real document — was judged the freshest, since the Bluetooth-speaker pairing joke (Candidate B, also 23/25) is already a fairly common bit. Candidate A also packs three concrete, real printer behaviours into a single line — test pages, alignment sheets, and low-ink warnings — and ends on the "defuse a bomb" punch, which lifts the first-read laugh. The new line is 156 characters, and `main.py` is deterministic: it writes the same constant text on every run, so repeated runs produce byte-identical output.
