import pytest
from framework.utils.other_utils.test_data import TestData
from framework.utils.other_utils.random_text import RandomText
from framework.utils.other_utils.image_preprocessor import ImagePreprocessor
from test_and_data.pages.main_page import MainPage
from test_and_data.pages.home_page import HomePage
from test_and_data.pages.vk_user_page import VkUserFormPage
from test_and_data.pages.vk_user_post_page import VkUserPostPage
from test_and_data.pages.vk_user_edit_post_page import VkUserEditPostPage
from test_and_data.pages.vk_user_create_comment_page import VkUserCreateCommentPage
from test_and_data.pages.vk_user_likes_page import VkUserLikesPage
from test_and_data.pages.vk_user_delete_post_page import VkUserDeletePostPage
from framework.utils.other_utils.vk_photos_requests import PhotosRequests
from framework.utils.other_utils.vk_likes_requests import LikeRequests
from framework.utils.other_utils.vk_wall_requests import WallRequests
from framework.utils.other_utils.params_creator import ParamsCreator
from conftest import Logger
from framework.utils.api_requests.wall_requests import WallAPIRequests
from framework.utils.api_requests.photos_requests import PhotosAPIRequests
from framework.utils.api_requests.likes_requests import LikesAPIRequests
from models.post import Post
from models.photo import Photo
from models.likes import Likes

logger = Logger()


class TestVKApi:
    def test_one(self, driver):
        logger.info("Start of VK API test")
        test_data = TestData("test_data.json")
        main_page = MainPage()
        logger.info("Step_1.Attempt to go on main page")
        assert main_page.wait_until_loaded_and_check_if_displayed(), "You are on wrong site , please check again"
        log = test_data.get_data("login1")
        password = test_data.get_data("password1")
        logger.info("Step_2.Attempt to authorize on site")

        main_page.vk_authorization(log, password)
        home_page = HomePage()
        assert home_page.wait_until_loaded_and_check_if_displayed(), "You are not authorized , look credentials"
        home_page.go_on_my_page()
        vk_user_page = VkUserFormPage()
        logger.info("Step_3.Trying to go on user page")
        assert vk_user_page.wait_until_loaded_and_check_if_displayed(), "You are not on 'my_page' now"

        base_url = test_data.get_data("base_api_url")
        method = WallRequests.WALL_POST
        url = base_url + method
        user_id_param = test_data.get_data("user_id_param1")
        rand_text = RandomText()(10)
        message_param = ParamsCreator.create_param("message", rand_text)
        token_param = test_data.get_data("token_param1")
        version_param = test_data.get_data("version")
        vk_user_post_page = VkUserPostPage()
        post = Post(WallAPIRequests.post_msg_on_wall(url, user_id_param, message_param, version_param, token_param))
        logger.info("Step_4. Getting wall post id")
        assert type(post.get_id()) == int, f"Response returned wrong data . Expected to be int" \
                                           f", Got {type(post.get_id())} instead"
        user_id = int(user_id_param[1])
        wall_user_id, wall_post_text = vk_user_post_page.check_post_data()
        logger.info("Step_5. Checking post data")
        assert (user_id, rand_text) == (wall_user_id, wall_post_text), f"Wrong post data : Expected to be :" \
                                                                       f"{user_id} , {rand_text} , Got : {wall_user_id} , {wall_post_text}"
        url_upload_method = PhotosRequests.GET_WALL_UPLOAD_SERVER
        url = base_url + url_upload_method
        new_message = RandomText()(10)
        vk_user_edit_post_page = VkUserEditPostPage()
        req = Photo(PhotosAPIRequests.get_photo_upload_url(url, token_param, version_param))
        img_path = test_data.get_data("image_path")
        image = {'photo': ('img.jpg', open(img_path, 'rb'))}
        req = Photo(PhotosAPIRequests.upload_image_on_url(req.get_upload_url(), image))
        save_photo_method = PhotosRequests.SAVE_WALL_PHOTO
        url = base_url + save_photo_method
        server_param = ParamsCreator.create_param("server", req.get_server())
        photo_param = ParamsCreator.create_param("photo", req.get_photo())
        hash_param = ParamsCreator.create_param("hash", req.get_hash())
        req = Photo(PhotosAPIRequests.save_wall_photo(url, token_param, version_param, user_id_param, server_param,
                                                      photo_param, hash_param))
        attachment_param = ParamsCreator.create_param("attachments",
                                                      "photo" + f"{user_id}_" + str(req.get_save_photo_id()))
        edit_method = WallRequests.WALL_EDIT
        url = base_url + edit_method
        new_message_param = ParamsCreator.create_param("message", new_message)
        post_id_param = ParamsCreator.create_param("post_id", post.get_id())
        logger.info("Step_6. Trying to edit message and attach photo")
        WallAPIRequests.edit_msg_on_wall(url, user_id_param, new_message_param, version_param, post_id_param,
                                         token_param,
                                         attachment_param)
        edited_post_text = vk_user_edit_post_page.get_text_from_wall()
        edited_post_pixel_sum = vk_user_edit_post_page.get_image_and_calc_pixel_sum()
        real_image_pixel_sum = ImagePreprocessor.get_image_pixel_sum(img_path)
        is_similar_images = ImagePreprocessor.is_same_images(edited_post_pixel_sum, real_image_pixel_sum)
        logger.info("Step_7. Checking that text changed and images are the same")
        assert edited_post_text != rand_text, f" Text from editing are the same . Got {edited_post_text} instead of {rand_text}"
        assert is_similar_images, f" Images are different . Check again"
        method = WallRequests.WALL_CREATE_COMMENT
        url = base_url + method
        comment_text = RandomText()(10)
        message_param = ParamsCreator.create_param("message", comment_text)
        post_id_param = ParamsCreator.create_param("post_id", post.get_id())
        logger.info("Step_8. Attempt to create random comment in post")
        vk_user_create_comment_page = VkUserCreateCommentPage()
        WallAPIRequests.create_post_comment(url, post_id_param, user_id_param, message_param, version_param,
                                            token_param)
        wall_author_name, wall_comment_text = vk_user_create_comment_page.check_comment_data()
        logger.info("Step_9.Checking comment data")
        assert (user_id, comment_text) == (
            wall_author_name, wall_comment_text), f"Wrong comment data : Expected to be :" \
                                                  f"{user_id} , {comment_text} , Got : {wall_author_name} , {wall_comment_text}"
        logger.info("Step_10.Sending like to comment")
        vk_user_likes_page = VkUserLikesPage()
        vk_user_likes_page.click_like_on_post()
        like_method = LikeRequests.GET_LIKES_LIST
        url = base_url + like_method
        add_params = test_data.get_data("likes_additional_params")
        item_id_param = ParamsCreator.create_param("item_id", post.get_id())
        req = Likes(LikesAPIRequests.get_likes_list(url, add_params, token_param, version_param, item_id_param))
        logger.info("Step_11.Checking if like from needed user appears")
        assert user_id in req.get_likes_list(), "No like from needed user discovered"
        delete_method = WallRequests.DELETE_WALL_POST
        url = base_url + delete_method
        logger.info("Step_12.Attempt to delete post")
        vk_user_delete_post_page = VkUserDeletePostPage()
        WallAPIRequests.delete_post(url, token_param, post_id_param, user_id_param, version_param)
        deletion_time = test_data.get_data("post_deletion_wait")
        post_existion_flag = vk_user_delete_post_page.check_post_deletion(deletion_time)
        logger.info("Step_13.Check if post is deleted")
        assert not post_existion_flag, "Post still exists"


if __name__ == "__main__":
    pytest.main()
