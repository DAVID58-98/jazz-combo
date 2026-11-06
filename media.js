/* =====================================================================
   FOTKY A VIDEA JAZZ COMBO
   Jediné místo, kde se doplňují. Platí pro českou, anglickou i německou verzi.
   Dokud jsou seznamy prázdné, web ukazuje připravené rámečky.

   FOTKY
   1) Soubory nahrajte do složky /foto/ (formát .webp, na výšku 3:4,
      ideálně 900 × 1200 px, do cca 150 kB).
   2) Každou fotku přidejte do seznamu "photos" níže.
      alt = krátký popis toho, co je na fotce (pro nevidomé a vyhledávače).

   VIDEA
   Videa se už nepíší sem, ale do souboru videa.json (návod: NAVOD-videa.md).
   GitHub Action je po uložení videa.json sama zapíše do seznamu "videos" níže.
   Seznam "videos" ručně neupravujte, při dalším běhu by se přepsal.

   PORTRÉTY HUDEBNÍKŮ
   1) Fotku nahrajte do /hudebnici/ pod přesným názvem (čtverec .webp, 400 × 400 px):
      frantisek-kukula.webp, marketa-greifonerova.webp, david-farek.webp,
      martin-juzl.webp, zdenek-kram.webp
   2) Nic dalšího není potřeba: stránka si fotku pod tímto názvem najde sama.
      Dokud soubor chybí, zobrazují se iniciály. Seznam "portraits" níže
      proto nechte prázdný. (Kleňha, Bárta a Greifoner už fotky mají.)
   ===================================================================== */
window.JC_MEDIA = {
  photos: [
    // { file: 'foto_1.webp', alt: { cs: 'Jazz Combo na galavečeru', en: 'Jazz Combo at a gala evening', de: 'Jazz Combo bei einem Galaabend' } },
  ],
  portraits: [
    // 'frantisek-kukula', 'marketa-greifonerova', 'david-farek', 'martin-juzl', 'zdenek-kram'
  ],
  videos: [
    // VIDEA:START – generuje se z videa.json, ručně neupravovat
    {"name": "Fly Me to the Moon", "place": {"cs": "Galavečer · Obecní dům, Praha", "en": "Gala evening · Municipal House, Prague", "de": "Galaabend · Gemeindehaus, Prag"}, "yt": "a3JUoQfeBxE", "vert": true},
    {"name": "What a Wonderful World", "place": {"cs": "Firemní večer · Občanská plovárna, Praha", "en": "Corporate evening · Občanská plovárna, Prague", "de": "Firmenabend · Občanská plovárna, Prag"}, "yt": "mQ8mido7Xcc", "vert": true},
    {"name": "Don't Get Around Much Anymore", "place": {"cs": "Firemní večer · Občanská plovárna, Praha", "en": "Corporate evening · Občanská plovárna, Prague", "de": "Firmenabend · Občanská plovárna, Prag"}, "yt": "hAwyRm_FjOc", "vert": false},
    {"name": "Route 66", "place": {"cs": "Firemní večer · Praha-Benice", "en": "Corporate evening · Prague-Benice", "de": "Firmenabend · Prag-Benice"}, "yt": "bizzWQf13hQ", "vert": true},
    {"name": "Sway", "place": {"cs": "Galavečer · Obecní dům, Praha", "en": "Gala evening · Municipal House, Prague", "de": "Galaabend · Gemeindehaus, Prag"}, "yt": "u_BV76EtrFU", "vert": true},
    {"name": {"cs": "Instrumentální ukázka", "en": "Instrumental piece", "de": "Instrumentalstück"}, "place": {"cs": "Firemní večer · Občanská plovárna, Praha", "en": "Corporate evening · Občanská plovárna, Prague", "de": "Firmenabend · Občanská plovárna, Prag"}, "yt": "5ba3IbNXGCY", "vert": true},
    {"name": "The Girl from Ipanema", "place": {"cs": "Galavečer · Obecní dům, Praha", "en": "Gala evening · Municipal House, Prague", "de": "Galaabend · Gemeindehaus, Prag"}, "yt": "9IHGvyik7O0", "vert": true},
    {"name": {"cs": "Instrumentální ukázka", "en": "Instrumental piece", "de": "Instrumentalstück"}, "place": {"cs": "Firemní večer · Občanská plovárna, Praha", "en": "Corporate evening · Občanská plovárna, Prague", "de": "Firmenabend · Občanská plovárna, Prag"}, "yt": "9-5WzJw37AY", "vert": true},
    {"name": "Cheek to Cheek", "place": {"cs": "Galavečer · Obecní dům, Praha", "en": "Gala evening · Municipal House, Prague", "de": "Galaabend · Gemeindehaus, Prag"}, "yt": "D79zqi0o2bY", "vert": true},
    // VIDEA:END
  ]
};
