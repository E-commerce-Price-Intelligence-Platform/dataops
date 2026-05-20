terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = "price-intelligence-project"
  region  = "europe-west1"
}

# Google Cloud Bigtable
resource "google_bigtable_instance" "price_intelligence" {
  name         = "price-intelligence-bigtable"
  display_name = "Price Intelligence Bigtable"

  cluster {
    cluster_id   = "price-cluster"
    zone         = "europe-west1-b"
    num_nodes    = 1
    storage_type = "SSD"
  }
}

# Google Kubernetes Engine
resource "google_container_cluster" "dataops_cluster" {
  name     = "dataops-cluster"
  location = "europe-west1"

  initial_node_count = 1

  node_config {
    machine_type = "e2-medium"
    disk_size_gb = 50
  }
}