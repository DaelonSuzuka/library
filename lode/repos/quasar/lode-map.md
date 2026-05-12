# Quasar — Lode Map

```
lode/repos/quasar/
├── summary.md       # overview, architecture, package table, deployment modes
└── lode-map.md      # this file
```

## UI Components (79 directories, 100+ Q-components)

Each component directory at `ui/src/components/<name>/` contains `Q*.js` source, `index.js` registration, and `.sass` styles.

### Buttons & Actions

| Component | Directory | Key Files |
|-----------|-----------|------------|
| QBtn | `btn/` | QBtn.js, use-btn.js |
| QBtnDropdown | `btn-dropdown/` | QBtnDropdown.js |
| QBtnGroup | `btn-group/` | QBtnGroup.js |
| QBtnToggle | `btn-toggle/` | QBtnToggle.js |
| QFab, QFabAction | `fab/` | QFab.js, QFabAction.js, use-fab.js |

### Input & Selection

| Component | Directory | Key Files |
|-----------|-----------|------------|
| QInput | `input/` | QInput.js, use-mask.js |
| QFile | `file/` | QFile.js |
| QSelect | `select/` | QSelect.js |
| QCheckbox | `checkbox/` | QCheckbox.js, use-checkbox.js |
| QRadio | `radio/` | QRadio.js |
| QToggle | `toggle/` | QToggle.js |
| QOptionGroup | `option-group/` | QOptionGroup.js |
| QSlider | `slider/` | QSlider.js, use-slider.js |
| QRange | `range/` | QRange.js |
| QKnob | `knob/` | QKnob.js |
| QRating | `rating/` | QRating.js |
| QColor | `color/` | QColor.js |
| QDate | `date/` | QDate.js, use-datetime.js |
| QTime | `time/` | QTime.js, use-datetime.js |

### Layout & Structure

| Component | Directory |
|-----------|-----------|
| QLayout | `layout/` |
| QHeader | `header/` |
| QFooter | `footer/` |
| QDrawer | `drawer/` |
| QPage, QPageContainer | `page/` |
| QPageScroller | `page-scroller/` |
| QPageSticky | `page-sticky/` (+ use-page-sticky.js) |
| QCard, QCardSection, QCardActions | `card/` |
| QSeparator | `separator/` |
| QSpace | `space/` |
| QSplitter | `splitter/` |
| QScrollArea | `scroll-area/` (+ ScrollAreaControls.js) |
| QToolbar, QToolbarTitle | `toolbar/` |
| QBar | `bar/` |
| QBanner | `banner/` |

### Navigation

| Component | Directory |
|-----------|-----------|
| QTabs, QTab, QRouteTab | `tabs/` (+ use-tab.js) |
| QTabPanels, QTabPanel | `tab-panels/` |
| QBreadcrumbs, QBreadcrumbsEl | `breadcrumbs/` |
| QStepper, QStep, QStepperNavigation | `stepper/` (+ StepHeader.js) |
| QPagination | `pagination/` |
| QMenu | `menu/` |
| QDialog | `dialog/` |
| QPopupProxy | `popup-proxy/` |
| QPopupEdit | `popup-edit/` |

### Data Display

| Component | Directory | Key Files |
|-----------|-----------|------------|
| QTable, QTr, QTd, QTh | `table/` | + table-column-selection.js, table-filter.js, table-pagination.js, table-row-expand.js, table-row-selection.js, table-sort.js |
| QTree | `tree/` |
| QMarkupTable | `markup-table/` |
| QChatMessage | `chat/` |
| QTimeline, QTimelineEntry | `timeline/` |
| QCarousel, QCarouselSlide, QCarouselControl | `carousel/` |
| QBadge | `badge/` |
| QChip | `chip/` |
| QAvatar | `avatar/` |
| QImg | `img/` |
| QVideo | `video/` |
| QParallax | `parallax/` |
| QIntersection | `intersection/` |

### Progress & Loading

| Component | Directory |
|-----------|-----------|
| QLinearProgress | `linear-progress/` |
| QCircularProgress | `circular-progress/` |
| QSpinner (28 variants) | `spinner/` (+ use-spinner.js) |
| QInnerLoading | `inner-loading/` |
| QAjaxBar | `ajax-bar/` |
| QSkeleton | `skeleton/` |

### Feedback & Overlay

| Component | Directory |
|-----------|-----------|
| QTooltip | `tooltip/` |
| QDialog | `dialog/` |
| QExpansionItem | `expansion-item/` |
| QPullToRefresh | `pull-to-refresh/` |
| QInfiniteScroll | `infinite-scroll/` |
| QSlideItem | `slide-item/` |
| QNoSsr | `no-ssr/` |
| QResponsive | `responsive/` |

### Form Elements

| Component | Directory |
|-----------|-----------|
| QField | `field/` |
| QForm, QFormChildMixin | `form/` |

### Lists & Items

| Component | Directory |
|-----------|-----------|
| QList, QItem, QItemSection, QItemLabel | `item/` |

### Observers

| Component | Directory |
|-----------|-----------|
| QResizeObserver | `resize-observer/` |
| QScrollObserver | `scroll-observer/` |

### Virtual Scroll

| Component | Directory | Key Files |
|-----------|-----------|------------|
| QVirtualScroll | `virtual-scroll/` | + use-virtual-scroll.js |

### Transition

| Component | Directory |
|-----------|-----------|
| QSlideTransition | `slide-transition/` |

### Upload

| Component | Directory | Key Files |
|-----------|-----------|------------|
| QUploader, QUploaderAddTrigger | `uploader/` | + uploader-core.js, xhr-uploader-plugin.js |

## Composables (Public)

| Composable | Purpose |
|------------|---------|
| `useQuasar` | Access Quasar instance (plugins, dark mode, etc.) |
| `useForm` | Form validation |
| `useMeta` | SSR meta tags |
| `useDialogPluginComponent` | Create custom dialog plugins |
| `useHydration` | SSR hydration state |
| `useId` | Unique ID generation |
| `useInterval` | setInterval wrapper with auto-cleanup |
| `useTimeout` | setTimeout wrapper with auto-cleanup |
| `useTick` | nextTick wrapper |
| `useRenderCache` | SSR render caching |
| `useSplitAttrs` | Split attrs between root/fallback |

## Directives

| Directive | Purpose |
|-----------|---------|
| `v-close-popup` | Close parent popup/dialog/menu |
| `v-intersection` | Intersection Observer |
| `v-morph` | Morphing animations |
| `v-mutation` | Mutation Observer |
| `v-ripple` | Material ripple effect |
| `v-scroll-fire` | Trigger on scroll into view |
| `v-scroll` | Scroll event handler |
| `v-touch-hold` | Touch and hold |
| `v-touch-pan` | Touch pan gesture |
| `v-touch-repeat` | Touch repeat |
| `v-touch-swipe` | Touch swipe gesture |

## Plugins

| Plugin | Purpose |
|--------|---------|
| Addressbar Color | Set browser address bar color (mobile) |
| App Fullscreen | Toggle fullscreen mode |
| App Visibility | Detect app visibility state |
| Bottom Sheet | Bottom Sheet action list |
| Cookies | Cookie read/write API |
| Dark | Dark mode toggle |
| Dialog | Programmatic dialog API |
| Icon Set | Icon set management |
| Lang | i18n language management (50+ packs) |
| Loading | Loading overlay |
| Loading Bar | Top-of-page loading bar |
| Meta | SSR meta tag management |
| Notify | Toast notification API |
| Platform | Platform/device detection |
| Screen | Responsive screen breakpoints |
| Storage | Web storage (localStorage/sessionStorage) |

## CSS

`ui/src/css/`: core CSS, helpers, flex addon, normalize, SASS variables.

## Utils (`ui/src/utils/`)

Public: `clone`, `colors`, `copy-to-clipboard`, `create-meta-mixin`, `create-uploader-component`, `css-var`, `date`, `debounce`, `dom`, `event`, `EventBus`, `export-file`, `extend`, `format`, `frame-debounce`, `is`, `morph`, `open-url`, `patterns`, `run-sequential-promises`, `scroll`, `throttle`, `uid`

## App-Vite (`app-vite/`)

Project scaffolding and build system:
- CLI commands: dev, build, clean, describe, ext, help, info, inspect, mode, new, prepare, run
- Mode support: SPA, PWA, SSR, Electron, Capacitor, Cordova, BEX
- Config: `quasar.config.js` (or `.ts`)
- Templates: `templates/` for project scaffolding

## Docs (`docs/`)

Quasar documentation site built with Quasar itself:
- `src/pages/vue-components/` — 72 component doc pages
- `src/pages/vue-directives/` — 11 directive doc pages
- `src/pages/vue-composables/` — 11 composable doc pages
- `src/pages/quasar-plugins/` — 12 plugin doc pages
- `src/pages/options/` — 13 option pages (animations, i18n, icon-sets, rtl, screen, etc.)
- `src/pages/style/` — 12 style pages (typography, breakpoints, spacing, etc.)
- `src/examples/` — 98 live code example directories
- Language packs: `ui/lang/` (50+ locales)
- Icon sets: `ui/icon-set/`