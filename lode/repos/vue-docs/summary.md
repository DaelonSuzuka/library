# Vue 3 Documentation

**What:** Official Vue.js 3 documentation — guide, API reference, examples, tutorial, style guide.
**Repo:** `repos/vue-docs` | https://github.com/vuejs/docs
**Format:** VitePress Markdown site
**License:** MIT

## Architecture

Vue 3 docs are organized into a VitePress site with interactive examples (REPL) and a step-by-step tutorial. Content is Markdown + Vue components + VitePress config.

## Content Overview

| Section | Files | Description |
|---------|-------|-------------|
| Guide: Essentials | 12 | Reactivity, computed, template syntax, conditional, list, event handling, forms, lifecycle, refs, watchers, components basics |
| Guide: Components | 8 | Props, events, v-model, slots, provide/inject, async, registration, attrs |
| Guide: Reusability | 3 | Composables, custom directives, plugins |
| Guide: Built-ins | 5 | Keep-alive, suspense, teleport, transition, transition-group |
| Guide: Scaling Up | 6 | Routing, SFC, SSR, state management, testing, tooling |
| Guide: Best Practices | 4 | Accessibility, performance, production deployment, security |
| Guide: TypeScript | 3 | Overview, composition API, options API |
| Guide: Extras | 8 | Animation, reactivity in-depth, reactivity transform, render function, rendering mechanism, composition API FAQ, web components, ways of using Vue |
| API Reference | 28 | Application, built-in components/directives/special-elements/attributes, composition API (setup, lifecycle, dependency injection, helpers), reactivity (core, advanced, utilities), options API (state, rendering, lifecycle, misc, composition), render function, SFC (spec, script-setup, CSS features), SSR, compile-time flags, utility types, general, custom renderer, custom elements |
| Examples | 20 | Hello world through markdown editor, each with composition/options variants |
| Tutorial | 15 steps | Interactive tutorial from basics through components |
| Style Guide | 5 | Essential, recommended, strongly recommended, use with caution rules |
| Error Reference | 1 | Runtime error catalog |
| About | 6 | Team, community guide, FAQ, releases, CoC, privacy |

## Key API Reference Pages

| Topic | Path |
|-------|------|
| Application API | `/src/api/application.md` |
| Reactivity Core | `/src/api/reactivity-core.md` |
| Reactivity Utilities | `/src/api/reactivity-utilities.md` |
| Reactivity Advanced | `/src/api/reactivity-advanced.md` |
| Composition API: setup() | `/src/api/composition-api-setup.md` |
| Composition API: Lifecycle | `/src/api/composition-api-lifecycle.md` |
| Composition API: DI | `/src/api/composition-api-dependency-injection.md` |
| Composition API: Helpers | `/src/api/composition-api-helpers.md` |
| Options: State | `/src/api/options-state.md` |
| Options: Rendering | `/src/api/options-rendering.md` |
| Options: Lifecycle | `/src/api/options-lifecycle.md` |
| Options: Misc | `/src/api/options-misc.md` |
| Component Instance | `/src/api/component-instance.md` |
| Built-in Components | `/src/api/built-in-components.md` |
| Built-in Directives | `/src/api/built-in-directives.md` |
| SFC Script Setup | `/src/api/sfc-script-setup.md` |
| SFC Spec | `/src/api/sfc-spec.md` |
| SSR | `/src/api/ssr.md` |
| Render Function | `/src/api/render-function.md` |

## See Also

- [lode-map.md](lode-map.md)