from enum import Enum

class PitchingStats(str, Enum):
    pitch_type = 'pitch_type'
    game_date = 'game_date'
    release_speed = 'release_speed'
    release_pos_x = 'release_pos_x'
    release_pos_z = 'release_pos_z'
    player_name = 'player_name'
    batter = 'batter'
    pitcher = 'pitcher'
    events = 'events'
    pitch_description = 'description'
    spin_dir_deprecated = 'spin_dir' # deprecated column 
    spin_rate_deprecated = 'spin_rate_deprecated' # deprecated column - Replaced by release_spin
    break_angle_deprecated = 'break_angle_deprecated' # deprecated column 
    break_length_deprecated = 'break_length_deprecated' # deprecated column 
    plate_zone = 'zone'
    pa_description = 'des' # description of plate appearance
    game_type = 'game_type'
    b_bats = 'stand'
    p_throws = 'p_throws'
    home_team = 'home_team'
    away_team = 'away_team'
    pitch_result = 'type'
    hit_fielded_location = 'hit_location' 
    batted_ball_type = 'bb_type'
    balls_in_count = 'balls'    
    strikes_in_count = 'strikes' 
    game_year = 'game_year' 
    pitch_movement_x = 'pfx_x' 
    pitch_movement_z = 'pfx_z' 
    plate_x = 'plate_x' 
    plate_z = 'plate_z' 
    on_1b = 'on_1b' 
    on_2b = 'on_2b' 
    on_3b = 'on_3b' 
    outs_when_up = 'outs_when_up' 
    inning = 'inning' 
    topbot_of_inning = 'inning_topbot'
    hit_coord_x = 'hc_x'
    hit_coord_y = 'hc_y'
    tfs_deprecated = 'tfs_deprecated' # deprecated column 
    tfs_zulu_deprecated = 'tfs_zulu_deprecated' # deprecated column 
    catcher = 'fielder_2'
    umpire_deprecated = 'umpire' # deprecated column 
    sv_id = 'sv_id'
    pitch_velocity_x = 'vx0'
    pitch_velocity_y = 'vy0'
    pitch_velocity_z = 'vz0'
    pitch_acceleration_x = 'ax'
    pitch_acceleration_y = 'ay'
    pitch_acceleration_z = 'az'
    top_of_strikezone = 'sz_top'
    bottom_of_strikezone = 'sz_bot'
    hit_distance = 'hit_distance'
    effective_speed = 'effective_speed'
    release_spin = 'release_spin'
    release_extension = 'release_extension'
    game_pk = 'game_pk'
    fielder_1 = pitcher
    fielder_2 = 'fielder_2'
    fielder_3 = 'fielder_3'
    fielder_4 = 'fielder_4'
    fielder_5 = 'fielder_5'
    fielder_6 = 'fielder_6'
    fielder_7 = 'fielder_7'
    fielder_8 = 'fielder_8'
    fielder_9 = 'fielder_9'
    release_pos_y = 'release_pos_y'
    estimated_ba_using_speedangle = 'estimated_ba_using_speedangle'
    estimated_woba_using_speedangle = 'estimated_woba_using_speedangle'
    woba_value = 'woba_value'
    woba_denom = 'woba_denom'
    babip_value = 'babip_value'
    iso_value = 'iso_value'
    launch_speed_angle = 'launch_speed_angle'
    pa_number = 'at_bat_number'
    pa_pitch_count = 'pitch_number'
    pitch_name = 'pitch_name'
    home_score = 'home_score'
    away_score = 'away_score'
    bat_score = 'bat_score' # reminder: not the same as home score
    fld_score = 'fld_score' # reminder: not the same as away score
    post_home_score = 'post_home_score'
    post_away_score = 'post_away_score'
    post_bat_score = 'post_bat_score'
    if_fielding_alignment = 'if_fielding_alignment'
    of_fielding_alignment = 'of_fielding_alignment'
    pitch_spin_axis = 'spin_axis'
    delta_home_win_exp = 'delta_home_win_exp'
    delta_run_exp = 'delta_run_exp'




# pitch_type
# The type of pitch derived from Statcast.
# pitch_type = 'pitch_type'

# game_date
# Date of the Game.
# game_date = 'game_date'

# release_speed
# Pitch velocities from 2008-16 are via Pitch F/X, and adjusted to roughly out-of-hand release point. All velocities from 2017 and beyond are Statcast, which are reported out-of-hand.
# release_speed = 'release_speed'

# release_pos_x
# Horizontal Release Position of the ball measured in feet from the catcher's perspective.
# release_pos_x = 'release_pos_x'

# release_pos_z
# Vertical Release Position of the ball measured in feet from the catcher's perspective.
# release_pos_z = 'release_pos_z'

# player_name
# Player's name tied to the event of the search.
# player_name = 'player_name'

# batter
# MLB Player Id tied to the play event.
# batter = 'batter'

# pitcher
# MLB Player Id tied to the play event.
# pitcher = 'pitcher'

# events
# Event of the resulting Plate Appearance.
# events = 'events'

# description
# Description of the resulting pitch.
# PitchDescription = 'description'

# spin_dir
# * Deprecated field from the old tracking system.
# spin_dir = 'spin_dir'

# spin_rate_deprecated
# * Deprecated field from the old tracking system. Replaced by release_spin
# spin_rate_deprecated = 'spin_rate_deprecated'

# break_angle_deprecated
# * Deprecated field from the old tracking system.
# break_angle_deprecated = 'break_angle_deprecated'

# break_length_deprecated
# * Deprecated field from the old tracking system.
# break_length_deprecated = 'break_length_deprecated'

# zone
# Zone location of the ball when it crosses the plate from the catcher's perspective.
# zone = 'zone'

# des
# Plate appearance description from game day.
# pa_description = 'des'

# game_type
# Type of Game. E = Exhibition, S = Spring Training, R = Regular Season, F = Wild Card, D = Divisional Series, L = League Championship Series, W = World Series
# game_type = 'game_type'

# stand
# Side of the plate batter is standing.
# b_bats = 'stand'

# p_throws
# Hand pitcher throws with.
# p_throws = 'p_throws'

# home_team
# Abbreviation of home team.
# home_team = 'home_team'

# away_team
# Abbreviation of away team.
# away_team = 'away_team'

# type
# Short hand of pitch result. B = ball, S = strike, X = in play.
# pitch_result = 'type'

# hit_location
# Position of first fielder to touch the ball.
# hit_fielded_location = 'hit_location'

# bb_type
# Batted ball type, ground_ball, line_drive, fly_ball, popup.
# batted_ball_type = 'bb_type' # i dont like the re-use of bb as its known as walks usually  

# balls
# Pre-pitch number of balls in count.
# balls_in_count = 'balls' 

# strikes
# Pre-pitch number of strikes in count.
# strikes_in_count = 'strikes' 

# game_year
# Year game took place.
# game_year = 'game_year' 

# pfx_x
# Horizontal movement in feet from the catcher's perspective. --- pfx's meaning is lost or never had a meaning? maybe pitch f/x camera is the source? nobody 
# pitch_movement_x = 'pfx_x' 

# pfx_z
# Vertical movement in feet from the catcher's perpsective.
# pitch_movement_z = 'pfx_z' 

# plate_x
# Horizontal position of the ball when it crosses home plate from the catcher's perspective.
# plate_x = 'plate_x' 

# plate_z
# Vertical position of the ball when it crosses home plate from the catcher's perspective.
# plate_z = 'plate_z' 

# on_3b
# Pre-pitch MLB Player Id of Runner on 3B.
# runner_on_3b = 'on_3b' 

# on_2b
# Pre-pitch MLB Player Id of Runner on 2B.
# runner_on_2b = 'on_2b' 

# on_1b
# Pre-pitch MLB Player Id of Runner on 1B.
# runner_on_1b = 'on_1b' 

# outs_when_up
# Pre-pitch number of outs.
# outs_when_up = 'outs_when_up' 

# inning
# Pre-pitch inning number.
# inning = 'inning' 

# inning_topbot
# Pre-pitch top or bottom of inning.
# inning_topbot = 'inning_topbot

# hc_x
# Hit coordinate X of batted ball.
# hit_coord_x = 'hc_x


# hc_y
# Hit coordinate Y of batted ball.
# hit_coord_y = 'hc_y

# tfs_deprecated
# * Deprecated field from old tracking system.
# tfs_deprecated = 'tfs_deprecated

# tfs_zulu_deprecated
# * Deprecated field from old tracking system.
# tfs_zulu_deprecated = 'tfs_zulu_deprecated

# fielder_2
# Pre-pitch MLB Player Id of Catcher.
# fielder_2 = 'fielder_2'

# umpire
# * Deprecated field from old tracking system.
# umpireDep = 'umpire'

# sv_id
# Non-unique Id of play event per game.
# sv_id = 'sv_id'

# vx0
# The velocity of the pitch, in feet per second, in x-dimension, determined at y=50 feet.
# pitch_velocity_x = 'vx0'

# vy0
# The velocity of the pitch, in feet per second, in y-dimension, determined at y=50 feet.
# pitch_velocity_y = 'vy0'

# vz0
# The velocity of the pitch, in feet per second, in z-dimension, determined at y=50 feet.
# pitch_velocity_z = 'vz0'

# ax
# The acceleration of the pitch, in feet per second per second, in x-dimension, determined at y=50 feet.
# pitch_acceleration_x = 'ax'

# ay
# The acceleration of the pitch, in feet per second per second, in y-dimension, determined at y=50 feet.
# pitch_acceleration_y = 'ay'

# az
# The acceleration of the pitch, in feet per second per second, in z-dimension, determined at y=50 feet.
# pitch_acceleration_z = 'az'

# sz_top
# Top of the batter's strike zone set by the operator when the ball is halfway to the plate.
# top_of_strikezone = 'sz_top'

# sz_bot
# Bottom of the batter's strike zone set by the operator when the ball is halfway to the plate.
# bottom_of_strikezone = 'sz_bot'

# hit_distance
# Projected hit distance of the batted ball.
# hit_distance = 'hit_distance'

# launch_speed
# Exit velocity of the batted ball as tracked by Statcast. For the limited subset of batted balls not tracked directly, estimates are included based on the process described here.
# hit_distance = 'hit_distance'

# launch_angle
# Launch angle of the batted ball as tracked by Statcast. For the limited subset of batted balls not tracked directly, estimates are included based on the process described here.
# launch_angle = 'launch_angle'

# effective_speed
# Derived speed based on the the extension of the pitcher's release.
# effective_speed = 'effective_speed'

# release_spin
# Spin rate of pitch tracked by Statcast. probably tracked on release
# release_spin = 'release_spin'

# release_extension
# Release extension of pitch in feet as tracked by Statcast.
# release_extension = 'release_extension'

# game_pk
# Unique Id for Game.
# game_pk = 'game_pk'

# pitcher
# MLB Player Id tied to the play event.
# fielder_1 = 'pitcher'

# fielder_2
# MLB Player Id for catcher.
# fielder_2 = 'fielder_2'

# fielder_3
# MLB Player Id for 1B.
# fielder_3 = 'fielder_3'

# fielder_4
# MLB Player Id for 2B.
# fielder_4 = 'fielder_4'

# fielder_5
# MLB Player Id for 3B.
# fielder_5 = 'fielder_5'

# fielder_6
# MLB Player Id for SS.
# fielder_6 = 'fielder_6'

# fielder_7
# MLB Player Id for LF.
# fielder_7 = 'fielder_7'

# fielder_8
# MLB Player Id for CF.
# fielder_8 = 'fielder_8'

# fielder_9
# MLB Player Id for RF.
# fielder_9 = 'fielder_9'

# release_pos_y
# Release position of pitch measured in feet from the catcher's perspective.
# release_pos_y = 'release_pos_y'

# estimated_ba_using_speedangle
# Estimated Batting Avg based on launch angle and exit velocity.
# estimated_ba_using_speedangle = 'estimated_ba_using_speedangle'

# estimated_woba_using_speedangle
# Estimated wOBA based on launch angle and exit velocity.
# estimated_woba_using_speedangle = 'estimated_woba_using_speedangle'

# woba_value
# wOBA value based on result of play.
# woba_value = 'woba_value'

# woba_denom
# wOBA denominator based on result of play.
# woba_denom = 'woba_denom'

# babip_value
# BABIP value based on result of play.
# babip_value = 'babip_value'

# iso_value
# ISO value based on result of play.
# iso_value = 'iso_value'

# launch_speed_angle
# Launch speed/angle zone based on launch angle and exit velocity.
# 1: Weak
# 2: Topped
# 3: Under
# 4: Flare/Burner
# 5: Solid Contact
# 6: Barrel
# launch_speed_angle = 'launch_speed_angle'

# at_bat_number
# Plate appearance number of the game.
# pa_number = 'at_bat_number'

# pitch_number
# Total pitch number of the plate appearance.
# pa_pitch_count = 'pitch_number'

# pitch_name
# The name of the pitch derived from the Statcast Data.
# pitch_name = 'pitch_name'

# home_score
# Pre-pitch home score
# home_score = 'home_score'

# away_score
# Pre-pitch away score
# away_score = 'away_score'

# bat_score
# Pre-pitch bat team score
# bat_score = 'bat_score'

# fld_score
# Pre-pitch field team score
# fld_score = 'fld_score'

# post_home_score
# Post-pitch home score
# post_home_score = 'post_home_score'

# post_away_score
# Post-pitch away score
# post_away_score = 'post_away_score'

# post_bat_score
# Post-pitch bat team score
# post_bat_score = 'post_bat_score'

# if_fielding_alignment
# Infield fielding alignment at the time of the pitch.
# if_fielding_alignment = 'if_fielding_alignment'

# of_fielding_alignment
# Outfield fielding alignment at the time of the pitch.
# of_fielding_alignment = 'of_fielding_alignment'

# spin_axis
# The Spin Axis in the 2D X-Z plane in degrees from 0 to 360, such that 180 represents a pure backspin fastball and 0 degrees represents a pure topspin (12-6) curveball
# pitch_spin_axis = 'spin_axis'

# delta_home_win_exp
# The change in Win Expectancy before the Plate Appearance and after the Plate Appearance
# delta_home_win_exp = 'delta_home_win_exp'

# delta_run_exp
# The change in Run Expectancy before the Pitch and after the Pitch
# delta_run_exp = 'delta_run_exp'
