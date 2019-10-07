#! /usr/bin/python

import sys, os.path, glob, re, fnmatch

if (len(sys.argv)>1):
    start_location=str(sys.argv[1])
else:
    start_location=raw_input("Enter location of pre-cert package")

pkgpath=os.path.expanduser(start_location)

#Directory names
main_dir=['Misc', 'YouTube_Application', 'DIAL', 'YTS']
yts_dir=['Automated', 'Manual']
yts_man_dir=['DRM', 'cobalt_map_to_mesh', 'Initial_playbackRate', 'Dynamic_playbackRate', 'WebP', 'Cookies']
yt_app_dir=['Language', 'Performance']

#File names
yts_man_file=['web_audio','dual_video', 'resizing', 'localization', 'key_event', 'fonts', 'fetch_api', 'current_time', 'application_lifecycle_api', 'adaptive_bit_rate']
yts_man_cookies_file=['cookies_0hrs', 'cookies_24hrs', 'cookies_72hrs']
yts_man_DRM_file=['drm', 'purchased_movie', 'widevine']
yts_man_DPBR_file=['runtime_change']
yts_man_IPBR_file=['0_25x', '0_5x', '1_0x', '1_25x', '1_5x', '2_0x']
yts_man_webp_file=['animated_webp', 'webp', 'youtube_app_with_webp']
yts_man_webgl_file=['webgl_vp9']
yts_man_cobaltm2m_file=['720p', '1080p', '1440p', '2160p']
yts_auto_file=['cobalt_spherical_tests', 'css_conformance_tests', 'dom_chardata', 'dom_css_tests', 'dom_document_tests', 'eme_conformance_tests', 'format_support_tests', 'functional_tests', 'html_dom_element_tests', 'mse_conformance_tests', 'playback_performance_tests', 'progressive_tests']
yt_dial_file=['additionalData_browser', 'additionalData_inapp', 'dial_inappcast_vol', 'menu_inappcast_vol', 'multicast_seek', 'oobe', 'remote_inappcast_vol', 'wolan_25hrs', 'wowlan_25hrs', 'dial_unit_tests']
yt_misc_file=['websockets', 'yt_logo']
yt_app_file=['3d_video','360_support', 'aspect_ratio', 'high_bitrate', 'high_frame_rate', 'hlg_hdr_support', 'in_app_exit', 'launch_menu', 'launch_remote', 'launch_voice', 'live_stream_drm_key_rotation', 'live_stream_support_vp9', 'live_stream_support', 'network_interface_switching', 'pq_hdr_support', 'signin_persistence', 'system_wide_exit', 'user_agent', 'visual_av_sync_test', 'visual_inspection', 'vp9_support', 'web_audio_navigation_sounds']
yt_app_lang_file=['language_settings', 'language_youtube']
yt_app_perf_file=['automated_performance_latencies', 'loading_time', 'observed_performance_latencies_system_functions', 'ui_frame_rate_stress_test', 'youtube_performance_after', 'youtube_performance_before', '12hr_input_endurance', '4hr_endurance'] 
yt_app_speech_file=['storage_acknowledgement.txt', 'soft_mic_button', 'hard_mic_button', 'condition_query_outside_youtube', 'condition_query_inside_youtube']

#Folder tree 
path={'yt_precert' : pkgpath, 'yts_precert': pkgpath+"/YTS", 'yts_man_precert': pkgpath+"/YTS/Manual/", 'yt_app_precert' : pkgpath+"/YouTube_Application", 'yts_man_DRM_precert' : pkgpath+"/YTS/Manual/DRM/", 'yts_man_DPBR_precert' : pkgpath+"/YTS/Manual/Dynamic_playbackRate/", 'yts_man_IPBR_precert' : pkgpath+"/YTS/Manual/Initial_playbackRate/", 'yts_man_webp_precert' : pkgpath+"/YTS/Manual/Webp/", 'yts_man_webgl_precert': pkgpath+"YTS/Manual/webgl/", 'yts_man_cobaltm2m_precert' : pkgpath+"/YTS/Manual/cobalt_map_to_mesh", 'yts_auto_precert' : pkgpath+"/YTS/Automated/", 'yt_dial_precert' : pkgpath+"/DIAL/", 'yt_misc_precert' : pkgpath+"/Misc/",  'yt_app_lang_precert' : pkgpath+"/YouTube_Application/Language/", 'yt_app_perf_precert' : pkgpath+"/YouTube_Application/Performance/", 'yt_app_speech_precert' : pkgpath+"/YouTube_Application/Speech/"}

def insensitive_glob(path):
    def char(ch):
        return '[%s%s]' % (ch.lower(), ch.upper()) if ch.isalpha() else ch
    return glob.glob(''.join(map(char, path)))

def d_exist(chk_dir, a_dir):
	for i in range (len(a_dir)):
            direct=chk_dir+'/'+a_dir[i]
            if insensitive_glob(direct):
	        continue
       	    else:
	        print("\033[1;31;40mMISSING Directory:"+" "+a_dir[i]+"\033[0m")

def f_exist(chk_dir, a_dir):
	for i in range (len(a_dir)):
                files=chk_dir+'/'+a_dir[i]+"*"
                if insensitive_glob(files):
			continue
		else:
			print("\033[1;31;40mMISSING File:"+" "+a_dir[i]+"\033[0m")

def main():
	d_exist(path['yt_precert'], main_dir)
	d_exist(path['yts_precert'], yts_dir)
	d_exist(path['yts_man_precert'], yts_man_dir)
	d_exist(path['yt_app_precert'], yt_app_dir)
	f_exist(path['yts_man_precert'], yts_man_file)
	f_exist(path['yts_man_DRM_precert'], yts_man_DRM_file)
	f_exist(path['yts_man_DPBR_precert'], yts_man_DPBR_file)
	f_exist(path['yts_man_IPBR_precert'], yts_man_IPBR_file)
	f_exist(path['yts_man_webp_precert'], yts_man_webp_file)
	f_exist(path['yts_man_webgl_precert'], yts_man_webgl_file)
	f_exist(path['yts_man_cobaltm2m_precert'], yts_man_cobaltm2m_file)
	f_exist(path['yts_auto_precert'], yts_auto_file)
	f_exist(path['yt_dial_precert'], yt_dial_file)
	f_exist(path['yt_misc_precert'], yt_misc_file)
	f_exist(path['yts_auto_precert'], yts_auto_file)
	f_exist(path['yt_app_precert'], yt_app_file)
	f_exist(path['yt_app_lang_precert'], yt_app_lang_file)
	f_exist(path['yt_app_perf_precert'], yt_app_perf_file)
	f_exist(path['yt_app_speech_precert'], yt_app_speech_file)
	

if __name__ == "__main__":
	main()


