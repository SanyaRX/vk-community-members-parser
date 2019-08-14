import vk 
import vk_page_parser as vpp
import csv
import sys

_optional_fields_to_parse = ['sex', 'bdate', 'city', 'country', 'education', 'contacts', 'connections', 'counters', 'verified']
_required_fields = ['id', 'first_name', 'last_name', 'can_access_closed', 'is_closed']


def get_members(group_id, verbose=True):
    """
        Returns a list storing ids of all group members.

        Parameters:
        -----------
        group_id : integer
            an id of a group to work with.
        verbose : boolean 
            True - print additional info. False - print nothing. (default is True)
    """

    first = vk_api.groups.getMembers(group_id=group_id, v=5.92)
    data = first["items"]
    count = first["count"] // 1000
    
    for i in range(1, count+1):  
        data = data + vk_api.groups.getMembers(group_id=group_id, v=5.92, offset=i*1000)["items"]
    
    if verbose:
        print('group id - {}, num members = {}'.format(group_id, len(data)))
    return data

def get_info_in_csv(member_list, vk_api, output_file_name='result.csv', fields=_optional_fields_to_parse, verbose=True):
    """
        Recives profile data and saves it to .csv file.

        Parameters
        ----------
        member_list : list of integers
            list of profiles ids to get data about
        vk_api : vk.API(session)
            object of vk.API(session)
        output_file_name : string
           file name to save data (default is 'result.csv')
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
        verbose : boolean 
            True - print additional info. False - print nothing. (default is True)
    """

    with open(output_file_name, 'w', newline='', encoding='utf-8') as f:
        field_names = _required_fields + fields
        
        csv_writer = csv.DictWriter(f, fieldnames=field_names, extrasaction='ignore')
        csv_writer.writeheader()        

        counter = 0
        num_members = len(member_list)

        for profile_id in member_list:
            profile_data = vpp.get_vk_profile_data(profile_id, vk_api, fields=fields)
           
            csv_writer.writerow(profile_data)
            
            counter += 1
            if verbose:
                print('processed {}/{}'.format(counter, num_members))


if __name__=='__main__':
    if len(sys.argv) != 3:
        print('Invalid parameters.')
        print('Use: python file_name_.py group_id vk_token')
        exit()

    group_id = int(sys.argv[1])
    token = sys.argv[2]

    session = vk.Session(access_token=token)
    vk_api = vk.API(session)
    
    members = get_members(group_id)

    get_info_in_csv(members, vk_api, fields=_optional_fields_to_parse)
        
        