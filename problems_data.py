"""
NurseryIQ seed data: 35 common plant problems.

Symptom keys match the checkboxes in index.html:
yellow, spots, wilting, white, curling, insects

Line format (pipe separated):
name | emoji | symptoms | likely cause | suggested action | severity (low/medium/high)
"""

SYMPTOMS = {"yellow", "spots", "wilting", "white", "curling", "insects"}

_RAW = """
Overwatering / Root Rot|💧|yellow,wilting|Soil stays soggy, so roots lack oxygen and begin to rot.|Stop watering until the top soil dries, improve drainage and repot into fresh mix, trimming any mushy brown roots.|high
Underwatering|🏜️|wilting,curling|Soil dries out completely, so leaves lose water faster than roots supply it.|Water deeply until it drains, then keep a steady schedule; mulch to hold moisture.|medium
Nitrogen Deficiency|🍂|yellow|Older, lower leaves turn pale yellow because the plant lacks nitrogen.|Feed with a balanced fertilizer or compost and remove badly yellowed leaves.|low
Iron Deficiency (Chlorosis)|🟡|yellow|New leaves turn yellow while veins stay green, often from alkaline soil or poor drainage.|Apply chelated iron, avoid overwatering and use acidic fertilizer for acid-loving plants.|medium
Magnesium Deficiency|🟡|yellow|Older leaves yellow between the veins, common in depleted or acidic soil.|Apply diluted Epsom salt (1 tsp per litre) every few weeks and refresh the soil.|low
Powdery Mildew|⚪|white|Fungal disease that leaves a white powdery coating on leaves in humid, still air.|Remove affected leaves, improve airflow, avoid wetting foliage and spray neem oil or a fungicide.|medium
Aphids|🐛|insects,curling,yellow|Small sap-sucking insects cluster on new growth and cause curled, sticky leaves.|Wash off with a strong water jet, then spray insecticidal soap or neem oil weekly.|medium
Spider Mites|🕷️|insects,spots,yellow,curling|Tiny mites cause fine yellow speckles and sometimes thin webbing, mostly in dry, warm air.|Rinse leaves, raise humidity and spray neem oil or insecticidal soap every 5-7 days.|high
Mealybugs|🐛|insects,white,yellow,wilting|Cottony white insects hide in leaf joints and weaken the plant.|Dab with alcohol-soaked cotton, then spray neem oil; isolate the plant.|high
Whiteflies|🦟|insects,yellow|Tiny white flying insects live under leaves and leave sticky residue.|Use yellow sticky traps, spray neem oil or soap underneath leaves and repeat weekly.|medium
Scale Insects|🐛|insects,yellow|Small brown bumps on stems and leaves suck sap and weaken the plant.|Scrape off gently, wipe with alcohol and follow with horticultural oil.|medium
Thrips|🐛|insects,spots,curling|Slender insects cause silvery streaks and distorted new growth.|Use blue sticky traps, prune damaged parts and spray insecticidal soap.|medium
Fungal Leaf Spot|⚫|spots,yellow|Dark spots with yellow edges form in warm, wet conditions.|Remove spotted leaves, water at the base, space plants out and use a copper-based fungicide if it spreads.|medium
Bacterial Leaf Spot|⚫|spots,yellow|Water-soaked, angular spots that spread in wet weather.|Remove infected leaves, avoid overhead watering and sanitize tools between plants.|medium
Anthracnose|⚫|spots,wilting|Sunken dark lesions on leaves or fruit caused by fungus in humid weather.|Prune affected parts, clean up fallen debris and use a suitable fungicide.|medium
Rust Disease|🟠|spots,yellow|Orange or brown pustules on the underside of leaves.|Remove infected leaves, keep foliage dry and apply a fungicide if severe.|medium
Sooty Mold|⚫|spots,insects|Black film on leaves that grows on honeydew left by sap-sucking insects.|Control aphids, whiteflies or scale, then wipe leaves with mild soapy water.|low
Downy Mildew|⚪|yellow,white|Yellow patches on top and fuzzy growth underneath in cool, damp conditions.|Remove affected leaves, increase airflow and water early in the day.|medium
Sunburn / Leaf Scorch|☀️|spots,curling,wilting|Brown, crispy patches appear when leaves get more sun than they can handle.|Move to partial shade, acclimatize gradually and water deeply.|low
Insufficient Light|🌑|yellow,wilting|Leaves turn pale and stems grow thin and leggy.|Move to a brighter spot or add a grow light; rotate the pot regularly.|low
Cold Stress|❄️|spots,wilting,yellow|Cold nights or drafts damage leaves, causing dark spots and drooping.|Move away from cold windows and AC vents; reduce watering in winter.|medium
Heat Stress|🔥|wilting,curling|Very hot weather causes midday wilting and curled leaves.|Provide afternoon shade, water early in the morning and mulch soil.|medium
Low Humidity|🌵|spots,curling|Dry air causes brown leaf tips and curling edges.|Group plants, use a pebble tray or humidifier and avoid heating vents.|low
Fertilizer Burn|🧂|spots,wilting,yellow|Excess fertilizer or salts burn roots and leaf edges.|Flush the soil with plenty of water, pause feeding and use half-strength fertilizer later.|medium
Root-Bound Plant|🪴|wilting,yellow|Roots circle the pot, leaving little room for water or nutrients.|Repot into a pot 2-5 cm larger and loosen the root ball.|low
Transplant Shock|📦|wilting,yellow|Plants droop after repotting or moving because roots are disturbed.|Keep in light shade, water well and avoid fertilizing for 2-3 weeks.|low
Fusarium Wilt|🍂|wilting,yellow|Soil-borne fungus blocks water flow and causes one-sided yellowing and wilting.|Remove and discard affected plants, avoid replanting the same crop in that soil and sanitize tools.|high
Verticillium Wilt|🍂|wilting,yellow|Soil fungus causes wilting even when soil is moist, often with yellow lower leaves.|Remove infected plants, rotate crops and use clean pots and soil.|high
Gray Mold (Botrytis)|🌫️|spots,white|Fuzzy grey mold on flowers and leaves in cool, humid conditions.|Remove infected parts, improve airflow and avoid wetting flowers.|medium
Leaf Miners|🐛|spots,curling|Larvae tunnel inside leaves, leaving pale winding trails.|Remove affected leaves, use sticky traps and spray neem oil.|low
Caterpillar Damage|🐛|insects,spots|Chewed leaves with holes and droppings.|Hand-pick caterpillars, check leaf undersides and use neem or a biological spray if numerous.|low
Mosaic Virus|🧬|yellow,curling,spots|Mottled yellow-green leaves and stunted growth; there is no cure.|Remove and discard infected plants, control aphids and wash hands and tools.|high
Leaf Curl Virus|🧬|curling,yellow|Leaves curl and crinkle, usually spread by whiteflies; there is no cure.|Remove severely affected plants, control whiteflies and use healthy seedlings.|high
Salt / Hard Water Buildup|🧂|white,yellow|White crust on soil or pot rim and yellowing leaf edges from mineral salts.|Flush the soil with clean water, use rainwater or filtered water and repot if heavy.|low
Calcium Deficiency|🍅|spots,wilting|Dark sunken patches on fruit or new leaves caused by uneven watering.|Water consistently, mulch and add gypsum or crushed eggshell to the soil.|low
"""


def _parse(raw):
    problems = []
    for number, line in enumerate(raw.strip().splitlines(), start=1):
        parts = [p.strip() for p in line.split("|")]
        if len(parts) != 6:
            raise ValueError(
                f"problems_data line {number}: expected 6 fields, got {len(parts)}: {line[:60]}"
            )

        name, emoji, symptoms, cause, solution, severity = parts
        symptom_list = [s.strip() for s in symptoms.split(",")]

        unknown = set(symptom_list) - SYMPTOMS
        if unknown:
            raise ValueError(f"problems_data line {number}: unknown symptoms {unknown}")

        problems.append({
            "name": name,
            "emoji": emoji,
            "symptoms": symptom_list,
            "cause": cause,
            "solution": solution,
            "severity": severity,
        })
    return problems


PROBLEMS = _parse(_RAW)
