# FlorisBoard

FlorisBoard is an Apache-2.0 Kotlin Android IME focused on privacy, theming, extensions, and configuration. The reference clone is `repos/florisboard` from `https://github.com/florisboard/florisboard`.

## Board-wide gesture layer

FlorisBoard already implements the closest open reference to Fleksy's editing gestures. Users can independently bind swipe up, down, left, and right across the main keyboard to actions including delete word, insert space, shift, cursor movement, hide keyboard, undo, redo, and mode changes. Distance and velocity thresholds are configurable.

`SwipeGesture.Detector` tracks displacement and velocity and resolves eight directions. `SwipeAction` is a typed action vocabulary, `GesturesScreen.kt` exposes bindings, and `TextKeyboardLayout.kt` arbitrates gesture events and dispatches actions through `KeyboardManager`.

The general swipe bindings are disabled while glide typing is enabled. That explicit conflict is relevant to any combined design: directional actions, per-key flicks, and word-trace typing consume overlapping motion and require a declared priority/state model.

## Current limitation

The current releases do not include word suggestions or spell checking; the repository describes them as a future milestone. FlorisBoard is therefore the cleanest permissively licensed gesture-action reference, but not presently the closest complete replacement for a correction-heavy Fleksy workflow.

See [FUTO Keyboard](../android-keyboard/summary.md) for the stronger prediction base and [Unexpected Keyboard](../unexpected-keyboard/summary.md) for per-key directional slots.
