provider "aws" {
  region = var.region
}

resource "aws_ecr_repository" "wms_repo" {
  name = var.ecr_repo
}

resource "aws_ecs_cluster" "wms_cluster" {
  name = var.ecs_cluster
}

resource "aws_cloudwatch_log_group" "wms_logs" {
  name              = "/ecs/wms-logs"
  retention_in_days = 7
}
