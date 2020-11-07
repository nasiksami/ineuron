#pip install bing-image-downloader
from bing_image_downloader import downloader


downloader.download("nature", limit=20, output_dir='./desktop', adult_filter_off=True, force_replace=False)
