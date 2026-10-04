"""
NurseryIQ translations (Hindi + Marathi) for data that lives in the backend.

Line format (pipe separated):  English name | Hindi | Marathi

* NAMES      -> plant names              (all plants)
* PROBLEMS   -> plant-problem names      (all problems)
* TEXT_HI / TEXT_MR hold OPTIONAL translated description and care tips:

      TEXT_HI["Snake Plant"] = ("<description in Hindi>", "<care tip in Hindi>")

  Until a plant has an entry there, the app shows the English description
  and care tip for it (names, labels and the rest of the page are translated).
"""

_PLANT_NAMES = """
Snake Plant|स्नेक प्लांट|स्नेक प्लांट
Money Plant|मनी प्लांट|मनी प्लांट
Peace Lily|पीस लिली|पीस लिली
Spider Plant|स्पाइडर प्लांट|स्पायडर प्लांट
ZZ Plant|जेडज़ेड प्लांट|झेडझेड प्लांट
Rubber Plant|रबर प्लांट|रबर प्लांट
Areca Palm|अरेका पाम|अरेका पाम
Boston Fern|बोस्टन फर्न|बोस्टन फर्न
Heartleaf Philodendron|हार्टलीफ फिलोडेंड्रोन|हार्टलीफ फिलोडेंड्रॉन
Monstera|मॉन्स्टेरा|मॉन्स्टेरा
Chinese Evergreen|चाइनीज़ एवरग्रीन|चायनीज एव्हरग्रीन
Dragon Tree|ड्रैगन ट्री|ड्रॅगन ट्री
Jade Plant|जेड प्लांट|जेड प्लांट
Lucky Bamboo|लकी बैंबू|लकी बांबू
Fiddle Leaf Fig|फिडल लीफ फिग|फिडल लीफ फिग
Calathea|कैलाथिया|कॅलाथिया
Peperomia|पेपेरोमिया|पेपेरोमिया
Cast Iron Plant|कास्ट आयरन प्लांट|कास्ट आयर्न प्लांट
Dumb Cane|डंब केन|डंब केन
Parlor Palm|पार्लर पाम|पार्लर पाम
Rose|गुलाब|गुलाब
Hibiscus|गुड़हल|जास्वंद
Arabian Jasmine|मोगरा|मोगरा
Marigold|गेंदा|झेंडू
Bougainvillea|बोगनवेलिया|बोगनवेल
Chrysanthemum|गुलदाउदी|शेवंती
Petunia|पेटुनिया|पेटुनिया
Zinnia|जिनिया|झिनिया
Periwinkle|सदाबहार|सदाफुली
Gerbera Daisy|जरबेरा|जरबेरा
Phalaenopsis Orchid|फेलेनोप्सिस ऑर्किड|फॅलेनॉप्सिस ऑर्किड
African Violet|अफ्रीकन वायलेट|आफ्रिकन व्हायोलेट
Geranium|जेरेनियम|जेरेनियम
Sunflower|सूरजमुखी|सूर्यफूल
Dahlia|डहलिया|डेलिया
Ixora|इक्सोरा (रंगन)|इक्झोरा
Moss Rose|पोर्टुलाका (नौ बजे का फूल)|पोर्टुलाका
Cosmos|कॉसमॉस|कॉसमॉस
Anthurium|एंथुरियम|अँथुरियम
Kalanchoe|कलांचो|कालांचो
Lemon|नींबू|लिंबू
Dwarf Mango|बौना आम|बुटका आंबा
Guava|अमरूद|पेरू
Papaya|पपीता|पपई
Banana|केला|केळी
Pomegranate|अनार|डाळिंब
Strawberry|स्ट्रॉबेरी|स्ट्रॉबेरी
Fig|अंजीर|अंजीर
Sapota|चीकू|चिकू
Custard Apple|सीताफल|सीताफळ
Passion Fruit|पैशन फ्रूट|पॅशन फ्रूट
Grapes|अंगूर|द्राक्षे
Amla|आंवला|आवळा
Mulberry|शहतूत|तूत
Cherry Tomato|चेरी टमाटर|चेरी टोमॅटो
Chilli Pepper|मिर्च|मिरची
Dragon Fruit|ड्रैगन फ्रूट|ड्रॅगन फ्रूट
Pineapple|अनानास|अननस
Mandarin Orange|संतरा|संत्रे
Dwarf Coconut|बौना नारियल|बुटका नारळ
Mint|पुदीना|पुदिना
Sweet Basil|स्वीट बेसिल|स्वीट बेसिल
Coriander|धनिया|कोथिंबीर
Curry Leaf|कढ़ी पत्ता|कढीपत्ता
Rosemary|रोज़मेरी|रोझमेरी
Thyme|थाइम|थाइम
Oregano|ओरिगैनो|ओरेगानो
Parsley|अजमोद|पार्सली
Lemongrass|लेमनग्रास|गवती चहा
Lavender|लैवेंडर|लव्हेंडर
Sage|सेज|सेज
Chives|चाइव्स|चाइव्हज
Dill|सोया|शेपू
Fenugreek|मेथी|मेथी
Lemon Balm|लेमन बाम|लेमन बाम
Marjoram|मार्जोरम|मार्जोरम
Fennel|सौंफ|बडीशेप
Spring Onion|हरी प्याज़|कांद्याची पात
Thai Basil|थाई बेसिल|थाई बेसिल
Bay Laurel|तेज पत्ता|तमालपत्र
Aloe Vera|एलोवेरा (घृतकुमारी)|कोरफड
Tulsi|तुलसी|तुळस
Neem|नीम|कडुनिंब
Giloy|गिलोय|गुळवेल
Ashwagandha|अश्वगंधा|अश्वगंधा
Brahmi|ब्राह्मी|ब्राह्मी
Turmeric|हल्दी|हळद
Ginger|अदरक|आले
Indian Borage|पत्थरचूर (अजवाइन पत्ता)|पानओवा
Stevia|स्टीविया|स्टेव्हिया
Betel Leaf|पान|विड्याचे पान
Shatavari|शतावरी|शतावरी
Kalmegh|कालमेघ|कालमेघ
Gotu Kola|मंडूकपर्णी|गोटू कोला
Moringa|सहजन|शेवगा
Chamomile|कैमोमाइल|कॅमोमाइल
Henna|मेहंदी|मेंदी
Insulin Plant|इंसुलिन प्लांट|इन्सुलिन प्लांट
Vasaka|अडूसा|अडुळसा
Ajwain|अजवाइन|ओवा
Croton|क्रोटन|क्रोटॉन
Sago Palm|सागो पाम|सागो पाम
Foxtail Palm|फॉक्सटेल पाम|फॉक्सटेल पाम
Bottle Palm|बॉटल पाम|बॉटल पाम
Thuja|थूजा|थुजा
Golden Duranta|गोल्डन डुरंटा|गोल्डन डुरांटा
Weeping Fig|वीपिंग फिग|वीपिंग फिग
Clumping Bamboo|बांस|बांबू
Yucca|युक्का|युका
Agave|एगेव (रामबांस)|घायपात
Desert Rose|डेज़र्ट रोज़ (एडेनियम)|डेझर्ट रोझ
Frangipani|चंपा|चाफा
Lantana|लैंटाना|घाणेरी
Coleus|कोलियस|कोलियस
Ashoka|अशोक|अशोक
Bottlebrush|बॉटलब्रश|बॉटलब्रश
Yellow Bells|येलो बेल्स (टेकोमा)|येलो बेल्स (टेकोमा)
Pampas Grass|पम्पास घास|पंपास गवत
Oleander|कनेर|कण्हेर
Rangoon Creeper|मधुमालती|मधुमालती
English Ivy|इंग्लिश आइवी|इंग्लिश आयव्ही
Prayer Plant|प्रेयर प्लांट|प्रेयर प्लांट
String of Pearls|स्ट्रिंग ऑफ पर्ल्स|स्ट्रिंग ऑफ पर्ल्स
Burro's Tail|बरोज़ टेल|बरोज टेल
Zebra Haworthia|ज़ेबरा हॉवर्थिया|झेब्रा हॉवर्थिया
Echeveria|एकेवेरिया|एकेव्हेरिया
Christmas Cactus|क्रिसमस कैक्टस|ख्रिसमस कॅक्टस
Bird's Nest Fern|बर्ड्स नेस्ट फर्न|बर्ड्स नेस्ट फर्न
Kentia Palm|केंटिया पाम|केंटिया पाम
Ponytail Palm|पोनीटेल पाम|पोनीटेल पाम
Polka Dot Plant|पोल्का डॉट प्लांट|पोल्का डॉट प्लांट
Wandering Jew|वांडरिंग ज्यू|वांडरिंग ज्यू
Chinese Money Plant|चाइनीज़ मनी प्लांट|चायनीज मनी प्लांट
Rex Begonia|रेक्स बेगोनिया|रेक्स बेगोनिया
Nerve Plant|नर्व प्लांट|नर्व्ह प्लांट
Syngonium|सिंगोनियम|सिंगोनियम
Philodendron Birkin|फिलोडेंड्रोन बर्किन|फिलोडेंड्रॉन बर्किन
Lotus|कमल|कमळ
Spanish Jasmine|चमेली|जाई
Night Jasmine|हरसिंगार (पारिजात)|पारिजातक
Tuberose|रजनीगंधा|निशिगंध
Crossandra|कनकांबरम|अबोली
Balsam|गुलमेहंदी|तेरडा
Globe Amaranth|गोम्फ्रेना (बटन फूल)|गोम्फ्रेना
China Aster|चाइना एस्टर|चायना अॅस्टर
Scarlet Sage|साल्विया|साल्व्हिया
Snapdragon|स्नैपड्रैगन|स्नॅपड्रॅगन
Pansy|पैंज़ी|पॅन्सी
Lily|लिली|लिली
Gladiolus|ग्लैडियोलस|ग्लॅडिओलस
Canna Lily|कैना लिली|कर्दळ (कॅना)
Hydrangea|हाइड्रेंजिया|हायड्रेंजिया
Fuchsia|फुशिया|फुशिया
Wax Begonia|वैक्स बेगोनिया|वॅक्स बेगोनिया
Jackfruit|कटहल|फणस
Jamun|जामुन|जांभूळ
Indian Jujube|बेर|बोर
Tamarind|इमली|चिंच
Karonda|करौंदा|करवंद
Kokum|कोकम|कोकम
Starfruit|कमरख|कमरख
Lychee|लीची|लिची
Avocado|एवोकाडो|अॅव्होकॅडो
Bael|बेल|बेल
Wood Apple|कैथा|कवठ
Sweet Lime|मौसंबी|मोसंबी
Muskmelon|खरबूजा|खरबूज
Watermelon|तरबूज|कलिंगड
Date Palm|खजूर|खजूर
Phalsa|फालसा|फालसा
Rose Apple|जम्बू (रोज़ एप्पल)|जंबू (रोझ अॅपल)
Arjuna|अर्जुन|अर्जुन
Sarpagandha|सर्पगंधा|सर्पगंधा
Shankhpushpi|शंखपुष्पी|शंखपुष्पी
Haritaki|हरड़|हिरडा
Bibhitaki|बहेड़ा|बेहडा
Safed Musli|सफेद मूसली|सफेद मुसळी
Noni|नोनी|नोनी
Bhringraj|भृंगराज|माका
Punarnava|पुनर्नवा|पुनर्नवा
Chitrak|चित्रक|चित्रक
Sweet Flag|वच|वेखंड
Echinacea|इकिनेशिया|एकिनेशिया
Calendula|कैलेंडुला|कॅलेंडुला
Black Cumin|कलौंजी|काळे जिरे
Long Pepper|पिप्पली|पिंपळी
Black Pepper|काली मिर्च|काळी मिरी
Cardamom|इलायची|वेलची
Tarragon|टैरागन|टॅरागॉन
Lemon Thyme|लेमन थाइम|लेमन थाइम
Spearmint|स्पेयरमिंट|स्पिअरमिंट
Peppermint|पेपरमिंट|पेपरमिंट
Catnip|कैटनिप|कॅटनिप
Borage|बोरेज|बोरेज
Summer Savory|समर सेवरी|समर सेव्हरी
Sorrel|चुक्का|चुका
Arugula|अरुगुला|अरुगुला
Celery|सेलरी|सेलरी
Garlic|लहसुन|लसूण
Garlic Chives|लहसुनी चाइव्स|गार्लिक चाइव्ह्ज
Mustard Greens|सरसों का साग|मोहरीची पाने
Pandan|पैंडन|पँडन
Vietnamese Coriander|वियतनामी धनिया|व्हिएतनामी कोथिंबीर
Anise|अनीस|अॅनिस
Gulmohar|गुलमोहर|गुलमोहर
Mountain Ebony|कचनार|कांचन
Jacaranda|जकरंदा|जॅकरांडा
Pride of India|जारुल|तामण
Crape Myrtle|क्रेप मर्टल|क्रेप मर्टल
Ti Plant|टी प्लांट|टी प्लांट
Song of India|सॉन्ग ऑफ इंडिया|सॉन्ग ऑफ इंडिया
Firebush|फायरबुश|फायरबुश
Crape Jasmine|चांदनी|चांदणी
Gardenia|गार्डेनिया|गंधराज
Night Queen|रात की रानी|रातराणी
Mussaenda|मुसेंडा|मुसेंडा
Blue Trumpet Vine|ब्लू ट्रंपेट वाइन|ब्लू ट्रम्पेट व्हाइन
Golden Trumpet|एलामंडा (गोल्डन ट्रंपेट)|अलमांडा
Crown of Thorns|क्राउन ऑफ थॉर्न्स|क्राऊन ऑफ थॉर्न्स
Pentas|पेंटास|पेंटास
"""

_PROBLEM_NAMES = """
Overwatering / Root Rot|अधिक पानी / जड़ सड़न|जास्त पाणी / मुळे सडणे
Underwatering|कम पानी|कमी पाणी
Nitrogen Deficiency|नाइट्रोजन की कमी|नायट्रोजनची कमतरता
Iron Deficiency (Chlorosis)|आयरन की कमी (क्लोरोसिस)|लोहाची कमतरता (क्लोरोसिस)
Magnesium Deficiency|मैग्नीशियम की कमी|मॅग्नेशियमची कमतरता
Powdery Mildew|चूर्णिल फफूंद (पाउडरी मिल्ड्यू)|भुरी रोग (पावडरी मिल्ड्यू)
Aphids|माहू (एफिड्स)|मावा (अॅफिड्स)
Spider Mites|मकड़ी माइट|कोळी कीड (स्पायडर माइट)
Mealybugs|मिलीबग|पिठ्या ढेकूण
Whiteflies|सफेद मक्खी|पांढरी माशी
Scale Insects|शल्क कीट (स्केल)|खवले कीड (स्केल)
Thrips|थ्रिप्स|फुलकिडे (थ्रिप्स)
Fungal Leaf Spot|फफूंद जनित पत्ती धब्बे|बुरशीजन्य पानांवरील ठिपके
Bacterial Leaf Spot|जीवाणु पत्ती धब्बे|जिवाणूजन्य पानांवरील ठिपके
Anthracnose|एन्थ्रेक्नोज|अँथ्रॅक्नोज
Rust Disease|रतुआ (रस्ट)|तांबेरा रोग
Sooty Mold|काली फफूंद (सूटी मोल्ड)|काजळी रोग
Downy Mildew|मृदुरोमिल फफूंद (डाउनी मिल्ड्यू)|केवडा रोग
Sunburn / Leaf Scorch|धूप से झुलसना|उन्हामुळे पाने करपणे
Insufficient Light|कम रोशनी|अपुरा प्रकाश
Cold Stress|ठंड का तनाव|थंडीचा ताण
Heat Stress|गर्मी का तनाव|उष्णतेचा ताण
Low Humidity|कम नमी|कमी आर्द्रता
Fertilizer Burn|उर्वरक से जलना|खताने जळणे
Root-Bound Plant|जड़ों का गमले में जकड़ना|मुळे कुंडीत दाटणे
Transplant Shock|रोपाई का झटका|पुनर्लागवडीचा धक्का
Fusarium Wilt|फ्यूज़ेरियम विल्ट|फ्युझेरियम मर रोग
Verticillium Wilt|वर्टिसिलियम विल्ट|व्हर्टिसिलियम मर रोग
Gray Mold (Botrytis)|ग्रे मोल्ड (बोट्राइटिस)|ग्रे मोल्ड (बोट्रायटिस)
Leaf Miners|पत्ती सुरंगक (लीफ माइनर)|पान पोखरणारी अळी
Caterpillar Damage|इल्ली से नुकसान|अळ्यांचे नुकसान
Mosaic Virus|मोज़ेक वायरस|मोझॅक व्हायरस
Leaf Curl Virus|पत्ती मोड़क वायरस|पाने गुंडाळणारा विषाणू (लीफ कर्ल)
Salt / Hard Water Buildup|नमक / कठोर पानी का जमाव|क्षार / कठीण पाण्याचा साठा
Calcium Deficiency|कैल्शियम की कमी|कॅल्शियमची कमतरता
"""


def _parse(raw):
    table = {}
    for number, line in enumerate(raw.strip().splitlines(), start=1):
        parts = [p.strip() for p in line.split("|")]
        if len(parts) != 3 or not all(parts):
            raise ValueError(f"translations line {number}: bad line: {line[:50]}")
        table[parts[0]] = {"hi": parts[1], "mr": parts[2]}
    return table


NAMES = _parse(_PLANT_NAMES)
PROBLEMS = _parse(_PROBLEM_NAMES)

# Optional: English name -> (description, care tip) in that language.
TEXT_HI = {}
TEXT_MR = {}
TEXT = {"hi": TEXT_HI, "mr": TEXT_MR}
