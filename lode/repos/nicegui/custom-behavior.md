# NiceGUI — Custom Behavior

How to customize and extend NiceGUI elements, from pure-Python tweaks to full custom Vue components.

## 1. Props, Classes, Style (Python-only)

Every element has `.props()`, `.classes()`, `.style()` for Quasar props and CSS:

```python
ui.button('Click').props('flat rounded').classes('q-ma-md').style('color: red')
```

Class-level defaults before instantiation:

```python
ui.button.default_classes('q-ma-md')
ui.button.default_props('flat rounded')
ui.button.default_style('color: red')
```

## 2. Event Handlers (Python callback)

`.on()` subscribes to any DOM or Vue event:

```python
element.on('click', handler=my_handler)
element.on('update:model-value', handler=on_change, args=['value'])
element.on('keydown.enter', handler=on_enter)
```

Key params: `handler` (Python callback), `args` (which args to send), `throttle`, `js_handler`.

50+ typed event dataclasses: `ClickEventArguments(sender, client)`, `EChartPointClickEventArguments`, `UploadEventArguments`, etc.

## 3. js_handler — Client-side Event Filtering

The `js_handler` param on `.on()` runs JavaScript client-side to transform or filter events before they reach Python:

```python
# Only emit when value > 0
element.on('change', handler=on_change, js_handler='(e) => { if (e > 0) emit(e) }')
```

Default `js_handler` is `'(...args) => emit(...args)'` — sends everything. Replace it to filter, transform, or handle entirely client-side.

## 4. run_method() — Python calling JS component methods

```python
class Counter(ui.element, component='counter.js'):
    def reset(self):
        self.run_method('reset')  # calls reset() method on the Vue instance
```

Each element has a numeric `id` mapping 1:1 to its Vue instance. `runMethod(id, name, args)` is a global JS function. Awaitable: `result = await self.run_method('getData')`.

## 5. ui.run_javascript() — Arbitrary JS execution

```python
result = await ui.run_javascript('document.title = "Hello"')
result = await ui.run_javascript('return getElement(42).value')   # access Vue component
result = await ui.run_javascript('return getHtmlElement(id).value') # access raw DOM
```

Escape hatch for one-off DOM manipulation, browser APIs, or third-party JS library interaction.

## 6. Custom Vue Components (component= parameter)

Primary mechanism for new elements with frontend behavior. Uses `__init_subclass__` on Element:

**`.js` file** (render function only):
```python
class Counter(ui.element, component='counter.js'):
    def __init__(self, title: str, *, on_change=None):
        super().__init__()
        self._props['title'] = title
        self.on('change', handler=on_change)
```

```js
export default {
  template: `<button @click="handle_click">{{title}}: {{value}}</button>`,
  props: { title: String },
  data() { return { value: 0 } },
  methods: {
    handle_click() { this.value += 1; this.$emit('change', this.value) },
    reset() { this.value = 0 },
  },
}
```

**`.vue` file** (single-file component with template, script, style):
```python
class OnOff(ui.element, component='on_off.vue'):
    ...
```

Vue SFC built by NiceGUI's VBuild at registration time (not per request). Supports `<template>`, `<script>`, `<style scoped>`.

## 7. ESM Modules (NPM dependencies)

For complex components needing third-party NPM packages. Uses `esm=` in `__init_subclass__`:

```python
class AgGrid(Element, component='aggrid.js', esm={'nicegui-aggrid': 'dist'},
             default_classes='nicegui-aggrid'):
```

ESM system: registers import map entry pointing to pre-built `dist/`, JS file uses `import` for NPM packages, bundled via rollup/vite. `setup_esm_package()` in `dependencies.py` provides lazy import loading.

All heavy elements use this: EChart, AG Grid, CodeMirror, Leaflet, Mermaid, Plotly, Scene (Three.js), XTerm, JSON Editor, Joystick, Sortable.

## 8. AnyWidget Integration (Jupyter ecosystem)

```python
ui.anywidget(some_anywidget_instance)
```

Wraps the widget's `_esm` and `_css`, syncs `sync=True` traits bidirectionally. Access to the [AnyWidget gallery](https://try.anywidget.dev/) without writing integration code.

## See Also

- [summary.md](summary.md) — overview, architecture, element hierarchy
- [lode-map.md](lode-map.md) — package structure, all elements, examples
- `repos/nicegui/nicegui/element.py` — `Element.__init_subclass__` with component/esm/dependencies params
- `repos/nicegui/nicegui/dependencies.py` — Component, VueComponent, JsComponent, Library, EsmModule registration
- `repos/nicegui/examples/custom_vue_component/` — working .js and .vue examples