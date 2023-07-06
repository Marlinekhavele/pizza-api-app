data "aws_eks_cluster_auth" "default" {
  name = local.cluster_name
}

data "aws_eks_cluster" "default" {
  name = local.cluster_name
}
