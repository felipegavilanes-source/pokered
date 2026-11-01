# Pokémon Blue — Challenge Edition

Development branch: `challenge-edition`. Target: Pokémon Blue (Game Boy), preserving original graphics, Kanto story and music.

## Core rules (v0.1)

- All 151 species obtainable in one save without trading, glitches or another version.
- Progressive encounters: preserve early-route difficulty and introduce version exclusives in appropriate habitats.
- Oak offers Magikarp, Tangela or Zubat at level 5. Bulbasaur, Charmander and Squirtle are rare wild encounters on Routes 24, 25 and 6, respectively.
- Both fossils recoverable within one save.
- Both Hitmonlee and Hitmonchan obtainable without trading.
- Mew accessible through a difficult, one-time postgame event.
- Legendaries remain rare, with unique encounters.
- Existing trade evolutions converted to level evolutions: Kadabra 37, Machoke 40, Graveler 40, Haunter 38 (implemented).
- No duplicate softlocks: one-time gift, fossil and legendary encounters must have a recovery route where necessary to make 151 possible.
- More challenging but fair: increase boss team quality, improve movesets, and raise trainer levels progressively without excessive grinding.
- Maintain original Gen I battle rules for first release; do not promise modern battle AI without implementation and testing.

## Visual character customization

- Player overworld sprite slot uses Professor Oak graphics while the original NPC Oak remains present in the laboratory.
- Do not rewrite story, dialogue or events to explain the player's appearance.
- Battle/intro and other player graphics still require verification.

## Implementation milestones

1. **Evolution accessibility** — level-based trade evolutions (done).
2. **Encounter availability** — audit Blue encounter tables and add Red exclusives; check all nonlegendary species or evolution lines.
3. **Choice-locked species** — fossil and Fighting Dojo reward events; original starters are now rare wild encounters.
4. **Postgame** — Mew event and completion verification.
5. **Challenge battles** — Brock through Champion, rival and trainer progression.
6. **Build/QA** — compile Blue ROM, verify encounters, Pokédex completion path, save behavior and Delta compatibility.

## Release criteria

- Reproducible build from the repository.
- A documented obtainable location or evolution path for every species #001–#151.
- A complete-playthrough test demonstrating no mandatory external trade.
- No claim of a playable release until a build has succeeded and been tested.

## Distribution

Prefer distributing source and/or patch files; users apply patches to a legitimately obtained ROM. Do not commit copyrighted ROM binaries.
