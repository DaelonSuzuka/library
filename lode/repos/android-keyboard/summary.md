# FUTO Keyboard

FUTO Keyboard is a modern offline Android IME forked from AOSP LatinIME. It combines a mature Java/Kotlin keyboard and input pipeline with native dictionary and swipe-decoding code, Compose settings UI, bundled language assets, and optional offline voice input. The reference clone is `repos/android-keyboard` from `https://github.com/futo-org/android-keyboard`.

## License boundary

The repository uses FUTO Source First License 1.1-kb, not an OSI-approved open-source license. It permits modification for non-commercial personal use and free non-commercial distribution, but restricts commercial modification and distribution. This is compatible with a private personal keyboard experiment, while making it a poor source for code intended to become conventionally open-source later.

## Gesture and layout architecture

The current v2 layout engine already supports `type: flick` keys with a primary value and up to eight directional children: up, down, left, right, and four diagonals. Layouts are YAML resources; the Japanese 12-key layout is the complete working example. `FlickKey.kt` converts the declarations into `ComputedFlickData`, `Key.kt` resolves displacement against a threshold of one third of key width, and `PointerTracker.java` previews and emits the selected child key.

```yaml
- type: flick
  primary: "a"
  up: "1"
  downLeft: "_"
  right: "@"
```

FUTO's flick implementation therefore overlaps substantially with Unexpected Keyboard's signature feature. The missing Fleksy behavior is a board-wide action gesture layer: swipe left to delete a word, swipe right to insert a space, and candidate-control gestures. That layer must arbitrate short per-key flicks against longer board-wide swipes because both begin with the same pointer motion.

## Relevant seams

- `java/src/org/futo/inputmethod/v2keyboard/FlickKey.kt` - declarative eight-direction flick keys
- `java/src/org/futo/inputmethod/keyboard/Key.kt` - direction and threshold resolution
- `java/src/org/futo/inputmethod/keyboard/PointerTracker.java` - touch lifecycle and flick dispatch
- `java/src/org/futo/inputmethod/latin/inputlogic/` - text mutation and composing behavior
- `native/jni/src/suggest/` - dictionary, correction, and swipe suggestion engine
- `java/assets/layouts/LayoutSpec.md` - current layout schema
- `java/assets/layouts/Japanese/flick.yaml` - complete flick-layout example

The likely experiment is to preserve the existing flick and input engines, then add a configurable board-wide action recognizer with an explicit distance/state boundary. See [Unexpected Keyboard](../unexpected-keyboard/summary.md) and [FlorisBoard](../florisboard/summary.md).
