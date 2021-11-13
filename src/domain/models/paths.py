import os

from pydantic import validator, BaseModel


class Paths(BaseModel):
    video_input_dir: str
    video_output_dir: str
    frames_input_dir: str
    frames_output_dir: str

    @validator('video_input_dir', 'video_output_dir', 'frames_input_dir', 'frames_output_dir')
    def is_dir(cls, value):
        assert os.path.isdir(value), "{} should be a directory".format(value)
        return value
