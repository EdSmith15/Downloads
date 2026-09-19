# Binomial Drill

A single-file flashcard app for learning plant species names (genus + species).
Open `index.html` in any browser, or add it to your phone's home screen.

## Levels

| Level  | What you see                                   | What you type                         |
|--------|------------------------------------------------|---------------------------------------|
| Easy   | Both words with ~40% of the letters replaced by dashes. The blanked letters are re-rolled every time the card comes up. | The missing letters, one per dash |
| Medium | Either the genus or the species blanked out completely (chosen at random each time). | The whole missing word, one letter per dash |
| Hard   | Only the common name and family.               | The full name, e.g. `Quercus robur`   |

Every blank is shown as a dash. Input comes from the built-in iOS-style keyboard
(a physical keyboard also works on desktop). Cards you get wrong come back a few
cards later in the same round, and the round-end summary lists what to revisit.

## Your own species

Tap **Deck** in the top-left and paste one plant per line:

```
Genus species | Common name | Family | https://example.com/optional-photo.jpg
```

Family and photo are optional. The deck is saved in the browser on that device.
The sample deck of 32 common UK plants is there as a placeholder; replace it with
your list.
