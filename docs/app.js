// AI Plugin Directory - TripAdvisor for AI Agent Plugins
// Pure vanilla JS, no build tools, hash-based routing

(function () {
    'use strict';

    // ========== CONFIG ==========
    const CDN_BASE = 'https://cdn.jsdelivr.net/gh/dmgrok/agent-plugins@main/';
    const isLocal = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1';
    const BASE = isLocal ? './' : CDN_BASE;

    const PLUGINS_URL = BASE + 'plugins.json';
    const CATALOG_URL = BASE + 'catalog.json';
    const TAXONOMY_URL = BASE + 'taxonomy.json';
    const GAP_URL = BASE + 'gap_analysis.json';
    const BUNDLES_URL = BASE + 'bundles.json';
    const USE_CASES_URL = BASE + 'use_cases.json';
    const REVIEWS_URL = BASE + 'reviews.json';

    const PAGE_SIZE = 24;

    // ========== PERSONAS ==========
    const PERSONAS = [
        { id: 'knowledge-worker', name: 'Knowledge Worker', icon: '📚', tagline: 'Documents, research, and productivity', categories: ['documents', 'enterprise'], tags: ['docs', 'productivity', 'writing', 'notion'] },
        { id: 'web-developer', name: 'Web Developer', icon: '🌐', tagline: 'Frontend, React, and modern web apps', categories: ['development'], tags: ['frontend', 'web', 'react', 'nextjs', 'design', 'ui'] },
        { id: 'backend-engineer', name: 'Backend Engineer', icon: '⚙️', tagline: 'APIs, databases, and microservices', categories: ['development'], tags: ['backend', 'api', 'python', 'database'] },
        { id: 'mobile-developer', name: 'Mobile Developer', icon: '📱', tagline: 'iOS, Android, and cross-platform', categories: ['development'], tags: ['mobile', 'expo', 'react-native', 'ios', 'android'] },
        { id: 'devops-engineer', name: 'DevOps Engineer', icon: '🚀', tagline: 'CI/CD, cloud, and infrastructure', categories: ['development'], tags: ['devops', 'ci-cd', 'github', 'azure', 'cloud', 'docker'] },
        { id: 'data-scientist', name: 'Data Scientist', icon: '🧬', tagline: 'ML, data pipelines, and experiments', categories: ['ml-ai', 'data'], tags: ['ml', 'data', 'huggingface', 'python', 'ai'] },
        { id: 'security-engineer', name: 'Security Engineer', icon: '🔒', tagline: 'Security audits, compliance, and hardening', categories: ['development'], tags: ['security', 'audit', 'compliance'] },
        { id: 'startup-founder', name: 'Startup Founder', icon: '💡', tagline: 'Ship fast with full-stack bundles', categories: ['development', 'creative'], tags: ['fullstack', 'deployment', 'design', 'ai'] }
    ];

    // ========== COMPATIBILITY PLATFORMS ==========
    const PLATFORMS = [
        { id: 'claude', label: 'Claude', abbr: 'CL' },
        { id: 'cursor', label: 'Cursor', abbr: 'CU' },
        { id: 'copilot', label: 'Copilot', abbr: 'CP' },
        { id: 'gemini', label: 'Gemini', abbr: 'GE' },
        { id: 'codex', label: 'Codex', abbr: 'CX' }
    ];

    // Official providers
    const OFFICIAL_PROVIDERS = ['anthropics', 'github', 'openai', 'vercel', 'huggingface'];

    // ========== STATE ==========
    let state = {
        plugins: [],
        bundles: [],
        taxonomy: null,
        gapData: null,
        reviews: {},
        currentView: 'home', // home | persona | search | usecase
        currentPersona: null,
        currentUseCase: null,
        searchQuery: '',
        filterCategory: 'all',
        filterSort: 'stars',
        searchSort: 'relevance',
        visibleCount: PAGE_SIZE,
        selectedStack: new Set(JSON.parse(localStorage.getItem('plugstack_stack') || '[]')),
        loading: true
    };

    // ========== DATA LOADING ==========
    async function loadJSON(url, fallbackUrl) {
        try {
            const res = await fetch(url);
            if (!res.ok && fallbackUrl) {
                const fb = await fetch(fallbackUrl);
                if (fb.ok) return await fb.json();
            }
            if (res.ok) return await res.json();
        } catch (e) {
            if (fallbackUrl) {
                try {
                    const fb = await fetch(fallbackUrl);
                    if (fb.ok) return await fb.json();
                } catch (_) {}
            }
        }
        return null;
    }

    async function loadData() {
        state.loading = true;
        render();

        const [pluginsData, catalogData, taxonomyData, gapData, bundlesData, useCasesData, reviewsData] = await Promise.all([
            loadJSON(PLUGINS_URL),
            loadJSON(CATALOG_URL),
            loadJSON(TAXONOMY_URL),
            loadJSON(GAP_URL),
            loadJSON(BUNDLES_URL),
            loadJSON(USE_CASES_URL),
            loadJSON(REVIEWS_URL)
        ]);

        // Use plugins.json if available, otherwise fall back to catalog.json
        if (pluginsData && (pluginsData.plugins || pluginsData.skills)) {
            state.plugins = pluginsData.plugins || pluginsData.skills;
        } else if (catalogData && catalogData.skills) {
            state.plugins = catalogData.skills;
        } else {
            state.plugins = [];
        }

        state.taxonomy = taxonomyData;
        state.gapData = gapData;
        state.bundles = bundlesData ? bundlesData.bundles || [] : [];
        state.useCases = useCasesData ? useCasesData.use_cases || [] : [];
        state.reviews = reviewsData ? reviewsData.reviews || {} : {};

        // Derive compatibility for plugins based on provider and skill type
        state.plugins = state.plugins.map(p => {
            if (!p.compatibility) {
                p.compatibility = deriveCompatibility(p);
            }
            return p;
        });

        state.loading = false;
        updateStackBadge();
        handleRoute();
    }

    function deriveCompatibility(plugin) {
        // Heuristic: all skills work with Claude, most work with Cursor
        // MCP-required ones are Claude/Cursor only
        const compat = { claude: true, cursor: true, copilot: false, gemini: false, codex: false };
        if (!plugin.requires_mcp) {
            compat.copilot = true;
            compat.gemini = true;
            compat.codex = true;
        }
        if (plugin.provider === 'openai') {
            compat.codex = true;
            compat.copilot = true;
        }
        if (plugin.provider === 'github') {
            compat.copilot = true;
        }
        return compat;
    }

    // ========== ROUTING ==========
    function handleRoute() {
        const hash = window.location.hash.slice(1);
        if (hash.startsWith('persona/')) {
            const personaId = hash.replace('persona/', '');
            const persona = PERSONAS.find(p => p.id === personaId);
            if (persona) {
                state.currentView = 'persona';
                state.currentPersona = persona;
                state.visibleCount = PAGE_SIZE;
                render();
                return;
            }
        } else if (hash.startsWith('plugin/')) {
            const pluginId = hash.replace('plugin/', '').replace(/-/g, '/');
            const plugin = state.plugins.find(p => p.id === pluginId || p.id.replace(/\//g, '-') === hash.replace('plugin/', ''));
            if (plugin) {
                state.currentView = 'home';
                render();
                openModal(plugin);
                return;
            }
        } else if (hash.startsWith('search/')) {
            state.searchQuery = decodeURIComponent(hash.replace('search/', ''));
            state.currentView = 'search';
            state.visibleCount = PAGE_SIZE;
            render();
            const input = document.getElementById('search-input');
            if (input) input.value = state.searchQuery;
            return;
        } else if (hash.startsWith('usecase/')) {
            state.currentUseCase = hash.replace('usecase/', '');
            state.currentView = 'usecase';
            state.visibleCount = PAGE_SIZE;
            render();
            return;
        }

        state.currentView = 'home';
        state.currentPersona = null;
        state.searchQuery = '';
        state.visibleCount = PAGE_SIZE;
        render();
    }

    window.addEventListener('hashchange', handleRoute);

    // ========== THEME ==========
    function initTheme() {
        const stored = localStorage.getItem('theme');
        if (stored) {
            document.documentElement.setAttribute('data-theme', stored);
        }
        document.getElementById('theme-toggle').addEventListener('click', toggleTheme);
    }

    function toggleTheme() {
        const current = document.documentElement.getAttribute('data-theme');
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        let next;
        if (current === 'dark') next = 'light';
        else if (current === 'light') next = 'dark';
        else next = prefersDark ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', next);
        localStorage.setItem('theme', next);
    }

    // ========== RENDERING ==========
    function render() {
        const app = document.getElementById('app');
        if (state.loading) {
            app.innerHTML = renderLoading();
            return;
        }

        switch (state.currentView) {
            case 'home':
                app.innerHTML = renderHome();
                break;
            case 'persona':
                app.innerHTML = renderPersonaView();
                break;
            case 'search':
                app.innerHTML = renderSearchView();
                break;
            case 'usecase':
                app.innerHTML = renderUseCaseView();
                break;
        }

        attachEventListeners();
        initSearch();
    }

    function renderLoading() {
        return `
            <div class="loading-container">
                <div class="loading-spinner"></div>
                <p class="loading-text">Loading plugin directory...</p>
            </div>
        `;
    }

    // ========== HOME VIEW ==========
    function renderHome() {
        const trending = getTrendingPlugins();
        return `
            ${renderHero()}
            ${renderUseCaseSection()}
            <div class="section-header">
                <h2 class="section-title">Or browse by role</h2>
                <span class="section-subtitle">Get a curated plugin stack for your persona</span>
            </div>
            ${renderPersonaGrid()}
            <div class="section-header">
                <h2 class="section-title">Trending Plugins</h2>
                <span class="section-subtitle">Most popular by stars</span>
            </div>
            ${renderTrendingRow(trending)}
            <div class="section-header">
                <h2 class="section-title">All Plugins</h2>
                <span class="section-subtitle">${state.plugins.length} plugins available</span>
            </div>
            ${renderFilterBar()}
            ${renderPluginsGrid(getFilteredPlugins())}
            ${renderLoadMore(getFilteredPlugins().length)}
        `;
    }

    function renderUseCaseSection() {
        if (!state.useCases || state.useCases.length === 0) return '';
        const featured = state.useCases.slice(0, 8);
        return `
            <div class="section-header">
                <h2 class="section-title">What are you building?</h2>
                <span class="section-subtitle">Start with an outcome, get a complete plugin stack</span>
            </div>
            <div class="use-case-pills">
                ${featured.map(uc => `
                    <button class="use-case-pill" data-usecase="${uc.id}">
                        <span class="use-case-pill-title">${uc.title}</span>
                        <span class="use-case-pill-persona">${PERSONAS.find(p => p.id === uc.persona)?.icon || ''} ${uc.persona.replace('-', ' ')}</span>
                    </button>
                `).join('')}
            </div>
        `;
    }

    function renderHero() {
        const totalPlugins = state.plugins.length;
        const categories = [...new Set(state.plugins.map(p => p.category))].length;
        const providers = [...new Set(state.plugins.map(p => p.provider))].length;
        return `
            <section class="hero" aria-label="Welcome">
                <div class="hero-content">
                    <h1>What are you trying to build?</h1>
                    <p>Don't browse categories — describe your goal. We'll recommend the plugin stack that gets you there, show what's covered, and flag what's missing.</p>
                    <div class="hero-search">
                        <div class="search-container">
                            <svg class="search-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg>
                            <input type="text" id="search-input" class="search-input" placeholder="Ship an MVP, automate code reviews, build a RAG system..." autocomplete="off" aria-label="Search plugins and use cases">
                            <div id="search-autocomplete" class="search-autocomplete" role="listbox"></div>
                        </div>
                    </div>
                    <div class="hero-stats">
                        <div class="hero-stat">
                            <span class="hero-stat-value">${totalPlugins.toLocaleString()}</span>
                            <span class="hero-stat-label">Plugins</span>
                        </div>
                        <div class="hero-stat">
                            <span class="hero-stat-value">${providers}</span>
                            <span class="hero-stat-label">Providers</span>
                        </div>
                        <div class="hero-stat">
                            <span class="hero-stat-value">${categories}</span>
                            <span class="hero-stat-label">Categories</span>
                        </div>
                    </div>
                </div>
            </section>
        `;
    }

    function renderPersonaGrid() {
        return `
            <div class="persona-grid">
                ${PERSONAS.map((p, i) => `
                    <div class="persona-card fade-in stagger-${i + 1}" tabindex="0" role="button" aria-label="View ${p.name} plugins" data-persona="${p.id}">
                        <div class="persona-icon">${p.icon}</div>
                        <div class="persona-card-title">${p.name}</div>
                        <div class="persona-card-tagline">${p.tagline}</div>
                    </div>
                `).join('')}
            </div>
        `;
    }

    function renderTrendingRow(plugins) {
        return `
            <div class="trending-row">
                ${plugins.map((p, i) => `
                    <div class="trending-card fade-in stagger-${i + 1}" data-plugin-id="${p.id}">
                        <span class="trending-rank">#${i + 1}</span>
                        <div class="trending-card-name">${escapeHtml(p.name)}</div>
                        <div class="trending-card-provider">${escapeHtml(p.provider)}</div>
                        <div class="trending-card-stars">
                            <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                            ${formatStars(p.github_stars)}
                        </div>
                    </div>
                `).join('')}
            </div>
        `;
    }

    function renderFilterBar() {
        const categories = ['all', ...new Set(state.plugins.map(p => p.category).filter(Boolean))].sort();
        return `
            <div class="filter-bar">
                <label for="filter-category">Category</label>
                <select id="filter-category" class="filter-select" aria-label="Filter by category">
                    ${categories.map(c => `<option value="${c}" ${state.filterCategory === c ? 'selected' : ''}>${c === 'all' ? 'All Categories' : capitalize(c)}</option>`).join('')}
                </select>
                <label for="filter-sort">Sort by</label>
                <select id="filter-sort" class="filter-select" aria-label="Sort plugins">
                    <option value="stars" ${state.filterSort === 'stars' ? 'selected' : ''}>Most Stars</option>
                    <option value="name" ${state.filterSort === 'name' ? 'selected' : ''}>Name A-Z</option>
                    <option value="recent" ${state.filterSort === 'recent' ? 'selected' : ''}>Recently Updated</option>
                    <option value="quality" ${state.filterSort === 'quality' ? 'selected' : ''}>Quality Score</option>
                </select>
            </div>
        `;
    }

    function renderPluginsGrid(plugins) {
        const visible = plugins.slice(0, state.visibleCount);
        if (visible.length === 0) {
            return `
                <div class="empty-state">
                    <div class="empty-state-icon">&#x1F50D;</div>
                    <div class="empty-state-title">No plugins found</div>
                    <p>Try adjusting your filters or search query.</p>
                </div>
            `;
        }
        return `
            <div class="plugins-grid">
                ${visible.map(p => renderPluginCard(p)).join('')}
            </div>
        `;
    }

    function renderPluginCard(plugin) {
        const sourceBadge = getSourceBadge(plugin);
        const rating = getPluginRating(plugin.id);
        const compat = plugin.compatibility || {};
        return `
            <article class="plugin-card" data-plugin-id="${plugin.id}" tabindex="0" role="button" aria-label="View details for ${escapeHtml(plugin.name)}">
                <div class="plugin-card-header">
                    <div class="plugin-card-name">${escapeHtml(plugin.name)}</div>
                    <div style="display:flex;align-items:center;gap:6px;">
                        ${plugin.github_stars ? `
                            <div class="plugin-card-stars">
                                <svg viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                                ${formatStars(plugin.github_stars)}
                            </div>
                        ` : ''}
                        <button class="btn-add-stack ${state.selectedStack.has(plugin.id) ? 'in-stack' : ''}" data-stack-add="${plugin.id}" aria-label="Add to stack" title="${state.selectedStack.has(plugin.id) ? 'Remove from stack' : 'Add to stack'}">${state.selectedStack.has(plugin.id) ? '✓' : '+'}</button>
                    </div>
                </div>
                <div class="plugin-card-description">${escapeHtml(truncateDescription(plugin.description))}</div>
                <div class="plugin-card-meta">
                    <span class="source-badge ${sourceBadge.class}">${sourceBadge.label}</span>
                </div>
                <div class="plugin-card-compatibility">
                    ${PLATFORMS.map(pl => `
                        <span class="compat-icon ${compat[pl.id] ? 'active' : ''}" title="${pl.label}${compat[pl.id] ? ' (compatible)' : ''}">${pl.abbr}</span>
                    `).join('')}
                </div>
                <div class="plugin-card-tags">
                    ${(plugin.tags || []).slice(0, 3).map(t => `<span class="tag">${escapeHtml(t)}</span>`).join('')}
                </div>
                <div class="plugin-card-footer">
                    <span class="plugin-card-category">${escapeHtml(plugin.category || 'uncategorized')}</span>
                    ${rating ? `<span class="plugin-card-rating">${renderStars(rating.rating, 'sm')}<span class="rating-count">${rating.rating.toFixed(1)}</span></span>` : ''}
                    <button class="btn-view-details">View Details</button>
                </div>
            </article>
        `;
    }

    function renderLoadMore(totalCount) {
        if (state.visibleCount >= totalCount) return '';
        const remaining = totalCount - state.visibleCount;
        return `
            <div class="load-more-container">
                <button class="btn-load-more" id="btn-load-more">Show More (${remaining} remaining)</button>
            </div>
        `;
    }

    // ========== PERSONA VIEW ==========
    function renderPersonaView() {
        const persona = state.currentPersona;
        const recommended = getPersonaPlugins(persona);
        const allCategories = ['development', 'ml-ai', 'creative', 'integrations', 'documents', 'enterprise', 'data'];
        const coveredCategories = [...new Set(recommended.map(p => p.category))];
        const gaps = allCategories.filter(c => !coveredCategories.includes(c));

        return `
            <button class="back-button" id="btn-back" aria-label="Back to home">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
                Back to Directory
            </button>
            <div class="persona-view-header">
                <div class="persona-view-icon">${persona.icon}</div>
                <div class="persona-view-info">
                    <h2>${persona.name}</h2>
                    <p>${persona.tagline}</p>
                </div>
            </div>
            ${renderCoverageSection(recommended, allCategories, coveredCategories, gaps)}
            ${renderStackBuilder(recommended)}
            <div class="section-header">
                <h2 class="section-title">Recommended Plugins</h2>
                <span class="section-subtitle">${recommended.length} plugins for this role</span>
            </div>
            <div class="plugins-grid">
                ${recommended.slice(0, state.visibleCount).map(p => renderPluginCard(p)).join('')}
            </div>
            ${renderLoadMore(recommended.length)}
        `;
    }

    function renderCoverageSection(plugins, allCategories, covered, gaps) {
        return `
            <div class="coverage-section">
                <div class="coverage-title">Taxonomy Coverage</div>
                <div class="coverage-bar-container">
                    ${allCategories.map(cat => {
                        const pluginsInCat = plugins.filter(p => p.category === cat);
                        let status = 'gap';
                        if (pluginsInCat.length >= 2) status = 'covered';
                        else if (pluginsInCat.length === 1) status = 'partial';
                        // Check if selected stack changes things
                        if (state.selectedStack.size > 0) {
                            const selectedInCat = plugins.filter(p => state.selectedStack.has(p.id) && p.category === cat);
                            if (selectedInCat.length >= 2) status = 'covered';
                            else if (selectedInCat.length === 1) status = 'partial';
                            else status = 'gap';
                        }
                        return `<div class="coverage-segment ${status}" title="${capitalize(cat)}: ${status}"><span class="coverage-segment-label">${capitalize(cat)}</span></div>`;
                    }).join('')}
                </div>
                <div class="coverage-legend">
                    <span class="coverage-legend-item"><span class="coverage-legend-dot green"></span>Covered (2+ plugins)</span>
                    <span class="coverage-legend-item"><span class="coverage-legend-dot yellow"></span>Partial (1 plugin)</span>
                    <span class="coverage-legend-item"><span class="coverage-legend-dot red"></span>Gap (no plugins)</span>
                </div>
                ${gaps.length > 0 ? `
                    <div class="gap-callouts">
                        ${gaps.map(gap => {
                            const suggestion = getSuggestionForGap(gap);
                            return `
                                <div class="gap-callout">
                                    <svg class="gap-callout-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 8v4M12 16h.01"/></svg>
                                    <span>You're missing: <strong>${capitalize(gap)}</strong>. Consider: ${suggestion}</span>
                                </div>
                            `;
                        }).join('')}
                    </div>
                ` : ''}
            </div>
        `;
    }

    function renderStackBuilder(plugins) {
        const topPlugins = plugins.slice(0, 8);
        const selectedCount = state.selectedStack.size;
        return `
            <div class="stack-builder">
                <div class="stack-builder-header">
                    <div class="stack-builder-title">Build Your Stack</div>
                    <div class="stack-count">${selectedCount} selected</div>
                </div>
                ${topPlugins.map(p => `
                    <div class="stack-plugin-item ${state.selectedStack.has(p.id) ? 'checked' : ''}" data-stack-id="${p.id}">
                        <input type="checkbox" class="stack-checkbox" ${state.selectedStack.has(p.id) ? 'checked' : ''} aria-label="Add ${escapeHtml(p.name)} to stack">
                        <span class="stack-plugin-name">${escapeHtml(p.name)}</span>
                        <span class="stack-plugin-category">${escapeHtml(p.category || '')}</span>
                    </div>
                `).join('')}
            </div>
        `;
    }

    // ========== SEARCH VIEW ==========
    function renderSearchView() {
        const useCaseResults = getUseCaseSearchResults(state.searchQuery);
        const pluginResults = getSearchResults(state.searchQuery);
        const sortedPlugins = applySortToResults(pluginResults);

        return `
            <button class="back-button" id="btn-back" aria-label="Back to home">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
                Back to Directory
            </button>
            <div class="search-results-header">
                <h2 class="search-results-title">Results for "${escapeHtml(state.searchQuery)}"</h2>
                <p class="search-results-count">${pluginResults.length} plugin${pluginResults.length !== 1 ? 's' : ''}${useCaseResults.length > 0 ? ` &middot; ${useCaseResults.length} use case${useCaseResults.length !== 1 ? 's' : ''}` : ''} found</p>
            </div>
            ${useCaseResults.length > 0 ? `
                <div class="search-section">
                    <h3 class="search-section-title">Matching Use Cases</h3>
                    <div class="use-case-pills" style="padding:0 0 1rem;">
                        ${useCaseResults.slice(0, 6).map(uc => `
                            <button class="use-case-pill" data-usecase="${uc.id}">
                                <span class="use-case-pill-title">${escapeHtml(uc.title)}</span>
                                <span class="use-case-pill-persona">${PERSONAS.find(p => p.id === uc.persona)?.icon || ''} ${uc.persona.replace(/-/g, ' ')}</span>
                            </button>
                        `).join('')}
                    </div>
                </div>
            ` : ''}
            <div class="search-section">
                <div class="search-section-toolbar">
                    <h3 class="search-section-title">Plugins</h3>
                    <div class="search-sort">
                        <label for="search-sort-select">Sort:</label>
                        <select id="search-sort-select" class="filter-select">
                            <option value="relevance" ${state.searchSort === 'relevance' ? 'selected' : ''}>Relevance</option>
                            <option value="stars" ${state.searchSort === 'stars' ? 'selected' : ''}>Most Stars</option>
                            <option value="name" ${state.searchSort === 'name' ? 'selected' : ''}>Name A-Z</option>
                            <option value="quality" ${state.searchSort === 'quality' ? 'selected' : ''}>Quality Score</option>
                        </select>
                    </div>
                </div>
                ${renderPluginsGrid(sortedPlugins)}
                ${renderLoadMore(sortedPlugins.length)}
            </div>
        `;
    }

    function applySortToResults(results) {
        switch (state.searchSort) {
            case 'stars':
                return [...results].sort((a, b) => (b.github_stars || 0) - (a.github_stars || 0));
            case 'name':
                return [...results].sort((a, b) => a.name.localeCompare(b.name));
            case 'quality':
                return [...results].sort((a, b) => (b.quality_score || 0) - (a.quality_score || 0));
            default:
                return results; // relevance = original order from getSearchResults
        }
    }

    // ========== USE CASE VIEW ==========
    function renderUseCaseView() {
        const uc = (state.useCases || []).find(u => u.id === state.currentUseCase);
        if (!uc) {
            return `
                <button class="back-button" id="btn-back">← Back to Directory</button>
                <div class="empty-state"><p>Use case not found.</p></div>
            `;
        }
        const persona = PERSONAS.find(p => p.id === uc.persona);
        const recommended = getUseCasePlugins(uc);
        const related = (state.useCases || []).filter(u => u.persona === uc.persona && u.id !== uc.id).slice(0, 4);

        return `
            <button class="back-button" id="btn-back">← Back to Directory</button>
            <div class="persona-view-header">
                <div class="persona-view-icon">${persona ? persona.icon : '🎯'}</div>
                <div class="persona-view-info">
                    <h2>${escapeHtml(uc.title)}</h2>
                    <p>${escapeHtml(uc.description)}</p>
                    <div style="display:flex;gap:0.5rem;flex-wrap:wrap;margin-top:0.5rem;align-items:center;">
                        ${persona ? `<span class="tag">${persona.icon} ${escapeHtml(persona.name)}</span>` : ''}
                        <span class="source-badge" style="text-transform:capitalize;">${escapeHtml(uc.complexity || 'intermediate')}</span>
                    </div>
                </div>
            </div>

            ${uc.pain_today ? `
                <div class="gap-callout" style="margin:1.5rem 0;">
                    <strong>Pain today:</strong> ${escapeHtml(uc.pain_today)}
                </div>
            ` : ''}

            ${uc.plugins_needed && uc.plugins_needed.length > 0 ? `
                <div class="coverage-section">
                    <div class="coverage-title">What you'll need</div>
                    <div style="display:flex;flex-direction:column;gap:0.5rem;margin-top:0.75rem;">
                        ${uc.plugins_needed.map((plugin, i) => `
                            <div style="display:flex;align-items:center;gap:0.75rem;padding:0.6rem 0.75rem;background:var(--bg-card,#f9fafb);border-radius:8px;border:1px solid var(--border,#e5e7eb);">
                                <span style="width:1.5rem;height:1.5rem;border-radius:50%;background:var(--primary,#6B21A8);color:#fff;display:flex;align-items:center;justify-content:center;font-size:0.75rem;font-weight:700;">${i + 1}</span>
                                <span style="font-weight:500;text-transform:capitalize;">${escapeHtml(plugin.replace(/-/g, ' '))}</span>
                            </div>
                        `).join('')}
                    </div>
                </div>
            ` : ''}

            ${uc.success_criteria ? `
                <div class="coverage-section" style="margin-top:1rem;">
                    <div class="coverage-title">✓ Success looks like</div>
                    <p style="margin-top:0.5rem;color:var(--text-muted,#6b7280);line-height:1.6;">${escapeHtml(uc.success_criteria)}</p>
                </div>
            ` : ''}

            ${recommended.length > 0 ? `
                <div class="section-header" style="margin-top:2rem;">
                    <h2 class="section-title">Recommended Plugins</h2>
                    <span class="section-subtitle">${recommended.length} plugins for this use case</span>
                </div>
                <div class="plugins-grid">
                    ${recommended.map(p => renderPluginCard(p)).join('')}
                </div>
            ` : ''}

            ${related.length > 0 ? `
                <div class="section-header" style="margin-top:2rem;">
                    <h2 class="section-title">Related Use Cases</h2>
                    <span class="section-subtitle">More for ${persona ? persona.name : uc.persona}</span>
                </div>
                <div class="use-case-pills">
                    ${related.map(r => `
                        <button class="use-case-pill" data-usecase="${r.id}">
                            <span class="use-case-pill-title">${escapeHtml(r.title)}</span>
                            <span class="use-case-pill-persona">${PERSONAS.find(p => p.id === r.persona)?.icon || ''} ${r.persona.replace(/-/g, ' ')}</span>
                        </button>
                    `).join('')}
                </div>
            ` : ''}
        `;
    }

    function getUseCasePlugins(uc) {
        const terms = [
            ...(uc.taxonomy_categories || []),
            ...(uc.search_queries || []).join(' ').split(/\s+/),
            ...(uc.plugins_needed || [])
        ].map(t => t.toLowerCase().replace(/-/g, ' '));

        return state.plugins.filter(p => {
            const searchable = [p.name, p.description, p.category, ...(p.tags || [])].join(' ').toLowerCase();
            return terms.some(term => searchable.includes(term));
        }).sort((a, b) => (b.github_stars || 0) - (a.github_stars || 0)).slice(0, 12);
    }

    // ========== MODAL ==========
    function openModal(plugin) {
        const modal = document.getElementById('plugin-modal');
        const title = document.getElementById('modal-title');
        const body = document.getElementById('modal-body');

        title.textContent = plugin.name;
        body.innerHTML = renderModalContent(plugin);

        modal.hidden = false;
        requestAnimationFrame(() => modal.classList.add('active'));

        // Update hash without triggering re-render
        const pluginHash = 'plugin/' + plugin.id.replace(/\//g, '-');
        history.replaceState(null, '', '#' + pluginHash);

        // Focus trap
        const closeBtn = modal.querySelector('.modal-close');
        closeBtn.focus();
    }

    function closeModal() {
        const modal = document.getElementById('plugin-modal');
        modal.classList.remove('active');
        setTimeout(() => { modal.hidden = true; }, 200);

        // Restore hash
        if (state.currentView === 'persona' && state.currentPersona) {
            history.replaceState(null, '', '#persona/' + state.currentPersona.id);
        } else if (state.currentView === 'search') {
            history.replaceState(null, '', '#search/' + encodeURIComponent(state.searchQuery));
        } else {
            history.replaceState(null, '', window.location.pathname);
        }
    }

    function renderModalContent(plugin) {
        const compat = plugin.compatibility || {};
        const sourceBadge = getSourceBadge(plugin);
        const pairs = getPairsWellWith(plugin);

        return `
            <div class="plugin-card-meta" style="margin-bottom: 1rem;">
                <span class="source-badge ${sourceBadge.class}">${sourceBadge.label}</span>
                ${plugin.github_stars ? `
                    <span class="plugin-card-stars" style="margin-left: auto;">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                        ${formatStars(plugin.github_stars)} stars
                    </span>
                ` : ''}
            </div>
            <div class="modal-description">${escapeHtml(plugin.description || 'No description available.')}</div>

            <div class="modal-section">
                <div class="modal-section-title">Compatibility</div>
                <div class="modal-compat-grid">
                    ${PLATFORMS.map(pl => `
                        <div class="modal-compat-item ${compat[pl.id] ? 'active' : 'inactive'}">
                            <span>${pl.abbr}</span>
                            <span>${pl.label}</span>
                        </div>
                    `).join('')}
                </div>
            </div>

            <div class="modal-section">
                <div class="modal-section-title">Category Coverage</div>
                <div class="modal-tags">
                    <span class="tag">${escapeHtml(plugin.category || 'uncategorized')}</span>
                    ${(plugin.tags || []).map(t => `<span class="tag">${escapeHtml(t)}</span>`).join('')}
                </div>
            </div>

            ${pairs.length > 0 ? `
                <div class="modal-section">
                    <div class="modal-section-title">Pairs Well With</div>
                    <div class="modal-pairs-grid">
                        ${pairs.map(p => `<div class="modal-pair-item" data-plugin-id="${p.id}">${escapeHtml(p.name)}</div>`).join('')}
                    </div>
                </div>
            ` : ''}

            <div class="modal-section">
                <div class="modal-section-title">Install</div>
                <div class="modal-install">
                    <code>claude plugin add ${plugin.id}</code>
                    <button class="btn-copy" data-copy="claude plugin add ${plugin.id}">Copy</button>
                </div>
            </div>

            ${plugin.source && plugin.source.repo ? `
                <div class="modal-section">
                    <div class="modal-section-title">Source</div>
                    <p style="font-size: 0.85rem; color: var(--text-secondary);">
                        <a href="${escapeHtml(plugin.source.repo)}" target="_blank" rel="noopener" style="color: var(--primary-light); text-decoration: none;">${escapeHtml(plugin.source.repo)}</a>
                    </p>
                </div>
            ` : ''}

            <div class="modal-section">
                <div class="modal-section-title">Reviews</div>
                ${renderReviewCards(plugin.id)}
            </div>
        `;
    }

    // ========== EVENT LISTENERS ==========
    function attachEventListeners() {
        // Use case pills
        document.querySelectorAll('.use-case-pill').forEach(pill => {
            pill.addEventListener('click', () => {
                window.location.hash = 'usecase/' + pill.dataset.usecase;
            });
        });

        // Persona cards
        document.querySelectorAll('.persona-card').forEach(card => {
            card.addEventListener('click', () => {
                const id = card.dataset.persona;
                window.location.hash = 'persona/' + id;
            });
            card.addEventListener('keydown', (e) => {
                if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    card.click();
                }
            });
        });

        // Plugin cards
        document.querySelectorAll('.plugin-card').forEach(card => {
            card.addEventListener('click', () => {
                const id = card.dataset.pluginId;
                const plugin = state.plugins.find(p => p.id === id);
                if (plugin) openModal(plugin);
            });
            card.addEventListener('keydown', (e) => {
                if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    card.click();
                }
            });
        });

        // Trending cards
        document.querySelectorAll('.trending-card').forEach(card => {
            card.addEventListener('click', () => {
                const id = card.dataset.pluginId;
                const plugin = state.plugins.find(p => p.id === id);
                if (plugin) openModal(plugin);
            });
        });

        // Back button
        const backBtn = document.getElementById('btn-back');
        if (backBtn) {
            backBtn.addEventListener('click', () => {
                window.location.hash = '';
            });
        }

        // Load more
        const loadMoreBtn = document.getElementById('btn-load-more');
        if (loadMoreBtn) {
            loadMoreBtn.addEventListener('click', () => {
                state.visibleCount += PAGE_SIZE;
                render();
            });
        }

        // Filters
        const catFilter = document.getElementById('filter-category');
        if (catFilter) {
            catFilter.addEventListener('change', (e) => {
                state.filterCategory = e.target.value;
                state.visibleCount = PAGE_SIZE;
                render();
            });
        }

        const sortFilter = document.getElementById('filter-sort');
        if (sortFilter) {
            sortFilter.addEventListener('change', (e) => {
                state.filterSort = e.target.value;
                state.visibleCount = PAGE_SIZE;
                render();
            });
        }

        const searchSortEl = document.getElementById('search-sort-select');
        if (searchSortEl) {
            searchSortEl.addEventListener('change', (e) => {
                state.searchSort = e.target.value;
                state.visibleCount = PAGE_SIZE;
                render();
            });
        }

        // Stack checkboxes
        document.querySelectorAll('.stack-plugin-item').forEach(item => {
            item.addEventListener('click', (e) => {
                if (e.target.type === 'checkbox') return; // handled below
                const id = item.dataset.stackId;
                toggleStack(id);
            });
            const checkbox = item.querySelector('.stack-checkbox');
            if (checkbox) {
                checkbox.addEventListener('change', () => {
                    const id = item.dataset.stackId;
                    toggleStack(id);
                });
            }
        });

        // Add-to-stack buttons (delegated)
        document.querySelectorAll('.btn-add-stack').forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.stopPropagation();
                toggleStack(btn.dataset.stackAdd);
            });
        });
    }

    function toggleStack(id) {
        if (state.selectedStack.has(id)) {
            state.selectedStack.delete(id);
        } else {
            state.selectedStack.add(id);
        }
        persistStack();
        if (state.currentView === 'persona') {
            render();
        } else {
            updateStackDrawer();
            updateAddButtons();
        }
    }

    function persistStack() {
        localStorage.setItem('plugstack_stack', JSON.stringify([...state.selectedStack]));
        updateStackBadge();
    }

    function updateStackBadge() {
        const btn = document.getElementById('nav-stack-btn');
        const badge = document.getElementById('stack-badge-count');
        if (!btn || !badge) return;
        const count = state.selectedStack.size;
        badge.textContent = count;
        btn.hidden = count === 0;
    }

    function updateAddButtons() {
        document.querySelectorAll('.btn-add-stack').forEach(btn => {
            const id = btn.dataset.stackAdd;
            const inStack = state.selectedStack.has(id);
            btn.classList.toggle('in-stack', inStack);
            btn.textContent = inStack ? '✓' : '+';
            btn.title = inStack ? 'In your stack' : 'Add to stack';
        });
    }

    function openStackDrawer() {
        const drawer = document.getElementById('stack-drawer');
        if (!drawer) return;
        updateStackDrawer();
        drawer.hidden = false;
        requestAnimationFrame(() => drawer.classList.add('open'));
    }

    function closeStackDrawer() {
        const drawer = document.getElementById('stack-drawer');
        if (!drawer) return;
        drawer.classList.remove('open');
        setTimeout(() => { drawer.hidden = true; }, 300);
    }

    function updateStackDrawer() {
        const body = document.getElementById('stack-drawer-body');
        if (!body) return;
        const plugins = state.plugins.filter(p => state.selectedStack.has(p.id));
        if (plugins.length === 0) {
            body.innerHTML = '<div class="stack-drawer-empty">Add plugins with the + button on any card.</div>';
            return;
        }
        body.innerHTML = plugins.map(p => `
            <div class="stack-drawer-item">
                <div class="stack-drawer-item-info">
                    <span class="stack-drawer-item-name">${escapeHtml(p.name)}</span>
                    <span class="stack-drawer-item-provider">${escapeHtml(p.provider)}</span>
                </div>
                <button class="stack-drawer-remove" data-remove-id="${p.id}" aria-label="Remove ${escapeHtml(p.name)}">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6L6 18M6 6l12 12"/></svg>
                </button>
            </div>
        `).join('');
    }

    function exportStack() {
        const plugins = state.plugins.filter(p => state.selectedStack.has(p.id));
        if (plugins.length === 0) return;
        const md = `# My PlugStack\n\n${plugins.map(p => `- **${p.name}** (${p.provider}) — ${p.category}`).join('\n')}\n\nBuilt with [PlugStack](https://dmgrok.github.io/agent-plugins/)`;
        navigator.clipboard.writeText(md).then(() => {
            const btn = document.getElementById('btn-export-stack');
            if (!btn) return;
            btn.textContent = 'Copied!';
            setTimeout(() => { btn.textContent = 'Export'; }, 2000);
        });
    }

    // ========== SEARCH ==========
    function initSearch() {
        const input = document.getElementById('search-input');
        const autocomplete = document.getElementById('search-autocomplete');
        if (!input || !autocomplete) return;
        let focusedIndex = -1;

        input.addEventListener('input', () => {
            const query = input.value.trim();
            if (query.length < 2) {
                autocomplete.classList.remove('active');
                autocomplete.innerHTML = '';
                return;
            }
            const useCaseResults = getUseCaseSearchResults(query).slice(0, 3);
            const pluginResults = getSearchResults(query).slice(0, 5);
            if (useCaseResults.length === 0 && pluginResults.length === 0) {
                autocomplete.classList.remove('active');
                return;
            }
            focusedIndex = -1;
            const parts = [];
            let idx = 0;
            if (useCaseResults.length > 0) {
                parts.push(`<div class="autocomplete-section-label">Use Cases</div>`);
                useCaseResults.forEach(uc => {
                    parts.push(`
                        <div class="autocomplete-item autocomplete-item--usecase" data-index="${idx++}" data-usecase-id="${uc.id}" role="option">
                            <span class="autocomplete-item-icon">🎯</span>
                            <div>
                                <div class="autocomplete-item-name">${escapeHtml(uc.title)}</div>
                                <div class="autocomplete-item-meta">Use case · ${escapeHtml(uc.persona.replace(/-/g, ' '))}</div>
                            </div>
                        </div>
                    `);
                });
            }
            if (pluginResults.length > 0) {
                if (useCaseResults.length > 0) parts.push(`<div class="autocomplete-section-label">Plugins</div>`);
                pluginResults.forEach(p => {
                    parts.push(`
                        <div class="autocomplete-item" data-index="${idx++}" data-plugin-id="${p.id}" role="option">
                            <div>
                                <div class="autocomplete-item-name">${escapeHtml(p.name)}</div>
                                <div class="autocomplete-item-meta">${escapeHtml(p.provider)} · ${escapeHtml(p.category || '')}</div>
                            </div>
                        </div>
                    `);
                });
            }
            autocomplete.innerHTML = parts.join('');
            autocomplete.classList.add('active');

            autocomplete.querySelectorAll('.autocomplete-item').forEach(item => {
                item.addEventListener('click', () => {
                    const usecaseId = item.dataset.usecaseId;
                    const pluginId = item.dataset.pluginId;
                    autocomplete.classList.remove('active');
                    input.value = '';
                    if (usecaseId) {
                        window.location.hash = 'usecase/' + usecaseId;
                    } else if (pluginId) {
                        const plugin = state.plugins.find(p => p.id === pluginId);
                        if (plugin) openModal(plugin);
                    }
                });
            });
        });

        input.addEventListener('keydown', (e) => {
            const items = autocomplete.querySelectorAll('.autocomplete-item');
            if (!autocomplete.classList.contains('active') || items.length === 0) {
                if (e.key === 'Enter' && input.value.trim()) {
                    e.preventDefault();
                    window.location.hash = 'search/' + encodeURIComponent(input.value.trim());
                    autocomplete.classList.remove('active');
                }
                return;
            }

            if (e.key === 'ArrowDown') {
                e.preventDefault();
                focusedIndex = Math.min(focusedIndex + 1, items.length - 1);
                updateFocused(items, focusedIndex);
            } else if (e.key === 'ArrowUp') {
                e.preventDefault();
                focusedIndex = Math.max(focusedIndex - 1, -1);
                updateFocused(items, focusedIndex);
            } else if (e.key === 'Enter') {
                e.preventDefault();
                if (focusedIndex >= 0 && items[focusedIndex]) {
                    items[focusedIndex].click();
                } else {
                    window.location.hash = 'search/' + encodeURIComponent(input.value.trim());
                    autocomplete.classList.remove('active');
                }
            } else if (e.key === 'Escape') {
                autocomplete.classList.remove('active');
            }
        });

        input.addEventListener('blur', () => {
            setTimeout(() => autocomplete.classList.remove('active'), 200);
        });
    }

    function updateFocused(items, index) {
        items.forEach((item, i) => {
            item.classList.toggle('focused', i === index);
        });
    }

    // ========== MODAL EVENTS ==========
    function initModal() {
        const modal = document.getElementById('plugin-modal');
        const closeBtn = modal.querySelector('.modal-close');

        closeBtn.addEventListener('click', closeModal);
        modal.addEventListener('click', (e) => {
            if (e.target === modal) closeModal();
        });

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && modal.classList.contains('active')) {
                closeModal();
            }
        });

        // Delegated events within modal body
        modal.addEventListener('click', (e) => {
            // Copy button
            const copyBtn = e.target.closest('.btn-copy');
            if (copyBtn) {
                const text = copyBtn.dataset.copy;
                navigator.clipboard.writeText(text).then(() => {
                    copyBtn.textContent = 'Copied!';
                    setTimeout(() => { copyBtn.textContent = 'Copy'; }, 2000);
                });
                return;
            }

            // Pair item
            const pairItem = e.target.closest('.modal-pair-item');
            if (pairItem) {
                const id = pairItem.dataset.pluginId;
                const plugin = state.plugins.find(p => p.id === id);
                if (plugin) {
                    closeModal();
                    setTimeout(() => openModal(plugin), 250);
                }
            }
        });
    }

    // ========== HELPERS ==========
    function getTrendingPlugins() {
        return [...state.plugins]
            .filter(p => p.github_stars)
            .sort((a, b) => (b.github_stars || 0) - (a.github_stars || 0))
            .slice(0, 5);
    }

    function getFilteredPlugins() {
        let filtered = [...state.plugins];

        if (state.filterCategory !== 'all') {
            filtered = filtered.filter(p => p.category === state.filterCategory);
        }

        filtered = sortPlugins(filtered, state.filterSort);
        return filtered;
    }

    function sortPlugins(plugins, sortBy) {
        switch (sortBy) {
            case 'stars':
                return plugins.sort((a, b) => (b.github_stars || 0) - (a.github_stars || 0));
            case 'name':
                return plugins.sort((a, b) => a.name.localeCompare(b.name));
            case 'recent':
                return plugins.sort((a, b) => {
                    const da = a.last_updated_at || '';
                    const db = b.last_updated_at || '';
                    return db.localeCompare(da);
                });
            case 'quality':
                return plugins.sort((a, b) => (b.quality_score || 0) - (a.quality_score || 0));
            default:
                return plugins;
        }
    }

    function getPersonaPlugins(persona) {
        let results = state.plugins.filter(p => {
            // Match by category
            if (persona.categories.includes(p.category)) return true;
            // Match by tags
            if (p.tags && p.tags.some(t => persona.tags.includes(t))) return true;
            return false;
        });

        // Sort by quality and stars
        results.sort((a, b) => {
            const scoreA = (a.quality_score || 0) + Math.min((a.github_stars || 0) / 100, 50);
            const scoreB = (b.quality_score || 0) + Math.min((b.github_stars || 0) / 100, 50);
            return scoreB - scoreA;
        });

        return results;
    }

    function getSearchResults(query) {
        const q = query.toLowerCase();
        const terms = q.split(/\s+/);

        return state.plugins.filter(p => {
            const searchable = [
                p.name,
                p.description,
                p.provider,
                p.category,
                ...(p.tags || [])
            ].join(' ').toLowerCase();

            return terms.every(term => searchable.includes(term));
        }).sort((a, b) => {
            // Exact name match first
            const aName = a.name.toLowerCase().includes(q) ? 1 : 0;
            const bName = b.name.toLowerCase().includes(q) ? 1 : 0;
            if (aName !== bName) return bName - aName;
            return (b.github_stars || 0) - (a.github_stars || 0);
        });
    }

    function getUseCaseSearchResults(query) {
        if (!state.useCases || state.useCases.length === 0) return [];
        const q = query.toLowerCase();
        const terms = q.split(/\s+/);
        return state.useCases.filter(uc => {
            const searchable = [uc.title, uc.description, ...(uc.search_queries || [])].join(' ').toLowerCase();
            return terms.every(term => searchable.includes(term));
        });
    }

    function getSourceBadge(plugin) {
        if (OFFICIAL_PROVIDERS.includes(plugin.provider)) {
            return { label: 'Official', class: 'official' };
        }
        if (plugin.provider === 'skillcreatorai' || plugin.provider === 'community') {
            return { label: 'Community', class: 'community' };
        }
        return { label: 'Third-party', class: 'third-party' };
    }

    function getPairsWellWith(plugin) {
        // Find plugins in the same category or with overlapping tags
        const sameCat = state.plugins.filter(p =>
            p.id !== plugin.id &&
            p.category === plugin.category &&
            p.provider !== plugin.provider
        );

        // Also look in bundles
        const bundlePartners = [];
        state.bundles.forEach(bundle => {
            if (bundle.skills.includes(plugin.id)) {
                bundle.skills.forEach(sid => {
                    if (sid !== plugin.id) {
                        const found = state.plugins.find(p => p.id === sid);
                        if (found) bundlePartners.push(found);
                    }
                });
            }
        });

        // Combine and deduplicate
        const combined = [...bundlePartners, ...sameCat];
        const seen = new Set();
        const unique = [];
        for (const p of combined) {
            if (!seen.has(p.id)) {
                seen.add(p.id);
                unique.push(p);
            }
        }
        return unique.slice(0, 4);
    }

    function getSuggestionForGap(category) {
        const suggestions = {
            'ml-ai': 'huggingface/hf-cli or skillcreatorai/llm-application-dev',
            'creative': 'anthropics/canvas-design or anthropics/algorithmic-art',
            'integrations': 'anthropics/mcp-builder or github/gh-cli',
            'documents': 'anthropics/pdf or anthropics/docx',
            'enterprise': 'openai/notion-knowledge-capture',
            'development': 'skillcreatorai/backend-development',
            'data': 'huggingface/hugging-face-datasets'
        };
        return suggestions[category] || 'browse the directory for options';
    }

    function formatStars(stars) {
        if (!stars) return '0';
        if (stars >= 1000) return (stars / 1000).toFixed(1) + 'k';
        return stars.toString();
    }

    function truncateDescription(desc) {
        if (!desc) return 'No description available.';
        if (desc.length <= 120) return desc;
        return desc.substring(0, 117) + '...';
    }

    function capitalize(str) {
        if (!str) return '';
        return str.charAt(0).toUpperCase() + str.slice(1).replace(/-/g, ' ');
    }

    function escapeHtml(str) {
        if (!str) return '';
        const div = document.createElement('div');
        div.textContent = str;
        return div.innerHTML;
    }

    function getPluginRating(pluginId) {
        const r = state.reviews[pluginId];
        return r && r.aggregate ? r.aggregate : null;
    }

    function renderStars(rating, size) {
        const full = Math.floor(rating);
        const half = (rating - full) >= 0.5 ? 1 : 0;
        const empty = 5 - full - half;
        const s = size === 'lg' ? 16 : 12;
        const starFull = `<svg class="star-icon${size === 'lg' ? ' lg' : ''}" width="${s}" height="${s}" viewBox="0 0 24 24"><path class="star-filled" d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>`;
        const starHalf = `<svg class="star-icon${size === 'lg' ? ' lg' : ''}" width="${s}" height="${s}" viewBox="0 0 24 24"><defs><linearGradient id="half-g"><stop offset="50%" stop-color="var(--warning)"/><stop offset="50%" stop-color="transparent"/></linearGradient></defs><path fill="url(#half-g)" stroke="var(--warning)" stroke-width="1" d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>`;
        const starEmpty = `<svg class="star-icon${size === 'lg' ? ' lg' : ''}" width="${s}" height="${s}" viewBox="0 0 24 24"><path class="star-empty" d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>`;
        return `<span class="stars-row">${starFull.repeat(full)}${half ? starHalf : ''}${starEmpty.repeat(empty)}</span>`;
    }

    function renderReviewCards(pluginId) {
        const data = state.reviews[pluginId];
        if (!data || !data.items || data.items.length === 0) {
            return '<div class="modal-review-placeholder">Be the first to review this plugin.</div>';
        }
        return `
            <div class="review-aggregate">
                ${renderStars(data.aggregate.rating, 'lg')}
                <span class="review-aggregate-text">${data.aggregate.rating.toFixed(1)} out of 5 &middot; ${data.aggregate.count} reviews</span>
            </div>
            <div class="review-list">
                ${data.items.map(r => `
                    <div class="review-card">
                        <div class="review-card-header">
                            <span class="review-author">${escapeHtml(r.author)}</span>
                            ${r.verified ? '<span class="review-verified">Verified</span>' : ''}
                            <span class="review-date">${r.date}</span>
                        </div>
                        <div class="review-rating">${renderStars(r.rating, 'sm')}</div>
                        <p class="review-text">${escapeHtml(r.text)}</p>
                    </div>
                `).join('')}
            </div>
        `;
    }

    // ========== INIT ==========
    function init() {
        initTheme();
        initSearch();
        initModal();

        // Stack drawer
        document.getElementById('nav-stack-btn').addEventListener('click', openStackDrawer);
        document.getElementById('stack-drawer-close').addEventListener('click', closeStackDrawer);
        document.getElementById('btn-export-stack').addEventListener('click', exportStack);
        document.getElementById('stack-drawer-body').addEventListener('click', (e) => {
            const removeBtn = e.target.closest('.stack-drawer-remove');
            if (removeBtn) toggleStack(removeBtn.dataset.removeId);
        });
        updateStackBadge();

        loadData();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
