# Unexpected Keyboard

Unexpected Keyboard is a lightweight Java Android IME designed around configurable directional slots on each key. The reference clone is `repos/unexpected-keyboard` from `https://github.com/Julow/Unexpected-Keyboard` and is licensed under GPL-3.0.

## Directional input model

Each key contains nine values arranged as center plus eight compass directions. XML accepts `c`, `n`, `ne`, `e`, `se`, `s`, `sw`, `w`, and `nw` attributes. Pointer motion is quantized into sixteen angular sectors, which map onto the eight slots. If the exact direction is empty, the resolver searches nearby sectors within a bounded arc, making sparse layouts forgiving.

`Pointers.java` owns the touch state, directional resolution, modifiers, latching, long press, repeat, and sliding keys. `Gesture.java` adds round-trip, clockwise-circle, and anticlockwise-circle recognition. The layout representation and recognizer are compact and unusually easy to reason about.

## Relevance

The valuable reference is its interaction design rather than a prediction engine. It demonstrates visible per-key sublabels, eight-way selection, sparse-direction fallback, and robust gesture state transitions. Its GPL code cannot simply be copied into a differently licensed distributed application, although private use does not trigger GPL source-distribution obligations.

Unexpected Keyboard is not the strongest base for conventional autocorrection or language prediction. Adding a modern suggestion engine to it would be a larger integration than adding board-wide actions to a keyboard that already has both prediction and flick keys. See [FUTO Keyboard](../android-keyboard/summary.md).
