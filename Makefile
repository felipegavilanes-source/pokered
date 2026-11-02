roms := \
	pokered.gbc \
	pokeblue.gbc \
	pokeblue_debug.gbc
patches := \
	pokered.patch \
	pokeblue.patch

rom_obj := \
	audio.o \
	home.o \
	main.o \
	maps.o \
	ram.o \
	text.o \
	gfx/pics.o \
	gfx/sprites.o \
	gfx/tilesets.o

pokered_obj        := $(rom_obj:.o=_red.o)
pokeblue_obj       := $(rom_obj:.o=_blue.o)
pokeblue_debug_obj := $(rom_obj:.o=_blue_debug.o)
pokered_vc_obj     := $(rom_obj:.o=_red_vc.o)
pokeblue_vc_obj    := $(rom_obj:.o=_blue_vc.o)


### Build tools

ifeq (,$(shell command -v sha1sum 2>/dev/null))
SHA1 := shasum
else
SHA1 := sha1sum
endif

RGBDS ?=
RGBASM  ?= $(RGBDS)rgbasm
RGBFIX  ?= $(RGBDS)rgbfix
RGBGFX  ?= $(RGBDS)rgbgfx
RGBLINK ?= $(RGBDS)rgblink

RGBASMFLAGS  ?= -Weverything -Wtruncation=1
RGBLINKFLAGS ?= -Weverything -Wtruncation=1
RGBFIXFLAGS  ?= -Weverything
RGBGFXFLAGS  ?= -Weverything


### Build targets

.SUFFIXES:
.SECONDEXPANSION:
.PRECIOUS:
.SECONDARY:
.PHONY: \
	all \
	red \
	blue \
	blue_debug \
	red_vc \
	blue_vc \
	clean \
	tidy \
	compare \
	tools

all: $(roms)
red:        pokered.gbc
blue:       pokeblue.gbc
blue_debug: pokeblue_debug.gbc
red_vc:     pokered.patch
blue_vc:    pokeblue.patch

clean: tidy
	find gfx \
	     \( -iname '*.1bpp' \
	        -o -iname '*.2bpp' \
	        -o -iname '*.pic' \) \
	     -delete

tidy:
	$(RM) $(roms) \
	      $(roms:.gbc=.sym) \
	      $(roms:.gbc=.map) \
	      $(patches) \
	      $(patches:.patch=_vc.gbc) \
	      $(patches:.patch=_vc.sym) \
	      $(patches:.patch=_vc.map) \
	      $(patches:%.patch=vc/%.constants.sym) \
	      $(pokered_obj) \
	      $(pokeblue_obj) \
	      $(pokered_vc_obj) \
	      $(pokeblue_vc_obj) \
	      $(pokeblue_debug_obj) \
	      rgbdscheck.o
	$(MAKE) clean -C tools/

compare: $(roms) $(patches)
	@$(SHA1) -c roms.sha1

tools:
	$(MAKE) -C tools/


RGBASMFLAGS += -Q8 -P includes.asm
# Create a sym/map for debug purposes if `make` run with `DEBUG=1`
ifeq ($(DEBUG),1)
RGBASMFLAGS += -E
endif

$(pokered_obj):        RGBASMFLAGS += -D _RED
$(pokeblue_obj):       RGBASMFLAGS += -D _BLUE
$(pokeblue_debug_obj): RGBASMFLAGS += -D _BLUE -D _DEBUG
$(pokered_vc_obj):     RGBASMFLAGS += -D _RED -D _RED_VC
$(pokeblue_vc_obj):    RGBASMFLAGS += -D _BLUE -D _BLUE_VC

%.patch: %_vc.gbc %.gbc vc/%.patch.template
	tools/make_patch $*_vc.sym $^ $@

rgbdscheck.o: rgbdscheck.asm
	$(RGBASM) -o $@ $<

# Build tools when building the rom.
# This has to happen before the rules are processed, since that's when scan_includes is run.
ifeq (,$(filter clean tidy tools,$(MAKECMDGOALS)))

$(info $(shell $(MAKE) -C tools))

# The dep rules have to be explicit or else missing files won't be reported.
# As a side effect, they're evaluated immediately instead of when the rule is invoked.
# It doesn't look like $(shell) can be deferred so there might not be a better way.
preinclude_deps := includes.asm $(shell tools/scan_includes includes.asm)
define DEP
$1: $2 $$(shell tools/scan_includes $2) $(preinclude_deps) | rgbdscheck.o
	$$(RGBASM) $$(RGBASMFLAGS) -o $$@ $$<
endef

# Dependencies for objects (drop _red and _blue from asm file basenames)
$(foreach obj, $(pokered_obj), $(eval $(call DEP,$(obj),$(obj:_red.o=.asm))))
$(foreach obj, $(pokeblue_obj), $(eval $(call DEP,$(obj),$(obj:_blue.o=.asm))))
$(foreach obj, $(pokeblue_debug_obj), $(eval $(call DEP,$(obj),$(obj:_blue_debug.o=.asm))))
$(foreach obj, $(pokered_vc_obj), $(eval $(call DEP,$(obj),$(obj:_red_vc.o=.asm))))
$(foreach obj, $(pokeblue_vc_obj), $(eval $(call DEP,$(obj),$(obj:_blue_vc.o=.asm))))

endif


RGBLINKFLAGS += -d
pokered.gbc:        RGBLINKFLAGS += -p 0x00
pokeblue.gbc:       RGBLINKFLAGS += -p 0x00
pokeblue_debug.gbc: RGBLINKFLAGS += -p 0xff
pokered_vc.gbc:     RGBLINKFLAGS += -p 0x00
pokeblue_vc.gbc:    RGBLINKFLAGS += -p 0x00

RGBFIXFLAGS += -jsv -n 0 -k 01 -l 0x33 -m MBC3+RAM+BATTERY -r 03
pokered.gbc:        RGBFIXFLAGS += -p 0x00 -t "POKEMON RED"
pokeblue.gbc:       RGBFIXFLAGS += -p 0x00 -t "POKEMON BLUE"
pokeblue_debug.gbc: RGBFIXFLAGS += -p 0xff -t "POKEMON BLUE"
pokered_vc.gbc:     RGBFIXFLAGS += -p 0x00 -t "POKEMON RED"
pokeblue_vc.gbc:    RGBFIXFLAGS += -p 0x00 -t "POKEMON BLUE"

%.gbc: $$(%_obj) layout.link
	$(RGBLINK) $(RGBLINKFLAGS) -l layout.link -m $*.map -n $*.sym -o $@ $(filter %.o,$^)
	$(RGBFIX) $(RGBFIXFLAGS) $@


### Misc file-specific graphics rules

gfx/battle/move_anim_0.2bpp: tools/gfx += --trim-whitespace
gfx/battle/move_anim_1.2bpp: tools/gfx += --trim-whitespace

gfx/intro/blue_jigglypuff_1.2bpp: RGBGFXFLAGS += --columns
gfx/intro/blue_jigglypuff_2.2bpp: RGBGFXFLAGS += --columns
gfx/intro/blue_jigglypuff_3.2bpp: RGBGFXFLAGS += --columns
gfx/intro/red_nidorino_1.2bpp: RGBGFXFLAGS += --columns
gfx/intro/red_nidorino_2.2bpp: RGBGFXFLAGS += --columns
gfx/intro/red_nidorino_3.2bpp: RGBGFXFLAGS += --columns
gfx/intro/gengar.2bpp: RGBGFXFLAGS += --columns
gfx/intro/gengar.2bpp: tools/gfx += --remove-duplicates --preserve=0x19,0x76

gfx/credits/the_end.2bpp: tools/gfx += --interleave --png=$<

gfx/slots/red_slots_1.2bpp: tools/gfx += --trim-whitespace
gfx/slots/blue_slots_1.2bpp: tools/gfx += --trim-whitespace

gfx/tilesets/%.2bpp: tools/gfx += --trim-whitespace
gfx/tilesets/reds_house.2bpp: tools/gfx += --preserve=0x48

gfx/trade/game_boy.2bpp: tools/gfx += --remove-duplicates


### Challenge Edition: reproducible four-shade football trainer portraits
# Explicit PNG targets override the catch-all empty PNG rule below.
gfx/trainers/messi.png gfx/trainers/cr7.png gfx/trainers/neymar.png gfx/trainers/trump.png gfx/trainers/elon_musk.png gfx/trainers/jeff_bezos.png gfx/trainers/bill_gates.png gfx/trainers/steve_jobs.png gfx/trainers/xi_jinping.png gfx/trainers/kim_jong_un.png gfx/trainers/maduro.png gfx/trainers/che_guevara.png gfx/trainers/putin.png: gfx/trainers/%.png: tools/generate_football_trainer.py tools/football_redesign.py tools/neymar_reference.py tools/messi_reference.py tools/cr7_reference.py tools/trump_reference.py tools/elon_musk_reference.py
	python3 $< $* $@

# CR7 overworld graphic (six 16x16 frames).
gfx/sprites/cr7.png: tools/create_cr7_sprite.py
	python3 $<

# Messi's unique NPC sheet is compiled in the same six-frame Gen 1 layout.
gfx/sprites/messi.png: tools/create_messi_sprite.py
	python3 $<

# Neymar's overworld uses a standalone 6-frame 16x96 sheet.
gfx/sprites/neymar.png: tools/create_neymar_sprite.py
	python3 $<

# Always regenerate Agumon graphics correctly for local and CI builds.
gfx/sprites/agumon.png: tools/create_agumon_sprite.py
	python3 $<

### Catch-all graphics rules

%.2bpp: %.png
	$(RGBGFX) --colors dmg $(RGBGFXFLAGS) -o $@ $<
	$(if $(tools/gfx),\
		tools/gfx $(tools/gfx) -o $@ $@ || $$($(RM) $@ && false))

%.1bpp: %.png
	$(RGBGFX) --colors dmg $(RGBGFXFLAGS) --depth 1 -o $@ $<
	$(if $(tools/gfx),\
		tools/gfx $(tools/gfx) --depth 1 -o $@ $@ || $$($(RM) $@ && false))

%.pic: %.2bpp
	tools/pkmncompress $< $@


### File extensions that are never generated and should be manually created

%.asm: ;
%.inc: ;
%.png: ;
%.pal: ;
%.bin: ;
%.blk: ;
%.bst: ;
%.rle: ;
