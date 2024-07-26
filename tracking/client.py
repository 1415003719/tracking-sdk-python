# coding: utf-8
#
# This code was auto generated by AfterShip SDK Generator.
# Do not edit the class manually.

__all__ = ["Client"]

from typing import Optional

from .configuration import Configuration
from .api import CourierApi, EstimatedDeliveryDateApi, TrackingApi


class Client:
    def __init__(self, configuration: Optional[Configuration] = None) -> None:
        if configuration is None:
            configuration = Configuration()

        self.courier = CourierApi(configuration)
        self.estimated_delivery_date = EstimatedDeliveryDateApi(configuration)
        self.tracking = TrackingApi(configuration)