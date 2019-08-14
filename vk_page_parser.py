import sys
import vk

def get_vk_profile_data(profile_id, vk_api, fields=[]):
    """
        Returns a dict containing data about a profile.
        
        Parameters
        ----------
        profile_id : int
            id of a profile to work with
        vk_api : vk.API(session)
            object of vk.API(session)
        fields : list of strings
            additional fields for receiving data
            available values : 
                photo_id, verified, sex, bdate, city, country, home_town, 
                has_photo, photo_50, photo_100, photo_200_orig, photo_200, 
                photo_400_orig, photo_max, photo_max_orig, online, domain, 
                has_mobile, contacts, site, education, universities, schools, 
                status, last_seen, followers_count, common_count, occupation, 
                nickname, relatives, relation, personal, connections, exports, 
                activities, interests, music, movies, tv, books, games, about, 
                quotes, can_post, can_see_all_posts, can_see_audio, 
                can_write_private_message, can_send_friend_request, is_favorite, 
                is_hidden_from_feed, timezone, screen_name, maiden_name, crop_photo, 
                is_friend, friend_status, career, military, blacklisted, blacklisted_by_me,
                can_be_invited_group.
    """

    page_info = []
    try:
        page_info = vk_api.users.get(user_id=profile_id, fields=fields, v=5.92)
    except Exception as e:
        print("id - {}, error: {}".format(profile_id, e))
    return page_info[0] 



if __name__=='__main__':

    if len(sys.argv) != 3:
        print('Invalid parameters.')
        print('Use: python file_name_.py profile_id vk_token')
        exit()

    profile_id = int(sys.argv[1])
    token = sys.argv[2]

    session = vk.Session(access_token=token)
    vk_api = vk.API(session)

    page_info = get_vk_profile_data(profile_id, vk_api, fields=['sex', 'bdate', 'city', 'country', 'education', 'contacts', 'connections', 'counters', 'verified'])
    print(page_info)