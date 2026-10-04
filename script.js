document.addEventListener("DOMContentLoaded", () => {

    // =====================================================
    // API CONFIGURATION
    // =====================================================
    // Local development uses the FastAPI server started with:
    //   uvicorn main:app --reload
    // After deploying the backend (Render, Railway, etc.),
    // put its public HTTPS address in PRODUCTION_API below.

    const PRODUCTION_API = "https://nursery-information.onrender.com/api";

    const isLocal = ["localhost", "127.0.0.1", ""].includes(
        window.location.hostname
    );

    const API_URL = isLocal
        ? "http://localhost:8000/api"
        : PRODUCTION_API;


    // =====================================================
    // ELEMENTS
    // =====================================================

    const $ = (id) => document.getElementById(id);

    const menuBtn = $("menuBtn");
    const mainNav = $("mainNav");
    const plantGrid = $("plantGrid");
    const plantSearch = $("plantSearch");
    const categoryFilter = $("categoryFilter");
    const sunFilter = $("sunFilter");
    const waterFilter = $("waterFilter");
    const recommendBtn = $("recommendBtn");
    const recommendationResult = $("recommendationResult");
    const diagnosisButton = $("diagnoseBtn");
    const diagnosisResult = $("diagnosisResult");
    const seasonResult = $("seasonResult");
    const modal = $("careModal");
    const modalContent = $("modalContent");
    const modalClose = $("modalClose");
    const langSelect = $("langSelect");


    // =====================================================
    // HELPERS
    // =====================================================

    // Plant data comes from our own API, but escaping keeps the page
    // safe if the database is ever edited with unexpected characters.
    function esc(value) {
        return String(value ?? "").replace(/[&<>"']/g, (c) => ({
            "&": "&amp;",
            "<": "&lt;",
            ">": "&gt;",
            '"': "&quot;",
            "'": "&#39;"
        }[c]));
    }

    const sunlightText = (v) =>
        tr({ low: "Low light", medium: "Partial", high: "Bright" }[v] || v || "Unknown");

    const waterText = (v) =>
        tr({ low: "Low water", medium: "Moderate", high: "High water" }[v] || v || "Unknown");

    const cap = (text) =>
        text ? text.charAt(0).toUpperCase() + text.slice(1) : "";

    async function api(path, options) {
        const response = await fetch(`${API_URL}${path}`, options);

        let data = null;
        try {
            data = await response.json();
        } catch (e) {
            // not JSON, handled below
        }

        if (!response.ok || !data || data.success === false) {
            throw new Error(
                (data && data.message) || `Server error: ${response.status}`
            );
        }

        return data;
    }

    function post(path, body) {
        return api(path, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(body)
        });
    }


    // =====================================================
    // LANGUAGE  (English / Hindi / Marathi)
    // =====================================================
    // Translations live in i18n.js. The English text is the key, so
    // tr("Home") gives "होम" in Hindi. Static page text is translated by
    // swapping text nodes; text built by this file calls tr() directly.

    const LANG_KEY = "nurseryiq_lang";
    const LANGS = ["en", "hi", "mr"];
    let lang = "en";

    try {
        const saved = localStorage.getItem(LANG_KEY);
        if (LANGS.includes(saved)) lang = saved;
    } catch (e) {
        // storage blocked, stay in English
    }

    function tr(text, vars) {
        const entry = window.I18N && window.I18N[text];
        let out = (lang !== "en" && entry && entry[lang]) || text;

        if (vars) {
            out = out.replace(/\{(\w+)\}/g, (match, key) =>
                vars[key] != null ? vars[key] : match
            );
        }
        return out;
    }

    // Plant names / texts come from the API in every language.
    const plantName = (plant) =>
        (lang !== "en" && plant.names && plant.names[lang]) || plant.name;

    const plantText = (plant, field) =>
        (lang !== "en" && plant.texts && plant.texts[lang] &&
            plant.texts[lang][field]) || plant[field];

    const problemName = (problem) =>
        (lang !== "en" && problem.names && problem.names[lang]) || problem.name;

    const staticNodes = [];
    const staticAttrs = [];
    const metaDescription = document.querySelector('meta[name="description"]');
    const metaEnglish = metaDescription
        ? metaDescription.getAttribute("content").replace(/\s+/g, " ").trim()
        : "";

    function collectStatic() {
        const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
        let node;

        while ((node = walker.nextNode())) {
            const parent = node.parentElement;
            if (!parent || ["SCRIPT", "STYLE", "NOSCRIPT"].includes(parent.tagName)) continue;
            if (parent.closest("[data-no-i18n]")) continue;

            const raw = node.nodeValue;
            const key = raw.replace(/\s+/g, " ").trim();

            if (key && window.I18N && window.I18N[key]) {
                staticNodes.push({
                    node,
                    key,
                    lead: raw.match(/^\s*/)[0],
                    trail: raw.match(/\s*$/)[0]
                });
            }
        }

        document.querySelectorAll("[placeholder]").forEach((el) => {
            const key = el.getAttribute("placeholder");
            if (window.I18N && window.I18N[key]) staticAttrs.push({ el, key });
        });
    }

    function applyStatic() {
        staticNodes.forEach(({ node, key, lead, trail }) => {
            node.nodeValue = lead + tr(key) + trail;
        });
        staticAttrs.forEach(({ el, key }) => el.setAttribute("placeholder", tr(key)));

        document.documentElement.lang = lang;
        document.title = tr("NurseryIQ | Smart Nursery Information Portal");
        if (metaDescription) metaDescription.setAttribute("content", tr(metaEnglish));
        if (langSelect) langSelect.value = lang;
    }

    collectStatic();
    applyStatic();


    // =====================================================
    // MOBILE MENU
    // =====================================================

    if (menuBtn && mainNav) {
        menuBtn.addEventListener("click", () => {
            mainNav.classList.toggle("open");
        });

        mainNav.querySelectorAll("a").forEach((link) => {
            link.addEventListener("click", () => {
                mainNav.classList.remove("open");
            });
        });
    }


    // =====================================================
    // CUSTOM CURSOR
    // =====================================================

    const cursor = document.querySelector(".cursor");
    const ring = document.querySelector(".cursor-ring");

    if (window.innerWidth > 700 && cursor && ring) {

        let mouseX = 0, mouseY = 0, ringX = 0, ringY = 0;

        document.addEventListener("mousemove", (event) => {
            mouseX = event.clientX;
            mouseY = event.clientY;
            cursor.style.left = mouseX + "px";
            cursor.style.top = mouseY + "px";
        });

        (function moveRing() {
            ringX += (mouseX - ringX) * 0.12;
            ringY += (mouseY - ringY) * 0.12;
            ring.style.left = ringX + "px";
            ring.style.top = ringY + "px";
            requestAnimationFrame(moveRing);
        })();
    }


    // =====================================================
    // MODAL
    // =====================================================

    function openModal(html) {
        modalContent.innerHTML = html;
        modal.classList.add("active");
        document.body.style.overflow = "hidden";
    }

    function closeModal() {
        modal.classList.remove("active");
        document.body.style.overflow = "";
    }

    if (modal && modalContent) {
        modalClose && modalClose.addEventListener("click", closeModal);

        modal.addEventListener("click", (event) => {
            if (event.target === modal) closeModal();
        });

        document.addEventListener("keydown", (event) => {
            if (event.key === "Escape") closeModal();
        });
    }


    // =====================================================
    // PLANT CARDS
    // =====================================================

    // A real photo when images/plants/<slug>.jpg exists, otherwise the emoji
    // (see the "error" listener below).
    function plantPicture(plant) {
        const emoji = plant.emoji || "🌱";

        // Works even if the backend does not send slug/image fields.
        const slug = plant.slug || String(plant.name || "")
            .toLowerCase().replace(/'/g, "").replace(/[^a-z0-9]+/g, "-")
            .replace(/^-+|-+$/g, "");
        const image = plant.image || `images/plants/${slug}.jpg`;

        return `<img class="plant-photo" src="${esc(image)}"
                     alt="${esc(plantName(plant))}" loading="lazy"
                     data-emoji="${esc(emoji)}" data-slug="${esc(slug)}"
                     data-sci="${esc(plant.scientificName || "")}"
                     data-en="${esc(plant.name || "")}">`;
    }

    // Photo order: 1) images/plants/<slug>.jpg (from fetch_images.py),
    // 2) a photo looked up live on Wikipedia (remembered in this browser),
    // 3) the emoji.
    const WIKI_KEY = "nurseryiq_wiki_images";
    const wikiMisses = new Set();
    let wikiCache = {};

    try {
        wikiCache = JSON.parse(localStorage.getItem(WIKI_KEY)) || {};
    } catch (e) {
        wikiCache = {};
    }

    async function wikiImage(slug, scientific, common) {
        if (wikiCache[slug]) return wikiCache[slug];
        if (wikiMisses.has(slug)) return "";

        const clean = scientific.replace(/'/g, "").replace(/ x /g, " ");
        const titles = [clean, clean.split(" ").slice(0, 2).join(" "), common, common + " plant"];

        for (const title of [...new Set(titles)]) {
            try {
                const response = await fetch(
                    "https://en.wikipedia.org/api/rest_v1/page/summary/" +
                    encodeURIComponent(title.replace(/ /g, "_"))
                );
                if (!response.ok) continue;

                const info = await response.json();
                const thumb = info.thumbnail && info.thumbnail.source;

                if (thumb) {
                    wikiCache[slug] = thumb.replace(/\/\d+px-/, "/480px-");
                    try {
                        localStorage.setItem(WIKI_KEY, JSON.stringify(wikiCache));
                    } catch (e) {
                        // cache not saved, still fine
                    }
                    return wikiCache[slug];
                }
            } catch (e) {
                // offline or blocked, try the next name
            }
        }

        wikiMisses.add(slug);
        return "";
    }

    function showEmoji(img) {
        const fallback = document.createElement("span");
        fallback.className = "plant-emoji";
        fallback.textContent = img.dataset.emoji || "🌱";
        img.replaceWith(fallback);
    }

    document.addEventListener("error", (event) => {
        const img = event.target;

        if (!img || img.tagName !== "IMG" || !img.classList.contains("plant-photo")) return;

        if (img.dataset.wiki) {
            showEmoji(img);
            return;
        }

        img.dataset.wiki = "tried";

        wikiImage(img.dataset.slug, img.dataset.sci || "", img.dataset.en || "")
            .then((url) => (url ? (img.src = url) : showEmoji(img)));
    }, true);

    function createPlantCard(plant) {

        const tags = Array.isArray(plant.tags) ? plant.tags : [];

        return `
            <article class="plant-card" data-plant-id="${esc(plant.id)}"
                     tabindex="0" role="button"
                     aria-label="${esc(plantName(plant))}">

                <div class="plant-image">${plantPicture(plant)}</div>

                <h3>${esc(plantName(plant) || "Unknown Plant")}</h3>

                <div class="scientific">${esc(plant.scientificName || "")}</div>

                <div class="plant-info">
                    <div class="info-pill">☀️ ${esc(sunlightText(plant.sun))}</div>
                    <div class="info-pill">💧 ${esc(waterText(plant.water))}</div>
                </div>

                <div class="tags">
                    ${tags.map((tag) => `<span class="tag">${esc(tr(tag))}</span>`).join("")}
                </div>

            </article>
        `;
    }

    function showPlantDetails(plant) {

        const detail = (label, value) => value
            ? `<div class="detail-row"><span>${tr(label)}</span><strong>${esc(value)}</strong></div>`
            : "";

        const list = (items) =>
            (items || []).map((item) => tr(cap(item))).join(", ");

        openModal(`
            <div class="plant-detail">

                <div class="detail-emoji">${plantPicture(plant)}</div>

                <h2>${esc(plantName(plant))}</h2>
                <div class="scientific">${esc(plant.scientificName)}</div>

                <p class="detail-text">${esc(plantText(plant, "description"))}</p>

                ${detail("☀️ Sunlight", sunlightText(plant.sun))}
                ${detail("💧 Water", waterText(plant.water))}
                ${detail("🌡️ Temperature", plant.temperature)}
                ${detail("🌱 Soil", plant.soil)}
                ${detail("📍 Grows in", list(plant.environment))}
                ${detail("🗓️ Best season", list(plant.seasons))}
                ${detail("⭐ Difficulty", tr(cap(plant.difficulty)))}

                <div class="detail-care">
                    <strong>${esc(tr("Care tip"))}</strong>
                    <p>${esc(plantText(plant, "care"))}</p>
                </div>

            </div>
        `);
    }

    // One click handler for every plant card on the page
    // (library, recommendations and seasonal results).
    function handleCardActivate(card) {
        const plant = plantCache.get(Number(card.dataset.plantId));
        if (plant) showPlantDetails(plant);
    }

    document.addEventListener("click", (event) => {
        const card = event.target.closest("[data-plant-id]");
        if (card) handleCardActivate(card);
    });

    document.addEventListener("keydown", (event) => {
        if (event.key !== "Enter" && event.key !== " ") return;
        const card = event.target.closest(".plant-card[data-plant-id]");
        if (card) {
            event.preventDefault();
            handleCardActivate(card);
        }
    });

    const plantCache = new Map();

    function remember(plants) {
        plants.forEach((plant) => plantCache.set(plant.id, plant));
    }


    // =====================================================
    // PLANT LIBRARY
    // =====================================================
    // All plants are downloaded once and filtered in the browser,
    // so searching and filtering feel instant.

    let allPlants = [];

    // The library opens with just these plants (one or two per type).
    // As soon as the visitor searches or picks a filter, every
    // matching plant is shown.
    const PREVIEW_COUNT = 6;
    const FEATURED = [
        "Snake Plant", "Rose", "Dwarf Mango", "Tulsi", "Mint", "Croton"
    ];

    function previewPlants() {
        const picked = FEATURED
            .map((name) => allPlants.find((plant) => plant.name === name))
            .filter(Boolean);

        for (const plant of allPlants) {
            if (picked.length >= PREVIEW_COUNT) break;
            if (!picked.includes(plant)) picked.push(plant);
        }
        return picked.slice(0, PREVIEW_COUNT);
    }

    function renderLibrary() {

        const search = plantSearch ? plantSearch.value.toLowerCase().trim() : "";
        const category = categoryFilter ? categoryFilter.value : "all";
        const sun = sunFilter ? sunFilter.value : "all";
        const water = waterFilter ? waterFilter.value : "all";

        const exploring =
            search !== "" || category !== "all" || sun !== "all" || water !== "all";

        // Plants can be searched in English, Hindi or Marathi.
        const nameMatches = (plant) =>
            [plant.name, ...Object.values(plant.names || {})]
                .some((name) => name.toLowerCase().includes(search));

        const filtered = !exploring ? previewPlants() : allPlants.filter((plant) => {

            const searchMatch =
                !search ||
                nameMatches(plant) ||
                plant.scientificName.toLowerCase().includes(search) ||
                plant.tags.some((tag) => tag.toLowerCase().includes(search));

            const categoryMatch =
                category === "all" ||
                plant.tags.some((tag) => tag.toLowerCase() === category);

            const sunMatch = sun === "all" || plant.sun === sun;
            const waterMatch = water === "all" || plant.water === water;

            return searchMatch && categoryMatch && sunMatch && waterMatch;
        });

        if (filtered.length === 0) {
            plantGrid.innerHTML = `
                <div class="state-box">
                    <div class="state-emoji">🌱</div>
                    <h3>${esc(tr("No plants found"))}</h3>
                    <p>${esc(tr("Try different filters."))}</p>
                </div>
            `;
            return;
        }

        const note = (text) => `<p class="library-note">${esc(text)}</p>`;

        plantGrid.innerHTML = exploring
            ? note(tr("{n} plants found", { n: filtered.length })) +
              filtered.map(createPlantCard).join("")
            : filtered.map(createPlantCard).join("") +
              note(tr(
                  "Showing {n} of {total} plants. Use the search and filters above to explore more.",
                  { n: filtered.length, total: allPlants.length }
              ));
    }

    async function loadPlants() {

        if (!plantGrid) return;

        plantGrid.innerHTML = `
            <div class="state-box"><p>${esc(tr("🌱 Loading plants..."))}</p></div>
        `;

        try {
            const data = await api("/plants");
            allPlants = data.plants || [];
            remember(allPlants);
            renderLibrary();

        } catch (error) {
            console.error("Plant loading error:", error);

            plantGrid.innerHTML = `
                <div class="state-box">
                    <h3>⚠️ ${esc(tr("Could not load plants"))}</h3>
                    <p>${esc(error.message)}</p>
                    <button id="retryPlants" class="retry-btn">${esc(tr("Try Again"))}</button>
                </div>
            `;

            const retry = $("retryPlants");
            retry && retry.addEventListener("click", loadPlants);
        }
    }

    [plantSearch, categoryFilter, sunFilter, waterFilter].forEach((control) => {
        if (!control) return;
        control.addEventListener(
            control === plantSearch ? "input" : "change",
            renderLibrary
        );
    });

    document.querySelectorAll(".category-grid button").forEach((button) => {
        button.addEventListener("click", () => {
            if (categoryFilter) categoryFilter.value = button.dataset.category;
            renderLibrary();
            $("plants") && $("plants").scrollIntoView({ behavior: "smooth" });
        });
    });

    loadPlants();


    // =====================================================
    // LIVE STATS (counts come from the database)
    // =====================================================

    function animateCount(element, target) {
        const duration = 1200;
        const start = performance.now();

        function tick(now) {
            const progress = Math.min((now - start) / duration, 1);
            element.textContent = Math.round(target * progress);
            if (progress < 1) requestAnimationFrame(tick);
        }

        requestAnimationFrame(tick);
    }

    async function loadStats() {
        let stats = {};

        try {
            stats = await api("/stats");
        } catch (error) {
            console.warn("Using default stats:", error.message);
        }

        // data-stat="plants|categories|problems" is filled from the database;
        // if the API is down, the number written in data-count is used instead.
        document.querySelectorAll("[data-count]").forEach((element) => {
            const live = stats[element.dataset.stat];
            animateCount(element, live != null ? live : Number(element.dataset.count));
        });
    }

    const statsSection = document.querySelector(".stats");

    if (statsSection && "IntersectionObserver" in window) {
        const observer = new IntersectionObserver((entries) => {
            if (entries.some((entry) => entry.isIntersecting)) {
                observer.disconnect();
                loadStats();
            }
        }, { threshold: 0.3 });

        observer.observe(statsSection);
    } else {
        loadStats();
    }


    // =====================================================
    // SMART RECOMMENDATION
    // =====================================================

    let recState = null;

    function renderRecommendation() {

        if (!recommendationResult || !recState) return;

        if (recState.error) {
            recommendationResult.innerHTML = `
                <div class="plant-card">
                    <h3>⚠️ ${esc(tr("Recommendation Error"))}</h3>
                    <p>${esc(tr(recState.error))}</p>
                </div>
            `;
            return;
        }

        if (recState.plants.length === 0) {
            recommendationResult.innerHTML = `
                <div class="plant-card">
                    <div class="plant-image">🌱</div>
                    <h3>${esc(tr("No match found"))}</h3>
                    <p>${esc(tr("No plants matched. Try selecting fewer conditions."))}</p>
                </div>
            `;
            return;
        }

        const note = recState.exact
            ? ""
            : `<p class="result-note">${esc(tr("No exact match, so these are the closest plants to your choices."))}</p>`;

        recommendationResult.innerHTML =
            note + recState.plants.map(createPlantCard).join("");
    }

    if (recommendBtn && recommendationResult) {

        recommendBtn.addEventListener("click", async () => {

            recommendBtn.disabled = true;
            recommendationResult.innerHTML = `<p>${esc(tr("🌱 Finding suitable plants..."))}</p>`;

            try {
                const data = await post("/recommend", {
                    environment: $("environment")?.value || "all",
                    sunlight: $("finderSun")?.value || "all",
                    water: $("finderWater")?.value || "all",
                    experience: $("experience")?.value || "all"
                });

                const matches = data.plants || [];
                remember(matches);

                recState = { plants: matches, exact: data.exact };

            } catch (error) {
                console.error("Recommendation error:", error);
                recState = { error: error.message };

            } finally {
                recommendBtn.disabled = false;
            }

            renderRecommendation();
        });
    }


    // =====================================================
    // PLANT DIAGNOSIS
    // =====================================================

    const SYMPTOM_LABELS = {
        yellow: "Yellow leaves",
        spots: "Brown / black spots",
        wilting: "Wilting",
        white: "White powder",
        curling: "Curling leaves",
        insects: "Small insects"
    };

    const SEVERITY_LABELS = {
        low: "Low risk",
        medium: "Medium risk",
        high: "High risk"
    };

    let diagState = null;

    function emptyResult(icon, title, text) {
        return `
            <div class="empty-result">
                <span>${icon}</span>
                <h3>${esc(tr(title))}</h3>
                <p>${esc(tr(text))}</p>
            </div>
        `;
    }

    function renderDiagnosis() {

        if (!diagnosisResult || !diagState) return;

        if (diagState.type === "select") {
            diagnosisResult.innerHTML = emptyResult(
                "⚠️", "Select at least one symptom",
                "Choose symptoms to generate a basic report."
            );
            return;
        }

        if (diagState.type === "error") {
            diagnosisResult.innerHTML = `
                <div class="empty-result">
                    <span>⚠️</span>
                    <h3>${esc(tr("Diagnosis Error"))}</h3>
                    <p>${esc(tr(diagState.message))}</p>
                </div>
            `;
            return;
        }

        if (diagState.problems.length === 0) {
            diagnosisResult.innerHTML = emptyResult(
                "🌱", "No matching problem found",
                "Try selecting another symptom."
            );
            return;
        }

        diagnosisResult.innerHTML = diagState.problems.map((problem) => `
            <div class="diagnosis-item">
                <strong>
                    ${esc(problem.emoji)} ${esc(problemName(problem))}
                    <span class="severity severity-${esc(problem.severity)}">
                        ${esc(tr(SEVERITY_LABELS[problem.severity] || problem.severity))}
                    </span>
                </strong>
                <p><b>${esc(tr("Matched symptoms:"))}</b> ${esc(
                    (problem.matchedSymptoms || [])
                        .map((symptom) => tr(SYMPTOM_LABELS[symptom] || symptom))
                        .join(", ")
                )}</p>
                <p><b>${esc(tr("Likely cause:"))}</b> ${esc(problem.cause)}</p>
                <p><b>${esc(tr("What to do:"))}</b> ${esc(problem.solution)}</p>
            </div>
        `).join("");
    }

    if (diagnosisButton && diagnosisResult) {

        diagnosisButton.addEventListener("click", async () => {

            const selected = [
                ...document.querySelectorAll(".symptom-box input:checked")
            ].map((input) => input.value);

            if (selected.length === 0) {
                diagState = { type: "select" };
                renderDiagnosis();
                return;
            }

            diagnosisButton.disabled = true;
            diagnosisResult.innerHTML = `<p>${esc(tr("🔍 Analyzing symptoms..."))}</p>`;

            try {
                const data = await post("/diagnose", { symptoms: selected });
                diagState = { type: "result", problems: data.problems || [] };

            } catch (error) {
                console.error("Diagnosis error:", error);
                diagState = { type: "error", message: error.message };

            } finally {
                diagnosisButton.disabled = false;
            }

            renderDiagnosis();
        });
    }


    // =====================================================
    // CARE GUIDES (static, so they work even if the API is down)
    // =====================================================

    const careGuides = {
        water: {
            title: "💧 Watering Guide",
            points: [
                "Check the soil with your finger: water when the top 2-3 cm is dry (succulents: when fully dry).",
                "Water deeply until it drains from the bottom, then empty the saucer.",
                "Overwatering kills more plants than underwatering. Yellow leaves and soggy soil are warning signs.",
                "Water in the early morning; in summer, check pots more often, in winter, less.",
                "Pots must have drainage holes."
            ]
        },
        sun: {
            title: "☀️ Sunlight Guide",
            points: [
                "Low light: a room or corner without direct sun, for example snake plant or ZZ plant.",
                "Partial light: 3-5 hours of soft or morning sun, or bright indirect light.",
                "Bright light: 6+ hours of direct sun, for example roses, hibiscus and most fruit and herbs.",
                "Stretched, pale growth means too little light; brown crispy patches mean too much.",
                "Turn pots every week so the plant grows evenly, and move plants to new light levels gradually."
            ]
        },
        soil: {
            title: "🌱 Soil & Fertilizer Guide",
            points: [
                "Good soil holds some moisture but drains quickly. Add sand or perlite for succulents and coco peat or compost for leafy plants.",
                "Mix compost or vermicompost into garden soil to feed plants slowly.",
                "Feed growing plants every 3-4 weeks in the growing season, and reduce in winter.",
                "More fertilizer is not better: over-feeding burns roots. Use half strength if unsure.",
                "Refresh the top layer of soil or repot once a year."
            ]
        },
        environment: {
            title: "🌡️ Environment Guide",
            points: [
                "Most common plants are happy between 18-30°C. Keep them away from AC vents, heaters and cold drafts.",
                "Humidity-loving plants such as ferns and calatheas benefit from grouping, pebble trays or a humidifier.",
                "Good airflow reduces fungal problems; avoid crowding plants.",
                "Protect plants from midday summer heat with partial shade.",
                "Acclimatize plants gradually when moving them between indoors and outdoors."
            ]
        }
    };

    document.querySelectorAll("[data-care]").forEach((button) => {
        button.addEventListener("click", () => {
            const guide = careGuides[button.dataset.care];
            if (!guide) return;

            openModal(`
                <h2>${esc(tr(guide.title))}</h2>
                <ul class="guide-list">
                    ${guide.points.map((p) => `<li>${esc(tr(p))}</li>`).join("")}
                </ul>
            `);
        });
    });


    // =====================================================
    // SEASONAL GUIDE
    // =====================================================

    let seasonState = null;

    function renderSeason() {

        if (!seasonResult || !seasonState) return;

        if (seasonState.error) {
            seasonResult.innerHTML = `⚠️ ${esc(tr(seasonState.error))}`;
            return;
        }

        const { season, total, plants } = seasonState;
        const seasonLabel = lang === "en" ? season : tr(cap(season));

        seasonResult.innerHTML = `
            <p class="season-summary">
                ${esc(tr(
                    "{n} plants grow well when planted in {season}. Here are some ideas:",
                    { n: total, season: seasonLabel }
                ))}
            </p>
            <div class="season-list">
                ${plants.map((plant) => `
                    <button type="button" class="season-chip"
                            data-plant-id="${esc(plant.id)}">
                        ${esc(plant.emoji)} ${esc(plantName(plant))}
                    </button>
                `).join("")}
            </div>
        `;
    }

    document.querySelectorAll("[data-season]").forEach((button) => {
        button.addEventListener("click", async () => {

            if (!seasonResult) return;

            const season = button.dataset.season;
            seasonResult.innerHTML = esc(tr("🌱 Loading ideas..."));

            try {
                const data = await api(`/season/${season}`);
                remember(data.plants);
                seasonState = { season, total: data.total, plants: data.plants };

            } catch (error) {
                console.error("Season error:", error);
                seasonState = { error: error.message };
            }

            renderSeason();
        });
    });


    // =====================================================
    // CARE REMINDERS (saved in this browser only)
    // =====================================================

    const reminderForm = $("reminderForm");
    const reminderList = $("reminderList");
    const REMINDER_KEY = "nurseryiq_reminders";

    function loadReminders() {
        try {
            return JSON.parse(localStorage.getItem(REMINDER_KEY)) || [];
        } catch (e) {
            return [];
        }
    }

    function saveReminders(reminders) {
        try {
            localStorage.setItem(REMINDER_KEY, JSON.stringify(reminders));
        } catch (e) {
            console.warn("Could not save reminders:", e);
        }
    }

    function renderReminders() {
        if (!reminderList) return;

        const reminders = loadReminders()
            .sort((a, b) => a.date.localeCompare(b.date));

        if (reminders.length === 0) {
            reminderList.innerHTML = "";
            return;
        }

        const today = new Date().toISOString().slice(0, 10);

        reminderList.innerHTML = reminders.map((item) => `
            <div class="reminder-item">
                <span>
                    ${item.date < today ? "⏰ " : ""}${esc(item.plant)} · ${esc(tr(item.type))} · ${esc(item.date)}
                </span>
                <button class="delete-reminder" data-id="${esc(item.id)}"
                        aria-label="Delete reminder">✕</button>
            </div>
        `).join("");
    }

    if (reminderForm) {

        reminderForm.addEventListener("submit", (event) => {
            event.preventDefault();

            const plant = $("reminderPlant").value.trim();
            const type = $("reminderType").value;
            const date = $("reminderDate").value;

            if (!plant || !date) return;

            const reminders = loadReminders();
            reminders.push({ id: Date.now().toString(), plant, type, date });
            saveReminders(reminders);

            reminderForm.reset();
            renderReminders();
        });

        reminderList.addEventListener("click", (event) => {
            const button = event.target.closest(".delete-reminder");
            if (!button) return;

            saveReminders(
                loadReminders().filter((item) => item.id !== button.dataset.id)
            );
            renderReminders();
        });

        renderReminders();
    }

    // =====================================================
    // LANGUAGE SWITCHER
    // =====================================================

    function setLanguage(next) {
        if (!LANGS.includes(next)) return;

        lang = next;

        try {
            localStorage.setItem(LANG_KEY, lang);
        } catch (e) {
            // not saved, still works for this visit
        }

        applyStatic();

        if (allPlants.length) renderLibrary();
        renderRecommendation();
        renderDiagnosis();
        renderSeason();
        renderReminders();
    }

    if (langSelect) {
        langSelect.addEventListener("change", () => setLanguage(langSelect.value));
    }


});
