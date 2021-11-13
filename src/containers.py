from dependency_injector import providers, containers

from application.paths.services.path_service import PathService
from application.prediction.services.inference_service import InferenceService
from application.prediction.services.openvino_prediction_service import OpenvinoPredictionService
from application.video.services.video_merger_service import VideoMergerService
from application.video.services.video_splitter_service import VideoSplitterService
from domain.contracts.abstract_openvino_service import AbstractOpenvinoService
from domain.contracts.abstract_path_service import AbstractPathService
from domain.contracts.abstract_video_processing_service import AbstractVideoProcessingService


class Container(containers.DeclarativeContainer):
    path_service = providers.Singleton(AbstractPathService.register(PathService))
    uploader_service = providers.Factory(AbstractOpenvinoService.register(OpenvinoPredictionService),
                                         path_service=path_service)
    splitter_service = providers.Factory(AbstractVideoProcessingService.register(VideoSplitterService),
                                         path_service=path_service)
    merger_service = providers.Factory(AbstractVideoProcessingService.register(VideoMergerService),
                                       path_service=path_service)
    inference_service = providers.Factory(InferenceService, splitter_service=splitter_service,
                                          uploader_service=uploader_service, merger_service=merger_service,
                                          path_service=path_service)
