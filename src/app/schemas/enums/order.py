from enum import Enum


class Status(str, Enum):
    DRAFT = "Draft"
    PROCESSING = "Processing"
    CANCELLED = "Cancelled"
    DELIVERED = "Delivered"
