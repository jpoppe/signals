from io import BytesIO
from unittest.mock import MagicMock

from PIL import Image

from signals.apps.services.images import get_context_data_images, resize
from signals.apps.signals.factories import AttachmentFactory, SignalFactory
from tests.test import SIAReadWriteUserMixin, SignalsBaseApiTestCase


class TestImagesService(SIAReadWriteUserMixin, SignalsBaseApiTestCase):
    def setUp(self):
        self.signal = SignalFactory.create()

    def test_resize_image_too_wide(self):
        too_wide = MagicMock()
        too_wide.width = 1600
        too_wide.height = 800
        resize(too_wide, 800)
        too_wide.resize.assert_called_with(size=(800, 400), resample=Image.LANCZOS)

    def test_resize_iamge_too_heigh(self):
        too_heigh = MagicMock()
        too_heigh.width = 800
        too_heigh.height = 1600
        resize(too_heigh, 800)
        too_heigh.resize.assert_called_with(size=(400, 800), resample=Image.LANCZOS)

    def test_get_context_data_no_images(self):
        AttachmentFactory(_signal=self.signal, file__filename='blah.txt', file__data=b'blah', is_image=False)
        jpg_data_uris = get_context_data_images(self.signal, 800)
        self.assertEqual(len(jpg_data_uris), 0)

    def test_get_context_data_invalid_images(self):
        AttachmentFactory.create(_signal=self.signal, file__filename='blah.jpg', file__data=b'blah', is_image=True)
        jpg_data_uris = get_context_data_images(self.signal, 800)
        self.assertEqual(len(jpg_data_uris), 0)

    def test_get_context_data_valid_image(self):
        image = Image.new("RGB", (100, 100), (0, 0, 0))
        buffer = BytesIO()
        image.save(buffer, format='JPEG')

        AttachmentFactory.create(_signal=self.signal, file__filename='blah.jpg', file__data=buffer.getvalue())
        jpg_data_uris = get_context_data_images(self.signal, 80)
        self.assertEqual(len(jpg_data_uris), 1)
        self.assertEqual(jpg_data_uris[0][:22], 'data:image/jpg;base64,')
        self.assertGreater(len(jpg_data_uris[0]), 22)
