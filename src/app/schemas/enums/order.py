from enum import Enum


class OrderStatus(str, Enum):
    DRAFT = "Draft"
    PROCESSING = "Processing"
    CANCELLED = "Cancelled"
    DELIVERED = "Delivered"
