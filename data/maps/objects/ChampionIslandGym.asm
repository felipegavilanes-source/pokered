	object_const_def
	const_export CHAMPIONISLANDGYM_OAK

ChampionIslandGym_Object:
	db $3 ; gym border block

	def_warp_events
	warp_event 4, 13, LAST_MAP, 1
	warp_event 5, 13, LAST_MAP, 2

	def_bg_events

	def_object_events
	object_event 4, 1, SPRITE_OAK, STAY, DOWN, TEXT_CHAMPIONISLANDGYM_OAK, OPP_PROF_OAK, 1

	def_warps_to CHAMPION_ISLAND_GYM
