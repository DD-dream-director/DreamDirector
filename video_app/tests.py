from django.test import TestCase


class Video_appTests(TestCase):
    '''
    video_appのテストコード
    '''

    def test_should_return_200_statusCode_for_recomendVideos(self):
        '''
        "/video_app/recomend_videos/"のhttpステータスコードが200で帰ってくるか否か
        -> 指定されたwebサイトが表示可能か否か

        '''
        response = self.client.get('/video_app/recommend_videos/')
        self.assertEqual(response.status_code, 200)

    def test_should_return_200_statusCode_for_otherVideos(self):
        '''
        以下略
        '''
        response = self.client.get('/video_app/recommend_videos/')
        self.assertEqual(response.status_code, 200)

    def test_should_return_200_statusCode_for_videos(self):
        '''
        以下略
        '''
        response = self.client.get('/video_app/videos/')
        self.assertEqual(response.status_code, 200)
