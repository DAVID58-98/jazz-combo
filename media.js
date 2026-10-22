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
   1) Náhledový obrázek nahrajte do složky /video/ (čtverec .webp, cca 600 × 600 px).
   2) Přidejte video do seznamu "videos":
      thumb = soubor ve /video/, name = název skladby, place = místo,
      yt = ID videa z YouTube (část adresy za "watch?v=" nebo za "shorts/"),
      vert: true jen u videí na výšku (YouTube Shorts).

   PORTRÉTY HUDEBNÍKŮ
   1) Fotku nahrajte do /hudebnici/ pod přesným názvem (čtverec .webp, 400 × 400 px):
      frantisek-kukula.webp, marketa-greifonerova.webp, david-farek.webp,
      martin-juzl.webp, zdenek-kram.webp
   2) Název bez přípony přidejte do seznamu "portraits" níže.
      (David Kleňha, Jaroslav Bárta a Jan Greifoner už fotky mají.)
   ===================================================================== */
window.JC_MEDIA = {
  photos: [
    // { file: 'foto_1.webp', alt: { cs: 'Jazz Combo na galavečeru', en: 'Jazz Combo at a gala evening', de: 'Jazz Combo bei einem Galaabend' } },
  ],
  portraits: [
    // 'frantisek-kukula', 'marketa-greifonerova', 'david-farek', 'martin-juzl', 'zdenek-kram'
  ],
  videos: [
    // { thumb: '1.webp', name: 'In the Mood', place: 'Praha', yt: 'YOUTUBE_ID', vert: false },
  ]
};
