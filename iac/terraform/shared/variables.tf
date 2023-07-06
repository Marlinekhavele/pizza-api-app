variable "region" {
  description = "AWS Region"
  type        = string
  default     = "eu-central-1"
}

variable "env" {
  description = "The env"
  type        = string
  default     = "shared"
  validation {
    condition     = can(regex("^(shared)$", var.env))
    error_message = "The environment name must be `shared`."
  }
}

variable "allow_mutable_tags" {
  description = "Allow tag mutability"
  type        = bool
  default     = false
}

variable "scan_on_push" {
  description = "Scanning the image while pushing to ECR"
  type        = bool
  default     = true
}

variable "tag_prefix" {
  description = "For Lifecycle policies "
  type        = string
  default     = "master"
}

variable "keep_images" {
  description = "Retention days for the ECR image with tag prefix"
  type        = number
  default     = 100
}

variable "keep_untagged_days" {
  description = "Retention for images that are not tagged"
  type        = number
  default     = 30
}

variable "enable_kaniko_cache" {
  type        = bool
  description = "(optional) Allow to create a cache repository for kaniko. WARNING: If you already created one, delete this cache ECR before to apply."
  default     = true
}
