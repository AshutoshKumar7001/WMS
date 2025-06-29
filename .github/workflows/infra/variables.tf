variable "aws_region" {
  description = "AWS Region"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project name prefix"
  type        = string
  default     = "wms"
}

variable "container_image" {
  description = "ECR Image URI (with tag)"
  type        = string
}

variable "vpc_id" {
  description = "VPC ID for ECS tasks"
  type        = string
}

variable "subnet_ids" {
  description = "Subnets for ECS tasks"
  type        = list(string)
}
