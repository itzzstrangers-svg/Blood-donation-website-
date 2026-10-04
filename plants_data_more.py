"""
NurseryIQ extra seed data: 100 more plants (16-17 per primary category).

Uses exactly the same line format and codes as plants_data.py:
name | scientific name | emoji | tags (first = primary category) | sun | water |
environments | level | temperature | soil | best planting seasons | description | care
"""

_RAW_MORE = """
English Ivy|Hedera helix|🌿|Indoor|m|m|i,b|b|10-25°C|Well-draining potting mix|m,w|Classic trailing vine that looks great in hanging pots.|Keep soil lightly moist, provide bright indirect light and trim to shape.
Prayer Plant|Maranta leuconeura|🍃|Indoor|l|m|i|e|18-27°C|Rich, moist, well-draining mix|m,w|Patterned leaves fold upward at night like praying hands.|Use filtered water, keep humid and avoid direct sun.
String of Pearls|Curio rowleyanus|🪴|Indoor|h|l|i,b|e|15-27°C|Gritty succulent mix|s,w|Trailing succulent with bead-like leaves, ideal for hanging pots.|Water only when soil is dry and give very bright light.
Burro's Tail|Sedum morganianum|🪴|Indoor|h|l|i,b|b|15-30°C|Gritty succulent mix|s,w|Long trailing stems covered in plump, blue-green leaves.|Water sparingly and handle gently because leaves drop easily.
Zebra Haworthia|Haworthiopsis attenuata|🪴|Indoor|m|l|i,b|b|15-28°C|Gritty succulent mix|s,m,w|Tiny rosette succulent with white-striped leaves for desks and shelves.|Water when soil is dry and give bright indirect light.
Echeveria|Echeveria elegans|🪴|Indoor|h|l|i,b|b|15-28°C|Gritty succulent mix|s,w|Rose-shaped succulent rosettes in silver-blue shades.|Give bright light, water deeply but rarely and avoid wetting the leaves.
Christmas Cactus|Schlumbergera truncata|🌸|Indoor|m|m|i|b|15-25°C|Light, well-draining potting mix|m,w|Segmented stems that bloom in pink or red during cool seasons.|Water when the top soil dries and keep cool nights for flowering.
Bird's Nest Fern|Asplenium nidus|🌿|Indoor|l|m|i|b|18-28°C|Rich, airy, humus-heavy mix|m,w|Wavy, glossy fronds growing in a neat rosette.|Keep soil lightly moist and water around the edge, not into the centre.
Kentia Palm|Howea forsteriana|🌴|Indoor|l|m|i|e|15-27°C|Well-draining potting mix|s,m|Elegant, slow-growing palm that tolerates low light.|Water when the top soil dries and avoid sudden changes in position.
Ponytail Palm|Beaucarnea recurvata|🌴|Indoor|h|l|i,b|b|15-30°C|Sandy, well-draining mix|s,w|Swollen trunk base stores water, topped with long curly leaves.|Water deeply but rarely and give bright light.
Polka Dot Plant|Hypoestes phyllostachya|🌸|Indoor|m|m|i|b|18-27°C|Light, well-draining potting mix|m,w|Speckled pink, red or white leaves add colour to small spaces.|Pinch tips for bushiness and keep soil lightly moist.
Wandering Jew|Tradescantia zebrina|🌿|Indoor|m|m|i,b|b|15-28°C|Light, well-draining potting mix|s,m,w|Fast trailing plant with purple and silver striped leaves.|Water when the top soil dries and trim regularly to stay full.
Chinese Money Plant|Pilea peperomioides|🪴|Indoor|m|m|i|b|15-27°C|Light, well-draining potting mix|s,m|Round coin-shaped leaves and easy-to-share baby plants.|Water when the top soil dries and rotate the pot for even growth.
Rex Begonia|Begonia rex|🍃|Indoor|m|m|i|e|16-26°C|Light, humus-rich mix|m,w|Showy, swirled leaves in silver, red and green.|Keep soil lightly moist, avoid wetting the leaves and give humidity.
Nerve Plant|Fittonia albivenis|🌿|Indoor|l|m|i|e|18-27°C|Moist, well-draining mix|m,w|Low plant with leaves veined in white, pink or red.|Never let it dry out fully and keep it away from direct sun.
Syngonium|Syngonium podophyllum|🍃|Indoor|m|m|i|b|18-30°C|Well-draining potting mix|s,m,w|Arrow-shaped leaves on an easy climbing or trailing vine.|Water when the top soil dries and pinch tips to keep it compact.
Philodendron Birkin|Philodendron 'Birkin'|🌿|Indoor|m|m|i|e|18-28°C|Well-draining potting mix|s,m|Dark green leaves with creamy white stripes on a compact plant.|Give bright indirect light and water when the top soil dries.
Lotus|Nelumbo nucifera|🪷|Flowering,Outdoor|h|h|o|e|22-35°C|Heavy clay-loam in a water tub|s,m|Sacred aquatic flower with large pink or white blooms.|Plant in a tub with 15-30 cm of water in full sun and feed with aquatic fertilizer.
Spanish Jasmine|Jasminum grandiflorum|🌼|Flowering,Outdoor|h|m|o,b|b|18-35°C|Well-draining loamy soil|s,m|Sweetly scented white flowers (chameli) on a climbing shrub.|Prune after flowering, water regularly and give a support to climb.
Night Jasmine|Nyctanthes arbor-tristis|🌼|Flowering,Outdoor|h|m|o|b|18-35°C|Well-draining loamy soil|m|Parijat shrub whose fragrant white-and-orange flowers open at night.|Water regularly in summer and prune after the flowering season.
Tuberose|Polianthes tuberosa|🌼|Flowering,Outdoor|h|m|o,b|b|20-35°C|Rich, well-draining soil|s,m|Rajnigandha produces tall spikes of strongly fragrant white flowers.|Plant bulbs in full sun and keep soil lightly moist.
Crossandra|Crossandra infundibuliformis|🌸|Flowering,Outdoor|m|m|o,b|b|20-35°C|Light, well-draining soil|s,m|Aboli bears orange flowers in warm weather and suits pots well.|Water when the top soil dries and feed monthly while flowering.
Balsam|Impatiens balsamina|🌸|Flowering,Outdoor|m|m|o,b|b|18-30°C|Rich, well-draining soil|m|Quick monsoon annual with colourful flowers along the stem.|Sow in partial sun and keep soil moist but not soggy.
Globe Amaranth|Gomphrena globosa|🌸|Flowering,Outdoor|h|l|o,b|b|18-35°C|Average, well-draining soil|s,m|Round, papery purple or pink blooms that last for weeks.|Give full sun and water lightly; it tolerates heat well.
China Aster|Callistephus chinensis|🌼|Flowering,Outdoor|h|m|o,b|b|15-26°C|Loamy, well-draining soil|w|Bright daisy-like flowers that are popular as cut flowers.|Water at the base and stake taller varieties.
Scarlet Sage|Salvia splendens|🌸|Flowering,Outdoor|h|m|o,b|b|15-30°C|Rich, well-draining soil|w,m|Spikes of vivid red flowers that attract hummingbirds and bees.|Water regularly and remove spent spikes to prolong blooms.
Snapdragon|Antirrhinum majus|🌸|Flowering,Outdoor|h|m|o,b|b|10-24°C|Light, well-draining soil|w|Tall flower spikes in many colours, best in cool weather.|Keep soil moist and pinch young plants for more flower stems.
Pansy|Viola x wittrockiana|🌸|Flowering,Outdoor|m|m|o,b|b|8-22°C|Rich, well-draining soil|w|Cool-season flowers with face-like markings in many colours.|Water evenly and deadhead often; it struggles in hot weather.
Lily|Lilium longiflorum|🌷|Flowering,Outdoor|m|m|o,b|e|12-25°C|Well-draining, humus-rich soil|w|Large trumpet-shaped fragrant flowers grown from bulbs.|Plant bulbs 15 cm deep and keep roots shaded and cool.
Gladiolus|Gladiolus hortulanus|🌷|Flowering,Outdoor|h|m|o|b|15-28°C|Sandy, well-draining loam|w|Tall flower spikes grown from corms, popular as cut flowers.|Plant corms in full sun, water regularly and stake tall stems.
Canna Lily|Canna indica|🌺|Flowering,Outdoor|h|h|o|b|20-35°C|Rich, moist soil|s,m|Bold tropical foliage with bright red, orange or yellow blooms.|Water generously and cut back old stems after flowering.
Hydrangea|Hydrangea macrophylla|💠|Flowering,Outdoor|m|h|o|e|12-25°C|Rich, moist, slightly acidic soil|m,w|Big rounded flower heads in blue, pink or white.|Water often, give afternoon shade and prune after blooming.
Fuchsia|Fuchsia x hybrida|🌸|Flowering,Outdoor|m|m|o,b|e|10-24°C|Light, humus-rich soil|w|Hanging two-tone flowers that suit cool, shaded balconies.|Keep soil evenly moist and protect from heat.
Wax Begonia|Begonia semperflorens|🌸|Flowering,Outdoor|m|m|o,b|b|15-28°C|Light, well-draining soil|m,w|Compact bedding plant with small flowers nearly all year.|Water when top soil dries and avoid wetting the leaves.
Jackfruit|Artocarpus heterophyllus|🍈|Fruit,Outdoor|h|m|o|e|22-35°C|Deep, well-draining loamy soil|m|Large tropical tree producing the world's biggest tree-borne fruit.|Plant in a large space with full sun and water young trees regularly.
Jamun|Syzygium cumini|🫐|Fruit,Outdoor|h|m|o|b|20-38°C|Deep, well-draining loamy soil|m|Hardy tree with purple, sweet-tart fruits ripening in summer.|Water young plants well and prune lightly after harvest.
Indian Jujube|Ziziphus mauritiana|🍎|Fruit,Outdoor|h|l|o|b|20-40°C|Sandy to loamy soil|m|Ber is a hardy, drought-tolerant tree with small sweet apples.|Water young plants lightly and prune after fruiting.
Tamarind|Tamarindus indica|🌳|Fruit,Outdoor|h|l|o|b|22-38°C|Deep, well-draining soil|m|Slow-growing tree producing tangy pods used in cooking.|Water young trees regularly; mature trees are very drought tolerant.
Karonda|Carissa carandas|🍒|Fruit,Outdoor|h|l|o,b|b|20-38°C|Sandy, well-draining soil|m|Thorny, hardy shrub with tart fruits used in pickles.|Needs little water and full sun; it makes a good hedge.
Kokum|Garcinia indica|🍒|Fruit,Outdoor|m|m|o|e|22-35°C|Rich, well-draining loamy soil|m|Coastal tree whose sour fruit is used in curries and drinks.|Provide partial shade when young and keep soil moist.
Starfruit|Averrhoa carambola|⭐|Fruit,Outdoor|h|m|o|e|22-35°C|Rich, well-draining soil|s,m|Tree with star-shaped, juicy fruits when sliced.|Water regularly, protect from strong wind and feed twice a year.
Lychee|Litchi chinensis|🍒|Fruit,Outdoor|h|m|o|e|20-35°C|Slightly acidic, rich loamy soil|m|Subtropical tree with sweet, juicy fruits in red shells.|Keep soil moist while young and mulch well.
Avocado|Persea americana|🥑|Fruit,Outdoor|h|m|o|e|18-32°C|Deep, well-draining soil|m|Creamy fruit from a large evergreen tree; grafted plants fruit sooner.|Never let water stand around roots and protect young trees from frost.
Bael|Aegle marmelos|🍈|Fruit,Outdoor|h|l|o|b|20-40°C|Well-draining loamy soil|m|Sacred tree with hard-shelled fruit used as a cooling summer drink.|Water young trees only occasionally; it is very hardy.
Wood Apple|Limonia acidissima|🍈|Fruit,Outdoor|h|l|o|b|22-40°C|Sandy to loamy soil|m|Kaith is a tough tree with tangy fruit used in chutneys.|Water young plants regularly; mature trees need little care.
Sweet Lime|Citrus limetta|🍊|Fruit,Outdoor|h|m|o,b|b|18-35°C|Well-draining loamy soil|m|Mosambi produces mild, sweet and juicy citrus fruit.|Water deeply and feed with compost every few months.
Muskmelon|Cucumis melo|🍈|Fruit,Outdoor|h|m|o|b|22-35°C|Sandy loam rich in compost|s|Sweet summer vine fruit that grows quickly from seed.|Water at the base, give full sun and room to spread.
Watermelon|Citrullus lanatus|🍉|Fruit,Outdoor|h|m|o|b|22-35°C|Sandy, well-draining loam|s|Hot-season vine producing large, juicy summer fruit.|Water deeply but less once fruits ripen and give full sun.
Date Palm|Phoenix dactylifera|🌴|Fruit,Outdoor|h|l|o|e|20-42°C|Sandy, well-draining soil|s,m|Tall palm that thrives in heat and bears sweet dates.|Water young palms regularly and provide lots of open space.
Phalsa|Grewia asiatica|🍇|Fruit,Outdoor|h|l|o|b|20-40°C|Well-draining loamy soil|w|Small shrub bearing sweet-sour purple berries in summer.|Prune hard in winter and water lightly.
Rose Apple|Syzygium jambos|🍎|Fruit,Outdoor|h|m|o|b|20-35°C|Moist, well-draining loamy soil|m|Fragrant pale fruit with a rose-like aroma on a tropical tree.|Keep soil moist and mulch around the base.
Arjuna|Terminalia arjuna|🌳|Medicinal,Outdoor|h|m|o|b|20-38°C|Deep, moist loamy soil|m|Tall tree whose bark is used in traditional heart tonics.|Plant near water if possible and give plenty of space.
Sarpagandha|Rauvolfia serpentina|🌿|Medicinal,Outdoor|m|m|o,b|e|20-35°C|Rich, well-draining loamy soil|m|Traditional herb with slender stems and clusters of pink flowers; roots are potent.|Grow in partial sun and use only under qualified guidance.
Shankhpushpi|Convolvulus pluricaulis|🌿|Medicinal,Herb|h|l|o,b|b|20-38°C|Sandy, well-draining soil|s,m|Low spreading herb with small blue flowers, used in traditional brain tonics.|Needs full sun and light watering; avoid soggy soil.
Haritaki|Terminalia chebula|🌳|Medicinal,Outdoor|h|m|o|b|20-38°C|Deep, well-draining loamy soil|m|Large tree producing fruits central to traditional triphala.|Water young plants well; it grows slowly at first.
Bibhitaki|Terminalia bellirica|🌳|Medicinal,Outdoor|h|m|o|b|20-38°C|Deep, well-draining loamy soil|m|Tall deciduous tree used in traditional triphala.|Water young plants regularly and give lots of space.
Safed Musli|Chlorophytum borivilianum|🌿|Medicinal|m|m|o,b|b|20-35°C|Light, well-drained sandy loam|m|Monsoon herb grown for its tuberous roots.|Plant tubers at the start of the rains in loose soil.
Noni|Morinda citrifolia|🍈|Medicinal,Outdoor|h|m|o|b|22-35°C|Well-draining loamy soil|s,m|Tropical tree with knobby fruits used in traditional tonics.|Water regularly and prune for shape.
Bhringraj|Eclipta prostrata|🌿|Medicinal|m|h|o,b|b|18-35°C|Moist, loamy soil|m|Small moisture-loving herb traditionally used for hair-care oils.|Keep soil damp and let it grow in partial sun.
Punarnava|Boerhavia diffusa|🌿|Medicinal|m|m|o,b|b|20-38°C|Light, well-draining soil|m|Spreading herb with small pink flowers, used in traditional medicine.|Water lightly and let it spread; it is very hardy.
Chitrak|Plumbago zeylanica|🌿|Medicinal,Outdoor|m|m|o,b|b|20-35°C|Well-draining loamy soil|m|Shrubby herb with white flowers; roots are used traditionally but are harsh.|Grow with care and avoid handling roots without guidance.
Sweet Flag|Acorus calamus|🌿|Medicinal|m|h|o,b|b|15-32°C|Wet, loamy soil|m|Vacha is a marsh herb with sword-like aromatic leaves.|Keep soil constantly wet or grow at pond margins.
Echinacea|Echinacea purpurea|🌸|Medicinal,Flowering|h|m|o,b|b|10-28°C|Well-draining loamy soil|w|Purple coneflower grown for flowers and traditional immune-support teas.|Give full sun and water deeply but not too often.
Calendula|Calendula officinalis|🌼|Medicinal,Flowering|h|m|o,b|b|10-25°C|Well-draining loamy soil|w|Bright orange flowers used in soothing skin ointments.|Deadhead often to keep it blooming and water at the base.
Black Cumin|Nigella sativa|🌿|Medicinal,Herb|h|l|o,b|b|10-28°C|Light, well-draining soil|w|Kalonji is an annual herb grown for its aromatic black seeds.|Sow directly in winter and water lightly.
Long Pepper|Piper longum|🌿|Medicinal,Herb|m|m|o,b|e|20-35°C|Rich, well-draining soil|m|Pippali is a creeping vine with spicy catkins used in traditional medicine.|Give a support to climb and keep soil moist.
Black Pepper|Piper nigrum|🌿|Medicinal,Herb|m|m|o,b|e|20-35°C|Rich, humus-heavy soil|m|Climbing vine producing peppercorns in warm, humid places.|Use a moss pole or tree to climb and mulch well.
Cardamom|Elettaria cardamomum|🌿|Medicinal,Herb|l|h|o|e|18-32°C|Rich, moist, humus-heavy soil|m|Shade-loving plant producing aromatic green pods.|Keep soil moist, shaded and mulched.
Tarragon|Artemisia dracunculus|🌿|Herb|h|m|o,b|e|10-28°C|Light, well-draining soil|w|Narrow aromatic leaves with a gentle anise flavour.|Give full sun and avoid soggy soil.
Lemon Thyme|Thymus x citriodorus|🌿|Herb|h|l|o,b|b|10-28°C|Sandy, well-draining soil|w|Compact thyme with citrus-scented leaves.|Water lightly and trim after flowering.
Spearmint|Mentha spicata|🌿|Herb|m|h|o,b|b|15-30°C|Rich, moist soil|s,m,w|Refreshing mint used in teas and chutneys.|Keep soil moist and grow in its own pot because it spreads.
Peppermint|Mentha x piperita|🌿|Herb|m|h|o,b|b|15-28°C|Rich, moist soil|m,w|Strongly cooling mint with a high menthol content.|Water often and trim regularly for fresh growth.
Catnip|Nepeta cataria|🌿|Herb|h|m|o,b|b|12-30°C|Light, well-draining soil|w,m|Hardy herb that cats love and bees visit.|Give full sun and water when the top soil dries.
Borage|Borago officinalis|🌸|Herb,Flowering|h|m|o,b|b|10-26°C|Light, well-draining soil|w|Fuzzy leaves with edible blue star-shaped flowers.|Sow directly and water lightly.
Summer Savory|Satureja hortensis|🌿|Herb|h|l|o,b|b|12-30°C|Light, well-draining soil|w,s|Peppery herb often used with beans and lentils.|Water lightly and harvest before flowering.
Sorrel|Rumex acetosa|🌿|Herb|m|m|o,b|b|10-26°C|Moist, well-draining soil|w|Lemony leaves used in salads and soups.|Keep soil moist and pick young leaves.
Arugula|Eruca vesicaria|🌿|Herb|m|m|o,b|b|10-24°C|Light, well-draining soil|w|Fast-growing peppery salad leaves.|Sow thickly and harvest leaves in about 30 days.
Celery|Apium graveolens|🌿|Herb|m|h|o,b|e|12-25°C|Rich, moist soil|w|Crisp stalks and leaves for soups and salads.|Keep soil evenly moist and feed regularly.
Garlic|Allium sativum|🧄|Herb|h|m|o,b|b|10-25°C|Loose, well-draining soil|w|Grown from cloves to produce flavourful bulbs.|Plant cloves pointed side up and stop watering when leaves yellow.
Garlic Chives|Allium tuberosum|🌿|Herb|h|m|o,b|b|10-30°C|Rich, well-draining soil|s,m,w|Flat leaves with mild garlic flavour and white flowers.|Water regularly and cut back to encourage fresh leaves.
Mustard Greens|Brassica juncea|🥬|Herb|h|m|o,b|b|10-25°C|Rich, well-draining soil|w|Sarson leaves are a favourite winter leafy vegetable.|Sow in cool weather and harvest young leaves.
Pandan|Pandanus amaryllifolius|🌿|Herb|m|m|o,b|b|20-35°C|Rich, moist soil|s,m|Fragrant long leaves used to flavour rice and sweets.|Keep soil moist and shade from harsh midday sun.
Vietnamese Coriander|Persicaria odorata|🌿|Herb|m|h|o,b|b|18-35°C|Rich, moist soil|s,m|Heat-tolerant substitute for coriander with a spicy flavour.|Keep soil constantly moist and trim to prevent legginess.
Anise|Pimpinella anisum|🌿|Herb|h|m|o,b|e|15-28°C|Light, well-draining soil|w|Feathery herb grown for sweet, licorice-flavoured seeds.|Sow directly and avoid transplanting.
Gulmohar|Delonix regia|🌺|Outdoor,Flowering|h|m|o|b|22-40°C|Deep, well-draining soil|s|Spreading shade tree with fiery red-orange flowers in summer.|Give lots of space and water young trees regularly.
Mountain Ebony|Bauhinia purpurea|🌸|Outdoor,Flowering|h|m|o|b|18-35°C|Well-draining loamy soil|m|Orchid-like pink flowers on a medium tree.|Water young trees well and prune after flowering.
Jacaranda|Jacaranda mimosifolia|💜|Outdoor,Flowering|h|m|o|b|15-32°C|Well-draining loamy soil|m|Fern-like leaves and clouds of purple-blue flowers.|Water young trees and avoid waterlogging.
Pride of India|Lagerstroemia speciosa|🌸|Outdoor,Flowering|h|m|o|b|20-38°C|Deep, moist loamy soil|m|Large tree with showy pink-lilac flowers in summer.|Water young trees regularly and prune after flowering.
Crape Myrtle|Lagerstroemia indica|🌸|Outdoor,Flowering|h|m|o|b|15-35°C|Well-draining loamy soil|s,m|Shrub or small tree with frilled pink, white or red blooms.|Water deeply and prune in winter.
Ti Plant|Cordyline fruticosa|🌿|Outdoor|m|m|o,b|b|18-35°C|Well-draining potting mix|s,m|Colourful pink, red and green leaves on a bushy palm-like plant.|Keep soil lightly moist and avoid harsh midday sun.
Song of India|Dracaena reflexa|🌿|Outdoor,Indoor|m|m|o,i|b|18-32°C|Well-draining potting mix|s,m,w|Golden-edged leaves on an upright shrub.|Water when the top soil dries and avoid soggy soil.
Firebush|Hamelia patens|🌺|Outdoor,Flowering|h|m|o,b|b|20-38°C|Well-draining loamy soil|s,m|Red-orange tubular flowers loved by butterflies and birds.|Water regularly and prune lightly after flowering.
Crape Jasmine|Tabernaemontana divaricata|🌼|Outdoor,Flowering|m|m|o,b|b|20-35°C|Rich, well-draining soil|s,m|Chandni has glossy leaves and pure white pinwheel flowers.|Water regularly and prune for a bushy shape.
Gardenia|Gardenia jasminoides|🌼|Outdoor,Flowering|m|m|o,b|e|18-30°C|Acidic, humus-rich soil|m,w|Fragrant creamy white flowers on a glossy shrub.|Keep soil moist and acidic, and avoid moving the plant while in bud.
Night Queen|Cestrum nocturnum|🌼|Outdoor,Flowering|h|m|o|b|18-35°C|Well-draining loamy soil|s,m|Raat ki rani releases a strong perfume at night.|Plant away from windows if you dislike strong scent and prune after flowering.
Mussaenda|Mussaenda erythrophylla|🌺|Outdoor,Flowering|h|m|o,b|b|20-35°C|Rich, well-draining soil|s,m|Shrub with showy pink, red or white leaf-like bracts.|Water regularly and prune after flowering.
Blue Trumpet Vine|Thunbergia grandiflora|💜|Outdoor,Flowering|h|m|o|b|18-35°C|Rich, well-draining soil|m|Vigorous climber with large sky-blue trumpet flowers.|Provide a strong support and prune after flowering.
Golden Trumpet|Allamanda cathartica|🌼|Outdoor,Flowering|h|m|o,b|b|20-38°C|Well-draining loamy soil|s,m|Glossy leaves with large yellow trumpet flowers; toxic if eaten.|Water regularly and prune for a bushy shape.
Crown of Thorns|Euphorbia milii|🌺|Outdoor,Flowering|h|l|o,b|b|18-38°C|Sandy, well-draining soil|s,m,w|Thorny succulent shrub with small red or pink flowers year-round.|Water sparingly; the sap is irritating, so wear gloves.
Pentas|Pentas lanceolata|🌸|Outdoor,Flowering|h|m|o,b|b|18-35°C|Well-draining loamy soil|s,m|Star-shaped flower clusters that attract butterflies.|Water regularly and deadhead for continuous blooms.
"""
