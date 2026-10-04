"""
NurseryIQ seed data: 120 plants here + 100 more in plants_data_more.py
(220 plants in total).

Line format (pipe separated):
name | scientific name | emoji | tags (first = primary category) | sun | water |
environments | level | temperature | soil | best planting seasons | description | care

Codes
  sun / water : l = low, m = medium, h = high
  environment : i = indoor, o = outdoor, b = balcony
  level       : b = beginner, e = expert
  seasons     : s = summer, m = monsoon, w = winter
"""

SUN = {"l": "low", "m": "medium", "h": "high"}
WATER = {"l": "low", "m": "medium", "h": "high"}
ENV = {"i": "indoor", "o": "outdoor", "b": "balcony"}
LEVEL = {"b": "beginner", "e": "expert"}
SEASON = {"s": "summer", "m": "monsoon", "w": "winter"}

_RAW = """
Snake Plant|Dracaena trifasciata|🪴|Indoor|l|l|i,b|b|15-30°C|Well-draining cactus mix|s,m,w|Hardy upright plant that tolerates low light and neglect.|Water only when the soil is fully dry; never leave it in standing water.
Money Plant|Epipremnum aureum|🌿|Indoor|m|m|i,b|b|18-30°C|Well-draining potting mix|s,m,w|Fast-growing trailing vine that also grows in a jar of water.|Water weekly, keep out of harsh sun and trim long vines to keep it bushy.
Peace Lily|Spathiphyllum wallisii|🌼|Indoor|l|m|i|b|18-28°C|Rich, evenly moist potting mix|m,w|Glossy leaves with white spoon-shaped blooms; copes well with shade.|Keep soil lightly moist; it droops clearly when thirsty.
Spider Plant|Chlorophytum comosum|🌿|Indoor|m|m|i,b|b|15-27°C|Loose, well-draining potting mix|s,m,w|Arching striped leaves and baby plantlets that are easy to propagate.|Water when the top soil dries; brown tips often mean tap-water salts.
ZZ Plant|Zamioculcas zamiifolia|🪴|Indoor|l|l|i|b|18-30°C|Well-draining potting mix|s,m,w|Shiny, drought-tolerant leaves that suit offices and dim corners.|Water sparingly every 2-3 weeks; overwatering is its main enemy.
Rubber Plant|Ficus elastica|🌳|Indoor|m|m|i|b|18-28°C|Well-draining potting mix|s,m|Bold, glossy leaves on a sturdy upright stem.|Wipe leaves occasionally and water once the top soil is dry.
Areca Palm|Dypsis lutescens|🌴|Indoor|m|m|i,b|e|18-30°C|Rich, well-draining potting mix|s,m|Feathery palm that adds a tropical feel to bright rooms.|Keep soil lightly moist, avoid direct afternoon sun and dry air.
Boston Fern|Nephrolepis exaltata|🌿|Indoor|m|h|i,b|e|16-26°C|Rich, moist, humus-heavy mix|m,w|Lush, arching fronds that love humidity.|Keep soil evenly moist and mist often; never let it dry out completely.
Heartleaf Philodendron|Philodendron hederaceum|🍃|Indoor|m|m|i|b|18-30°C|Well-draining potting mix|s,m,w|Easy heart-shaped trailing vine for shelves and hanging pots.|Water when the top 2-3 cm of soil is dry; pinch tips for fuller growth.
Monstera|Monstera deliciosa|🌿|Indoor|m|m|i,b|b|18-30°C|Rich, well-draining potting mix|s,m|Large split leaves make it a popular statement plant.|Give a moss pole to climb on and water when the top soil is dry.
Chinese Evergreen|Aglaonema commutatum|🌿|Indoor|l|m|i|b|18-30°C|Well-draining potting mix|s,m,w|Patterned leaves in green, silver or pink; tolerates low light.|Water when the top soil dries and keep away from cold drafts.
Dragon Tree|Dracaena marginata|🌴|Indoor|m|l|i,b|b|18-30°C|Well-draining potting mix|s,m,w|Slim, spiky-leaved plant with a sculptural, tree-like form.|Water lightly; fluoride in tap water can brown the leaf tips.
Jade Plant|Crassula ovata|🪴|Indoor|h|l|i,b|b|15-27°C|Gritty succulent mix|s,w|Thick-leaved succulent often kept as a long-lived houseplant.|Give bright light and water deeply but rarely, only after soil dries.
Lucky Bamboo|Dracaena sanderiana|🎋|Indoor|l|m|i|b|18-32°C|Water with pebbles, or light potting mix|s,m,w|Popular desk plant grown in water or soil.|Use clean, non-chlorinated water and change it every 1-2 weeks.
Fiddle Leaf Fig|Ficus lyrata|🌳|Indoor|h|m|i|e|18-28°C|Well-draining potting mix|s,m|Large violin-shaped leaves; stylish but sensitive to change.|Place near a bright window, avoid moving it often and never overwater.
Calathea|Calathea ornata|🌿|Indoor|m|h|i|e|18-27°C|Rich, moist, well-draining mix|m,w|Striking patterned leaves that fold at night.|Keep soil lightly moist, use filtered water and give high humidity.
Peperomia|Peperomia obtusifolia|🌱|Indoor|m|l|i|b|18-28°C|Light, well-draining mix|s,m,w|Compact plant with thick, glossy leaves that suits small spaces.|Let the soil dry between waterings; its leaves store water.
Cast Iron Plant|Aspidistra elatior|🌿|Indoor|l|m|i|b|10-30°C|Well-draining potting mix|s,m,w|Extremely tough broad-leaved plant for dark corners.|Water moderately, avoid direct sun and mostly leave it alone.
Dumb Cane|Dieffenbachia seguine|🌿|Indoor|m|m|i|b|18-30°C|Well-draining potting mix|s,m|Large, creamy-patterned leaves; the sap irritates skin and mouth.|Handle with gloves, keep away from children and pets and water when top soil dries.
Parlor Palm|Chamaedorea elegans|🌴|Indoor|l|m|i|b|16-27°C|Well-draining potting mix|s,m,w|Compact, slow-growing palm that copes with low light.|Keep soil lightly moist and avoid direct sun.
Rose|Rosa x hybrida|🌹|Flowering,Outdoor|h|m|o,b|e|15-28°C|Fertile, well-draining loamy soil|w|Classic flowering shrub available in many colours and fragrances.|Give 6+ hours of sun, water deeply, feed regularly and prune after flowering.
Hibiscus|Hibiscus rosa-sinensis|🌺|Flowering,Outdoor|h|m|o,b|b|18-35°C|Rich, well-draining soil|s,m|Large, bright blooms that flower almost all year in warm climates.|Water regularly, feed every few weeks and prune lightly for more flowers.
Arabian Jasmine|Jasminum sambac|🌼|Flowering,Outdoor|h|m|o,b|b|20-35°C|Well-draining loamy soil|s,m|Fragrant white flowers (mogra) widely used in garlands and perfumes.|Provide full sun, water regularly and prune after each flowering flush.
Marigold|Tagetes erecta|🌼|Flowering,Outdoor|h|m|o,b|b|18-30°C|Well-draining loamy soil|m,w|Easy, cheerful orange and yellow blooms that grow quickly from seed.|Water at the base, remove spent flowers and give full sun.
Bougainvillea|Bougainvillea glabra|🌸|Flowering,Outdoor|h|l|o,b|b|20-38°C|Sandy, well-draining soil|s,w|Vigorous climber covered in papery pink, purple or white bracts.|Water sparingly; a little dryness encourages more colour.
Chrysanthemum|Chrysanthemum morifolium|🌼|Flowering,Outdoor|h|m|o,b|e|10-25°C|Loamy, well-draining soil|w|Autumn and winter bloomer with dense, colourful flower heads.|Pinch growing tips early for bushier plants and water at the root.
Petunia|Petunia x atkinsiana|🌸|Flowering,Outdoor|h|m|o,b|b|10-25°C|Light, well-draining potting mix|w|Trumpet-shaped flowers ideal for hanging baskets and pots.|Deadhead often, feed every 2 weeks and water when the top soil is dry.
Zinnia|Zinnia elegans|🌼|Flowering,Outdoor|h|m|o|b|18-32°C|Well-draining loamy soil|s,m|Fast, easy annual with bright daisy-like flowers.|Sow in full sun and water the soil, not the leaves, to avoid mildew.
Periwinkle|Catharanthus roseus|🌸|Flowering,Outdoor|h|l|o,b|b|20-35°C|Well-draining soil|s,m|Heat-loving bedding plant (sadabahar) that flowers nearly year-round; toxic if eaten.|Water lightly and avoid soggy soil; no fuss once established.
Gerbera Daisy|Gerbera jamesonii|🌼|Flowering,Outdoor|h|m|o,b|e|15-26°C|Light, well-draining soil|w|Large, vivid daisy flowers on tall stems.|Keep the crown above the soil line and water early in the day.
Phalaenopsis Orchid|Phalaenopsis amabilis|🌸|Flowering,Indoor|m|m|i|e|18-30°C|Bark-based orchid mix|m,w|Long-lasting elegant blooms; a favourite flowering houseplant.|Use orchid bark, water weekly and let the roots dry briefly in between.
African Violet|Saintpaulia ionantha|💜|Flowering,Indoor|m|m|i|e|18-26°C|Light African-violet mix|m,w|Compact indoor plant with velvety leaves and small purple blooms.|Water from the bottom and avoid wetting the leaves.
Geranium|Pelargonium x hortorum|🌸|Flowering,Outdoor|h|m|o,b|b|10-25°C|Light, well-draining potting mix|w|Rounded flower clusters on bushy plants, great for pots.|Water when the top soil dries and remove faded flowers.
Sunflower|Helianthus annuus|🌻|Flowering,Outdoor|h|m|o|b|18-32°C|Deep, well-draining loamy soil|s,m|Tall, sun-following flowers that grow quickly from seed.|Sow in full sun and water deeply; support tall stems.
Dahlia|Dahlia pinnata|🌺|Flowering,Outdoor|h|m|o,b|e|15-25°C|Rich, well-draining loamy soil|w|Showy blooms in many shapes and colours grown from tubers.|Water deeply but infrequently and stake taller varieties.
Ixora|Ixora coccinea|🌺|Flowering,Outdoor|h|m|o,b|b|20-35°C|Slightly acidic, well-draining soil|s,m|Clusters of small red-orange flowers on a compact evergreen shrub.|Water regularly, feed with acidic fertilizer and prune lightly.
Moss Rose|Portulaca grandiflora|🌸|Flowering,Outdoor|h|l|o,b|b|20-35°C|Sandy, well-draining soil|s|Low, spreading succulent with bright flowers that open in sunshine.|Needs very little water and full sun; avoid rich, wet soil.
Cosmos|Cosmos bipinnatus|🌸|Flowering,Outdoor|h|m|o|b|18-30°C|Average, well-draining soil|m,w|Airy, daisy-like flowers that attract butterflies.|Sow in full sun; avoid over-feeding or it makes leaves instead of flowers.
Anthurium|Anthurium andraeanum|❤️|Flowering,Indoor|m|m|i|e|18-28°C|Loose, airy orchid-style mix|m,w|Glossy red, pink or white heart-shaped flowers that last for weeks.|Provide bright indirect light, humidity and a well-draining mix.
Kalanchoe|Kalanchoe blossfeldiana|🌸|Flowering,Indoor|h|l|i,b|b|15-27°C|Gritty succulent mix|s,w|Compact succulent with clusters of long-lasting small flowers.|Give bright light, water only when dry and remove faded blooms.
Lemon|Citrus limon|🍋|Fruit,Outdoor|h|m|o,b|b|15-35°C|Well-draining loamy soil|m|Compact citrus tree that fruits well in large pots.|Give full sun, deep watering and a citrus fertilizer every 4-6 weeks.
Dwarf Mango|Mangifera indica|🥭|Fruit,Outdoor|h|m|o|e|24-38°C|Deep, well-draining soil|m|Dwarf grafted varieties can fruit within a few years in large pots.|Water young trees regularly and reduce watering during flowering.
Guava|Psidium guajava|🍈|Fruit,Outdoor|h|m|o|b|15-35°C|Well-draining loamy soil|m|Hardy, productive fruit tree that suits home gardens.|Water young plants regularly and prune lightly to control height.
Papaya|Carica papaya|🍈|Fruit,Outdoor|h|m|o|b|22-35°C|Rich, well-draining soil|s,m|Fast-growing tropical fruit that bears within a year.|Never let water stand around the stem; it rots very easily.
Banana|Musa acuminata|🍌|Fruit,Outdoor|h|h|o|b|20-35°C|Rich, moist, well-draining soil|s,m|Large leafy plant that fruits in about a year with good care.|Water often, mulch well and feed heavily with compost.
Pomegranate|Punica granatum|🍎|Fruit,Outdoor|h|l|o,b|b|15-38°C|Well-draining loamy soil|m|Drought-tolerant shrub with showy flowers and edible fruit.|Water deeply but infrequently; irregular watering can split fruits.
Strawberry|Fragaria x ananassa|🍓|Fruit,Outdoor|h|m|o,b|e|15-25°C|Rich, well-draining soil|w|Cool-season fruit that grows well in pots and hanging baskets.|Keep soil evenly moist and mulch to keep fruit off the soil.
Fig|Ficus carica|🌳|Fruit,Outdoor|h|l|o,b|b|15-35°C|Well-draining soil|w|Hardy fruit tree that does well in containers.|Water deeply but let the soil dry out between waterings.
Sapota|Manilkara zapota|🌳|Fruit,Outdoor|h|m|o|b|23-38°C|Deep, well-draining soil|m|Slow-growing evergreen (chikoo) with sweet brown fruit.|Water young trees regularly and feed with organic manure.
Custard Apple|Annona squamosa|🍈|Fruit,Outdoor|h|l|o|b|20-35°C|Light, well-draining soil|m|Hardy small tree producing creamy, sweet fruit (sitafal).|Needs little water once established; avoid waterlogging.
Passion Fruit|Passiflora edulis|🍇|Fruit,Outdoor|h|m|o,b|e|18-30°C|Rich, well-draining soil|s,m|Vigorous vine with striking flowers and aromatic fruit.|Provide a strong trellis, regular water and regular feeding.
Grapes|Vitis vinifera|🍇|Fruit,Outdoor|h|m|o|e|15-35°C|Well-draining loamy soil|w|Climbing vine that needs a sturdy support and annual pruning.|Prune once a year, train along a trellis and water at the base.
Amla|Phyllanthus emblica|🌿|Fruit,Medicinal,Outdoor|h|l|o|b|15-38°C|Well-draining loamy soil|m|Hardy tree (Indian gooseberry) with sour, vitamin C-rich fruit.|Water young plants regularly; mature trees need little care.
Mulberry|Morus alba|🫐|Fruit,Outdoor|h|m|o|b|15-35°C|Well-draining loamy soil|m,w|Fast-growing tree that bears sweet berries.|Water regularly while young and prune after fruiting.
Cherry Tomato|Solanum lycopersicum var. cerasiforme|🍅|Fruit,Outdoor|h|m|o,b|b|18-30°C|Rich, well-draining loamy soil|m,w|Productive small-fruited tomato that suits pots and balconies.|Stake the plants, water at the root and feed regularly while fruiting.
Chilli Pepper|Capsicum annuum|🌶️|Fruit,Outdoor|h|m|o,b|b|20-32°C|Well-draining loamy soil|s,m|Compact plant that produces fruit for months.|Water evenly and pick fruit regularly to encourage more.
Dragon Fruit|Selenicereus undatus|🌵|Fruit,Outdoor|h|l|o,b|b|20-35°C|Sandy, well-draining soil|m|Climbing cactus with large night-blooming flowers and sweet fruit.|Give a sturdy post to climb and water only when the soil is dry.
Pineapple|Ananas comosus|🍍|Fruit,Outdoor|h|m|o,b|e|20-32°C|Sandy, slightly acidic soil|m|Can be grown from a store-bought crown but needs patience.|Water at the base and give a sunny, warm spot.
Mandarin Orange|Citrus reticulata|🍊|Fruit,Outdoor|h|m|o,b|e|15-32°C|Well-draining loamy soil|m|Sweet, easy-peel citrus that grows well in large containers.|Water deeply, feed with citrus fertilizer and protect from heavy frost.
Dwarf Coconut|Cocos nucifera|🥥|Fruit,Outdoor|h|h|o|e|25-35°C|Sandy, well-draining loam|m|Dwarf varieties fruit earlier and stay manageable in gardens.|Water regularly in dry weather and mulch around the base.
Aloe Vera|Aloe barbadensis miller|🌿|Medicinal,Indoor|h|l|i,o,b|b|18-30°C|Sandy, well-draining soil|s,m,w|Popular succulent whose gel is traditionally used on skin.|Water only when the soil is completely dry and give bright light.
Tulsi|Ocimum tenuiflorum|🌿|Medicinal,Herb,Outdoor|h|m|o,b|b|20-35°C|Rich, well-draining soil|s,m|Sacred, aromatic holy basil widely grown at home and used in teas.|Give sunlight, pinch flower buds and avoid waterlogging.
Neem|Azadirachta indica|🌳|Medicinal,Outdoor|h|l|o|b|20-40°C|Well-draining soil|m|Tough, fast-growing tree with a long history in traditional use.|Water young trees regularly; mature trees are very drought tolerant.
Giloy|Tinospora cordifolia|🌿|Medicinal,Outdoor|m|m|o,b|b|20-35°C|Well-draining loamy soil|m|Hardy climbing vine commonly used in traditional remedies.|Give it support to climb and water when the top soil dries.
Ashwagandha|Withania somnifera|🌿|Medicinal,Outdoor|h|l|o,b|b|20-35°C|Sandy loam|m|Shrub traditionally grown for its roots.|Sow in sunny spots and avoid overwatering.
Brahmi|Bacopa monnieri|🌱|Medicinal,Herb|m|h|o,b|b|20-35°C|Moist, loamy soil|s,m|Creeping herb that likes damp soil and is traditionally used for memory.|Keep soil consistently moist and trim to encourage spreading.
Turmeric|Curcuma longa|🌿|Medicinal,Herb|m|m|o,b|b|20-35°C|Rich, loamy soil|m|Rhizome plant grown for the familiar yellow spice.|Plant rhizomes at the start of the rains and keep soil moist but draining.
Ginger|Zingiber officinale|🫚|Medicinal,Herb|m|m|o,b|b|20-30°C|Rich, well-draining soil|m|Rhizome plant that grows well in pots with some shade.|Plant pieces with buds, keep soil moist and shaded from harsh sun.
Indian Borage|Plectranthus amboinicus|🌿|Medicinal,Herb|m|l|i,o,b|b|18-35°C|Sandy, well-draining soil|s,m,w|Fleshy, aromatic leaves traditionally used for coughs and colds.|Easy to propagate from cuttings; water only when dry.
Stevia|Stevia rebaudiana|🌿|Medicinal,Herb|h|m|o,b|e|15-30°C|Light sandy loam|s,m|Small shrub with naturally sweet leaves.|Keep soil lightly moist and pinch tips for bushy growth.
Betel Leaf|Piper betle|🍃|Medicinal|m|h|o|e|20-35°C|Rich, humus-heavy soil|m|Climbing vine grown for its heart-shaped leaves.|Provide support, shade and constant moisture.
Shatavari|Asparagus racemosus|🌿|Medicinal,Outdoor|m|l|o,b|b|20-35°C|Light, well-draining soil|m|Climbing herb traditionally valued for its roots.|Water lightly and provide support to climb.
Kalmegh|Andrographis paniculata|🌿|Medicinal|h|m|o|b|20-35°C|Sandy loam|m|Upright herb traditionally used in home remedies.|Grow in sun and water lightly in dry weather.
Gotu Kola|Centella asiatica|🍀|Medicinal,Herb|m|h|o,b|b|20-30°C|Moist, rich soil|m|Low creeping herb that thrives in damp, shady spots.|Keep soil consistently moist and partially shaded.
Moringa|Moringa oleifera|🌿|Medicinal,Outdoor|h|l|o|b|25-38°C|Sandy, well-draining soil|s,m|Fast-growing drumstick tree with edible leaves and pods.|Water lightly and prune often to keep it low.
Chamomile|Matricaria chamomilla|🌼|Medicinal,Herb,Flowering|h|m|o,b|e|10-25°C|Light, well-draining soil|w|Daisy-like flowers used for herbal tea.|Sow in a cool season and harvest flowers when fully open.
Henna|Lawsonia inermis|🌿|Medicinal,Outdoor|h|l|o|b|20-40°C|Well-draining soil|m|Hardy shrub (mehndi) whose leaves are used for natural dye.|Water young plants regularly and prune to shape.
Insulin Plant|Costus igneus|🌿|Medicinal|m|m|i,o,b|b|18-32°C|Rich, well-draining soil|m|Leafy plant with spiral stems, traditionally used in home remedies.|Keep soil moist and protect from harsh sun.
Vasaka|Justicia adhatoda|🌿|Medicinal,Outdoor|m|l|o|b|20-35°C|Well-draining soil|m|Hardy shrub traditionally used for coughs.|Water lightly and prune to maintain shape.
Ajwain|Trachyspermum ammi|🌿|Medicinal,Herb|h|l|o,b|b|15-30°C|Sandy loam|w|Aromatic seed spice plant used in traditional remedies.|Sow in a cool season and water lightly.
Mint|Mentha spicata|🌿|Herb|m|h|i,o,b|b|15-30°C|Moist, rich soil|s,m,w|Fast-spreading kitchen herb (pudina) for chutneys, drinks and teas.|Grow in its own pot, keep soil moist and pinch tips often.
Sweet Basil|Ocimum basilicum|🌿|Herb|h|m|i,o,b|b|18-32°C|Rich, well-draining soil|s,m|Aromatic kitchen herb that grows quickly in warm weather.|Pinch flower buds and water when the top soil is dry.
Coriander|Coriandrum sativum|🌿|Herb|m|m|o,b|b|15-28°C|Light, well-draining soil|w|Fast-growing leafy herb used daily in Indian cooking.|Sow seeds directly and keep soil evenly moist; it bolts in heat.
Curry Leaf|Murraya koenigii|🌿|Herb|h|m|o,b|b|20-38°C|Well-draining loamy soil|m|Aromatic leaves essential in South Indian cooking.|Water regularly, feed with compost and harvest often to keep it bushy.
Rosemary|Salvia rosmarinus|🌿|Herb|h|l|o,b|e|15-28°C|Sandy, well-draining soil|w|Woody, fragrant herb for cooking and tea.|Water sparingly and make sure the pot drains well.
Thyme|Thymus vulgaris|🌿|Herb|h|l|o,b|b|15-28°C|Sandy, well-draining soil|w|Low-growing, aromatic cooking herb.|Let soil dry between waterings and trim after flowering.
Oregano|Origanum vulgare|🌿|Herb|h|l|o,b|b|15-30°C|Well-draining soil|w,m|Hardy herb for pizzas, pastas and salads.|Give sun, water lightly and pinch tips to keep it bushy.
Parsley|Petroselinum crispum|🌿|Herb|m|m|o,b|b|10-25°C|Rich, moist, well-draining soil|w|Leafy herb used for garnish and flavour.|Sow in a cool season and keep soil evenly moist.
Lemongrass|Cymbopogon citratus|🌾|Herb,Medicinal|h|m|o,b|b|20-35°C|Well-draining loamy soil|s,m|Tall, citrus-scented grass used in teas and cooking.|Water regularly and divide clumps once they get crowded.
Lavender|Lavandula angustifolia|💜|Herb,Flowering|h|l|o,b|e|10-25°C|Sandy, alkaline, well-draining soil|w|Fragrant purple flower spikes valued for aroma.|Needs excellent drainage and little water; prune after flowering.
Sage|Salvia officinalis|🌿|Herb|h|l|o,b|b|10-28°C|Well-draining soil|w|Soft grey-green leaves used in cooking and teas.|Water sparingly and prune lightly each year.
Chives|Allium schoenoprasum|🌱|Herb|h|m|o,b|b|10-25°C|Rich, well-draining soil|w|Mild onion-flavoured herb that regrows after cutting.|Keep soil moist and snip leaves regularly.
Dill|Anethum graveolens|🌿|Herb|h|m|o,b|b|10-25°C|Light, well-draining soil|w|Feathery herb used in salads, pickles and curries.|Sow directly in a cool season and avoid transplanting.
Fenugreek|Trigonella foenum-graecum|🌿|Herb|h|m|o,b|b|10-25°C|Light, well-draining soil|w|Quick-growing methi leaves ready to harvest in a few weeks.|Sow seeds densely and water lightly each day.
Lemon Balm|Melissa officinalis|🍋|Herb|m|m|o,b|b|10-28°C|Moist, well-draining soil|m,w|Lemon-scented herb used in teas.|Keep soil moist and cut back regularly to prevent flowering.
Marjoram|Origanum majorana|🌿|Herb|h|l|o,b|e|15-28°C|Light, well-draining soil|w|Sweet, delicate cooking herb related to oregano.|Water lightly and pinch tips for bushier growth.
Fennel|Foeniculum vulgare|🌿|Herb|h|m|o|b|10-25°C|Well-draining soil|w|Tall, feathery plant grown for leaves and seeds.|Sow directly in a cool season and water regularly.
Spring Onion|Allium fistulosum|🌱|Herb|h|m|o,b|b|15-28°C|Rich, well-draining soil|w,m|Easy kitchen plant that regrows from the white base.|Keep soil moist and harvest outer leaves.
Thai Basil|Ocimum basilicum var. thyrsiflora|🌿|Herb|h|m|o,b|b|20-32°C|Rich, well-draining soil|s,m|Anise-scented basil used in Asian dishes.|Pinch flowers and water when the top soil dries.
Bay Laurel|Laurus nobilis|🍃|Herb|m|m|o,b|e|10-28°C|Well-draining soil|m|Evergreen shrub with aromatic leaves for cooking.|Grow slowly in a large pot and water when the top soil dries.
Croton|Codiaeum variegatum|🍂|Outdoor|h|m|o,b|b|18-35°C|Well-draining soil|s,m|Colourful foliage in red, yellow and orange; sap is irritating.|Give bright light for best colour; keep soil lightly moist.
Sago Palm|Cycas revoluta|🌴|Outdoor|m|l|o,b|b|15-35°C|Sandy, well-draining soil|s,m|Slow-growing, fern-like palm. All parts are highly toxic.|Keep away from children and pets; water sparingly.
Foxtail Palm|Wodyetia bifurcata|🌴|Outdoor|h|m|o|b|20-38°C|Well-draining soil|s,m|Tall, fast-growing palm with feathery fronds.|Water regularly while young and give full sun.
Bottle Palm|Hyophorbe lagenicaulis|🌴|Outdoor|h|m|o,b|b|20-35°C|Sandy, well-draining soil|s,m|Striking palm with a swollen, bottle-shaped trunk.|Give sun, water moderately and protect from cold.
Thuja|Platycladus orientalis|🌲|Outdoor|h|m|o,b|b|10-30°C|Well-draining soil|m,w|Dense evergreen often used for hedges and screens.|Water regularly while young and trim lightly to shape.
Golden Duranta|Duranta erecta|🌿|Outdoor|h|m|o,b|b|18-38°C|Well-draining soil|s,m|Golden-leaved shrub popular for hedges; berries are toxic.|Prune regularly and keep berries away from children and pets.
Weeping Fig|Ficus benjamina|🌳|Outdoor,Indoor|m|m|i,o|b|18-30°C|Well-draining soil|s,m|Graceful evergreen that dislikes being moved.|Avoid moving it often; water when the top soil dries.
Clumping Bamboo|Bambusa multiplex|🎍|Outdoor|h|h|o|b|15-35°C|Rich, moist, well-draining soil|m|Fast, clumping bamboo for privacy screens.|Water well and mulch; clumps stay put and don't spread.
Yucca|Yucca gigantea|🌵|Outdoor,Indoor|h|l|o,i,b|b|10-35°C|Sandy, well-draining soil|s,m,w|Sword-leaved plant with a sturdy trunk, good for dry spots.|Water sparingly and give plenty of light.
Agave|Agave americana|🌵|Outdoor|h|l|o,b|b|10-38°C|Sandy, well-draining soil|s,w|Large, drought-tolerant rosette with sharp tips.|Needs almost no watering and excellent drainage; handle with care.
Desert Rose|Adenium obesum|🌺|Outdoor,Flowering|h|l|o,b|e|20-38°C|Gritty, fast-draining mix|s|Swollen trunk and bright flowers; very sensitive to overwatering.|Water only when dry and keep out of rain; sap is toxic.
Frangipani|Plumeria rubra|🌸|Outdoor,Flowering|h|l|o|b|20-38°C|Well-draining soil|s,m|Fragrant tropical blooms on a hardy small tree.|Water lightly and let the soil dry fully in between.
Lantana|Lantana camara|🌸|Outdoor,Flowering|h|l|o,b|b|18-38°C|Well-draining soil|s,m|Tough, colourful flower clusters that attract butterflies; berries are toxic.|Tolerates dry spells; may spread widely, so trim regularly.
Coleus|Plectranthus scutellarioides|🍂|Outdoor|m|m|o,b|b|18-30°C|Rich, moist, well-draining soil|s,m|Bright, multicoloured leaves that suit pots and borders.|Pinch flower spikes and water when the top soil is dry.
Ashoka|Polyalthia longifolia|🌲|Outdoor|h|m|o|b|20-38°C|Well-draining soil|m|Tall, slender evergreen often used for avenues and boundaries.|Water regularly while young; it needs little care later.
Bottlebrush|Callistemon citrinus|🌺|Outdoor,Flowering|h|m|o|b|15-35°C|Well-draining soil|m|Red brush-like flowers on a hardy, spreading small tree.|Water regularly while young; prune after flowering.
Yellow Bells|Tecoma stans|🌼|Outdoor,Flowering|h|l|o|b|18-38°C|Well-draining soil|s,m|Bright yellow trumpet flowers; fast-growing and heat-tolerant.|Water lightly once established and prune to keep it compact.
Pampas Grass|Cortaderia selloana|🌾|Outdoor|h|m|o|b|10-35°C|Well-draining loamy soil|m|Large ornamental grass with feathery plumes.|Give plenty of room and cut back old growth each year.
Oleander|Nerium oleander|🌸|Outdoor,Flowering|h|l|o|b|15-40°C|Well-draining soil|m|Heat-loving flowering shrub. All parts are highly poisonous.|Keep away from children and pets; wear gloves when pruning.
Rangoon Creeper|Combretum indicum|🌺|Outdoor,Flowering|h|m|o|b|20-35°C|Rich, well-draining soil|m|Vigorous climber with fragrant flowers that change colour.|Provide a strong support and prune after flowering.
"""


def _split(codes, table):
    return [table[c.strip()] for c in codes.split(",") if c.strip()]


def _parse(raw):
    plants = []
    for number, line in enumerate(raw.strip().splitlines(), start=1):
        parts = [p.strip() for p in line.split("|")]
        if len(parts) != 13:
            raise ValueError(
                f"plants_data line {number}: expected 13 fields, got {len(parts)}: {line[:60]}"
            )

        (name, scientific, emoji, tags, sun, water, env, level,
         temperature, soil, seasons, description, care) = parts

        tag_list = [t.strip() for t in tags.split(",")]

        plants.append({
            "name": name,
            "scientific_name": scientific,
            "emoji": emoji,
            "category": tag_list[0].lower(),
            "tags": tag_list,
            "sun": SUN[sun],
            "water": WATER[water],
            "environment": _split(env, ENV),
            "difficulty": LEVEL[level],
            "temperature": temperature,
            "soil": soil,
            "seasons": _split(seasons, SEASON),
            "description": description,
            "care": care,
        })
    return plants


from plants_data_more import _RAW_MORE  # noqa: E402

PLANTS = _parse(_RAW) + _parse(_RAW_MORE)
