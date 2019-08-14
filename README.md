# vk-community-members-parser
Script for parsing vk communities.

## vk_page_parser.py
Can be launched using command line and profile_id and vk_token as parameters. Receives some data from vk profile and prints it.
Consists of one function.
####  get_vk_profile_data(profile_id, vk_api, fields=[])
#####  Returns a dict containing data about a profile.
*  profile_id : int<br />
      id of a profile to work with
*  vk_api : vk.API(session)<br />
      object of vk.API(session)
*  fields : list of strings<br />
      additional fields for receiving data.
      

## vk_community_loader.py
Can be launched using command line and group_id and vk_token as parameters. Receives data about all community members and saves it to .csv file. 
Consists of two functions.
####  get_members(group_id, verbose=True)
#####  Returns a list storing ids of all group members.
*  group_id : integer<br />
      an id of a group to work with.
*  verbose : boolean<br /> 
      True - print additional info. False - print nothing. (default is True)
#### get_info_in_csv(member_list, vk_api, output_file_name, fields, verbose)
#####  Recives profile data and saves it to .csv file.
*  member_list : list of integers<br />
      list of profiles ids to get data about
*  vk_api : vk.API(session)<br />
      object of vk.API(session)
*  output_file_name : string<br />
     file name to save data (default is 'result.csv')
*  fields : list of strings<br />
      additional fields for receiving data
*  verbose : boolean <br />
            True - print additional info. False - print nothing. (default is True)

      
      
 
