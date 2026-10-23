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
   1) Náhled se bere sám z YouTube. Vlastní náhled (nepovinný): čtverec .webp cca 600 × 600 px
      do složky /video/ a k videu přidejte thumb: 'soubor.webp'.
   2) Přidejte video do seznamu "videos":
      thumb = soubor ve /video/, name = název skladby, place = místo,
      yt = ID videa z YouTube (část adresy za "watch?v=" nebo za "shorts/"),
      vert: true jen u videí na výšku (YouTube Shorts).

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
    // { name: 'In the Mood', place: { cs: 'Praha', en: 'Prague', de: 'Prag' }, yt: 'YOUTUBE_ID', vert: true },
    { name: "Fly Me to the Moon", place: {"cs": "Galavečer · Obecní dům, Praha", "en": "Gala evening · Municipal House, Prague", "de": "Galaabend · Gemeindehaus, Prag"}, yt: 'a3JUoQfeBxE', vert: true },
    { name: "What a Wonderful World", place: {"cs": "Firemní večer · Občanská plovárna, Praha", "en": "Corporate evening · Občanská plovárna, Prague", "de": "Firmenabend · Občanská plovárna, Prag"}, yt: 'mQ8mido7Xcc', vert: true },
    { name: "Don't Get Around Much Anymore", place: {"cs": "Firemní večer · Občanská plovárna, Praha", "en": "Corporate evening · Občanská plovárna, Prague", "de": "Firmenabend · Občanská plovárna, Prag"}, yt: 'hAwyRm_FjOc', vert: false },
    { name: "Route 66", place: {"cs": "Firemní večer · Praha-Benice", "en": "Corporate evening · Prague-Benice", "de": "Firmenabend · Prag-Benice"}, yt: 'bizzWQf13hQ', vert: true },
    { name: "Sway", place: {"cs": "Galavečer · Obecní dům, Praha", "en": "Gala evening · Municipal House, Prague", "de": "Galaabend · Gemeindehaus, Prag"}, yt: 'u_BV76EtrFU', vert: true },
    { name: {"cs": "Instrumentální ukázka", "en": "Instrumental piece", "de": "Instrumentalstück"}, place: {"cs": "Firemní večer · Občanská plovárna, Praha", "en": "Corporate evening · Občanská plovárna, Prague", "de": "Firmenabend · Občanská plovárna, Prag"}, yt: '5ba3IbNXGCY', vert: true },
    { name: "The Girl from Ipanema", place: {"cs": "Galavečer · Obecní dům, Praha", "en": "Gala evening · Municipal House, Prague", "de": "Galaabend · Gemeindehaus, Prag"}, yt: '9IHGvyik7O0', vert: true },
    { name: {"cs": "Instrumentální ukázka", "en": "Instrumental piece", "de": "Instrumentalstück"}, place: {"cs": "Firemní večer · Občanská plovárna, Praha", "en": "Corporate evening · Občanská plovárna, Prague", "de": "Firmenabend · Občanská plovárna, Prag"}, yt: '9-5WzJw37AY', vert: true },
    { name: "Cheek to Cheek", place: {"cs": "Galavečer · Obecní dům, Praha", "en": "Gala evening · Municipal House, Prague", "de": "Galaabend · Gemeindehaus, Prag"}, yt: 'D79zqi0o2bY', vert: true },
  ]
};
