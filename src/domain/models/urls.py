import validators
from pydantic import validator, BaseModel


class Urls(BaseModel):
    image_segmentation_url: str

    @validator('image_segmentation_url')
    def is_dir(cls, value):
        assert validators.url(value), "{} should be a url".format(value)
        return value
