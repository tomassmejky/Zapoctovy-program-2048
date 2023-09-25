# Dokumentace kódu
Hra běží v rozhraní pomocí knihovny Tkinter primárně pomocí funkcí, které se volají stisknutím tlačítek ve hře nebo šipek na klávesnici. 

## Základní popis
Hrací pole je interně reprezentováno maticí, na které se udělají výpočty odpovídající tahu hráče, a poté se data z matice nahrají do hrací plochy v uživatelském prostředí.
Program je rozdělený do 5 souborů pro lepší přehlednost, kde každý soubor je určený pro určitou část programu. Zde jsou jednotlivé části popsány:

## 2048.py
Hlavní program obsahující třídu Game, která po zavolání otevře okno s hrou a inicializuje potřebné proměnné. Funkce této třídy:

### init_info
Funkce inicializuje potřebné widgety knihovny tKinter - textové pole a tlačítka, a umístí je na správné místo.

### init_grid
Funkce inicializuje nové pod-okno, ve kterém vygeneruje grid na hrací kameny.

## GUIfunc.py
Zde jsou funkce pro uživatelské prostředí, tedy pro ovládání tlačítek a grafických změn. Funkce této třídy:

### update_grid
Funkce iteruje maticí s daty a pro každé pole zobrazí správné hodnoty a barvy kamenům na hrací ploše.

### swipe
Tato funkce vyhodnocuje tahy hráče. Udělá si kopii matice a zavolá konkrétní  funkci pro výpočet dat v matici. Pokud je nový stav odlišný od starého, zavolá funkci pro vygenerování nového kamene a updatuje hrací plochu. Poté zavolá funkci na kontrolu stavu hry - jestli hráč vyhrál, prohrál nebo hraje dál.

### help_button
Pomocná funkce pro tlačítko "How to play" v uživatelském prostředí - vygeneruje widgety knihovny tKinter s textem a tlačítkem na zavření okna.

### new_game_button
Pomocná funkce pro tlačítko "New Game" v uživatelském prostředí - vygeneruje widgety knihovny tKinter s textem a tlačítky na zavření okna a spuštění nové hry.

### new_game
Funkce pro obnovení hry. Resetuje skóre, zavolá funkci pro začátek nové hry.

### continue_game
Pomocná funkce pro kontrolu stavu hry.

### game_state
Funkce kontroluje stav hry. Tedy pokud hráč vyhrál, vygeneruje okno s widgety na novou hru nebo pokračování v té stejné, pokud prohrál, hru obnoví.

### update_score
Pomocná funkce pro updatování skóre hry.

## matrix.py
Zde jsou funkce pro interní výpočty na matici. Funkce této třídy:

### rotate_matrix_counter_clockwise
Otočí matici proti směru hodinových ručiček.

### rotate_matrix_180
Otočí matici o 180 stupňů.

### rotate_matrix_clockwise
Otočí matici po směru hodinových ručiček.

### generate_tile
Funkce náhodně najde pozici v matici, na které má hodnotu 0 a přiřadí jí hodnotu 2 s pravděpodobností 0.9 nebo hodnotu 4 s pravděpodobností 0.1.

### new_game
Funkce inicializuje matici, nastaví všechny její hodnoty na 0 a dvakrát zavolá funkci na vygenerování čísla. (Dostane matici do tvaru, ve kterým má být na začátku hry.)

### compress
Funkce prochází maticí po sloupcích a hledá hodnotu jinou od nuly pod hodnotou nula. Pokud najde, cyklem dostane hodnotu ve spodu sloupce co nejvýše (dokud nenarazí na jinou nenulovou hodnotu.)

### addition
Funkce prochází maticí po sloupcích a hledá stejné hodnoty vedle sebe. Pokud najde, hodnoty sečte, výsledek zapíše do horní pozice, přičte ho ke skóre a dolní nastaví na nulu. Algoritmus je rozdělen na dvě situace - pokud jsou ve sloupci dvě dvojice stejných hodnot ([2, 2, 4, 4]) a nebo jen jedna.

### win
Funkce projde matici a vrátí True v případě, že je některá z hodnot 2048, jinak vrátí False.

### loss
Funkce kontruje, jestli hráč může udělat další tah. V takovém případě existují dvě možnosti. Buď je některá z hodnot nula, nebo jsou dvě stejné hodnoty vedle sebe. Pokud ani jedna z možností neplatí, funkce vrátí True a tím říká, že hráč prohrál.

### swipe_up/down/left/right
Tyto funkce vhodně otočí matici tak, aby se mohly provést výpočty na odstranění mezer a sečtení hodnot směrem nahoru, a poté matici otočí zpět.

## score.py
Zde je třída Score, ve které se inicializují proměnné potřebné k hlídání aktuálního a nejlepšího skóre. Funkce této třídy:

### get_score
Funkce zobrazí skóre do widgetu v uživatelském prostředí a pokud je vyšší než nejlepší skóre, nahradí ho tím aktuálním.

## data.py
Zde jsou uloženy hodnoty potřebných barev a fontů pro větší přehlednost kódu.