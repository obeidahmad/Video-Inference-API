from pydantic import validator, BaseModel

from shared.helpers.url_validator import url_validate


class Urls(BaseModel):
    image_segmentation_url: str

    @validator('image_segmentation_url')
    def is_dir(cls, value):
        assert url_validate(value), "{} should be a url".format(value)
        return value
