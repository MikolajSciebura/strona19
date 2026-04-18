import os
import re

content_file = 'content_draft.txt'
with open(content_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Split content into parts based on headers to distribute them into sections
parts = content.split('## ')

header_html = """<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pomoc drogowa Częstochowa 24h – laweta i holowanie | DAWDAN-CARS</title>
    <meta name="description" content="Profesjonalna pomoc drogowa Częstochowa 24h, laweta i holowanie. Obsługa A1, DK1. Dojazd w 15 min do wszystkich dzielnic. Skup aut za gotówkę. Sprawdź!">
    <link rel="canonical" href="https://dawdan-cars.pl/">

    <!-- Open Graph -->
    <meta property="og:title" content="Pomoc drogowa Częstochowa 24h – laweta i holowanie | DAWDAN-CARS">
    <meta property="og:description" content="Najszybsza pomoc drogowa w Częstochowie i na A1. Holowanie 24/7, skup aut za gotówkę. Sprawdź naszą ofertę!">
    <meta property="og:image" content="https://dawdan-cars.pl/logo.webp">
    <meta property="og:url" content="https://dawdan-cars.pl/">
    <meta property="og:type" content="website">

    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "LocalBusiness",
      "name": "DAWDAN-CARS Pomoc Drogowa Częstochowa",
      "image": "https://dawdan-cars.pl/logo.webp",
      "@id": "https://dawdan-cars.pl/#business",
      "url": "https://dawdan-cars.pl/",
      "telephone": "+48790676446",
      "priceRange": "$$",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Częstochowa i okolice",
        "addressLocality": "Częstochowa",
        "postalCode": "42-200",
        "addressCountry": "PL"
      },
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": 50.8118,
        "longitude": 19.1203
      },
      "openingHoursSpecification": {
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": [
          "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
        ],
        "opens": "00:00",
        "closes": "23:59"
      },
      "hasOfferCatalog": {
        "@type": "OfferCatalog",
        "name": "Usługi Motoryzacyjne",
        "itemListElement": [
          {
            "@type": "Offer",
            "itemOffered": {
              "@type": "Service",
              "name": "Pomoc Drogowa Częstochowa 24h"
            }
          },
          {
            "@type": "Offer",
            "itemOffered": {
              "@type": "Service",
              "name": "Laweta Częstochowa"
            }
          },
          {
            "@type": "Offer",
            "itemOffered": {
              "@type": "Service",
              "name": "Skup Aut Częstochowa"
            }
          }
        ]
      }
    }
    </script>
    <link rel="stylesheet" href="style.min.css" media="print" onload="this.media='all'">
    <link rel="stylesheet" href="critical.min.css">
    <noscript><link rel="stylesheet" href="style.min.css"></noscript>
    <link rel="preload" as="style" href="style.min.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&family=Oswald:wght@500;700&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
    <link rel="stylesheet" href="font-awesome.min.css" media="print" onload="this.media='all'">
    <link rel="icon" href="favicony/favicon.ico" type="image/x-icon">
    <script src="script.min.js" defer></script>
</head>
<body>
    <header>
        <div class="top-bar">
            <div class="container">
                <div class="logo">
                    <a href="index.html">
                        <img src="logo.webp" fetchpriority="high" alt="DAWDAN-CARS Pomoc Drogowa Częstochowa" width="349" height="60">
                    </a>
                </div>
                <nav>
                    <ul>
                        <li><a href="index.html">STRONA GŁÓWNA</a></li>
                        <li><a href="o-nas.html">O NAS</a></li>
                        <li><a href="skup-samochodow.html">SKUP SAMOCHODÓW</a></li>
                        <li><a href="laweta-pomoc-drogowa.html">POMOC DROGOWA</a></li>
                        <li><a href="blog.html">BLOG</a></li>
                        <li><a href="kontakt.html">KONTAKT</a></li>
                    </ul>
                </nav>
                <div class="header-cta desktop-only">
                    <a href="tel:+48790676446" class="btn-call">
                        <i class="fas fa-phone-alt"></i>
                        <span>
                            <span class="btn-label">POMOC DROGOWA</span>
                            <span class="btn-number">790 676 446</span>
                        </span>
                    </a>
                </div>
                <button class="menu-toggle" aria-label="Otwórz menu">
                    <span></span><span></span><span></span>
                </button>
            </div>
        </div>
    </header>

    <section id="home" class="hero">
        <div class="container">
            <div class="hero-content">
                <div class="hero-text" data-aos-custom="fade-up">
                    <h1>Pomoc drogowa Częstochowa 24h – laweta i holowanie</h1>
                    <p class="hero-subtext">Najszybszy dojazd w mieście i na autostradę A1. Profesjonalny skup aut za gotówkę w Częstochowie i okolicach.</p>
                    <div class="hero-cta-buttons">
                        <a href="tel:+48790676446" class="btn-hero-call">
                            <i class="fas fa-phone-alt"></i>
                            <span>
                                <span class="btn-label">POMOC DROGOWA 24H</span>
                                <span class="btn-number">790 676 446</span>
                            </span>
                        </a>
                        <a href="tel:+48730035559" class="btn-hero-call" style="background: #2ecc71;">
                            <i class="fas fa-car"></i>
                            <span>
                                <span class="btn-label">SKUP AUT GOTÓWKA</span>
                                <span class="btn-number">730 035 559</span>
                            </span>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="service-boxes">
        <div class="container">
            <div class="box orange-box" role="article" data-aos-custom="fade-left">
                <div class="box-icon"><i class="fas fa-truck-moving"></i></div>
                <div class="box-content">
                    <h2>POMOC DROGOWA 24/7</h2>
                    <p>Laweta Częstochowa, A1, DK1. Holowanie po awarii i wypadku.</p>
                    <a href="tel:+48790676446" class="btn-outline" style="color: #000; border-color: #000;">ZADZWOŃ TERAZ</a>
                </div>
            </div>
            <div class="box blue-box" role="article" data-aos-custom="fade-right">
                <div class="box-icon"><i class="fas fa-car"></i></div>
                <div class="box-content">
                    <h2>SKUP AUT CZĘSTOCHOWA</h2>
                    <p>Gotówka od ręki. Każdy stan. Darmowa wycena i odbiór lawetą.</p>
                    <a href="skup-samochodow.html" class="btn-outline">SPRAWDŹ OFERTĘ</a>
                </div>
            </div>
        </div>
    </section>
"""

def format_section(title, text):
    content_html = f"<h2>{title}</h2>"
    # Basic bold replacements
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)

    # Split into blocks
    blocks = re.split(r'\n\n+', text.strip())

    for block in blocks:
        block = block.strip()
        if not block or block == "#":
            continue

        if block.startswith('### '):
            content_html += f"<h3>{block[4:].strip()}</h3>"
        elif block.startswith('* '):
            items = block.split('\n')
            content_html += "<ul>"
            for item in items:
                item_content = item.replace('* ', '').strip()
                if item_content:
                    content_html += f"<li>{item_content}</li>"
            content_html += "</ul>"
        elif re.match(r'^\d+\.', block):
            items = block.split('\n')
            content_html += "<ol>"
            for item in items:
                item_content = re.sub(r'^\d+\.\s*', '', item).strip()
                if item_content:
                    content_html += f"<li>{item_content}</li>"
            content_html += "</ol>"
        else:
            # Check for mini-headers (e.g., "Part 1: Description")
            if ':' in block.split('\n')[0] and len(block.split('\n')[0]) < 100:
                lines = block.split('\n')
                content_html += f"<strong>{lines[0]}</strong><br>"
                content_html += f"<p>{' '.join(lines[1:])}</p>"
            else:
                content_html += f"<p>{block}</p>"
    return content_html

main_content = ""
for i, part in enumerate(parts):
    lines = part.split('\n', 1)
    title = lines[0].strip()
    text = lines[1].strip() if len(lines) > 1 else ""

    if not title: continue
    if i == 0 and "Pomoc drogowa Częstochowa 24h" in title: continue

    main_content += f'<section class="seo-content {"bg-alt" if i%2==0 else ""}">\n'
    main_content += '    <div class="container">\n'
    main_content += '        <div class="seo-text-block" data-aos-custom="fade-up">\n'
    main_content += format_section(title, text)
    main_content += '        </div>\n'

    # Add CTA
    if i % 3 == 0:
        main_content += f"""
        <div style="text-align: center; margin-top: 40px;">
            <a href="tel:+48790676446" class="btn btn-primary"><i class="fas fa-phone-alt"></i> Zadzwoń po pomoc 24h: 790 676 446</a>
        </div>
        """

    main_content += '    </div>\n'
    main_content += '</section>\n'

# Testimonials
testimonials_html = """
<section class="testimonials bg-alt">
    <div class="container">
        <h2 class="section-title">CO MÓWIĄ O NAS KLIENCI W CZĘSTOCHOWIE</h2>
        <div class="benefits-grid">
            <div class="benefit-item">
                <div class="stars">★★★★★</div>
                <p>"Najlepsza laweta w Częstochowie! Przyjechali w 15 minut na Północ, kiedy auto odmówiło posłuszeństwa. Cena bardzo uczciwa."</p>
                <strong>Tomasz R.</strong>
            </div>
            <div class="benefit-item">
                <div class="stars">★★★★★</div>
                <p>"Szybka pomoc na autostradzie A1. Pan kierowca bardzo profesjonalny i pomocny. Polecam każdemu w potrzebie."</p>
                <strong>Magda W.</strong>
            </div>
            <div class="benefit-item">
                <div class="stars">★★★★★</div>
                <p>"Skup aut Częstochowa od DAWDAN-CARS to rewelacja. Sprzedałem powypadkowe auto w 2 godziny, gotówka do ręki. Zero problemów."</p>
                <strong>Andrzej K.</strong>
            </div>
        </div>
    </div>
</section>
"""

# Districts & Towns List for SEO
locations_html = """
<section class="locations-list">
    <div class="container">
        <h2 class="section-title">OBSŁUGIWANE LOKALIZACJE</h2>
        <div class="features-grid">
            <div class="feature-item">
                <h3>Dzielnice Częstochowy:</h3>
                <p>Błeszno, Częstochówka-Parkitka, Dźbów, Gnaszyn-Kawodrza, Grabówka, Kiedrzyn, Lisiniec, Mirów, Ostatni Grosz, Podjasnogórska, Północ, Raków, Stradom, Stare Miasto, Śródmieście, Trzech Wieszczów, Tysiąclecie, Wrzosowiak, Wyczerpy-Aniołów, Zawodzie-Dąbie.</p>
            </div>
            <div class="feature-item">
                <h3>Okolice Częstochowy:</h3>
                <p>Kłobuck, Myszków, Blachownia, Olsztyn, Mstów, Mykanów, Poczesna, Konopiska, Rędziny, Kamienica Polska, Janów, Kruszyna, Lelów, Przyrów, Starcza.</p>
            </div>
            <div class="feature-item">
                <h3>Drogi i Trasy:</h3>
                <p>Autostrada A1 (Bursztynowa), Droga Krajowa DK1, DK91, DK43, DK46, Droga Wojewódzka DW483, DW491, DW494, DW786, DW908.</p>
            </div>
        </div>
    </div>
</section>
"""

# Footer
footer_html = """
    <section class="map-section" style="padding: 80px 0;">
        <div class="container">
            <h2 class="section-title">POMOC DROGOWA CZĘSTOCHOWA NA MAPIE</h2>
            <div class="map-placeholder">
                <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m12!1m3!1d80653.2570417387!2d19.1203!3d50.8118!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4710b59368149807%3A0x64c9d7d4c7b809d!2zQ3rEmXN0b2Nob3dh!5e0!3m2!1spl!2spl!4v1700000000000!5m2!1spl!2spl" width="100%" height="450" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
            </div>
        </div>
    </section>

    <footer>
        <div class="container">
            <div class="footer-grid">
                <div class="footer-info">
                    <h3>DAWDAN-CARS CZĘSTOCHOWA</h3>
                    <p><i class="fas fa-map-marker-alt"></i> Obsługa: Częstochowa, Śląskie, A1, DK1</p>
                    <p><i class="fas fa-phone"></i> Pomoc Drogowa 24h: <a href="tel:+48790676446">790 676 446</a></p>
                    <p><i class="fas fa-phone"></i> Skup Samochodów: <a href="tel:+48730035559">730 035 559</a></p>
                </div>
                <div class="footer-links">
                    <h3>SZYBKIE LINKI</h3>
                    <ul>
                        <li><a href="index.html">Strona Główna</a></li>
                        <li><a href="skup-samochodow.html">Skup Aut</a></li>
                        <li><a href="laweta-pomoc-drogowa.html">Pomoc Drogowa</a></li>
                        <li><a href="blog.html">Blog</a></li>
                        <li><a href="kontakt.html">Kontakt</a></li>
                    </ul>
                </div>
                <div class="footer-hours">
                    <div class="hours-box">
                        <i class="far fa-clock"></i>
                        <span>24H / 7</span>
                        <p>Zawsze do Twojej dyspozycji</p>
                    </div>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2025 DAWDAN-CARS Częstochowa - Twoja najlepsza pomoc drogowa i laweta.</p>
            </div>
        </div>
    </footer>
</body>
</html>
"""

full_html = header_html + main_content + testimonials_html + locations_html + footer_html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(full_html)
