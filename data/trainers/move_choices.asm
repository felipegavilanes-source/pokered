DEF __move_choices__ = 0

MACRO move_choices
	IF _NARG
		db \# ; all args
	ENDC
	db 0 ; end
	DEF __move_choices__ += 1
ENDM

; move choice modification methods that are applied for each trainer class
TrainerClassMoveChoiceModifications:
	move_choices 1, 3 ; YOUNGSTER
	move_choices 1, 3 ; BUG_CATCHER
	move_choices 1, 3 ; LASS
	move_choices 1, 3 ; SAILOR
	move_choices 1, 3 ; JR_TRAINER_M
	move_choices 1, 3 ; JR_TRAINER_F
	move_choices 1, 3, 5 ; POKEMANIAC
	move_choices 1, 3 ; SUPER_NERD
	move_choices 1, 3 ; HIKER
	move_choices 1, 3 ; BIKER
	move_choices 1, 3 ; BURGLAR
	move_choices 1, 3 ; ENGINEER
	move_choices 1, 3 ; UNUSED_JUGGLER
	move_choices 1, 3 ; FISHER
	move_choices 1, 3 ; SWIMMER
	move_choices 1, 3 ; CUE_BALL
	move_choices 1, 3 ; GAMBLER
	move_choices 1, 3 ; BEAUTY
	move_choices 1, 3, 5 ; PSYCHIC_TR
	move_choices 1, 3 ; ROCKER
	move_choices 1, 3 ; JUGGLER
	move_choices 1, 3 ; TAMER
	move_choices 1, 3 ; BIRD_KEEPER
	move_choices 1, 3 ; BLACKBELT
	move_choices 1, 3, 5 ; RIVAL1
	move_choices 1, 2, 3 ; PROF_OAK: strategic setup/status and type-aware attacks
	move_choices 1, 3 ; CHIEF
	move_choices 1, 3, 5 ; SCIENTIST
	move_choices 1, 3, 5 ; GIOVANNI
	move_choices 1, 3, 5 ; ROCKET
	move_choices 1, 3, 5 ; COOLTRAINER_M
	move_choices 1, 3, 5 ; COOLTRAINER_F
	move_choices 1, 3, 5 ; BRUNO: evaluate type matchups and favor strong attacks
	move_choices 1, 3, 5 ; BROCK: type awareness and strong damaging moves
	move_choices 1, 3, 5 ; MISTY: type matchups and damaging move priority
	move_choices 1, 3, 5 ; LT_SURGE: favor effective, powerful attacks
	move_choices 1, 2, 3 ; ERIKA: tactical status/setup and type effectiveness
	move_choices 1, 2, 3 ; KOGA: favor tactical setup and type effectiveness, retain status moves
	move_choices 1, 3, 5 ; BLAINE: consider type effectiveness and prioritize strong attacks
	move_choices 1, 3, 5 ; SABRINA: favor strong attacks
	move_choices 1, 3 ; GENTLEMAN
	move_choices 1, 3, 5 ; RIVAL2
	move_choices 1, 3, 5 ; RIVAL3
	move_choices 1, 2, 3, 5 ; LORELEI: retain strategic AI and prioritize powerful attacks
	move_choices 1, 3 ; CHANNELER
	move_choices 1, 3    ; AGATHA: consider type effectiveness while preserving status tactics
	move_choices 1, 3    ; LANCE
	move_choices 1, 3, 5 ; MESSI
	move_choices 1, 3, 5 ; CR7
	assert __move_choices__ == NUM_TRAINERS, \
		"TrainerClassMoveChoiceModifications: expected {d:NUM_TRAINERS} entries, got {d:__move_choices__}"
