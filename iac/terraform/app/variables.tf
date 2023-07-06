# Variables that are overidden by environments/<environment>/variables.tfvars

variable "env" {
  description = "The environment (prod, dev)"
  type        = string
}

variable "enable_alb" {
  description = "Need an ALB or not?"
  type        = bool
  default     = true
}

variable "container_environment" {
  type        = map(string)
  description = "The environment variables to pass to your app container"
  default     = {}
}

variable "container_secrets" {
  type        = map(string)
  description = "The Container secrets variables in JSON format"
  default     = {}
}

# Common Variables

variable "region" {
  description = "AWS Region"
  type        = string
  default     = "eu-central-1"
}

variable "allowed_origins" {
  description = "Allowed Origins for CORS"
  type        = list(string)
  default     = ["*"]
}

variable "cluster_name_overwrite" {
  description = "EKS cluster to use. If not specify, it will use the cluster based on the environment and in the microservices cluster"
  type        = string
  default     = ""
}

# Opsgenie - Incident Management
variable "opsgenie_api_key" {
  description = "API Key to use Opsgenie provider"
  sensitive   = true
}

# RDS Variables

variable "engine" {
  type        = string
  description = "Database Engine"
}

variable "engine_version" {
  type        = string
  description = "Database Engine Version"
}

variable "instance_class" {
  type        = string
  description = "Database Instance Type"
}

variable "storage_size" {
  type        = number
  default     = 5
  description = "Database Storage Type"
}

variable "database_name" {
  type        = string
  description = "Database Engine"
}

variable "username" {
  type        = string
  description = "Database Engine"
}

variable "port" {
  type        = string
  description = "Database Instance Type"
}

variable "database_master_password" {
  description = "The Database password"
  type        = string
}

variable "deletion_protection" {
  type        = bool
  default     = true
  description = "Protects the database from being deleted accidentally. While this option is enabled, you can’t delete the database"
}

variable "backup_retention_period" { // By default there's no backup retention period defined
  type        = number
  default     = 1
  description = "Choose the number of days that RDS should retain automatic backups for this instance."
}

variable "monitoring_interval" {
  type        = number
  default     = 30
  description = "The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. To disable collecting Enhanced Monitoring metrics, specify 0. The default is 0. Valid Values: 0, 1, 5, 10, 15, 30, 60."
}

variable "switch_off" {
  type        = bool
  description = "Specifies whether the database is kept on out of business ours (Only for non-prod environments)"
}



