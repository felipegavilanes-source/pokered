ChampionIslandGym_Script:
	call EnableAutoTextBoxDrawing
	ld hl, ChampionIslandGymTrainerHeaders
	ld de, ChampionIslandGym_ScriptPointers
	ld a, [wRoute21CurScript]
	call ExecuteCurMapScriptInTable
	ld [wRoute21CurScript], a
	ret

ChampionIslandGym_ScriptPointers:
	def_script_pointers
	dw_const CheckFightingMapTrainers, SCRIPT_ROUTE21_DEFAULT
	dw_const DisplayEnemyTrainerTextAndStartBattle, SCRIPT_ROUTE21_START_BATTLE
	dw_const EndTrainerBattle, SCRIPT_ROUTE21_END_BATTLE

ChampionIslandGym_TextPointers:
	def_text_pointers
	dw_const ChampionIslandGymOakText, TEXT_CHAMPIONISLANDGYM_OAK

ChampionIslandGymTrainerHeaders:
	def_trainers
ChampionIslandGymOakTrainerHeader:
	trainer EVENT_BEAT_CHAMPION_ISLAND_OAK, 0, ChampionIslandGymOakBattleText, ChampionIslandGymOakEndBattleText, ChampionIslandGymOakAfterBattleText
	db -1

ChampionIslandGymOakText:
	text_asm
	ld hl, wElite4Flags
	bit BIT_UNUSED_BEAT_ELITE_4, [hl]
	jr z, .locked
	ld hl, ChampionIslandGymOakTrainerHeader
	call TalkToTrainer
	jp TextScriptEnd
.locked
	ld hl, ChampionIslandGymOakLockedText
	call PrintText
	jp TextScriptEnd

ChampionIslandGymOakLockedText:
	text "Only a CHAMPION"
	line "can challenge me."
	prompt

ChampionIslandGymOakBattleText:
	text "Welcome to the"
	line "ultimate challenge!"
	para "Show me all you"
	line "have learned!"
	end

ChampionIslandGymOakEndBattleText:
	text "Outstanding!"
	prompt

ChampionIslandGymOakAfterBattleText:
	text "You are a true"
	line "POKEMON master!"
	prompt
