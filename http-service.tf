# Use the latest version of the Kubernetes provider
terraform {
  required_providers {
    kubernetes = {
      source = "hashicorp/kubernetes"
      version = ">= 2.0.0"
    }
  }
}

# Configure the Kubernetes provider with the Minikube context
provider "kubernetes" {
  config_context_cluster = "minikube"
}

# Deploy the application with a Kubernetes Deployment
resource "kubernetes_deployment" "http_service" {
  metadata {
    name = "http-service"
  }

  spec {
    replicas = 2

    selector {
      match_labels = {
        app = "http-service"
      }
    }

    template {
      metadata {
        labels = {
          app = "http-service"
        }
      }

      spec {
        container {
          name  = "http-service"
          image = "jebin90/http-service:latest"
          port {
            container_port = 8080
          }
        }
      }
    }
  }
}

# Expose the application with a Kubernetes Service
resource "kubernetes_service" "http_service" {
  metadata {
    name = "http-service"
  }

  spec {
    selector = {
      app = "http-service"
    }

    port {
      port        = 80
      target_port = 8080
    }

    type = "NodePort"
  }
}

# Output the Service URL
#output "service_url" {
#  value = "http://${minikube_ip}:${kubernetes_service.http_service.spec.ports.0.node_port}"
#}

# Get the Minikube IP address
#data "external" "minikube" {
#  program = ["minikube", "ip"]
#}
